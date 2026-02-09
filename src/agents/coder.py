"""
Coder Agent (Factuality Engine) - Executes Python code for precise calculations.
Eliminates arithmetic hallucination by computing rather than estimating.
"""

import io
import ast
import builtins
import traceback
from typing import Optional
from contextlib import redirect_stdout, redirect_stderr
from ..utils.threading_utils import matplotlib_lock, plt as real_plt, plt
import numpy as np
from scipy import stats as scipy_stats
import seaborn as sns
from pathlib import Path
import time
from datetime import datetime
import uuid
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage

from ..config import config
from ..data.schema import VitalSignSeries, Demographics
from ..models import create_model
from ..logging import get_logger
from ..prompts import (
    CODER_SYSTEM_PROMPT, 
    CODER_USER_TEMPLATE, 
    CODER_USER_TEMPLATE, 
    CalculationResult
)
from ..utils.text_parsing import parse_coder_output


class PltProxy:
    """
    Proxy for matplotlib.pyplot that intercepts savefig calls
    to ensure images are saved in the correct results directory.
    """
    def __init__(self, original_plt, save_plot_func):
        self._plt = original_plt
        self._save_plot = save_plot_func

    def savefig(self, *args, **kwargs):
        """Intercept savefig and route to our safe helper."""
        # If the user passed a path/filename as first arg, use it
        filename = args[0] if args else "plot"
        self._save_plot(filename, **kwargs)

    def __getattr__(self, name):
        """Pass all other calls to original plt."""
        return getattr(self._plt, name)


