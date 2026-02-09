# Executed Code (Repaired)
# This code runs in a sandbox with injected variables (vitals, np, plt, etc.)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import datetime

# Helper function to simulate sandbox save_plot
def save_plot(filename, fig=None, **kwargs):
    if not filename.endswith('.png'): filename += '.png'
    if fig is None: fig = plt.gcf()
    fig.savefig(filename, **kwargs)
    plt.close(fig)
    print(f'Saved plot to {filename}')

# Injected Variables
visit_id = '99940356'
age = 82
gender = 'M'
ethnicity = 'White (Non-Hispanic/Non-Latino)'
heart_rate = [(datetime.datetime(2260, 1, 3, 21, 35, 50), 76.0), (datetime.datetime(2260, 1, 3, 22, 44, 50), 76.0), (datetime.datetime(2260, 1, 3, 23, 14, 50), 74.0), (datetime.datetime(2260, 1, 3, 23, 38, 50), 75.0), (datetime.datetime(2260, 1, 3, 23, 44, 50), 75.0), (datetime.datetime(2260, 1, 4, 0, 24, 50), 75.0), (datetime.datetime(2260, 1, 4, 0, 44, 50), 75.0), (datetime.datetime(2260, 1, 4, 1, 14, 50), 75.0), (datetime.datetime(2260, 1, 4, 1, 19, 50), 75.0), (datetime.datetime(2260, 1, 4, 1, 29, 50), 75.0), (datetime.datetime(2260, 1, 4, 1, 44, 50), 122.0), (datetime.datetime(2260, 1, 4, 1, 59, 50), 73.0), (datetime.datetime(2260, 1, 4, 2, 14, 50), 76.0), (datetime.datetime(2260, 1, 4, 2, 29, 50), 75.0), (datetime.datetime(2260, 1, 4, 2, 44, 50), 75.0), (datetime.datetime(2260, 1, 4, 2, 59, 50), 75.0), (datetime.datetime(2260, 1, 4, 3, 14, 50), 75.0), (datetime.datetime(2260, 1, 4, 3, 35, 50), 75.0), (datetime.datetime(2260, 1, 4, 3, 44, 50), 76.0), (datetime.datetime(2260, 1, 4, 3, 59, 50), 75.0), (datetime.datetime(2260, 1, 4, 4, 4, 50), 77.0), (datetime.datetime(2260, 1, 4, 4, 9, 50), 77.0), (datetime.datetime(2260, 1, 4, 4, 14, 50), 76.0), (datetime.datetime(2260, 1, 4, 4, 20, 50), 63.0), (datetime.datetime(2260, 1, 4, 4, 54, 50), 61.0), (datetime.datetime(2260, 1, 4, 5, 0, 50), 64.0), (datetime.datetime(2260, 1, 4, 5, 10, 50), 61.0), (datetime.datetime(2260, 1, 4, 5, 20, 50), 61.0), (datetime.datetime(2260, 1, 4, 5, 44, 50), 64.0), (datetime.datetime(2260, 1, 4, 5, 58, 50), 66.0), (datetime.datetime(2260, 1, 4, 6, 4, 50), 64.0), (datetime.datetime(2260, 1, 4, 6, 14, 50), 63.0)]
systolic_bp = [(datetime.datetime(2260, 1, 3, 21, 35, 50), 117.0), (datetime.datetime(2260, 1, 3, 23, 14, 50), 91.0), (datetime.datetime(2260, 1, 3, 23, 44, 50), 106.0), (datetime.datetime(2260, 1, 4, 0, 24, 50), 95.0), (datetime.datetime(2260, 1, 4, 0, 44, 50), 94.0), (datetime.datetime(2260, 1, 4, 1, 14, 50), 72.0), (datetime.datetime(2260, 1, 4, 1, 19, 50), 90.0), (datetime.datetime(2260, 1, 4, 1, 29, 50), 92.0), (datetime.datetime(2260, 1, 4, 1, 44, 50), 111.0), (datetime.datetime(2260, 1, 4, 1, 59, 50), 73.0), (datetime.datetime(2260, 1, 4, 2, 14, 50), 77.0), (datetime.datetime(2260, 1, 4, 2, 29, 50), 87.0), (datetime.datetime(2260, 1, 4, 2, 44, 50), 75.0), (datetime.datetime(2260, 1, 4, 2, 59, 50), 112.0), (datetime.datetime(2260, 1, 4, 3, 14, 50), 84.0), (datetime.datetime(2260, 1, 4, 3, 35, 50), 94.0), (datetime.datetime(2260, 1, 4, 3, 44, 50), 94.0), (datetime.datetime(2260, 1, 4, 3, 59, 50), 85.0), (datetime.datetime(2260, 1, 4, 4, 4, 50), 83.0), (datetime.datetime(2260, 1, 4, 4, 9, 50), 78.0), (datetime.datetime(2260, 1, 4, 4, 14, 50), 89.0), (datetime.datetime(2260, 1, 4, 4, 20, 50), 95.0), (datetime.datetime(2260, 1, 4, 4, 54, 50), 103.0), (datetime.datetime(2260, 1, 4, 5, 0, 50), 99.0), (datetime.datetime(2260, 1, 4, 5, 10, 50), 103.0), (datetime.datetime(2260, 1, 4, 5, 20, 50), 104.0), (datetime.datetime(2260, 1, 4, 5, 44, 50), 99.0), (datetime.datetime(2260, 1, 4, 5, 58, 50), 109.0), (datetime.datetime(2260, 1, 4, 6, 4, 50), 106.0), (datetime.datetime(2260, 1, 4, 6, 14, 50), 108.0)]
diastolic_bp = [(datetime.datetime(2260, 1, 3, 21, 35, 50), 53.0), (datetime.datetime(2260, 1, 3, 23, 14, 50), 48.0), (datetime.datetime(2260, 1, 3, 23, 44, 50), 44.0), (datetime.datetime(2260, 1, 4, 0, 24, 50), 56.0), (datetime.datetime(2260, 1, 4, 0, 44, 50), 52.0), (datetime.datetime(2260, 1, 4, 1, 14, 50), 53.0), (datetime.datetime(2260, 1, 4, 1, 19, 50), 53.0), (datetime.datetime(2260, 1, 4, 1, 29, 50), 49.0), (datetime.datetime(2260, 1, 4, 1, 44, 50), 101.0), (datetime.datetime(2260, 1, 4, 1, 59, 50), 53.0), (datetime.datetime(2260, 1, 4, 2, 14, 50), 44.0), (datetime.datetime(2260, 1, 4, 2, 29, 50), 43.0), (datetime.datetime(2260, 1, 4, 2, 44, 50), 62.0), (datetime.datetime(2260, 1, 4, 2, 59, 50), 49.0), (datetime.datetime(2260, 1, 4, 3, 14, 50), 54.0), (datetime.datetime(2260, 1, 4, 3, 35, 50), 67.0), (datetime.datetime(2260, 1, 4, 3, 44, 50), 65.0), (datetime.datetime(2260, 1, 4, 3, 59, 50), 68.0), (datetime.datetime(2260, 1, 4, 4, 4, 50), 64.0), (datetime.datetime(2260, 1, 4, 4, 9, 50), 43.0), (datetime.datetime(2260, 1, 4, 4, 14, 50), 44.0), (datetime.datetime(2260, 1, 4, 4, 20, 50), 63.0), (datetime.datetime(2260, 1, 4, 4, 54, 50), 53.0), (datetime.datetime(2260, 1, 4, 5, 0, 50), 40.0), (datetime.datetime(2260, 1, 4, 5, 10, 50), 48.0), (datetime.datetime(2260, 1, 4, 5, 20, 50), 48.0), (datetime.datetime(2260, 1, 4, 5, 44, 50), 36.0), (datetime.datetime(2260, 1, 4, 5, 58, 50), 53.0), (datetime.datetime(2260, 1, 4, 6, 4, 50), 47.0), (datetime.datetime(2260, 1, 4, 6, 14, 50), 49.0)]
spo2 = [(datetime.datetime(2260, 1, 3, 21, 35, 50), 98.0), (datetime.datetime(2260, 1, 3, 22, 44, 50), 97.0), (datetime.datetime(2260, 1, 3, 23, 14, 50), 96.0), (datetime.datetime(2260, 1, 3, 23, 38, 50), 94.0), (datetime.datetime(2260, 1, 3, 23, 44, 50), 95.0), (datetime.datetime(2260, 1, 4, 0, 24, 50), 98.0), (datetime.datetime(2260, 1, 4, 0, 44, 50), 98.0), (datetime.datetime(2260, 1, 4, 1, 14, 50), 97.0), (datetime.datetime(2260, 1, 4, 1, 19, 50), 97.0), (datetime.datetime(2260, 1, 4, 1, 29, 50), 97.0), (datetime.datetime(2260, 1, 4, 1, 44, 50), 100.0), (datetime.datetime(2260, 1, 4, 1, 59, 50), 98.0), (datetime.datetime(2260, 1, 4, 2, 14, 50), 97.0), (datetime.datetime(2260, 1, 4, 2, 29, 50), 98.0), (datetime.datetime(2260, 1, 4, 2, 44, 50), 96.0), (datetime.datetime(2260, 1, 4, 2, 59, 50), 100.0), (datetime.datetime(2260, 1, 4, 3, 14, 50), 99.0), (datetime.datetime(2260, 1, 4, 3, 35, 50), 100.0), (datetime.datetime(2260, 1, 4, 3, 44, 50), 96.0), (datetime.datetime(2260, 1, 4, 3, 59, 50), 98.0), (datetime.datetime(2260, 1, 4, 4, 4, 50), 98.0), (datetime.datetime(2260, 1, 4, 4, 9, 50), 98.0), (datetime.datetime(2260, 1, 4, 4, 14, 50), 96.0), (datetime.datetime(2260, 1, 4, 4, 20, 50), 98.0), (datetime.datetime(2260, 1, 4, 4, 54, 50), 98.0), (datetime.datetime(2260, 1, 4, 5, 0, 50), 95.0), (datetime.datetime(2260, 1, 4, 5, 10, 50), 95.0), (datetime.datetime(2260, 1, 4, 5, 20, 50), 95.0), (datetime.datetime(2260, 1, 4, 5, 44, 50), 96.0), (datetime.datetime(2260, 1, 4, 5, 58, 50), 94.0), (datetime.datetime(2260, 1, 4, 6, 4, 50), 96.0), (datetime.datetime(2260, 1, 4, 6, 14, 50), 96.0)]
respiratory_rate = [(datetime.datetime(2260, 1, 3, 21, 35, 50), 20.0), (datetime.datetime(2260, 1, 3, 22, 44, 50), 22.0), (datetime.datetime(2260, 1, 3, 23, 14, 50), 17.0), (datetime.datetime(2260, 1, 3, 23, 38, 50), 19.0), (datetime.datetime(2260, 1, 3, 23, 44, 50), 18.0), (datetime.datetime(2260, 1, 4, 0, 24, 50), 20.0), (datetime.datetime(2260, 1, 4, 0, 44, 50), 19.0), (datetime.datetime(2260, 1, 4, 1, 14, 50), 22.0), (datetime.datetime(2260, 1, 4, 1, 19, 50), 12.0), (datetime.datetime(2260, 1, 4, 1, 29, 50), 23.0), (datetime.datetime(2260, 1, 4, 1, 44, 50), 18.0), (datetime.datetime(2260, 1, 4, 1, 59, 50), 22.0), (datetime.datetime(2260, 1, 4, 2, 14, 50), 21.0), (datetime.datetime(2260, 1, 4, 2, 29, 50), 19.0), (datetime.datetime(2260, 1, 4, 2, 44, 50), 15.0), (datetime.datetime(2260, 1, 4, 2, 59, 50), 23.0), (datetime.datetime(2260, 1, 4, 3, 14, 50), 26.0), (datetime.datetime(2260, 1, 4, 3, 35, 50), 15.0), (datetime.datetime(2260, 1, 4, 3, 44, 50), 26.0), (datetime.datetime(2260, 1, 4, 3, 59, 50), 20.0), (datetime.datetime(2260, 1, 4, 4, 4, 50), 22.0), (datetime.datetime(2260, 1, 4, 4, 9, 50), 23.0), (datetime.datetime(2260, 1, 4, 4, 14, 50), 21.0), (datetime.datetime(2260, 1, 4, 4, 20, 50), 23.0), (datetime.datetime(2260, 1, 4, 4, 54, 50), 19.0), (datetime.datetime(2260, 1, 4, 5, 0, 50), 27.0), (datetime.datetime(2260, 1, 4, 5, 10, 50), 21.0), (datetime.datetime(2260, 1, 4, 5, 20, 50), 21.0), (datetime.datetime(2260, 1, 4, 5, 44, 50), 25.0), (datetime.datetime(2260, 1, 4, 5, 58, 50), 25.0), (datetime.datetime(2260, 1, 4, 6, 4, 50), 18.0), (datetime.datetime(2260, 1, 4, 6, 14, 50), 18.0)]
temperature = [(datetime.datetime(2260, 1, 3, 21, 35, 50), 39.72222222222222), (datetime.datetime(2260, 1, 3, 23, 14, 50), 37.888888888888886), (datetime.datetime(2260, 1, 3, 23, 38, 50), 38.400000000000006), (datetime.datetime(2260, 1, 3, 23, 44, 50), 38.400000000000006), (datetime.datetime(2260, 1, 4, 0, 24, 50), 38.099999999999994), (datetime.datetime(2260, 1, 4, 0, 44, 50), 38.0), (datetime.datetime(2260, 1, 4, 1, 14, 50), 37.888888888888886), (datetime.datetime(2260, 1, 4, 1, 19, 50), 37.72222222222222), (datetime.datetime(2260, 1, 4, 1, 29, 50), 37.77777777777778), (datetime.datetime(2260, 1, 4, 1, 44, 50), 37.72222222222222), (datetime.datetime(2260, 1, 4, 1, 59, 50), 37.72222222222222), (datetime.datetime(2260, 1, 4, 2, 14, 50), 37.7), (datetime.datetime(2260, 1, 4, 2, 29, 50), 37.77777777777778), (datetime.datetime(2260, 1, 4, 2, 44, 50), 37.77777777777778), (datetime.datetime(2260, 1, 4, 2, 59, 50), 37.888888888888886), (datetime.datetime(2260, 1, 4, 3, 14, 50), 37.900000000000006), (datetime.datetime(2260, 1, 4, 3, 35, 50), 38.0), (datetime.datetime(2260, 1, 4, 3, 44, 50), 38.099999999999994), (datetime.datetime(2260, 1, 4, 3, 59, 50), 38.2), (datetime.datetime(2260, 1, 4, 4, 4, 50), 38.2), (datetime.datetime(2260, 1, 4, 4, 9, 50), 38.22222222222222), (datetime.datetime(2260, 1, 4, 4, 14, 50), 38.27777777777778), (datetime.datetime(2260, 1, 4, 4, 20, 50), 38.3), (datetime.datetime(2260, 1, 4, 4, 54, 50), 38.400000000000006), (datetime.datetime(2260, 1, 4, 5, 0, 50), 38.388888888888886), (datetime.datetime(2260, 1, 4, 5, 10, 50), 38.27777777777778), (datetime.datetime(2260, 1, 4, 5, 20, 50), 38.27777777777778), (datetime.datetime(2260, 1, 4, 5, 44, 50), 38.2), (datetime.datetime(2260, 1, 4, 5, 58, 50), 38.2), (datetime.datetime(2260, 1, 4, 6, 4, 50), 38.2), (datetime.datetime(2260, 1, 4, 6, 14, 50), 38.3)]
# Previous Results
shock_index = 0.789
shock_index_interpretation = 'Elevated (0.79), above normal range (0.5-0.7). Early compensated shock possible, monitor closely.'
map_value = 66.3
map_interpretation = 'Normal (66 mmHg), within reference range 65-100 mmHg. Adequate perfusion pressure maintained.'
pulse_pressure = 43.0
qsofa_score = 2
qsofa_interpretation = 'High Risk (Score 2/3). Criteria met: SBP=91, RR=22. Associated with poor outcomes in sepsis.'
sirs = 1
spo2_trend = {'first': np.float64(98.0), 'last': np.float64(96.0), 'min': 94.0, 'mean': 97.0, 'slope': np.float64(-0.0385), 'r_squared': np.float64(0.049), 'trend_pct': np.float64(-1.22)}
hr_volatility = {'dispersion_ms': 93.79, 'rmssd_ms': 88.39, 'hr_std_bpm': 10.39, 'hr_range_bpm': 61.0, 'n_samples': 32, 'data_density': 'sparse'}
triage_vital_panel = 'Attached'
# CORRUPTED VAR REMOVED: create_a_time-aligned_plot_of_hr,_sbp,_dbp,_map,_and_pulse_pressure_(sbp−dbp)_with_temperature_overlaid_and_mark_hypotension_(sbp<80_or_map<65)_intervals. = None
# CORRUPTED VAR REMOVED: plot_rolling_shock_index_(hr/sbp)_and_rolling_map_with_annotations_for_episodes_(si>0.9,_hr>100,_sbp<80,_map<65)_and_report_episode_counts_plus_longest_consecutive_run-length_for_each_threshold. = None
# CORRUPTED VAR REMOVED: generate_a_scatter/hexbin_of_hr_vs_sbp_colored_by_temperature_and_add_overall_plus_rolling-window_correlation_coefficients_(e.g.,_5-sample_window)_to_quantify_hr–sbp_coupling. = None
# CORRUPTED VAR REMOVED: detect_abrupt_hr_step-change_events:_compute_δhr_between_consecutive_samples,_flag_events_where_|δhr|>20_bpm,_and_quantify_associated_δsbp_and_δmap_within_the_same_interval_(median_and_iqr)_plus_event_count_and_timestamps. = None
# CORRUPTED VAR REMOVED: create_a_phase-space_scatter:_pulse_pressure_(sbp-dbp)_vs_map,_points_colored_by_temperature_and_sized_by_hr,_with_quadrants_annotated_(low_map<65_with_wide_vs_narrow_pp)_and_a_summary_table_of_time_spent_per_quadrant_plus_median_hr_and_temperature_per_quadrant. = None
# CORRUPTED VAR REMOVED: plot_a_time-aligned_event_raster_overlay_on_the_existing_vitals_panel_marking_flagged_hr_step-change_events,_and_highlight_those_with_concurrent_map<65_or_sbp_drops_≥20_mmhg_to_distinguish_paroxysmal_instability_from_gradual_compensatory_tachycardia. = None

