"""
Unified Comparison Experiment.
"""

from typing import Optional, Sequence, Union
from dataclasses import asdict
from pathlib import Path
import json
from datetime import datetime
from sklearn.metrics import accuracy_score, cohen_kappa_score, mean_absolute_error, mean_squared_error, precision_score, recall_score, f1_score
import numpy as np
import concurrent.futures
from tqdm import tqdm

from ..config import config
from ..data.schema import PatientVisit
from ..data.loaders import VisitsLoader, NumericsLoader, PMHLoader, MedsLoader
from ..agents.zero_shot import ZeroShotBaseline
from ..agents.orchestrator import AgentOrchestrator
from ..prompts import ClinicalOutput
from ..logging import get_logger
from .results import ComparisonResult, ExperimentResults, build_ground_truth, convert_agentic_output


class UnifiedComparisonExperiment:
    """
    Runs comparison between Zero-Shot and Agentic approaches.
    """
    
    def __init__(
        self,
        visits_loader: VisitsLoader,
        numerics_loader: Optional[NumericsLoader] = None,
        model_name: Optional[str] = None,
    ):
        self.visits_loader = visits_loader
        self.numerics_loader = numerics_loader
        self.model_name = model_name
        
        # Additional Context Loaders
        self.pmh_loader = PMHLoader(config.dataset.visits_path.parent / "pmh.csv")
        self.meds_loader = MedsLoader(config.dataset.visits_path.parent / "meds.csv")
        
        # Initialize both approaches (no external data loaders)
        self.zero_shot = ZeroShotBaseline(model_name)
        self.agentic = AgentOrchestrator(model_name)
        
        self.logger = get_logger()
    
    @staticmethod
    def _safe_mean(values: Sequence[Union[float, int]]) -> float:
        """Calculate mean safely, returning 0.0 for empty lists."""
        return float(np.mean(values)) if values else 0.0

    @staticmethod
    def _safe_rmse(values: Sequence[Union[float, int]]) -> float:
        """Calculate RMSE from a list of errors/differences."""
        if not values:
            return 0.0
        return float(np.sqrt(np.mean(np.square(values))))
    
    def _process_single_visit(self, visit: PatientVisit) -> Optional[ComparisonResult]:
        """Process a single visit (designed for parallel execution)."""
        # 1. Get visit context
        try:
            with self.logger.visit_context(visit.visit_id):
                # Get vitals
                vitals = None
                if self.numerics_loader:
                     vitals = self.numerics_loader.get_vitals_for_visit(visit.visit_id)
                
                # Fetch Patient Context (Meds + PMH) using Patient ID (MRN)
                pmh = self.pmh_loader.get_history(visit.patient_id)
                meds = self.meds_loader.get_medications(visit.patient_id)
                
                # Extract simple lists for agents
                pmh_list = pmh.conditions
                meds_list = [f"{m.name} ({m.med_class})" if m.med_class else m.name for m in meds]
                
                # Skip visit if no vital sign data is available
                if not vitals or not vitals.has_data():
                    return None
                    
                # Build ground truth
                ground_truth = build_ground_truth(visit, vitals)
                
                # Run Zero-Shot
                start_zs = datetime.now()
                zs_output = self.zero_shot.process_visit(
                    visit, vitals, pmh=pmh_list, meds=meds_list
                )
                zs_output.duration_seconds = (datetime.now() - start_zs).total_seconds()
                
                # Run Agentic
                # Create a fresh orchestrator per visit to avoid shared state contamination
                # across parallel executions. Agents have internal memory that gets polluted if shared.
                start_ag = datetime.now()
                agentic_orchestrator = AgentOrchestrator(self.model_name)
                ag_result = agentic_orchestrator.process_visit(
                    visit, vitals, pmh=pmh_list, meds=meds_list, progress_callback=None
                )
                ag_output = convert_agentic_output(ag_result, visit)
                ag_output.duration_seconds = (datetime.now() - start_ag).total_seconds()
                
                return ComparisonResult(
                    visit_id=visit.visit_id,
                    ground_truth=ground_truth,
                    demographics={
                        "age": visit.demographics.age,
                        "gender": visit.demographics.gender,
                        "ethnicity": visit.demographics.ethnicity,
                        "insurance": visit.demographics.insurance_class,
                        "arrival_mode": visit.arrival_mode,
                        "comorbidity_count": len(pmh_list),
                        "medication_count": len(meds_list),
                    },
                    zero_shot_output=zs_output,
                    agentic_output=ag_output,
                )
        except Exception as e:
            self.logger.log_error(f"Error processing visit {visit.visit_id}: {e}")
            return None
    
    def run(
        self, 
        sample_size: int = 100,
        output_dir: Optional[Path] = None,
    ) -> ExperimentResults:
        """
        Run comparison experiment with full logging.
        """
        output_dir = output_dir or config.experiment.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Build experiment config for logging
        exp_config = {
            "model_name": self.model_name or config.model.default_model,
            "sample_size": sample_size,
            "dataset_path": str(config.dataset.visits_path),
            "random_seed": config.experiment.random_seed,
            "architecture": "agentic_coder",
        }
        
        results = ExperimentResults(
            experiment_name="Unified Comparison (Coder-Focused)",
            sample_size=sample_size,
        )
        
        # Use logging context for experiment
        with self.logger.experiment_context(
            experiment_name="unified_comparison",
            approach="both",
            config=exp_config,
            sample_size=sample_size,
        ) as exp_run:
            start_experiment = datetime.now()
            
            verified_count = 0
            visit_count = 0
            
            # --- Check for existing results to skip ---
            existing_results_path = output_dir / "full_results.json"
            processed_visit_ids = set()
            if existing_results_path.exists():
                try:
                    with open(existing_results_path, "r") as f:
                        existing_data = json.load(f)
                    
                    if "per_visit_results" in existing_data:
                        print(f"  - Found {len(existing_data['per_visit_results'])} existing results. Loading for skip-check...")
                        for vr in existing_data["per_visit_results"]:
                            comp = ComparisonResult.from_dict(vr)
                            results.results.append(comp)
                            processed_visit_ids.add(comp.visit_id)
                            visit_count += 1
                            
                            # Pre-populate metrics for aggregation
                            ground_truth = comp.ground_truth
                            zs_output = comp.zero_shot_output
                            ag_output = comp.agentic_output
                            
                            if ag_output and ag_output.verified:
                                verified_count += 1
                        
                        print(f"  - Successfully resumed {len(processed_visit_ids)} already processed visits.")
                except Exception as e:
                    self.logger.log_error(f"Error loading existing results: {e}. Starting fresh.")
                    results.results = []
                    visit_count = 0
                    verified_count = 0
                    processed_visit_ids = set()

            # Create thread pool
            max_workers = 3 # Reduced to avoid Vertex AI 429 Resource Exhausted errors
            
            # Collect all visits first, skipping already processed ones
            all_visits = []
            needed_samples = sample_size - len(processed_visit_ids)
            
            if needed_samples > 0:
                print(f"  - Target sample size: {sample_size}. Need {needed_samples} more visits.")
                for visit in self.visits_loader.iter_visits():
                    if len(all_visits) >= needed_samples:
                        break
                    if visit.triage_acuity is None:
                        continue
                    if visit.visit_id in processed_visit_ids:
                        continue
                    all_visits.append(visit)
            else:
                print(f"  - Target sample size {sample_size} already met by {len(processed_visit_ids)} processed visits. Skipping new work.")
            
            # Ensure sample size reflects total (existing + new)
            # ExperimentResults sample_size should ideally represent the target/requested size
            # but here it seems to represent the actual count being processed or available.
            
            # Create tqdm progress bar for ONLY the new visits
            model_name = self.model_name or config.model.default_model
            pbar = tqdm(
                total=len(all_visits),
                desc=f"[{model_name}] Resuming",
                unit="visit",
                ncols=120,
            )
            
            if all_visits:
                with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                    # Submit all tasks
                    future_to_visit = {
                        executor.submit(self._process_single_visit, visit): visit 
                        for visit in all_visits
                    }
                    
                    for future in concurrent.futures.as_completed(future_to_visit):
                        pbar.update(1)
                        try:
                            comparison = future.result()
                            if comparison:
                                visit_count += 1
                                results.results.append(comparison)
                                
                                ground_truth = comparison.ground_truth
                                zs_output = comparison.zero_shot_output
                                ag_output = comparison.agentic_output
                                
                                # Set postfix
                                zs_esi = zs_output.esi_level or "?"
                                ag_esi = ag_output.esi_level or "?"
                                gt_esi = ground_truth.esi if ground_truth.esi is not None else "?"
                                pbar.set_postfix_str(f"Last: GT={gt_esi} ZS={zs_esi} AG={ag_esi}", refresh=True)
                                
                                if ag_output.verified:
                                    verified_count += 1
                                    
                                # Incremental Save: Ensure data is persisted immediately
                                self._save_results(results, output_dir)
                            else:
                                # Visit processing returned None - track as failure
                                visit = future_to_visit[future]
                                results.failed_visits.append(visit.visit_id)
                                results.failed_errors[visit.visit_id] = "Processing returned None (check logs for details)"
                                    
                        except Exception as e:
                            # Track failed visit with error message
                            visit = future_to_visit[future]
                            results.failed_visits.append(visit.visit_id)
                            results.failed_errors[visit.visit_id] = str(e)
                            self.logger.log_error(f"Unexpected error in thread for visit {visit.visit_id}: {e}") 
            
            pbar.close()
            
            results.total_duration_seconds = (datetime.now() - start_experiment).total_seconds()
            
            # --- Calculate Aggregated Metrics ---
            # Use shared recalculation logic to ensure consistency and include new metrics (qSOFA, MAP)
            self._recalculate_metrics(results)
            
            # --- Cost & Efficiency ---
            # Retrieve all LLM calls for this experiment run
            if exp_run.run_id in self.logger.experiment_runs:
                 run_record = self.logger.experiment_runs[exp_run.run_id]
                 for call_id in run_record.llm_calls:
                     if call_id in self.logger.llm_calls:
                         call = self.logger.llm_calls[call_id]
                         results.total_prompt_tokens += call.prompt_tokens
                         results.total_completion_tokens += call.completion_tokens
            
            # Pricing (approximate per 1M tokens)
            PRICING = {
                # OpenAI - GPT-5.2 API (standard)
                "gpt-5.2": {"input": 1.75,   "output": 14.00},
                # Google - Gemini 3 Pro (standard context <=200K tokens)
                "gemini-3-pro": {"input": 2.00,   "output": 12.00},
                # Anthropic - Claude Opus 4.5 (premium 4.5 variant)
                "claude-4.5-opus": {"input": 5.00,   "output": 25.00},
                # Llama 4 Maverick
                "llama-4": {"input": 0.35,   "output": 1.15}
            }
            
            # Determine pricing model
            model_key = "not_found"
            for k in PRICING.keys():
                if k in self.model_name.lower():
                    model_key = k
                    break
            
            if model_key not in PRICING:
                self.logger.log_warning(f"Pricing not found for model {self.model_name}, defaulting to 0.")
                rates = {"input": 0.0, "output": 0.0}
            else:
                rates = PRICING[model_key]
            input_cost = (results.total_prompt_tokens / 1_000_000) * rates["input"]
            output_cost = (results.total_completion_tokens / 1_000_000) * rates["output"]
            results.total_cost = input_cost + output_cost
            
            # Log final metrics
            self.logger.log_experiment_metrics({
                "zs_esi_accuracy": results.zs_esi_accuracy,
                "zs_esi_mae": results.zs_esi_mae,
                "zs_esi_rmse": results.zs_esi_rmse,
                "zs_esi_precision": results.zs_esi_precision,
                "zs_esi_recall": results.zs_esi_recall,
                "zs_esi_f1": results.zs_esi_f1,
                
                "zs_pain_mae": results.zs_pain_mae,
                "zs_pain_rmse": results.zs_pain_rmse,
                "zs_los_mae": results.zs_los_mae,
                "zs_los_rmse": results.zs_los_rmse,
                "zs_si_mae": results.zs_shock_index_mae,
                
                "ag_esi_accuracy": results.ag_esi_accuracy,
                "ag_esi_mae": results.ag_esi_mae,
                "ag_esi_rmse": results.ag_esi_rmse,
                "ag_esi_precision": results.ag_esi_precision,
                "ag_esi_recall": results.ag_esi_recall,
                "ag_esi_f1": results.ag_esi_f1,
                
                "ag_pain_mae": results.ag_pain_mae,
                "ag_pain_rmse": results.ag_pain_rmse,
                "ag_los_mae": results.ag_los_mae,
                "ag_los_rmse": results.ag_los_rmse,
                "ag_si_mae": results.ag_shock_index_mae,
                
                "ag_verified_rate": verified_count / visit_count if visit_count > 0 else 0,
                
                "efficiency": {
                    "prompt_tokens": results.total_prompt_tokens,
                    "completion_tokens": results.total_completion_tokens,
                    "cost_usd": results.total_cost,
                    "total_duration_seconds": results.total_duration_seconds
                }
            })
        
        # Save results
        self._save_results(results, output_dir)
        
        # Save failed visits to separate file for retry capability
        if results.failed_visits:
            failed_path = output_dir / "failed_visits.json"
            failed_data = {
                "model": self.model_name,
                "timestamp": datetime.now().isoformat(),
                "failed_count": len(results.failed_visits),
                "failed_visits": results.failed_visits,
                "errors": results.failed_errors
            }
            with open(failed_path, "w") as f:
                json.dump(failed_data, f, indent=2)
            print(f"\n⚠️  {len(results.failed_visits)} visits failed. See: {failed_path}")
        
        # Export conversation logs for debugging
        self.logger.export_logs_to_markdown(exp_run.run_id)
        
        return results
    
    def rebuild_from_logs(self, logs_dir: Path, output_dir: Optional[Path] = None) -> ExperimentResults:
        """
        Reconstruct results from a logs directory.
        Finds the latest llm_calls for zero_shot and synthesizer for each visit.
        """
        results = ExperimentResults(
            experiment_name=self.model_name or "Rebuilt Experiment",
            sample_size=0,
            results=[]
        )
        
        visits_dir = logs_dir / "visits"
        if not visits_dir.exists():
            print(f"Error: visits directory not found in {logs_dir}")
            return results
            
        visit_ids = [d.name for d in visits_dir.iterdir() if d.is_dir()]
        print(f"Found {len(visit_ids)} visits in logs.")
        
        for visit_id in tqdm(visit_ids, desc="Rebuilding visits"):
            visit_logs = visits_dir / visit_id / "llm_calls"
            if not visit_logs.exists():
                continue
                
            # Find latest zero_shot and synthesizer calls
            zs_call = None
            ag_call = None
            
            # Sort by timestamp (in filename)
            log_files = sorted(visit_logs.glob("*.json"), reverse=True)
            
            # Fallbacks for ag_call if synthesizer is missing
            fallback_ag_call = None
            
            for f in log_files:
                try:
                    with open(f, 'r') as jf:
                        data = json.load(jf)
                        agent = data.get("agent_name")
                        parsed = data.get("parsed_json")
                        
                        if not parsed:
                            continue
                            
                        # Prioritize explicit synthesizer/zero_shot
                        if not zs_call and agent == "zero_shot":
                            zs_call = parsed
                            print(f"    -> Found Zero-Shot")
                        elif not ag_call and agent == "synthesizer":
                            ag_call = parsed
                            print(f"    -> Found Agentic (Synthesizer)")
                        
                        # Store latest alternative for ag_call if needed
                        if not ag_call and agent in ["doctor", "consultant"]:
                            if fallback_ag_call is None: # Keep the latest one
                                fallback_ag_call = parsed
                                print(f"    (Potential fallback for Agentic: {agent})")
                except Exception as e:
                    continue
                
                if zs_call and ag_call:
                    break
            
            if not ag_call and fallback_ag_call:
                ag_call = fallback_ag_call
                print(f"    -> Using fallback Agentic output")
            
            if not zs_call or not ag_call:
                print(f"  - Missing outputs for {visit_id}: ZS={zs_call is not None}, AG={ag_call is not None}")
                    
            if zs_call and ag_call:
                visit_obj = None
                for v in self.visits_loader.iter_visits():
                    if v.visit_id == visit_id:
                        visit_obj = v
                        break
                
                if not visit_obj:
                    continue
                
                # Fetch vitals if loader is available (Critical for Pain GT)
                vitals = None
                if self.numerics_loader:
                     vitals = self.numerics_loader.get_vitals_for_visit(visit_id)

                comparison = ComparisonResult(
                    visit_id=visit_id,
                    ground_truth=build_ground_truth(visit_obj, vitals),
                    demographics={
                        "age": visit_obj.demographics.age,
                        "gender": visit_obj.demographics.gender,
                        "ethnicity": visit_obj.demographics.ethnicity
                    },
                    zero_shot_output=ClinicalOutput.from_dict(zs_call, visit_id=visit_id, approach="zero_shot"),
                    agentic_output=ClinicalOutput.from_dict(ag_call, visit_id=visit_id, approach="agentic")
                )
                results.results.append(comparison)
                print(f"  + Added visit {visit_id}")
                
        results.sample_size = len(results.results)
        print(f"Total rebuilt: {results.sample_size}")
        
        # Calculate metrics for the rebuilt results
        if results.results:
            self._recalculate_metrics(results)
        
        if output_dir:
            self._save_results(results, output_dir)
            print(f"Rebuilt results saved to {output_dir}")
            
        return results

    def _recalculate_metrics(self, results: ExperimentResults):
        """Helper to recalculate aggregate metrics for ExperimentResults."""
        print(f"Recalculating metrics for {len(results.results)} results...")
        import numpy as np
        from sklearn.metrics import cohen_kappa_score, precision_recall_fscore_support, mean_absolute_error, mean_squared_error
        
        zs_esi_true, zs_esi_pred = [], []
        ag_esi_true, ag_esi_pred = [], []
        zs_pain_err, ag_pain_err = [], []
        zs_los_err, ag_los_err = [], []
        zs_si_err, ag_si_err = [], []
        zs_si_abs, ag_si_abs = [], []
        
        verified_count = 0
        total_loops = 0
        
        for comp in results.results:
            gt = comp.ground_truth
            zs = comp.zero_shot_output
            ag = comp.agentic_output
            
            # ESI
            if gt.esi:
                if zs.esi_level:
                    zs_esi_true.append(gt.esi)
                    zs_esi_pred.append(zs.esi_level)
                if ag.esi_level:
                    ag_esi_true.append(gt.esi)
                    ag_esi_pred.append(ag.esi_level)
            
            # Pain
            if gt.pain is not None:
                if zs.pain_score is not None:
                    zs_pain_err.append(abs(zs.pain_score - gt.pain))
                if ag.pain_score is not None:
                    ag_pain_err.append(abs(ag.pain_score - gt.pain))
                    
            # LOS
            if gt.los is not None:
                if zs.ed_los is not None:
                    zs_los_err.append(abs(zs.ed_los - gt.los))
                if ag.ed_los is not None:
                    ag_los_err.append(abs(ag.ed_los - gt.los))
                    
            # Shock Index
            if gt.shock_index is not None:
                gt_si = gt.shock_index
                if zs.metrics.shock_index is not None:
                    err = abs(zs.metrics.shock_index - gt_si)
                    zs_si_abs.append(err)
                    zs_si_err.append(err > 0.05)
                if ag.metrics.shock_index is not None:
                    err = abs(ag.metrics.shock_index - gt_si)
                    ag_si_abs.append(err)
                    ag_si_err.append(err > 0.05)
            
            if ag.verified:
                verified_count += 1
            if ag.iterations_used:
                total_loops += ag.iterations_used

        # Calculate ZS ESI
        if zs_esi_true:
            results.zs_esi_accuracy = sum(1 for t, p in zip(zs_esi_true, zs_esi_pred) if t == p) / len(zs_esi_true)
            results.zs_esi_mae = mean_absolute_error(zs_esi_true, zs_esi_pred)
            results.zs_esi_rmse = np.sqrt(mean_squared_error(zs_esi_true, zs_esi_pred))
            results.zs_esi_kappa = cohen_kappa_score(zs_esi_true, zs_esi_pred)
            p, r, f, _ = precision_recall_fscore_support(zs_esi_true, zs_esi_pred, average="weighted", zero_division=0)
            results.zs_esi_precision, results.zs_esi_recall, results.zs_esi_f1 = p, r, f

        # Calculate AG ESI
        if ag_esi_true:
            results.ag_esi_accuracy = sum(1 for t, p in zip(ag_esi_true, ag_esi_pred) if t == p) / len(ag_esi_true)
            results.ag_esi_mae = mean_absolute_error(ag_esi_true, ag_esi_pred)
            results.ag_esi_rmse = np.sqrt(mean_squared_error(ag_esi_true, ag_esi_pred))
            results.ag_esi_kappa = cohen_kappa_score(ag_esi_true, ag_esi_pred)
            p, r, f, _ = precision_recall_fscore_support(ag_esi_true, ag_esi_pred, average="weighted", zero_division=0)
            results.ag_esi_precision, results.ag_esi_recall, results.ag_esi_f1 = p, r, f

        # Pain
        if zs_pain_err:
            results.zs_pain_mae = np.mean(zs_pain_err)
            results.zs_pain_rmse = np.sqrt(np.mean(np.square(zs_pain_err)))
            results.zs_pain_acc_tol = sum(1 for e in zs_pain_err if e <= 1) / len(zs_pain_err)
        if ag_pain_err:
            results.ag_pain_mae = np.mean(ag_pain_err)
            results.ag_pain_rmse = np.sqrt(np.mean(np.square(ag_pain_err)))
            results.ag_pain_acc_tol = sum(1 for e in ag_pain_err if e <= 1) / len(ag_pain_err)

        # LOS
        if zs_los_err:
            results.zs_los_mae = np.mean(zs_los_err)
            results.zs_los_rmse = np.sqrt(np.mean(np.square(zs_los_err)))
            results.zs_los_acc_tol = sum(1 for e in zs_los_err if e <= 2) / len(zs_los_err)
        if ag_los_err:
            results.ag_los_mae = np.mean(ag_los_err)
            results.ag_los_rmse = np.sqrt(np.mean(np.square(ag_los_err)))
            results.ag_los_acc_tol = sum(1 for e in ag_los_err if e <= 2) / len(ag_los_err)

        # SI
        if zs_si_abs:
            results.zs_shock_index_mae = np.mean(zs_si_abs)
            results.zs_shock_index_error_rate = np.mean(zs_si_err)
        if ag_si_abs:
            results.ag_shock_index_mae = np.mean(ag_si_abs)
            results.ag_shock_index_error_rate = np.mean(ag_si_err)
            
        # MAP
        zs_map_err, ag_map_err = [], []
        
        # qSOFA 
        zs_qsofa_true, zs_qsofa_pred = [], []
        ag_qsofa_true, ag_qsofa_pred = [], []

        # Rerun loop to gather new metrics from results
        for comp in results.results:
            gt = comp.ground_truth
            zs = comp.zero_shot_output
            ag = comp.agentic_output
            
            # MAP
            if gt.map_value is not None:
                if zs.metrics.map_value is not None:
                    zs_map_err.append(abs(zs.metrics.map_value - gt.map_value))
                if ag.metrics.map_value is not None:
                    ag_map_err.append(abs(ag.metrics.map_value - gt.map_value))
                    
            # qSOFA
            if gt.qsofa_score is not None:
                if zs.metrics.qsofa_score is not None:
                    zs_qsofa_true.append(gt.qsofa_score)
                    zs_qsofa_pred.append(zs.metrics.qsofa_score)
                if ag.metrics.qsofa_score is not None:
                    ag_qsofa_true.append(gt.qsofa_score)
                    ag_qsofa_pred.append(ag.metrics.qsofa_score)

        # Calculate MAP Metrics
        if zs_map_err:
            results.zs_map_mae = np.mean(zs_map_err)
            results.zs_map_rmse = np.sqrt(np.mean(np.square(zs_map_err)))
            results.zs_map_acc_tol = sum(1 for e in zs_map_err if e <= 10) / len(zs_map_err)
            
        if ag_map_err:
            results.ag_map_mae = np.mean(ag_map_err)
            results.ag_map_rmse = np.sqrt(np.mean(np.square(ag_map_err)))
            results.ag_map_acc_tol = sum(1 for e in ag_map_err if e <= 10) / len(ag_map_err)

        # Calculate qSOFA Metrics (ZS)
        if zs_qsofa_true:
            results.zs_qsofa_accuracy = sum(1 for t, p in zip(zs_qsofa_true, zs_qsofa_pred) if t == p) / len(zs_qsofa_true)
            results.zs_qsofa_mae = mean_absolute_error(zs_qsofa_true, zs_qsofa_pred)
            results.zs_qsofa_rmse = np.sqrt(mean_squared_error(zs_qsofa_true, zs_qsofa_pred))
            results.zs_qsofa_kappa = cohen_kappa_score(zs_qsofa_true, zs_qsofa_pred)
            p, r, f, _ = precision_recall_fscore_support(zs_qsofa_true, zs_qsofa_pred, average="weighted", zero_division=0)
            results.zs_qsofa_precision, results.zs_qsofa_recall, results.zs_qsofa_f1 = p, r, f
            
        # Calculate qSOFA Metrics (AG)
        if ag_qsofa_true:
            results.ag_qsofa_accuracy = sum(1 for t, p in zip(ag_qsofa_true, ag_qsofa_pred) if t == p) / len(ag_qsofa_true)
            results.ag_qsofa_mae = mean_absolute_error(ag_qsofa_true, ag_qsofa_pred)
            results.ag_qsofa_rmse = np.sqrt(mean_squared_error(ag_qsofa_true, ag_qsofa_pred))
            results.ag_qsofa_kappa = cohen_kappa_score(ag_qsofa_true, ag_qsofa_pred)
            p, r, f, _ = precision_recall_fscore_support(ag_qsofa_true, ag_qsofa_pred, average="weighted", zero_division=0)
            results.ag_qsofa_precision, results.ag_qsofa_recall, results.ag_qsofa_f1 = p, r, f

        # Meta
        if results.sample_size > 0:
            results.ag_verified_rate = verified_count / results.sample_size
            results.ag_average_loops = total_loops / results.sample_size

    def _save_results(self, results: ExperimentResults, output_dir: Optional[Path]):
        """Save all results with full traceability."""
        # Summary markdown
        with open(output_dir / "comparison_summary.md", "w") as f:
            f.write(results.to_summary_table())
        
        # Full results with all data
        full_results = {
            "experiment_name": results.experiment_name,
            "sample_size": results.sample_size,
            "timestamp": datetime.now().isoformat(),
            "architecture": "agentic_coder",
            "metrics": {
                "zero_shot": {
                    "esi_accuracy": results.zs_esi_accuracy,
                    "esi_kappa": results.zs_esi_kappa,
                    "esi_mae": results.zs_esi_mae,
                    "esi_rmse": results.zs_esi_rmse,
                    "esi_precision": results.zs_esi_precision,
                    "esi_recall": results.zs_esi_recall,
                    "esi_f1": results.zs_esi_f1,
                    
                    "pain_mae": results.zs_pain_mae,
                    "pain_rmse": results.zs_pain_rmse,
                    "pain_tol_rate": results.zs_pain_acc_tol,
                    "los_mae": results.zs_los_mae,
                    "los_rmse": results.zs_los_rmse,
                    "los_tol_rate": results.zs_los_acc_tol,
                    "shock_index_mae": results.zs_shock_index_mae,
                    "shock_index_error_rate": results.zs_shock_index_error_rate,
                    
                    "qsofa_accuracy": results.zs_qsofa_accuracy,
                    "qsofa_kappa": results.zs_qsofa_kappa,
                    "qsofa_mae": results.zs_qsofa_mae,
                    "qsofa_rmse": results.zs_qsofa_rmse,
                    "qsofa_precision": results.zs_qsofa_precision,
                    "qsofa_recall": results.zs_qsofa_recall,
                    "qsofa_f1": results.zs_qsofa_f1,
                    
                    "map_mae": results.zs_map_mae,
                    "map_rmse": results.zs_map_rmse,
                    "map_tol_rate": results.zs_map_acc_tol,
                },
                "agentic": {
                    "esi_accuracy": results.ag_esi_accuracy,
                    "esi_kappa": results.ag_esi_kappa,
                    "esi_mae": results.ag_esi_mae,
                    "esi_rmse": results.ag_esi_rmse,
                    "esi_precision": results.ag_esi_precision,
                    "esi_recall": results.ag_esi_recall,
                    "esi_f1": results.ag_esi_f1,
                    
                    "pain_mae": results.ag_pain_mae,
                    "pain_rmse": results.ag_pain_rmse,
                    "pain_tol_rate": results.ag_pain_acc_tol,
                    "los_mae": results.ag_los_mae,
                    "los_rmse": results.ag_los_rmse,
                    "los_tol_rate": results.ag_los_acc_tol,
                    "shock_index_mae": results.ag_shock_index_mae,
                    "shock_index_error_rate": results.ag_shock_index_error_rate,
                    
                    "qsofa_accuracy": results.ag_qsofa_accuracy,
                    "qsofa_kappa": results.ag_qsofa_kappa,
                    "qsofa_mae": results.ag_qsofa_mae,
                    "qsofa_rmse": results.ag_qsofa_rmse,
                    "qsofa_precision": results.ag_qsofa_precision,
                    "qsofa_recall": results.ag_qsofa_recall,
                    "qsofa_f1": results.ag_qsofa_f1,
                    
                    "map_mae": results.ag_map_mae,
                    "map_rmse": results.ag_map_rmse,
                    "map_tol_rate": results.ag_map_acc_tol,
                    
                    "verified_rate": results.ag_verified_rate,
                    "average_loops": results.ag_average_loops,
                },
                "efficiency": {
                    "total_prompt_tokens": results.total_prompt_tokens,
                    "total_completion_tokens": results.total_completion_tokens,
                    "total_cost_usd": results.total_cost,
                    "total_duration_seconds": results.total_duration_seconds
                }
            },
            "per_visit_results": [
                {
                    "visit_id": r.visit_id,
                    "demographics": r.demographics,
                    "ground_truth": asdict(r.ground_truth) if r.ground_truth else None,
                    "zero_shot": asdict(r.zero_shot_output) if r.zero_shot_output else None,
                    "agentic": asdict(r.agentic_output) if r.agentic_output else None,
                }
                for r in results.results
            ]
        }
        
        with open(output_dir / "full_results.json", "w") as f:
            json.dump(full_results, f, indent=2, default=str)
        
        # Blinded outputs for expert review
        blinded = []
        for r in results.results:
            if r.zero_shot_output:
                zs_entry = r.zero_shot_output.to_blinded_format()
                zs_entry["id"] = f"{r.visit_id}_A"
                zs_entry["demographics"] = r.demographics
                blinded.append(zs_entry)

            if r.agentic_output:
                ag_entry = r.agentic_output.to_blinded_format()
                ag_entry["id"] = f"{r.visit_id}_B"
                ag_entry["demographics"] = r.demographics
                blinded.append(ag_entry)
        
        with open(output_dir / "blinded_outputs.json", "w") as f:
            json.dump(blinded, f, indent=2, default=str)
