"""
Research Transparency Logger - Comprehensive logging for scientific reproducibility.

Captures ALL LLM interactions, intermediate results, configurations, and outputs
to ensure experiments can be verified and audited.
"""

import json
import hashlib
import uuid
import threading
import sys
import importlib.metadata
import subprocess
import ast
from datetime import datetime
from pathlib import Path
from typing import Optional, Literal
from dataclasses import dataclass, field, asdict
from contextlib import contextmanager


@dataclass
class LLMCall:
    """Record of a single LLM API call."""
    call_id: str
    timestamp: str
    
    # Model configuration
    model_name: str
    temperature: float
    max_tokens: Optional[int] = None
    
    # Input
    system_prompt: str = ""
    user_prompt: str = ""
    full_messages: list = field(default_factory=list)
    
    # Output
    response_text: str = ""
    response_tokens: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    reasoning_tokens: int = 0
    total_tokens: int = 0
    latency_ms: float = 0.0
    
    # Context
    agent_name: str = ""  # planner, coder, retriever, reviewer, zero_shot
    task_description: str = ""
    visit_id: str = ""
    
    # Checksums for verification
    input_hash: str = ""
    output_hash: str = ""
    
    # Structured Data
    parsed_json: Optional[dict | list] = None


@dataclass
class AgentStep:
    """Record of a single agent step in the pipeline."""
    step_id: str
    timestamp: str
    agent_name: str
    
    # Input
    input_data: dict = field(default_factory=dict)
    
    # Processing
    llm_calls: list[str] = field(default_factory=list)  # References to LLMCall IDs
    calculations: list[dict] = field(default_factory=list)
    retrievals: list[dict] = field(default_factory=list)
    
    # Output
    output_data: dict = field(default_factory=dict)
    
    # Timing
    duration_ms: float = 0.0


@dataclass
class ExperimentRun:
    """Complete record of an experiment run."""
    run_id: str
    experiment_name: str
    started_at: str
    completed_at: str = ""
    
    # Configuration
    config: dict = field(default_factory=dict)
    model_config: dict = field(default_factory=dict)
    random_seed: int = 444
    
    # Data
    sample_size: int = 0
    visit_ids: list[str] = field(default_factory=list)
    
    # Results
    approach: Literal["zero_shot", "agentic"] = "agentic"
    metrics: dict = field(default_factory=dict)
    
    # Traceability
    agent_steps: list[str] = field(default_factory=list)  # References to AgentStep IDs
    llm_calls: list[str] = field(default_factory=list)  # All LLM call IDs
    
    # Reproducibility
    git_commit: str = ""
    python_version: str = ""
    package_versions: dict = field(default_factory=dict)