class CoderAgent:
    """
    The Coder (Data Scientist) Agent.
    
    Acts as the "Factuality Engine" - writes and executes Python code
    to calculate derived clinical metrics with mathematical precision.
    """
    
    def __init__(self, model_key: Optional[str] = None):
        self.model_key = model_key or config.model.default_model
        self.llm = create_model(self.model_key, agent_name="coder")
        self.logger = get_logger()
        self.history: list[dict] = []  # Private memory of calculations

    def reset(self):
        self.history = []

    def repair_code(self, code: str, namespace: Optional[dict] = None) -> tuple[str, list[str]]:
        """
        Attempt to repair common benign violations (Class A) using AST transformation.
        
        Repairs technically safe violations like:
        - Forbidden imports (matplotlib/seaborn) -> removed (since they are injected)
        - plt.savefig() -> converted to save_plot()
        - Missing plt.close() -> injected
        
        Args:
            code: The raw Python code from LLM
            namespace: Execution namespace
            
        Returns:
            Tuple of (repaired_code, list_of_repairs_made)
        """
        repairs = []
        
        try:
            tree = ast.parse(code)
        except SyntaxError:
            # If syntax is invalid, we can't repair via AST. Return original to let validation fail it.
            return code, []

        class RepairTransformer(ast.NodeTransformer):
            def __init__(self):
                self.found_save_plot = False
                self.modified = False

            def visit_Import(self, node):
                # Remove forbidden imports: matplotlib, seaborn
                new_names = []
                for alias in node.names:
                    # Check top-level package name
                    root_pkg = alias.name.split('.')[0]
                    if root_pkg in ['matplotlib', 'seaborn']:
                        repairs.append(f"Stripped forbidden import: {alias.name}")
                        self.modified = True
                    else:
                        new_names.append(alias)
                
                if not new_names:
                    return None # Remove the import statement entirely
                
                node.names = new_names
                return node

            def visit_ImportFrom(self, node):
                if node.module:
                    root_pkg = node.module.split('.')[0]
                    if root_pkg in ['matplotlib', 'seaborn']:
                        repairs.append(f"Stripped forbidden import from: {node.module}")
                        self.modified = True
                        return None
                return node

            def visit_Call(self, node):
                # Rewrite plt.savefig(...) -> save_plot(...)
                # Check for calls like: plt.savefig
                if isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'plt' and node.func.attr == 'savefig':
                        repairs.append("Rewrote plt.savefig -> save_plot")
                        self.found_save_plot = True
                        self.modified = True
                        # Replace 'plt.savefig' with 'save_plot' (Load context)
                        node.func = ast.Name(id='save_plot', ctx=ast.Load())
                        return node
                
                # Also track if they called 'save_plot' directly (for correct plt.close injection)
                if isinstance(node.func, ast.Name) and node.func.id == 'save_plot':
                    self.found_save_plot = True
                
                return self.generic_visit(node)

        transformer = RepairTransformer()
        try:
            new_tree = transformer.visit(tree)
            ast.fix_missing_locations(new_tree)
            new_code = ast.unparse(new_tree)
        except Exception as e:
            # Fallback for older python or unparse errors
            print(f"AST unparse failed: {e}")
            return code, []

        # Inject plt.close() if save_plot was used and plt.close() is missing
        # We do a simple string check on the result for 'plt.close' to avoid complex control-flow analysis
        if transformer.found_save_plot and "plt.close" not in new_code:
            new_code += "\n\nplt.close()"
            repairs.append("Injected plt.close()")

        return new_code, repairs

    def validate_code(self, code: str, namespace: Optional[dict] = None) -> None:
        """
        Validate generated code against execution contract using AST inspection.
        
        Args:
            code: The Python code to validate
            namespace: Optional execution namespace to check for recomputation
            
        Raises:
            ValueError: If code violates validaton rules
        """
        # 1. Length Check
        if code.count("\n") > 500:
            raise ValueError("Code exceeds maximum allowed length (500 lines). Please condense your logic.")

        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            raise ValueError(f"Generated code has syntax error: {e}")

        # 2. AST Inspection for Forbidden Constructs
        forbidden_imports = {'matplotlib', 'seaborn', 'os', 'sys', 'subprocess', 'socket'}
        forbidden_calls = {'eval', 'exec', 'open', '__import__'}
        
        for node in ast.walk(tree):
            # Check Imports
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                # Gather all module names involved
                modules = []
                if isinstance(node, ast.ImportFrom) and node.module:
                    modules.append(node.module.split('.')[0])
                for alias in node.names:
                    modules.append(alias.name.split('.')[0])
                
                for mod in modules:
                    if mod in forbidden_imports:
                        raise ValueError(f"Forbidden import detected: '{mod}'. Use provided libraries (plt, sns) and variables only.")

            # Check Calls
            if isinstance(node, ast.Call):
                func_name = None
                if isinstance(node.func, ast.Name):
                    func_name = node.func.id
                
                if func_name in forbidden_calls:
                    raise ValueError(f"Forbidden function call detected: '{func_name}'.")

            # Check Attribute Access (e.g., __builtins__)
            if isinstance(node, ast.Attribute):
                if node.attr == '__builtins__':
                    raise ValueError("Access to __builtins__ is forbidden.")

        # 3. Recomputation Check (Namespace Protection)
        # We check for Assignments to keys in the namespace
        if namespace:
            for node in ast.walk(tree):
                if isinstance(node, (ast.Assign, ast.AnnAssign)):
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target in targets:
                        if isinstance(target, ast.Name):
                            if target.id in namespace:
                                raise ValueError(f"Recomputation of injected metric '{target.id}' is not allowed. Use the existing variable directly.")

    def _is_fatal_error(self, error: Optional[str]) -> bool:
        """
        Classify whether an error is fatal (non-fixable policy violation) or transient.
        
        Args:
            error: The error message string
            
        Returns:
            True if the error is fatal and should NOT be retried.
        """
        if not error:
            return False

        fatal_markers = [
            "Forbidden construct detected",
            "Recomputation of injected metric",
            "Code exceeds maximum allowed length",
        ]

        return any(marker in error for marker in fatal_markers)

    def calculate_metric(
        self,
        task: str,
        vitals: VitalSignSeries,
        parameters: Optional[dict] = None,
        demographics: Optional[Demographics] = None,
        clinical_context: str = "",
        previous_results: Optional[list[CalculationResult]] = None,
        visit_id: str = "unknown"
    ) -> CalculationResult:
        """
        Calculate a clinical metric from vital signs data.
        
        Args:
            task: The clinical task or metric to calculate
            vitals: VitalSignSeries object with patient data
            parameters: Additional calculation parameters
            visit_id: ID of the patient visit for unique indexing
        
        Returns:
            CalculationResult with computed value
        """
        start_time = time.time()
        
        # Implement Auto-Fix Retry Loop
        max_retries = 3
        last_result = None

        for attempt in range(max_retries + 1):
            result = self._generate_and_execute(
                task, 
                vitals, 
                parameters, 
                demographics, 
                clinical_context,
                previous_results=previous_results,
                visit_id=visit_id
            )
            
            last_result = result
            
            # 1. Success -> Return immediately
            if result.success:
                return result
            
            # 2. Fatal Error -> Stop retrying
            if self._is_fatal_error(result.error_message):
                break
            
            # 3. Else -> Loop continues (Feedback is implicit via self.history)
        
        # If loop finishes without success, return the last result
        result = last_result
        
        # Log the calculation
        duration_ms = (time.time() - start_time) * 1000
        self.logger.log_agent_step(
            agent_name="coder",
            input_data={
                "task": task,
                "visit_id": vitals.visit_id,
                "parameters": parameters,
            },
            output_data={
                "success": result.success,
                "value": str(result.value) if result.value else None,
                "interpretation": result.interpretation,
                "image_paths": result.image_paths,
                "error": result.error_message,
            },
            duration_ms=duration_ms,
        )
        
        return result
    
    def _generate_and_execute(
        self,
        task: str,
        vitals: VitalSignSeries,
        parameters: Optional[dict] = None,
        demographics: Optional[Demographics] = None,
        clinical_context: str = "",
        previous_results: Optional[list[CalculationResult]] = None,
        visit_id: str = "unknown"
    ) -> CalculationResult:
        """Generate and execute custom calculation code via LLM."""
        # Base Prompt
        system_msg = SystemMessage(content=CODER_SYSTEM_PROMPT)
        
        # Add Stored Metrics to reasoning context
        stored_metrics_context = ""
        if previous_results:
            metrics = []
            for r in previous_results:
                if r.success:
                    var_name = r.metric_name.replace(" ", "_").lower()
                    val = r.value
                    # Try to determine type for prompt clarity
                    val_type = type(val).__name__
                    metrics.append(f"- `{var_name}`: {val} (Python Type: {val_type})")
            if metrics:
                stored_metrics_context = "\n## Available Variables (from state):\nThese variables are already injected in your namespace and ready for use:\n" + "\n".join(metrics) + "\n"
        
        # Initial User Request (Task Definition)
        initial_prompt = CODER_USER_TEMPLATE.format(
            task_description=task,
            vitals_summary=vitals.to_text_summary(),
            parameters=parameters or {},
            clinical_context=clinical_context,
            calculation_results=stored_metrics_context,
        )
        
        # Construct Dynamic Chat History
        messages: list[BaseMessage] = [system_msg, HumanMessage(content=initial_prompt)]
        
        # Append previous attempts as a conversation thread
        previous_attempts = [h for h in self.history if h["task"] == task][-2:]
        
        for attempt in previous_attempts:
            # AI: "Here is the code I tried..."
            # For raw mode, we just re-inject the raw code block
            code_block = f"```python\n{attempt['code']}\n```"
            messages.append(AIMessage(content=code_block))
            
            # User: "It failed with error..." or "It succeeded..."
            if attempt['success']:
                # If it succeeded previously, we shouldn't be here again unless forcing retry
                messages.append(HumanMessage(content=f"Previous attempt succeeded."))
            else:
                messages.append(HumanMessage(content=f"That code failed with error:\n{attempt['error']}\nPlease fix it."))

        # Use raw output and regex parsing
        response = self.llm.invoke(messages)
        coder_output = parse_coder_output(response.content)
        
        # Handle case where Coder couldn't generate code (e.g., parsing failure)
        if coder_output is None:
            return CalculationResult(
                success=False,
                metric_name=task,
                value=None,
                error_message="Failed to parse output from model.",
            )
        
        # Handle case where Coder explicitly didn't generate code
        if not coder_output:
            reasoning = "Unable to compute metric - code generation failed without explanation."
            return CalculationResult(
                success=False,
                metric_name=task,
                value=None,
                error_message=reasoning,
            )
        
        # Execute in sandbox
        result = self._execute_sandboxed(
            coder_output, 
            vitals, 
            demographics, 
            previous_results=previous_results,
            visit_id=visit_id
        )
        result.metric_name = task
        result.code_executed = coder_output
        
        # Update private memory
        self.history.append({
            "task": task,
            "success": result.success,
            "code": coder_output,
            "error": result.error_message if not result.success else None
        })
        
        return result
    
    def _execute_sandboxed(
        self, 
        code: str, 
        vitals: VitalSignSeries,
        demographics: Optional[Demographics] = None,
        previous_results: Optional[list[CalculationResult]] = None,
        visit_id: Optional[str] = None
    ) -> CalculationResult:
        """Execute code in a restricted sandbox."""
        # Use provided visit_id or fall back to vitals.visit_id
        visit_id = visit_id or getattr(vitals, 'visit_id', 'unknown')
        # Use logger's output directory if available, otherwise default to results
        base_dir = self.logger.output_dir if self.logger else Path("results")
        
        # 1. Define paths
        # Format: results/logs/visits/<visit_id>/coder_scripts/
        # Use logger's output directory if available, otherwise default to results
        base_dir = self.logger.output_dir if self.logger else Path("results")
        visit_base = base_dir / "visits" / visit_id
        script_dir = visit_base / "coder_scripts"
        results_dir = visit_base / "figures"
        script_dir.mkdir(parents=True, exist_ok=True)
        results_dir.mkdir(parents=True, exist_ok=True)
        
        generated_files = []



        def save_plot(filename: str, fig=None, **kwargs):
            """
            Helper to save plot from sandbox - must be called with lock held.
            
            Args:
                filename: Target filename (will be saved in results_dir)
                fig: Optional figure object or Seaborn grid (e.g., FacetGrid). 
                     If None, uses plt.gcf().
            """
            # If the user passed a path/filename as first arg, use it
            if not isinstance(filename, str):
                filename = "plot"
            if not filename.endswith('.png'):
                filename += '.png'
            
            # Use timestamp_visit_id_unique_filename format for sorting
            # Format: YYYYMMDD_HHMMSS_ffffff_uuid_filename.png
            dt = datetime.now()
            ts_str = dt.strftime("%Y%m%d_%H%M%S_%f")
            
            # Sanitize filename
            safe_filename = filename.replace("/", "_").replace("\\", "_")
            
            # Add UUID for absolute uniqueness across parallel processes/threads
            unique_id = uuid.uuid4().hex[:6]
            safe_name = f"{ts_str}_{unique_id}_{safe_filename}"
            path = results_dir / safe_name
            
            # Use plt.gcf().savefig directly to avoid any monkey-patching issues
            try:
                # Handle Seaborn Grid objects (FacetGrid, JointGrid, etc.)
                if fig is not None and hasattr(fig, 'savefig'):
                    target_fig = fig
                elif fig is not None and hasattr(fig, 'fig'): # Handle Grid objects with .fig attribute
                    target_fig = fig.fig
                else:
                    target_fig = plt.gcf()
                
                kwargs.setdefault('bbox_inches', 'tight')
                target_fig.savefig(path, **kwargs)
                plt.close(target_fig)
                
                # Verify file exists on disk
                if not path.exists():
                    print(f"CRITICAL ERROR: Matplotlib failed to save file to {path}")
                else:
                    generated_files.append(str(path))
                    print(f"Saved plot to {path}")
            except Exception as e:
                print(f"CRITICAL ERROR: Matplotlib save failed for {path}: {e}")

        # Acquire lock for ALL matplotlib operations
        with matplotlib_lock:
            try:
                # Create proxy inside lock to ensure thread isolation
                plt_proxy = PltProxy(real_plt, save_plot)

                namespace = {
                    "np": np,
                    "numpy": np,
                    "stats": scipy_stats,
                    "plt": plt_proxy, # Use proxy
                    "sns": sns,
                    "save_plot": save_plot,
                    "heart_rate": [(v.timestamp, v.value) for v in vitals.heart_rate],
                    "systolic_bp": [(v.timestamp, v.value) for v in vitals.systolic_bp],
                    "diastolic_bp": [(v.timestamp, v.value) for v in vitals.diastolic_bp],
                    "spo2": [(v.timestamp, v.value) for v in vitals.spo2],
                    "respiratory_rate": [(v.timestamp, v.value) for v in vitals.respiratory_rate],
                    "temperature": [(v.timestamp, v.value) for v in vitals.temperature],
                    # Pass demographics for agent to use
                    "age": demographics.age if demographics else 30,
                    "gender": demographics.gender if demographics else "unknown",
                    "ethnicity": demographics.ethnicity if demographics else "unknown",
                    "visit_id": visit_id,
                }
                
                # Inject Previous Results into Namespace (Metric Reuse with Safe Casting)
                if previous_results:
                    for r in previous_results:
                        if r.success:
                            key = r.metric_name.replace(" ", "_").lower()
                            val = r.value
                            
                            # Safe casting for numeric values extracted as strings
                            if isinstance(val, str):
                                try:
                                    if '.' in val:
                                        val = float(val)
                                    else:
                                        val = int(val)
                                except (ValueError, TypeError):
                                    pass # Keep as string if cast fails
                                    
                            namespace[key] = val
                
                stdout_capture = io.StringIO()
                stderr_capture = io.StringIO()
                
                try:
                    # 1. Repair (Attempt to fix benign Class A violations)
                    code, repairs = self.repair_code(code, namespace)

                    # Save the executed (repaired) script
                    timestamp = int(time.time())
                    script_name = f"{timestamp}_{uuid.uuid4().hex[:4]}_script.py"
                    script_path = script_dir / script_name
                    
                    try:
                        with open(script_path, "w", encoding="utf-8") as f:
                            # Add a header to indicate this is the repaired code
                            f.write("# Executed Code (Repaired)\n# This code runs in a sandbox with injected variables (vitals, np, plt, etc.)\n\n")
                            
                            # 1. Imports
                            f.write("import numpy as np\n")
                            f.write("import pandas as pd\n")
                            f.write("import matplotlib.pyplot as plt\n")
                            f.write("import seaborn as sns\n")
                            f.write("from scipy import stats\n")
                            f.write("import datetime\n")
                            f.write("\n")

                            # 2. Helpers
                            f.write("# Helper function to simulate sandbox save_plot\n")
                            f.write("def save_plot(filename, fig=None, **kwargs):\n")
                            f.write("    if not filename.endswith('.png'): filename += '.png'\n")
                            f.write("    if fig is None: fig = plt.gcf()\n")
                            f.write("    fig.savefig(filename, **kwargs)\n")
                            f.write("    plt.close(fig)\n")
                            f.write("    print(f'Saved plot to {filename}')\n")
                            f.write("\n")

                            # 3. Data Injection (Serialize Namespace)
                            f.write("# Injected Variables\n")
                            f.write(f"visit_id = {repr(visit_id)}\n")
                            f.write(f"age = {namespace.get('age')}\n")
                            f.write(f"gender = {repr(namespace.get('gender'))}\n")
                            f.write(f"ethnicity = {repr(namespace.get('ethnicity'))}\n")

                            # Serialize Vitals
                            f.write(f"heart_rate = {repr(namespace.get('heart_rate'))}\n")
                            f.write(f"systolic_bp = {repr(namespace.get('systolic_bp'))}\n")
                            f.write(f"diastolic_bp = {repr(namespace.get('diastolic_bp'))}\n")
                            f.write(f"spo2 = {repr(namespace.get('spo2'))}\n")
                            f.write(f"respiratory_rate = {repr(namespace.get('respiratory_rate'))}\n")
                            f.write(f"temperature = {repr(namespace.get('temperature'))}\n")

                            # Serialize Previous Results
                            # We iterate over keys in namespace that were injected from previous_results
                            # We can't easily know which ones came from previous results without checking the object,
                            # but we can check the `previous_results` list again.
                            if previous_results:
                                f.write("# Previous Results\n")
                                for r in previous_results:
                                    if r.success:
                                        key = r.metric_name.replace(" ", "_").lower()
                                        val = namespace.get(key)
                                        f.write(f"{key} = {repr(val)}\n")
                            
                            f.write("\n# --- Generated Code Starts Here ---\n")
                            f.write(code)
                    except Exception as e:
                        print(f"Failed to save script: {e}")
                    
                    # 2. Validate (Strict check for Class B violations)
                    self.validate_code(code, namespace)

                    # 3. Execute (Run the code in a sandboxed environment)
                    with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                        # Set style
                        sns.set_theme(style="whitegrid")
                        # Restrict builtins for safety
                        safe_builtin_names = {
                            'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 
                            'classmethod', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'filter', 
                            'float', 'format', 'frozenset', 'getattr', 'hasattr', 'hash', 'help', 'hex', 'id', 
                            'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'map', 'max', 'min', 
                            'next', 'object', 'oct', 'ord', 'pow', 'print', 'property', 'range', 'repr', 
                            'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 
                            'sum', 'super', 'tuple', 'type', 'vars', 'zip', '__import__', # __import__ allowed for safe modules, AST validation blocks unsafe ones
                            'True', 'False', 'None', 'Ellipsis', 'NotImplemented',
                            'Exception', 'ValueError', 'TypeError', 'IndexError', 'KeyError', 'AttributeError', 
                            'ImportError', 'ModuleNotFoundError', 'NameError', 'SyntaxError', 'IndentationError', 
                            'ZeroDivisionError', 'OverflowError', 'RuntimeError', 'StopIteration', 'AssertionError'
                        }
                        
                        restricted_builtins = {k: getattr(builtins, k) for k in safe_builtin_names if hasattr(builtins, k)}
                        
                        # Prepare globals with strict builtins
                        # Warning: Python exec works best when __builtins__ is under the key '__builtins__' in the globals dict
                        exec_globals = namespace.copy()
                        exec_globals['__builtins__'] = restricted_builtins
                        
                        exec(code, exec_globals)
                    
                    result_value = namespace.get("result", None)
                    interpretation = namespace.get("interpretation", "")
                    
                    # Convert DataFrame to dict to avoid truthiness ambiguity
                    # ("The truth value of a DataFrame is ambiguous")
                    if result_value is not None and hasattr(result_value, 'to_dict'):
                        result_value = result_value.to_dict()
                    
                    return CalculationResult(
                        success=True,
                        metric_name="",
                        value=result_value,
                        interpretation=interpretation,
                        image_paths=generated_files,  # Return all generated plots
                        script_path=str(script_path)
                    )
                except Exception as e:
                    return CalculationResult(
                        success=False,
                        metric_name="",
                        value=None,
                        error_message=f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}",
                    )
                finally:
                    # Cleanup matplotlib state
                    plt.close('all')
            finally:
                pass
