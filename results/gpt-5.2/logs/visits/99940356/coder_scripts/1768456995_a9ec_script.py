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
create_a_time-aligned_plot_of_hr,_sbp,_dbp,_map,_and_pulse_pressure_(sbp−dbp)_with_temperature_overlaid_and_mark_hypotension_(sbp<80_or_map<65)_intervals. = None
plot_rolling_shock_index_(hr/sbp)_and_rolling_map_with_annotations_for_episodes_(si>0.9,_hr>100,_sbp<80,_map<65)_and_report_episode_counts_plus_longest_consecutive_run-length_for_each_threshold. = None
generate_a_scatter/hexbin_of_hr_vs_sbp_colored_by_temperature_and_add_overall_plus_rolling-window_correlation_coefficients_(e.g.,_5-sample_window)_to_quantify_hr–sbp_coupling. = None
detect_abrupt_hr_step-change_events:_compute_δhr_between_consecutive_samples,_flag_events_where_|δhr|>20_bpm,_and_quantify_associated_δsbp_and_δmap_within_the_same_interval_(median_and_iqr)_plus_event_count_and_timestamps. = None
create_a_phase-space_scatter:_pulse_pressure_(sbp-dbp)_vs_map,_points_colored_by_temperature_and_sized_by_hr,_with_quadrants_annotated_(low_map<65_with_wide_vs_narrow_pp)_and_a_summary_table_of_time_spent_per_quadrant_plus_median_hr_and_temperature_per_quadrant. = None
plot_a_time-aligned_event_raster_overlay_on_the_existing_vitals_panel_marking_flagged_hr_step-change_events,_and_highlight_those_with_concurrent_map<65_or_sbp_drops_≥20_mmhg_to_distinguish_paroxysmal_instability_from_gradual_compensatory_tachycardia. = None

# --- Generated Code Starts Here ---
result = {}
interpretation = ''

def _to_arrays(ts_list):
    t = [x[0] for x in ts_list]
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)
hr_t, hr_v = _to_arrays(heart_rate)
sbp_t, sbp_v = _to_arrays(systolic_bp)
dbp_t, dbp_v = _to_arrays(diastolic_bp)
sbp_map = {t: float(v) for t, v in systolic_bp}
dbp_map = {t: float(v) for t, v in diastolic_bp}
aligned_idx = []
aligned_t = []
aligned_hr = []
aligned_sbp = []
aligned_dbp = []
for i, t in enumerate(hr_t):
    if t in sbp_map and t in dbp_map:
        aligned_idx.append(i)
        aligned_t.append(t)
        aligned_hr.append(float(hr_v[i]))
        aligned_sbp.append(float(sbp_map[t]))
        aligned_dbp.append(float(dbp_map[t]))
aligned_hr = np.array(aligned_hr, dtype=float)
aligned_sbp = np.array(aligned_sbp, dtype=float)
aligned_dbp = np.array(aligned_dbp, dtype=float)
aligned_map = aligned_dbp + (aligned_sbp - aligned_dbp) / 3.0
aligned_pp = aligned_sbp - aligned_dbp
n_aligned = len(aligned_hr)
threshold = 30.0
event_indices = []
event_timestamps = []
dhr = []
if n_aligned >= 2:
    dhr_all = np.diff(aligned_hr)
    for k in range(1, n_aligned):
        if abs(aligned_hr[k] - aligned_hr[k - 1]) >= threshold:
            event_indices.append(k)
            event_timestamps.append(aligned_t[k])
            dhr.append(aligned_hr[k] - aligned_hr[k - 1])
dhr = np.array(dhr, dtype=float)
win = 2
L = 2 * win + 1
center = win

def _init_matrix():
    return np.full((len(event_indices), L), np.nan, dtype=float)
E_hr = _init_matrix()
E_map = _init_matrix()
E_sbp = _init_matrix()
E_pp = _init_matrix()
for e, idx in enumerate(event_indices):
    for offset in range(-win, win + 1):
        j = idx + offset
        if 0 <= j < n_aligned:
            col = offset + win
            E_hr[e, col] = aligned_hr[j]
            E_map[e, col] = aligned_map[j]
            E_sbp[e, col] = aligned_sbp[j]
            E_pp[e, col] = aligned_pp[j]
x = np.arange(-win, win + 1, dtype=int)