class ResearchLogger:
    """
    Comprehensive logging for research transparency.
    
    Captures every LLM call, agent step, and experiment result with full
    provenance for scientific reproducibility and auditability.
    """
    
    def __init__(self, output_dir: Path = None):
        self.output_dir = output_dir or Path("results/logs")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Storage
        self.llm_calls: dict[str, LLMCall] = {}
        self.agent_steps: dict[str, AgentStep] = {}
        self.experiment_runs: dict[str, ExperimentRun] = {}
        
        # Current context - Thread Local Storage
        self._context = threading.local()
        # Initialize thread local defaults in case access happens before context manager
        self._context.visit_id = None
        
        self._current_run_id: Optional[str] = None

        self._lock = threading.Lock()
    
    def _generate_id(self) -> str:
        """Generate unique ID for records."""
        return str(uuid.uuid4())[:8]
    
    def _timestamp(self) -> str:
        """Generate ISO timestamp."""
        return datetime.now().isoformat()
    
    def _hash_content(self, content: str) -> str:
        """Generate SHA-256 hash of content."""
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    @contextmanager
    def experiment_context(
        self,
        experiment_name: str,
        approach: str,
        config: dict,
        sample_size: int,
    ):
        """Context manager for experiment runs."""
        run = ExperimentRun(
            run_id=self._generate_id(),
            experiment_name=experiment_name,
            started_at=self._timestamp(),
            config=config,
            approach=approach,
            sample_size=sample_size,
        )
        
        # Capture environment
        run.python_version = self._get_python_version()
        run.package_versions = self._get_package_versions()
        run.git_commit = self._get_git_commit()
        
        self._current_run_id = run.run_id
        self.experiment_runs[run.run_id] = run
        
        try:
            yield run
        finally:
            run.completed_at = self._timestamp()
            self._current_run_id = None
            self._save_experiment(run)
    
    @contextmanager
    def visit_context(self, visit_id: str):
        """Context manager for processing a visit."""
        # Set thread-local visit_id
        previous_visit_id = getattr(self._context, 'visit_id', None)
        self._context.visit_id = visit_id
        
        # Experiment run is global/shared, so we lock when modifying it
        if self._current_run_id:
             with self._lock:
                if self._current_run_id in self.experiment_runs:
                    self.experiment_runs[self._current_run_id].visit_ids.append(visit_id)
        
        try:
            yield
        finally:
            self._context.visit_id = previous_visit_id
    
    def log_llm_call(
        self,
        model_name: str,
        temperature: float,
        system_prompt: str,
        user_prompt: str,
        response_text: str,
        agent_name: str = "",
        task_description: str = "",
        latency_ms: float = 0.0,
        full_messages: list = None,
        max_tokens: int = None,
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
        reasoning_tokens: int = 0,
        parsed_json: Optional[dict | list] = None,
    ) -> str:
        """
        Log an LLM API call with full input/output.
        
        Returns:
            call_id for reference
        """
        # Ensure prompts are strings for hashing
        str_system = str(system_prompt) if not isinstance(system_prompt, str) else system_prompt
        str_user = str(user_prompt) if not isinstance(user_prompt, str) else user_prompt
        
        # Get visit_id from thread local storage
        current_visit_id = getattr(self._context, 'visit_id', "") or ""
        
        # Ensure response_text is string for consistency and hashing
        if not isinstance(response_text, str):
            response_text = str(response_text)

        call = LLMCall(
            call_id=self._generate_id(),
            timestamp=self._timestamp(),
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            system_prompt=str_system,
            user_prompt=str_user,
            full_messages=full_messages or [],
            response_text=response_text,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            reasoning_tokens=reasoning_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            latency_ms=latency_ms,
            agent_name=agent_name,
            task_description=task_description,
            visit_id=current_visit_id,
            input_hash=self._hash_content(str_system + str_user),
            output_hash=self._hash_content(response_text),
            parsed_json=parsed_json,
        )
        
        with self._lock:
            self.llm_calls[call.call_id] = call
            
            # Link to current experiment
            if self._current_run_id and self._current_run_id in self.experiment_runs:
                self.experiment_runs[self._current_run_id].llm_calls.append(call.call_id)
        
        # Save immediately for durability
        self._save_llm_call(call)
        
        return call.call_id
    
    def log_error(self, message: str, error: Exception = None):
        """Log an error message for debugging."""
        timestamp = self._timestamp()
        error_msg = f"[{timestamp}] ERROR: {message}"
        if error:
            error_msg += f"\nException: {str(error)}"
        
        # Print to console for immediate visibility
        print(error_msg)
        
        # Save to error log file
        errors_dir = self.output_dir / "errors"
        errors_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = errors_dir / f"error_{self._generate_id()}.txt"
        with open(filepath, "w") as f:
            f.write(error_msg)

    def log_warning(self, message: str):
        """Log a warning message."""
        timestamp = self._timestamp()
        warn_msg = f"[{timestamp}] WARNING: {message}"
        print(warn_msg)

    def log_recovery(self, message: str, original_error: Exception = None):
        """Log a successful recovery from an error (e.g., JSON repair)."""
        timestamp = self._timestamp()
        log_msg = f"[{timestamp}] RECOVERY: {message}"
        if original_error:
            log_msg += f"\nOriginal Exception: {str(original_error)}"
            if hasattr(original_error, 'doc'): # JSONDecodeError specific
                 log_msg += f"\nOriginal Doc (Snippet): {original_error.doc[:500]}..."

        # Print to console for immediate visibility
        print(log_msg)
        
        # Save to dedicated recovery log file
        recoveries_dir = self.output_dir / "recoveries"
        recoveries_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = recoveries_dir / f"recovery_{self._generate_id()}.txt"
        with open(filepath, "w") as f:
            f.write(log_msg)
    
    def log_agent_step(
        self,
        agent_name: str,
        input_data: dict,
        output_data: dict,
        llm_call_ids: list[str] = None,
        calculations: list[dict] = None,
        retrievals: list[dict] = None,
        duration_ms: float = 0.0,
    ) -> str:
        """
        Log an agent step with all inputs, outputs, and intermediate results.
        
        Returns:
            step_id for reference
        """
        step = AgentStep(
            step_id=self._generate_id(),
            timestamp=self._timestamp(),
            agent_name=agent_name,
            input_data=input_data,
            output_data=output_data,
            llm_calls=llm_call_ids or [],
            calculations=calculations or [],
            retrievals=retrievals or [],
            duration_ms=duration_ms,
        )
        
        with self._lock:
            self.agent_steps[step.step_id] = step
            
            if self._current_run_id and self._current_run_id in self.experiment_runs:
                self.experiment_runs[self._current_run_id].agent_steps.append(step.step_id)
        
        self._save_agent_step(step)
        
        return step.step_id
    
    def log_experiment_metrics(self, metrics: dict):
        """Log final experiment metrics."""
        with self._lock:
            if self._current_run_id and self._current_run_id in self.experiment_runs:
                self.experiment_runs[self._current_run_id].metrics = metrics
    
    def _save_llm_call(self, call: LLMCall):
        """Save LLM call to disk."""
        # Determine directory based on visit_id
        if call.visit_id:
            # results/logs/visits/<visit_id>/llm_calls/
            calls_dir = self.output_dir / "visits" / call.visit_id / "llm_calls"
        else:
            # results/logs/llm_calls/ (global/setup calls)
            calls_dir = self.output_dir / "llm_calls"
            
        calls_dir.mkdir(parents=True, exist_ok=True)
        
        # Format: YYYYMMDD_HHMMSS_ffffff_<model>_<call_id>.json
        # Convert ISO timestamp to suitable filename format
        try:
            dt = datetime.fromisoformat(call.timestamp)
            ts_str = dt.strftime("%Y%m%d_%H%M%S_%f")
        except ValueError:
            ts_str = call.timestamp.replace(":", "").replace("-", "").replace("T", "_")

        sanitized_model = call.model_name.replace("/", "_").replace(":", "")
        filename = f"{ts_str}_{sanitized_model}_{call.call_id}.json"
        
        filepath = calls_dir / filename
        
        # Prepare data for logging
        data = asdict(call)
        
        # Optimize storage: If parsed_json exists, we don't need the raw string response
        if data.get("parsed_json") is not None:
             data.pop("response_text", None)
             
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2, default=str)
    
    def _save_agent_step(self, step: AgentStep):
        """Save agent step to disk."""
        # Retrieve visit_id from context/input/output if possible since it's not directly on AgentStep
        # We'll check the thread local context first
        visit_id = getattr(self._context, 'visit_id', None)
        
        # Fallback: Check input_data for visit_id
        if not visit_id and "visit_id" in step.input_data:
            visit_id = step.input_data["visit_id"]
            
        if visit_id:
            # results/logs/visits/<visit_id>/agent_steps/
            steps_dir = self.output_dir / "visits" / visit_id / "agent_steps"
        else:
            steps_dir = self.output_dir / "agent_steps"
            
        steps_dir.mkdir(parents=True, exist_ok=True)
        
        # Format: YYYYMMDD_HHMMSS_ffffff_<agent>_<step_id>.json
        try:
            dt = datetime.fromisoformat(step.timestamp)
            ts_str = dt.strftime("%Y%m%d_%H%M%S_%f")
        except ValueError:
            ts_str = step.timestamp.replace(":", "").replace("-", "").replace("T", "_")

        filename = f"{ts_str}_{step.agent_name}_{step.step_id}.json"
        
        filepath = steps_dir / filename
        with open(filepath, "w") as f:
            json.dump(asdict(step), f, indent=2, default=str)
    
    def _save_experiment(self, run: ExperimentRun):
        """Save experiment run to disk."""
        runs_dir = self.output_dir / "experiments"
        runs_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = runs_dir / f"{run.run_id}_{run.experiment_name}.json"
        with open(filepath, "w") as f:
            json.dump(asdict(run), f, indent=2, default=str)
        
        # Also save a summary with all linked data
        self._save_full_experiment_trace(run)
    
    def _save_full_experiment_trace(self, run: ExperimentRun):
        """Save complete experiment trace with all linked data."""
        with self._lock:
            trace = {
                "experiment": asdict(run),
                "llm_calls": [
                    asdict(self.llm_calls[cid]) 
                    for cid in run.llm_calls 
                    if cid in self.llm_calls
                ],
                "agent_steps": [
                    asdict(self.agent_steps[sid])
                    for sid in run.agent_steps
                    if sid in self.agent_steps
                ],
            }
        
        traces_dir = self.output_dir / "full_traces"
        traces_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = traces_dir / f"{run.run_id}_full_trace.json"
        with open(filepath, "w") as f:
            json.dump(trace, f, indent=2, default=str)
    
    def _get_python_version(self) -> str:
        """Get Python version."""
        return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    
    def _get_package_versions(self) -> dict:
        """Get relevant package versions."""
        versions = {}
        packages = ["langchain", "openai", "pandas", "numpy", "scikit-learn"]
        
        for pkg in packages:
            try:
                versions[pkg] = importlib.metadata.version(pkg)
            except Exception:
                versions[pkg] = "unknown"
        
        return versions
    
    def _get_git_commit(self) -> str:
        """Get current git commit hash."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip()[:8] if result.returncode == 0 else ""
        except Exception:
            return ""

    def export_logs_to_markdown(self, run_id: str):
        """
        Export full conversation history for each agent in every visit to Markdown.
        Structure: results/logs/md-<run_id>-<visit_id>/<agent_name>.md
        """        
        with self._lock:
            if run_id not in self.experiment_runs:
                return
            run = self.experiment_runs[run_id]
            
            # Group calls by visit_id -> agent_name
            # visit_id -> agent_name -> list[LLMCall]
            grouped_calls = {}
            
            # We iterate through all calls in the run
            for call_id in run.llm_calls:
                if call_id not in self.llm_calls:
                    continue
                call = self.llm_calls[call_id]
                
                if not call.visit_id:
                    continue
                    
                if call.visit_id not in grouped_calls:
                    grouped_calls[call.visit_id] = {}
                
                # Normalize agent name
                agent = call.agent_name.lower() or "unknown"
                if agent not in grouped_calls[call.visit_id]:
                    grouped_calls[call.visit_id][agent] = []
                
                grouped_calls[call.visit_id][agent].append(call)
        
        # Write files (outside lock to minimize contention, though data is already copied references)
        # Note: Thread safety regarding 'call' objects: they are dataclasses and effectively immutable after creation
        
        # New Structure: results/logs/visits/<visit_id>/markdown_logs/
        
        for visit_id, agents in grouped_calls.items():
            # Create directory for this visit
            visit_dir = self.output_dir / "visits" / visit_id / "markdown_logs"
            visit_dir.mkdir(parents=True, exist_ok=True)
            
            for agent_name, calls in agents.items():
                # Sort calls by timestamp
                calls.sort(key=lambda x: x.timestamp)
                
                # Build markdown content
                md_lines = [
                    f"# Conversation Log: {agent_name.title()}",
                    f"**Visit ID:** {visit_id}",
                    f"**Run ID:** {run_id}",
                    f"**Total Calls:** {len(calls)}",
                    "",
                    "---"
                ]

                def format_multimodal_prompt(p_str):
                    """Helper to render list-based multimodal prompts as markdown."""
                    try:
                        p_str = p_str.strip()
                        # If it looks like a list repr
                        if p_str.startswith('[') and p_str.endswith(']'):
                            content = ast.literal_eval(p_str)
                            if isinstance(content, list):
                                parts = []
                                for item in content:
                                    if isinstance(item, dict):
                                        if item.get('type') == 'text':
                                            parts.append(item.get('text', ''))
                                        elif item.get('type') == 'image_url':
                                            url = item.get('image_url', {}).get('url', '')
                                            parts.append(f"\n![Image]({url})\n")
                                return "\n".join(parts)
                    except Exception:
                        # Fallback to original string if not parsable
                        pass
                    return p_str

                for i, call in enumerate(calls):
                    md_lines.extend([
                        f"## Call {i+1}",
                        f"**Timestamp:** {call.timestamp}",
                        f"**Model:** {call.model_name}",
                        f"**Latency:** {call.latency_ms:.0f}ms",
                        f"**Tokens:** {call.total_tokens} (Prompt: {call.prompt_tokens}, Completion: {call.completion_tokens})",
                        "",
                        "### 1. System Prompt",
                        call.system_prompt,
                        "",
                        "### 2. User Prompt",
                        format_multimodal_prompt(call.user_prompt),
                        "",
                        "### 3. Response",
                        "```json",
                        call.response_text,
                        "```",
                        "",
                        "---",
                        ""
                    ])
                
                # Write to file
                filepath = visit_dir / f"{agent_name}.md"
                try:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write("\n".join(md_lines))
                except Exception as e:
                    print(f"Failed to write log for {visit_id}/{agent_name}: {e}")


# Global logger instance
_logger: Optional[ResearchLogger] = None


def get_logger() -> ResearchLogger:
    """Get or create the global research logger."""
    global _logger
    if _logger is None:
        _logger = ResearchLogger()
    return _logger


def configure_logger(output_dir: Path) -> ResearchLogger:
    """
    Re-configure the global logger to use a specific output directory.
    Useful for separating logs by model or experiment run.
    """
    global _logger
    _logger = ResearchLogger(output_dir=output_dir)
    return _logger