# --- Generated Code Starts Here ---
result = {}
interpretation = {}

def _to_arrays(ts_list):
    if ts_list is None or len(ts_list) == 0:
        return (np.array([]), np.array([]))
    t = np.array([x[0] for x in ts_list], dtype=object)
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _align_nearest(ref_t, other_t, other_v, max_minutes=20.0):
    if ref_t.size == 0 or other_t.size == 0:
        return np.full(ref_t.shape, np.nan, dtype=float)
    out = np.full(ref_t.shape, np.nan, dtype=float)
    j = 0
    for i in range(ref_t.size):
        ti = ref_t[i]
        while j + 1 < other_t.size and abs((other_t[j + 1] - ti).total_seconds()) <= abs((other_t[j] - ti).total_seconds()):
            j += 1
        dt_min = abs((other_t[j] - ti).total_seconds()) / 60.0
        if dt_min <= max_minutes:
            out[i] = other_v[j]
    return out

def _episodes_from_mask(t, mask):
    episodes = []
    if t.size == 0 or mask.size == 0:
        return episodes
    in_run = False
    start_i = None
    for i in range(mask.size):
        if bool(mask[i]) and (not in_run):
            in_run = True
            start_i = i
        if in_run and (not bool(mask[i]) or i == mask.size - 1):
            end_i = i if bool(mask[i]) else i - 1
            if end_i >= start_i:
                start_t = t[start_i]
                end_t = t[end_i]
                dur_min = (end_t - start_t).total_seconds() / 60.0
                episodes.append({'start': start_t, 'end': end_t, 'n_points': int(end_i - start_i + 1), 'duration_min': float(max(dur_min, 0.0)), 'start_index': int(start_i), 'end_index': int(end_i)})
            in_run = False
            start_i = None
    return episodes
