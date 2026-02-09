"""
Full Benchmark Runner - Execute ALL experiments across ALL models.
Generates comprehensive results ready for Streamlit survey upload.

Flow:
1. Iterate through all specified models (GPT-5.2, Claude 4.5, etc.)
2. For each model:
   - Run Zero-Shot Baseline (N samples)
   - Run Agentic Pipeline (N samples)
3. Aggregate all results into a single standardized JSON structure.
"""

import argparse
import json
import time
import warnings
# Suppress noisy Vertex AI deprecation warnings
warnings.filterwarnings("ignore", message="This feature is deprecated", category=UserWarning, module="vertexai")
# Suppress Google Cloud Storage warning (internal to aiplatform)
warnings.filterwarnings("ignore", message="Support for google-cloud-storage < 3.0.0", category=FutureWarning)
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

from src.config import config
from src.models import SUPPORTED_MODELS
from src.data.loaders import VisitsLoader, NumericsLoader
from src.experiments.unified_comparison import UnifiedComparisonExperiment
from src.logging import configure_logger

def run_benchmark(
    models: List[str],
    sample_size: int = 50,
    output_dir: Path = Path("results"),
    specific_visits: List[str] = None,
    retry_failed: bool = False
) -> Dict[str, Any]:
    """Run full benchmark suite.
    
    Args:
        models: List of model keys to benchmark
        sample_size: Number of samples per model (0 or -1 for all)
        output_dir: Output directory
        specific_visits: If provided, only process these visit IDs
        retry_failed: If True, load failed_visits.json and re-run those
    """
    
    timestamp = datetime.now().isoformat()
    run_id = f"bench_{int(time.time())}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load Data (Once for all experiments)
    print(f"Loading dataset ({sample_size} visits)...")
    visits_loader = VisitsLoader(config.dataset.visits_path)
    
    # Load complete benchmark index (visits with complete GT + high-density vitals)
    complete_index_path = config.dataset.numerics_path.parent / "complete_benchmark_index.csv"
    
    if not complete_index_path.exists():
        raise ValueError(f"Complete benchmark index not found at {complete_index_path}. Run `python src/data/create_index.py` first.")
    
    print(f"Loading complete benchmark index from {complete_index_path}...")
    index_df = pd.read_csv(complete_index_path)
    valid_ids = set(index_df['CSN'].astype(str))
    print(f"  - {len(valid_ids):,} visits with complete ground truth + high-density vitals")
    print(f"  - Using stored 24h window boundaries for each visit")
    
    numerics_loader = None
    if config.dataset.numerics_path.exists():
        numerics_loader = NumericsLoader(config.dataset.numerics_path, window_index=index_df)
        numerics_loader.load()

    # Pre-filter visits based on index
    df = pd.read_csv(config.dataset.visits_path)
    if valid_ids:
        df['CSN_str'] = df['CSN'].astype(str)
        df = df[df['CSN_str'].isin(valid_ids)]
        print(f"Candidate pool: {len(df):,} visits")
    
    # Handle "use all samples" mode (--n 0 or --n -1)
    if sample_size <= 0:
        print(f"Using ALL {len(df):,} valid visits (no sampling limit)")
        sample_size = len(df)
        df = df.sample(frac=1.0, random_state=config.experiment.random_seed)  # Shuffle only
    elif len(df) < sample_size:
        print(f"Warning: Only {len(df)} valid visits available. Reducing sample size.")
        sample_size = len(df)
        df = df.sample(frac=1.0, random_state=config.experiment.random_seed)  # Shuffle only
    else:
        # Sample from the valid pool
        df = df.sample(n=sample_size, random_state=config.experiment.random_seed)
    
    # Apply visit filter if specific visits are requested
    if specific_visits:
        df['CSN_str'] = df['CSN'].astype(str) if 'CSN_str' not in df.columns else df['CSN_str']
        df = df[df['CSN_str'].isin(specific_visits)]
        print(f"Filtered to {len(df)} specific visits")
        sample_size = len(df)
    
    visits_loader._df = df  # Manually inject the filtered/sampled DF
    
    # 2. Initialize Result Structure
    benchmark_data = {
        "meta": {
            "run_id": run_id,
            "timestamp": timestamp,
            "sample_size": sample_size,
            "models_evaluated": models,
        },
        "results": {} # model_key -> results
    }
    
    # 3. Iterate Models
    for model_key in models:
        if model_key not in SUPPORTED_MODELS:
            print(f"[Warn] Skipping unknown model: {model_key}")
            continue
            
        model_config = SUPPORTED_MODELS[model_key]
        print(f"\n{'#'*60}")
        print(f"BENCHMARKING: {model_config.display_name}")
        print(f"{'#'*60}")
        
        # Configure logger for this model's specific directory
        model_output_path = output_dir / model_key
        configure_logger(model_output_path / "logs")
        print(f"  - Logs will be saved to: {model_output_path / 'logs'}")
        
        model_results = {
            "config": {
                "display_name": model_config.display_name,
                "provider": model_config.provider,
                "is_medical": model_config.is_medical_specialized
            },
            "comparison": {},
        }
        
        try:
            # A. Unified Comparison (Zero-Shot vs Agentic)
            print("  Running Unified Comparison (Clinical Accuracy)...")
            experiment = UnifiedComparisonExperiment(
                visits_loader=visits_loader,
                numerics_loader=numerics_loader,
                model_name=model_key
            )
            
            # This runs BOTH Zero-Shot and Agentic internally on the same visits
            comp_results = experiment.run(sample_size, output_dir / model_key)
            
            # Serialize comparison results
            model_results["comparison"] = {
                "zero_shot": {
                    "esi_accuracy": comp_results.zs_esi_accuracy,
                    "esi_kappa": comp_results.zs_esi_kappa,
                    "esi_mae": comp_results.zs_esi_mae,
                    "esi_rmse": comp_results.zs_esi_rmse,
                    "esi_precision": comp_results.zs_esi_precision,
                    "esi_recall": comp_results.zs_esi_recall,
                    "esi_f1": comp_results.zs_esi_f1,
                    "pain_mae": comp_results.zs_pain_mae,
                    "pain_rmse": comp_results.zs_pain_rmse,
                    "pain_tol_rate": comp_results.zs_pain_acc_tol,
                    "los_mae": comp_results.zs_los_mae,
                    "los_rmse": comp_results.zs_los_rmse,
                    "los_tol_rate": comp_results.zs_los_acc_tol,
                    "shock_index_mae": comp_results.zs_shock_index_mae,
                    "shock_index_error": comp_results.zs_shock_index_error_rate,
                    # qSOFA
                    "qsofa_accuracy": comp_results.zs_qsofa_accuracy,
                    "qsofa_kappa": comp_results.zs_qsofa_kappa,
                    "qsofa_mae": comp_results.zs_qsofa_mae,
                    "qsofa_rmse": comp_results.zs_qsofa_rmse,
                    "qsofa_precision": comp_results.zs_qsofa_precision,
                    "qsofa_recall": comp_results.zs_qsofa_recall,
                    "qsofa_f1": comp_results.zs_qsofa_f1,
                    # MAP
                    "map_mae": comp_results.zs_map_mae,
                    "map_rmse": comp_results.zs_map_rmse,
                    "map_tol_rate": comp_results.zs_map_acc_tol
                },
                "agentic": {
                    "esi_accuracy": comp_results.ag_esi_accuracy,
                    "esi_kappa": comp_results.ag_esi_kappa,
                    "esi_mae": comp_results.ag_esi_mae,
                    "esi_rmse": comp_results.ag_esi_rmse,
                    "esi_precision": comp_results.ag_esi_precision,
                    "esi_recall": comp_results.ag_esi_recall,
                    "esi_f1": comp_results.ag_esi_f1,
                    "pain_mae": comp_results.ag_pain_mae,
                    "pain_rmse": comp_results.ag_pain_rmse,
                    "pain_tol_rate": comp_results.ag_pain_acc_tol,
                    "los_mae": comp_results.ag_los_mae,
                    "los_rmse": comp_results.ag_los_rmse,
                    "los_tol_rate": comp_results.ag_los_acc_tol,
                    "shock_index_mae": comp_results.ag_shock_index_mae,
                    "shock_index_error": comp_results.ag_shock_index_error_rate,
                    # qSOFA
                    "qsofa_accuracy": comp_results.ag_qsofa_accuracy,
                    "qsofa_kappa": comp_results.ag_qsofa_kappa,
                    "qsofa_mae": comp_results.ag_qsofa_mae,
                    "qsofa_rmse": comp_results.ag_qsofa_rmse,
                    "qsofa_precision": comp_results.ag_qsofa_precision,
                    "qsofa_recall": comp_results.ag_qsofa_recall,
                    "qsofa_f1": comp_results.ag_qsofa_f1,
                    # MAP
                    "map_mae": comp_results.ag_map_mae,
                    "map_rmse": comp_results.ag_map_rmse,
                    "map_tol_rate": comp_results.ag_map_acc_tol,
                    "verified_rate": comp_results.ag_verified_rate,
                    "average_loops": comp_results.ag_average_loops
                },
                "efficiency": {
                    "total_prompt_tokens": comp_results.total_prompt_tokens,
                    "total_completion_tokens": comp_results.total_completion_tokens,
                    "total_cost_usd": comp_results.total_cost
                },
                # Detailed per-visit outputs for qualitative review
                "visits": [
                    {
                        "visit_id": r.visit_id,
                        "ground_truth": r.ground_truth,
                        "zero_shot_output": r.zero_shot_output.to_dict() if r.zero_shot_output else None,
                        "agentic_output": r.agentic_output.to_dict() if r.agentic_output else None
                    }
                    for r in comp_results.results
                ]
            }

        except Exception as e:
            print(f"  [Err] Error benchmarking {model_key}: {e}")
            model_results["error"] = str(e)
            
        benchmark_data["results"][model_key] = model_results

    # 4. Result Merging (when retrying specific visits)
    if specific_visits or retry_failed:
        for model_key in benchmark_data["results"]:
            existing_path = output_dir / model_key / "full_results.json"
            if existing_path.exists():
                print(f"Merging results for {model_key}...")
                with open(existing_path) as f:
                    existing = json.load(f)
                
                # Get existing visits as dict by visit_id
                existing_visits = {v["visit_id"]: v for v in existing.get("comparison", {}).get("visits", [])}
                
                # Merge new results (overwrite existing by visit_id)
                new_visits = benchmark_data["results"][model_key].get("comparison", {}).get("visits", [])
                for v in new_visits:
                    existing_visits[v["visit_id"]] = v
                
                # Replace the visits list with merged results
                if "comparison" in benchmark_data["results"][model_key]:
                    benchmark_data["results"][model_key]["comparison"]["visits"] = list(existing_visits.values())
                    print(f"  Merged {len(new_visits)} new/retry results. Total: {len(existing_visits)} visits.")

    # 5. Save Final Aggregated Report
    final_path = output_dir / "full_benchmark_results.json"
    with open(final_path, "w") as f:
        json.dump(benchmark_data, f, indent=2, default=str)
        
    print(f"\n{'='*60}")
    print(f"BENCHMARK COMPLETE. Results: {final_path}")
    print(f"{'='*60}")
    
    return benchmark_data


