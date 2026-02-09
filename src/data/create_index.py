"""
Regenerate the benchmark index with complete ground truth filtering.

This script creates an index that only includes visits with:
1. Sufficient vital sign density (HR, SBP, DBP, SpO2 >= N samples)
2. Complete ground truth values (ESI, LOS, Pain all non-null)
3. Sufficient medium vital sign density (RR, Temp >= N samples)
"""

import pandas as pd
import numpy as np
from pathlib import Path
from tqdm import tqdm


def check_24h_window(
    df_visit: pd.DataFrame,
    core_set: list[str],
    med_set: list[str],
    min_samples: int,
    min_samples_medium: int
) -> tuple[bool, pd.Timestamp | None, pd.Timestamp | None]:
    """
    Check if there exists a 24-hour window with enough samples.
    Uses a sliding window (two-pointer) approach for efficiency.
    
    Returns:
        (has_window, start_time, end_time): Tuple indicating if valid window exists
            and the start/end timestamps of that window
    """
    if df_visit.empty:
        return (False, None, None)

    # Ensure Time is datetime and sorted
    df_visit = df_visit.sort_values('Time')
    times = df_visit['Time'].values
    measures = df_visit['Measure'].values
    
    n = len(df_visit)
    window_counts = {m: 0 for m in core_set + med_set}
    
    left = 0
    # Window duration in nanoseconds (24 hours)
    window_duration = np.timedelta64(24, 'h')
    for right in range(n):
        # Add right sample to window
        m_right = measures[right]
        if m_right in window_counts:
            window_counts[m_right] += 1
            
        # Shrink window from left
        while times[right] - times[left] > window_duration:
            m_left = measures[left]
            if m_left in window_counts:
                window_counts[m_left] -= 1
            left += 1
            
        # Check if current window meets criteria
        enough_core = all(window_counts[m] >= min_samples for m in core_set)
        enough_med = all(window_counts[m] >= min_samples_medium for m in med_set)
        
        if enough_core and enough_med:
            # Return the window boundaries
            start_time = pd.Timestamp(times[left])
            end_time = pd.Timestamp(times[right])
            return (True, start_time, end_time)
            
    return (False, None, None)