t_sbp, v_sbp = _to_arrays(systolic_bp)
t_dbp, v_dbp = _to_arrays(diastolic_bp)
if t_sbp.size == 0:
    t_ref = t_dbp
    v_sbp_aligned = _align_nearest(t_ref, t_sbp, v_sbp, max_minutes=20.0)
    v_dbp_aligned = v_dbp
else:
    t_ref = t_sbp
    v_sbp_aligned = v_sbp
    v_dbp_aligned = _align_nearest(t_ref, t_dbp, v_dbp, max_minutes=20.0)
pp = v_sbp_aligned - v_dbp_aligned
map_ts = v_dbp_aligned + pp / 3.0
valid = np.isfinite(v_sbp_aligned) & np.isfinite(v_dbp_aligned) & np.isfinite(pp) & np.isfinite(map_ts)
t_plot = t_ref[valid]
dbp_plot = v_dbp_aligned[valid]
pp_plot = pp[valid]
map_plot = map_ts[valid]
thr_map = 65.0
thr_dbp = 45.0
thr_pp = 30.0
mask_map = map_plot < thr_map
mask_dbp = dbp_plot < thr_dbp
mask_pp = pp_plot < thr_pp
episodes_map = _episodes_from_mask(t_plot, mask_map)
episodes_dbp = _episodes_from_mask(t_plot, mask_dbp)
episodes_pp = _episodes_from_mask(t_plot, mask_pp)