def main():
    parser = argparse.ArgumentParser(description="Run Full Multi-Model Benchmark")
    parser.add_argument("--models", nargs="+", default=["gpt-5.2"], help="Models to benchmark (or 'all')")
    parser.add_argument("--n", type=int, default=1, help="Number of samples per model (0 or -1 for all)")
    parser.add_argument("--output", type=Path, default=Path("results"), help="Output directory")
    parser.add_argument("--visits", nargs="+", help="Specific visit IDs to process")
    parser.add_argument("--retry-failed", action="store_true", help="Re-run failed visits from previous run")

    args = parser.parse_args()
    
    models = list(SUPPORTED_MODELS.keys()) if "all" in args.models else args.models
    
    # Handle --retry-failed: load failed visits from each model's failed_visits.json
    specific_visits = args.visits
    if args.retry_failed:
        all_failed = []
        for model_key in models:
            failed_path = args.output / model_key / "failed_visits.json"
            if failed_path.exists():
                with open(failed_path) as f:
                    data = json.load(f)
                    all_failed.extend(data.get("failed_visits", []))
                print(f"Loaded {len(data.get('failed_visits', []))} failed visits from {failed_path}")
        if all_failed:
            specific_visits = list(set(all_failed))  # Deduplicate
            print(f"Total failed visits to retry: {len(specific_visits)}")
        else:
            print("No failed_visits.json found. Running normally.")
    
    # Run benchmark with optional visit filtering
    run_benchmark(models, args.n, args.output, specific_visits, args.retry_failed)

if __name__ == "__main__":
    main()