def create_index(
    visits_path: Path,
    numerics_path: Path,
    output_path: Path,
    min_samples: int = 30,
    min_samples_medium: int = 30,
) -> pd.DataFrame:
    """
    Create index of visits with complete data for benchmarking.
    
    Filters for:
    - Valid ESI (1-5)
    - Non-null LOS
    - Non-null Pain score
    - High-density vitals (>= min_samples for core vitals)
    - Medium-density vitals (>= min_samples_medium for medium vitals)
    
    Args:
        visits_path: Path to visits.csv
        numerics_path: Path to numerics.csv
        output_path: Path to save the index
        min_samples: Minimum number of samples for core vitals
    """
    print(f"Loading visits from {visits_path}...")
    visits_df = pd.read_csv(visits_path)
    
    # Ground truth filtering
    print("Filtering for complete ground truth (ESI + LOS)...")
    
    # ESI: Must have valid triage acuity (starts with 1-5)
    valid_esi = visits_df['Triage_acuity'].notna()
    esi_numeric = visits_df['Triage_acuity'].astype(str).str[0].apply(
        lambda x: x.isdigit() and int(x) in [1, 2, 3, 4, 5]
    )
    
    # LOS: Must have non-null ED_LOS
    valid_los = visits_df['ED_LOS'].notna()
    
    # Initial filter
    valid_mask = valid_esi & esi_numeric & valid_los
    
    print(f"  - Valid ESI: {valid_esi.sum():,} visits")
    print(f"  - Valid LOS: {valid_los.sum():,} visits")
    print(f"  - Combined (ESI + LOS): {valid_mask.sum():,} visits")
    
    valid_csns = set(visits_df.loc[valid_mask, 'CSN'].astype(str))
    
    # Filter for vital sign density
    print(f"\nIndexing high-density visits (N>={min_samples}) from {numerics_path}...")
    
    # Load CSN, Measure, Value, AND Time to check windows
    df_lite = pd.read_csv(numerics_path, usecols=['CSN', 'Measure', 'Value', 'Time'])
    
    # Convert Time to datetime early for efficiency (use ISO8601 format for performance)
    # Use errors='coerce' because some years (2292+) exceed pandas nanosecond range
    df_lite['Time'] = pd.to_datetime(df_lite['Time'], format='ISO8601', errors='coerce')
    df_lite = df_lite.dropna(subset=['Time'])
    
    # Only consider visits that passed GT filter
    df_lite = df_lite[df_lite['CSN'].astype(str).isin(valid_csns)]
    
    # VALIDATION: Convert Value to numeric, coerce errors (strings like 'Error', 'Refused' -> NaN)
    df_lite['Value'] = pd.to_numeric(df_lite['Value'], errors='coerce')
    
    # Drop rows with invalid values - we only want to count USABLE samples
    df_lite = df_lite.dropna(subset=['Value'])
    
    # Count valid measures per visit
    counts = df_lite.groupby(['CSN', 'Measure']).size().unstack(fill_value=0)
    
    # Filter criteria
    core_set = ['HR', 'SBP', 'DBP', 'SpO2']
    med_set = ['RR', 'Temp']
    
    # Ensure columns exist
    for col in core_set + med_set:
        if col not in counts.columns:
            counts[col] = 0
    
    # Apply vital sign density criteria
    mask_core = (counts[core_set] >= min_samples).all(axis=1)
    mask_med = (counts[med_set] >= min_samples_medium).all(axis=1)
    
    vitals_possible_csns = set(counts[mask_core & mask_med].index.astype(str))
    
    print(f"  - Core vitals (>= {min_samples} total samples each): {mask_core.sum():,} visits")
    print(f"  - Medium vitals (>= {min_samples_medium} total samples each): {mask_med.sum():,} visits")
    print(f"  - High-density (total): {len(vitals_possible_csns):,} visits")

    # Now apply the 24h window constraint to the candidates
    print(f"\nChecking 24h window constraint for {len(vitals_possible_csns):,} candidates...")
    
    valid_window_data = []  # Store CSN, start_time, end_time
    
    # Group df_lite by CSN once
    df_candidates = df_lite[df_lite['CSN'].astype(str).isin(vitals_possible_csns)]
    grouped = df_candidates.groupby('CSN')
    
    for csn, group in tqdm(grouped, desc="Validating 24h windows"):
        has_window, start_time, end_time = check_24h_window(
            group, core_set, med_set, min_samples, min_samples_medium
        )
        if has_window:
            valid_window_data.append({
                'CSN': str(csn),
                'window_start': start_time,
                'window_end': end_time
            })
            
    vitals_csns = set([row['CSN'] for row in valid_window_data])
    print(f"  - High-density vitals (in 24h window): {len(vitals_csns):,} visits")
    
    # Pain filtering (mandatory)
    print(f"\nFiltering for pain score availability...")
    # Reuse df_lite since we already processed values
    df_pain = df_lite[df_lite['CSN'].astype(str).isin(vitals_csns)]
    df_pain = df_pain[df_pain['Measure'].str.lower().isin(['pain', 'pain_score', 'pain score'])]
    
    csns_with_pain = set(df_pain['CSN'].astype(str))
    
    # Filter valid_window_data to only include CSNs with pain scores
    final_data = [row for row in valid_window_data if row['CSN'] in csns_with_pain]
    print(f"  - With valid pain score: {len(csns_with_pain):,} visits")
    print(f"  - Final (ESI + LOS + Pain + high-density vitals): {len(final_data):,} visits")
    
    # Save index with window boundaries
    result_df = pd.DataFrame(final_data)
    result_df.to_csv(output_path, index=False)
    print(f"\n✓ Index saved to {output_path}")
    print(f"  Columns: CSN, window_start, window_end")
    
    return result_df


if __name__ == "__main__":
    dataset_dir = Path("dataset")
    visits_path = dataset_dir / "visits.csv"
    numerics_path = dataset_dir / "numerics.csv"
    output_path = dataset_dir / "complete_benchmark_index.csv"
    
    create_index(
        visits_path=visits_path,
        numerics_path=numerics_path,
        output_path=output_path
    )
