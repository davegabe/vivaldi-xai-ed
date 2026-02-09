"""
Ablation Experiment: Zero-Shot Standard vs Zero-Shot Ablated.
"""

from typing import Optional
from dataclasses import asdict
from pathlib import Path
import json
import numpy as np
from datetime import datetime
from sklearn.metrics import accuracy_score, cohen_kappa_score, mean_absolute_error, mean_squared_error, precision_score, recall_score, f1_score
import concurrent.futures
from tqdm import tqdm

from ..logging import configure_logger
from ..config import config
from ..data.schema import PatientVisit
from ..data.loaders import VisitsLoader, NumericsLoader, PMHLoader, MedsLoader
from ..agents.zero_shot import ZeroShotBaseline
from .results import ComparisonResult, ExperimentResults, build_ground_truth
from ..prompts import ClinicalOutput

class AblationExperiment:
    """
    Runs comparison between Zero-Shot (Standard) and Zero-Shot (Ablated).
    Ablated version removes reasoning and derived metrics to test Chain-of-Thought efficacy.
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
        
        # Configure logger FIRST before agents are initialized
        self.logger = configure_logger(
            output_dir=config.experiment.output_dir / model_name / "ablation_experiment"
        )
        
        # Additional Context Loaders
        self.pmh_loader = PMHLoader(config.dataset.visits_path.parent / "pmh.csv")
        self.meds_loader = MedsLoader(config.dataset.visits_path.parent / "meds.csv")
        
        # Initialize both approaches
        self.zero_shot_standard = ZeroShotBaseline(model_name, ablation=False)
        self.zero_shot_ablated = ZeroShotBaseline(model_name, ablation=True)
    
    @staticmethod
    def _safe_mean(values: list[float]) -> float:
        """Calculate mean safely, returning 0.0 for empty lists."""
        return float(np.mean(values)) if values else 0.0

    @staticmethod
    def _safe_rmse(values: list[float]) -> float:
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
                    self.logger.log_error(f"Skipping {visit.visit_id}: No vital signs data.")
                    return None
                    
                # Build ground truth
                ground_truth = build_ground_truth(visit, vitals)
                
                # Run Zero-Shot Standard
                start_std = datetime.now()
                std_output = self.zero_shot_standard.process_visit(
                    visit, vitals, pmh=pmh_list, meds=meds_list
                )
                std_output.duration_seconds = (datetime.now() - start_std).total_seconds()
                
                # Run Zero-Shot Ablated
                start_abl = datetime.now()
                # Note: We can reuse the same vitals/context
                abl_output = self.zero_shot_ablated.process_visit(
                    visit, vitals, pmh=pmh_list, meds=meds_list
                )
                abl_output.duration_seconds = (datetime.now() - start_abl).total_seconds()
                abl_output.approach = "zero_shot_ablated"
                
                return ComparisonResult(
                    visit_id=visit.visit_id,
                    demographics=asdict(visit),
                    ground_truth=ground_truth,
                    zero_shot_output=std_output,  # Using standard as "zero_shot_output" in ComparisonResult
                    agentic_output=abl_output     # Hijacking "agentic_output" slot for ablated for simplified metric calc
                )

        except Exception as e:
            self.logger.log_error(f"Error processing visit {visit.visit_id}: {e}")
            return None
    
    def _accumulate_metrics_into(self, result: ComparisonResult, std_metrics: dict, abl_metrics: dict):
        """Helper to accumulate metrics from a single comparison result."""
        gt = result.ground_truth
        std = result.zero_shot_output
        abl = result.agentic_output  # Hijacked slot for ablated
        
        # ESI
        if gt.esi and std.esi_level and abl.esi_level:
            std_metrics["esi"].append((gt.esi, std.esi_level))
            abl_metrics["esi"].append((gt.esi, abl.esi_level))
        
        # Pain
        if gt.pain is not None:
            if std.pain_score is not None:
                std_metrics["pain"].append(abs(gt.pain - std.pain_score))
            if abl.pain_score is not None:
                abl_metrics["pain"].append(abs(gt.pain - abl.pain_score))
        
        # LOS
        if gt.los is not None:
            if std.ed_los is not None:
                std_metrics["los"].append(abs(gt.los - std.ed_los))
            if abl.ed_los is not None:
                abl_metrics["los"].append(abs(gt.los - abl.ed_los))
        
        # Shock Index
        if gt.shock_index is not None:
            # Standard
            if hasattr(std, "metrics") and std.metrics.shock_index is not None:
                diff = abs(gt.shock_index - std.metrics.shock_index)
                std_metrics["si_diff"].append(diff)
                std_metrics["si_error"].append(1 if diff > 0.1 else 0)
            
            # Ablated
            if hasattr(abl, "metrics") and abl.metrics.shock_index is not None:
                diff = abs(gt.shock_index - abl.metrics.shock_index)
                abl_metrics["si_diff"].append(diff)
                abl_metrics["si_error"].append(1 if diff > 0.1 else 0)

    def run(
        self, 
        sample_size: int = 100,
        output_dir: Optional[Path] = None,
    ) -> ExperimentResults:
        """
        Run comparison experiment with full logging.
        """
        output_dir = output_dir or config.experiment.output_dir / "ablation_experiment"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Build experiment config for logging
        exp_config = {
            "model_name": self.model_name or config.model.default_model,
            "sample_size": sample_size,
            "dataset_path": str(config.dataset.visits_path),
            "random_seed": config.experiment.random_seed,
            "architecture": "ablation_comparison",
        }
        
        results = ExperimentResults(
            experiment_name="Ablation Comparison (Standard vs Ablated)",
            sample_size=sample_size,
        )
        
        # Use logging context for experiment
        with self.logger.experiment_context(
            experiment_name="ablation_comparison",
            approach="zero_shot_comparison",
            config=exp_config,
            sample_size=sample_size,
        ) as exp_run:
            start_experiment = datetime.now()
            
            # Collect data for metric calculation
            std_metrics = {"esi": [], "pain": [], "los": [], "si_diff": [], "si_error": []}
            abl_metrics = {"esi": [], "pain": [], "los": [], "si_diff": [], "si_error": []}
            
            visit_count = 0
            
            # --- Check for existing results to skip ---
            existing_results_path = output_dir / "ablation_results.json"
            processed_visit_ids = set()
            if existing_results_path.exists():
                try:
                    with open(existing_results_path, "r") as f:
                        existing_data = json.load(f)
                    
                    if "per_visit_results" in existing_data:
                        print(f"  - Found {len(existing_data['per_visit_results'])} existing results. Loading for skip-check...")
                        for vr in existing_data["per_visit_results"]:                            
                            # Standard ClinicalOutput
                            std_data = vr.get("standard")
                            abl_data = vr.get("ablated")
                            
                            if not std_data or not abl_data:
                                continue
                                
                            std_out = ClinicalOutput.from_dict(std_data)
                            abl_out = ClinicalOutput.from_dict(abl_data)
                            
                            comp = ComparisonResult(
                                visit_id=vr["visit_id"],
                                ground_truth=vr["ground_truth"],
                                zero_shot_output=std_out,
                                agentic_output=abl_out
                            )
                            
                            results.results.append(comp)
                            processed_visit_ids.add(comp.visit_id)
                            visit_count += 1
                            
                            # Accumulate Metrics
                            self._accumulate_metrics_into(comp, std_metrics, abl_metrics)

                        print(f"  - Successfully resumed {len(processed_visit_ids)} already processed visits.")
                except Exception as e:
                    self.logger.log_error(f"Error loading existing results: {e}. Starting fresh.")
                    results.results = []
                    visit_count = 0
                    processed_visit_ids = set()

            # Create thread pool
            max_workers = 8
            
            # Collect all visits first, skipping already processed ones
            all_visits = []
            needed_samples = sample_size - len(processed_visit_ids) if sample_size > 0 else 999999
            
            if needed_samples > 0:
                print(f"  - Target sample size: {sample_size}. Need {needed_samples} more visits.")
                for visit in self.visits_loader.iter_visits(quiet=True):
                    if len(all_visits) >= needed_samples:
                        break
                    if visit.visit_id in processed_visit_ids:
                        continue
                    all_visits.append(visit)
            else:
                print(f"  - Target sample size {sample_size} already met. Skipping new work.")
            
            # Create tqdm progress bar for ONLY the new visits
            model_name = self.model_name or config.model.default_model
            pbar = tqdm(
                total=len(all_visits),
                desc=f"[{model_name}] Ablation Test",
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
                            result = future.result()
                            if result:
                                results.results.append(result)
                                visit_count += 1
                                
                                # Accumulate Real-time Metrics
                                self._accumulate_metrics_into(result, std_metrics, abl_metrics)
                                        
                                # Incremental Save
                                self._save_results(results, output_dir)
                        except Exception as e:
                            visit = future_to_visit[future]
                            self.logger.log_error(f"Unexpected error in thread for visit {visit.visit_id}: {e}")
            
            pbar.close()
            
            results.total_duration_seconds = (datetime.now() - start_experiment).total_seconds()
            
            # --- Calculate Aggregated Metrics ---            
            # Note: We are mapping Standard -> Zero Shot fields, Ablated -> Agentic fields in ExperimentResults for convenience
            
            # ESI
            if std_metrics["esi"]:
                y_true, y_pred = zip(*std_metrics["esi"])
                results.zs_esi_accuracy = accuracy_score(y_true, y_pred)
                results.zs_esi_mae = mean_absolute_error(y_true, y_pred)
                results.zs_esi_rmse = np.sqrt(mean_squared_error(y_true, y_pred))
                results.zs_esi_kappa = cohen_kappa_score(y_true, y_pred)
                results.zs_esi_precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
                results.zs_esi_recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
                results.zs_esi_f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
            
            if abl_metrics["esi"]:
                y_true, y_pred = zip(*abl_metrics["esi"])
                results.ag_esi_accuracy = accuracy_score(y_true, y_pred)
                results.ag_esi_mae = mean_absolute_error(y_true, y_pred)
                results.ag_esi_rmse = np.sqrt(mean_squared_error(y_true, y_pred))
                results.ag_esi_kappa = cohen_kappa_score(y_true, y_pred)
                results.ag_esi_precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
                results.ag_esi_recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
                results.ag_esi_f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
            
            # Pain
            results.zs_pain_mae = self._safe_mean(std_metrics["pain"])
            results.ag_pain_mae = self._safe_mean(abl_metrics["pain"])
            results.zs_pain_rmse = self._safe_rmse(std_metrics["pain"])
            results.ag_pain_rmse = self._safe_rmse(abl_metrics["pain"])
            # Tolerance +/- 1
            results.zs_pain_acc_tol = sum(1 for e in std_metrics["pain"] if e <= 1) / len(std_metrics["pain"]) if std_metrics["pain"] else 0.0
            results.ag_pain_acc_tol = sum(1 for e in abl_metrics["pain"] if e <= 1) / len(abl_metrics["pain"]) if abl_metrics["pain"] else 0.0
            
            # LOS
            results.zs_los_mae = self._safe_mean(std_metrics["los"])
            results.ag_los_mae = self._safe_mean(abl_metrics["los"])
            results.zs_los_rmse = self._safe_rmse(std_metrics["los"])
            results.ag_los_rmse = self._safe_rmse(abl_metrics["los"])
            # Tolerance +/- 2 hours
            results.zs_los_acc_tol = sum(1 for e in std_metrics["los"] if e <= 2) / len(std_metrics["los"]) if std_metrics["los"] else 0.0
            results.ag_los_acc_tol = sum(1 for e in abl_metrics["los"] if e <= 2) / len(abl_metrics["los"]) if abl_metrics["los"] else 0.0

            # Shock Index
            results.zs_shock_index_mae = self._safe_mean(std_metrics["si_diff"])
            results.ag_shock_index_mae = self._safe_mean(abl_metrics["si_diff"])
            results.zs_shock_index_error_rate = self._safe_mean(std_metrics["si_error"])
            results.ag_shock_index_error_rate = self._safe_mean(abl_metrics["si_error"])

            # Log final metrics
            print("\n=== ABLATION RESULTS ===")
            print(f"Standard ESI Acc: {results.zs_esi_accuracy:.3f} | Ablated ESI Acc: {results.ag_esi_accuracy:.3f}")
            print(f"Standard Pain MAE: {results.zs_pain_mae:.3f} | Ablated Pain MAE: {results.ag_pain_mae:.3f}")
            print(f"Standard LOS MAE: {results.zs_los_mae:.3f} | Ablated LOS MAE: {results.ag_los_mae:.3f}")
            
        # Save results
        self._save_results(results, output_dir)
        
        return results
    
    def _save_results(self, results: ExperimentResults, output_dir: Optional[Path]):
        """Save all results with full traceability."""
        
        # Full results with all data
        full_results = {
            "experiment_name": results.experiment_name,
            "sample_size": results.sample_size,
            "timestamp": datetime.now().isoformat(),
            "architecture": "ablation",
            "metrics": {
                "standard": {
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
                },
                "ablated": {
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
                }
            },
            "per_visit_results": [
                {
                    "visit_id": r.visit_id,
                    "ground_truth": asdict(r.ground_truth) if r.ground_truth else None,
                    "standard": asdict(r.zero_shot_output) if r.zero_shot_output else None,
                    "ablated": asdict(r.agentic_output) if r.agentic_output else None,
                }
                for r in results.results
            ]
        }
        
        with open(output_dir / "ablation_results.json", "w") as f:
            json.dump(full_results, f, indent=2, default=str)