def _longest_run(episodes):
    if not episodes:
        return {'duration_min': 0.0, 'n_points': 0, 'start': None, 'end': None}
    e = max(episodes, key=lambda x: (x['duration_min'], x['n_points']))
    return {'duration_min': e['duration_min'], 'n_points': e['n_points'], 'start': e['start'], 'end': e['end']}
fig, ax = plt.subplots(1, 1, figsize=(12, 6))
if t_plot.size > 0:
    ax.fill_between(t_plot, 0, 1, where=mask_map, transform=ax.get_xaxis_transform(), color='red', alpha=0.12, label='MAP < 65')
    ax.fill_between(t_plot, 0, 1, where=mask_dbp, transform=ax.get_xaxis_transform(), color='orange', alpha=0.1, label='DBP < 45')
    ax.fill_between(t_plot, 0, 1, where=mask_pp, transform=ax.get_xaxis_transform(), color='purple', alpha=0.08, label='PP < 30')
ax.plot(t_plot, map_plot, color='red', lw=2.0, label='MAP (mmHg)')
ax.plot(t_plot, dbp_plot, color='orange', lw=2.0, label='DBP (mmHg)')
ax.plot(t_plot, pp_plot, color='purple', lw=2.0, label='Pulse Pressure (mmHg)')
ax.axhline(thr_map, color='red', ls='--', lw=1.0, alpha=0.8)
ax.axhline(thr_dbp, color='orange', ls='--', lw=1.0, alpha=0.8)
ax.axhline(thr_pp, color='purple', ls='--', lw=1.0, alpha=0.8)