def _nanmean(x, axis=0):
    with np.errstate(invalid='ignore'):
        return np.nanmean(x, axis=axis)

def _nansem(x, axis=0):
    with np.errstate(invalid='ignore'):
        n = np.sum(~np.isnan(x), axis=axis).astype(float)
        sd = np.nanstd(x, axis=axis, ddof=1)
        sem = sd / np.sqrt(n)
        sem[(n <= 1) | ~np.isfinite(sem)] = np.nan
        return sem
ta = {'x_samples': x, 'hr_mean': _nanmean(E_hr), 'hr_sem': _nansem(E_hr), 'map_mean': _nanmean(E_map), 'map_sem': _nansem(E_map), 'sbp_mean': _nanmean(E_sbp), 'sbp_sem': _nansem(E_sbp), 'pp_mean': _nanmean(E_pp), 'pp_sem': _nansem(E_pp)}
map_drop_ge_10 = 0
pp_change_ge_10 = 0
both = 0
map_delta = []
pp_delta = []
for idx in event_indices:
    dm = aligned_map[idx] - aligned_map[idx - 1]
    dpp = aligned_pp[idx] - aligned_pp[idx - 1]
    map_delta.append(dm)
    pp_delta.append(dpp)
    mflag = dm <= -10.0
    ppflag = abs(dpp) >= 10.0
    if mflag:
        map_drop_ge_10 += 1
    if ppflag:
        pp_change_ge_10 += 1
    if mflag and ppflag:
        both += 1
map_delta = np.array(map_delta, dtype=float) if len(map_delta) else np.array([], dtype=float)
pp_delta = np.array(pp_delta, dtype=float) if len(pp_delta) else np.array([], dtype=float)
n_events = len(event_indices)
pct_map_drop = 100.0 * map_drop_ge_10 / n_events if n_events else np.nan
pct_pp_change = 100.0 * pp_change_ge_10 / n_events if n_events else np.nan
pct_both = 100.0 * both / n_events if n_events else np.nan
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(10, 11))

def _plot_panel(ax, E, mean, sem, ylabel, title):
    if E.shape[0] > 0:
        for r in range(E.shape[0]):
            ax.plot(x, E[r, :], color='0.7', linewidth=1.0, alpha=0.5)
        ax.plot(x, mean, color='black', linewidth=2.0, label='Triggered mean')
        ax.fill_between(x, mean - sem, mean + sem, color='black', alpha=0.15, label='±SEM')
    ax.axvline(0, color='tab:red', linestyle='--', linewidth=1.5)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.25)
_plot_panel(axes[0], E_hr, ta['hr_mean'], ta['hr_sem'], 'HR (bpm)', 'Triggered-average around HR step-change events (ΔHR ≥ 30 bpm): HR')
_plot_panel(axes[1], E_map, ta['map_mean'], ta['map_sem'], 'MAP (mmHg)', 'MAP')
_plot_panel(axes[2], E_sbp, ta['sbp_mean'], ta['sbp_sem'], 'SBP (mmHg)', 'SBP')
_plot_panel(axes[3], E_pp, ta['pp_mean'], ta['pp_sem'], 'Pulse Pressure (mmHg)', 'Pulse Pressure (SBP-DBP)')
axes[3].set_xlabel('Samples relative to event (0 = event sample)')
axes[0].legend(loc='best', frameon=False)
save_plot('triggered_average_hr_stepchange.png', fig=fig)
table = {'n_hr_sbp_dbp_aligned_samples': n_aligned, 'event_definition': 'abs(ΔHR) >= 30 bpm between consecutive aligned samples', 'n_events': n_events, 'pct_events_map_drop_ge_10_mmhg': pct_map_drop, 'pct_events_pp_change_ge_10_mmhg': pct_pp_change, 'pct_events_both_conditions': pct_both, 'map_delta_at_event_mmhg': map_delta, 'pp_delta_at_event_mmhg': pp_delta, 'event_timestamps': event_timestamps, 'event_dhr_bpm': dhr}
result = {'triggered_average': ta, 'event_summary': table}
interpretation = f'Detected {n_events} HR step-change events (|ΔHR|≥30 bpm) on aligned HR/SBP/DBP samples; {pct_map_drop:.1f}% had concurrent MAP drop ≥10 mmHg and {pct_pp_change:.1f}% had pulse pressure change ≥10 mmHg (both: {pct_both:.1f}%).'

plt.close()