def _annotate_episodes(episodes, y_frac, text, color):
    for e in episodes:
        x0, x1 = (e['start'], e['end'])
        ax.plot([x0, x1], [y_frac, y_frac], transform=ax.get_xaxis_transform(), color=color, lw=2.0, solid_capstyle='butt')
        ax.plot([x0, x0], [y_frac - 0.02, y_frac + 0.02], transform=ax.get_xaxis_transform(), color=color, lw=2.0)
        ax.plot([x1, x1], [y_frac - 0.02, y_frac + 0.02], transform=ax.get_xaxis_transform(), color=color, lw=2.0)
        dur = e['duration_min']
        ax.text(x0, y_frac + 0.03, f'{text} ({dur:.1f} min, n={e['n_points']})', transform=ax.get_xaxis_transform(), color=color, fontsize=8, ha='left', va='bottom')
_annotate_episodes(episodes_map, 0.92, 'Episodio MAP<65', 'red')
_annotate_episodes(episodes_dbp, 0.84, 'Episodio DBP<45', 'orange')
_annotate_episodes(episodes_pp, 0.76, 'Episodio PP<30', 'purple')
ax.set_title('Fenotipo Emodinamico (Allineato nel Tempo): MAP, DBP, Pressione Differenziale con Ombreggiatura per Ipoperfusione/Ipotensione')
ax.set_ylabel('mmHg')
ax.set_xlabel('Tempo')
ax.grid(True, alpha=0.25)
handles, labels = ax.get_legend_handles_labels()
seen = set()
h2, l2 = ([], [])
for h, l in zip(handles, labels):
    if l not in seen:
        h2.append(h)
        l2.append(l)
        seen.add(l)
ax.legend(h2, l2, loc='best', fontsize=9, frameon=True)
save_plot('hemodynamic_phenotype_map_dbp_pp.png', fig=fig)
result = {'thresholds': {'MAP_lt': thr_map, 'DBP_lt': thr_dbp, 'PP_lt': thr_pp}, 'counts': {'MAP_lt_65': int(len(episodes_map)), 'DBP_lt_45': int(len(episodes_dbp)), 'PP_lt_30': int(len(episodes_pp))}, 'episodes': {'MAP_lt_65': episodes_map, 'DBP_lt_45': episodes_dbp, 'PP_lt_30': episodes_pp}, 'longest_run': {'MAP_lt_65': _longest_run(episodes_map), 'DBP_lt_45': _longest_run(episodes_dbp), 'PP_lt_30': _longest_run(episodes_pp)}, 'n_points_plotted': int(t_plot.size), 'plot_file': 'hemodynamic_phenotype_map_dbp_pp.png'}
interpretation = {'MAP_lt_65': f'{len(episodes_map)} episodio/i contiguo/i di MAP<65 mmHg; corsa più lunga {result['longest_run']['MAP_lt_65']['duration_min']:.1f} min.', 'DBP_lt_45': f'{len(episodes_dbp)} episodio/i contiguo/i di DBP<45 mmHg; corsa più lunga {result['longest_run']['DBP_lt_45']['duration_min']:.1f} min.', 'PP_lt_30': f'{len(episodes_pp)} episodio/i contiguo/i di PP<30 mmHg; corsa più lunga {result['longest_run']['PP_lt_30']['duration_min']:.1f} min.'}

plt.close()