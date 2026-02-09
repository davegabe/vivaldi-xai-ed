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

# --- Generated Code Starts Here ---
def _extract_series(ts_list):
    if ts_list is None or len(ts_list) == 0:
        return ([], np.array([], dtype=float))
    t = [x[0] for x in ts_list]
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _time_to_minutes(t_list):
    if t_list is None or len(t_list) == 0:
        return np.array([], dtype=float)
    t0 = t_list[0]
    return np.array([(ti - t0).total_seconds() / 60.0 for ti in t_list], dtype=float)

def _rolling_time_mean(t, v, window_min):
    n = len(v)
    out = np.full(n, np.nan, dtype=float)
    if n == 0:
        return out
    j0 = 0
    for i in range(n):
        ti = t[i]
        while j0 < n and (ti - t[j0]).total_seconds() / 60.0 > window_min:
            j0 += 1
        if j0 <= i:
            seg = v[j0:i + 1]
            if seg.size > 0:
                out[i] = float(np.mean(seg))
    return out

def _longest_consecutive_run(t, mask):
    if mask is None or len(mask) == 0 or len(t) == 0:
        return {'max_run_points': 0, 'max_run_minutes': 0.0, 'n_episodes': 0}
    n = len(mask)
    max_len = 0
    max_minutes = 0.0
    n_episodes = 0
    i = 0
    while i < n:
        if bool(mask[i]):
            n_episodes += 1
            start = i
            i += 1
            while i < n and bool(mask[i]):
                i += 1
            end = i - 1
            run_len = end - start + 1
            if run_len > max_len:
                max_len = run_len
                if end > start:
                    max_minutes = (t[end] - t[start]).total_seconds() / 60.0
                else:
                    max_minutes = 0.0
        else:
            i += 1
    return {'max_run_points': int(max_len), 'max_run_minutes': float(max_minutes), 'n_episodes': int(n_episodes)}

def _build_union_timeline(series_dict):
    all_times = []
    for tlist, _ in series_dict.values():
        if tlist:
            all_times.extend(tlist)
    if len(all_times) == 0:
        return []
    all_times = sorted(set(all_times))
    return all_times

def _step_last_value_at(times, t_src, v_src):
    if len(times) == 0:
        return np.array([], dtype=float)
    if len(t_src) == 0:
        return np.full(len(times), np.nan, dtype=float)
    out = np.full(len(times), np.nan, dtype=float)
    j = 0
    last = np.nan
    for i, ti in enumerate(times):
        while j < len(t_src) and t_src[j] <= ti:
            last = float(v_src[j])
            j += 1
        out[i] = last
    return out
t_hr, v_hr = _extract_series(heart_rate)
t_sbp, v_sbp = _extract_series(systolic_bp)
t_dbp, v_dbp = _extract_series(diastolic_bp)
times_union = _build_union_timeline({'hr': (t_hr, v_hr), 'sbp': (t_sbp, v_sbp), 'dbp': (t_dbp, v_dbp)})
hr_u = _step_last_value_at(times_union, t_hr, v_hr)
sbp_u = _step_last_value_at(times_union, t_sbp, v_sbp)
dbp_u = _step_last_value_at(times_union, t_dbp, v_dbp)
with np.errstate(divide='ignore', invalid='ignore'):
    si_u = hr_u / sbp_u
map_u = (sbp_u + 2.0 * dbp_u) / 3.0
window_min = 30.0
si_roll = _rolling_time_mean(times_union, si_u, window_min)
map_roll = _rolling_time_mean(times_union, map_u, window_min)
mask_si = np.isfinite(si_u) & (si_u > 0.9)
mask_hr = np.isfinite(hr_u) & (hr_u > 100.0)
mask_sbp = np.isfinite(sbp_u) & (sbp_u < 80.0)
mask_map = np.isfinite(map_u) & (map_u < 65.0)
si_runs = _longest_consecutive_run(times_union, mask_si)
hr_runs = _longest_consecutive_run(times_union, mask_hr)
sbp_runs = _longest_consecutive_run(times_union, mask_sbp)
map_runs = _longest_consecutive_run(times_union, mask_map)
fig, axes = plt.subplots(2, 1, sharex=True, figsize=(12, 7))
x_min = _time_to_minutes(times_union)
ax = axes[0]
ax.plot(x_min, si_roll, color='tab:blue', linewidth=2, label=f'Rolling SI (mean, {int(window_min)} min)')
ax.axhline(0.9, color='tab:red', linestyle='--', linewidth=1.5, label='SI>0.9 threshold')
if len(times_union) > 0 and np.any(mask_si):
    ax.scatter(x_min[mask_si], si_roll[mask_si], color='tab:red', s=18, alpha=0.8, label='SI>0.9 episodes')
ax.set_ylabel('Shock Index (HR/SBP)')
ax.set_title('Rolling Shock Index and Rolling MAP with Episode Annotations')
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.25)
ax.legend(loc='upper right', fontsize=9)
ax2 = axes[1]
ax2.plot(x_min, map_roll, color='tab:green', linewidth=2, label=f'Rolling MAP (mean, {int(window_min)} min)')
ax2.axhline(65, color='tab:orange', linestyle='--', linewidth=1.5, label='MAP<65 threshold')
if len(times_union) > 0 and np.any(mask_map):
    ax2.scatter(x_min[mask_map], map_roll[mask_map], color='tab:orange', s=18, alpha=0.8, label='MAP<65 episodes')
if len(times_union) > 0 and np.any(mask_hr):
    ax2.scatter(x_min[mask_hr], map_roll[mask_hr], color='tab:purple', s=16, alpha=0.7, marker='^', label='HR>100')
if len(times_union) > 0 and np.any(mask_sbp):
    ax2.scatter(x_min[mask_sbp], map_roll[mask_sbp], color='tab:brown', s=16, alpha=0.7, marker='v', label='SBP<80')
ax2.set_ylabel('MAP (mmHg)')
ax2.set_xlabel('Minutes since first measurement')
ax2.grid(True, alpha=0.25)
ax2.legend(loc='upper right', fontsize=9)
plt.tight_layout()
save_plot('rolling_shock_index_map.png', fig=fig)
result = {'window_minutes': window_min, 'episodes': {'shock_index_gt_0_9': {'n_episodes': si_runs['n_episodes'], 'longest_run_points': si_runs['max_run_points'], 'longest_run_minutes': si_runs['max_run_minutes']}, 'heart_rate_gt_100_bpm': {'n_episodes': hr_runs['n_episodes'], 'longest_run_points': hr_runs['max_run_points'], 'longest_run_minutes': hr_runs['max_run_minutes']}, 'systolic_bp_lt_80_mmHg': {'n_episodes': sbp_runs['n_episodes'], 'longest_run_points': sbp_runs['max_run_points'], 'longest_run_minutes': sbp_runs['max_run_minutes']}, 'map_lt_65_mmHg': {'n_episodes': map_runs['n_episodes'], 'longest_run_points': map_runs['max_run_points'], 'longest_run_minutes': map_runs['max_run_minutes']}}, 'provided_metrics': {'shock_index': float(shock_index), 'shock_index_interpretation': str(shock_index_interpretation), 'map_value': float(map_value), 'map_interpretation': str(map_interpretation), 'qsofa_score': int(qsofa_score), 'qsofa_interpretation': str(qsofa_interpretation)}, 'plot_file': 'rolling_shock_index_map.png'}
interpretation = f'Rolling-vital episodes: SI>0.9={result['episodes']['shock_index_gt_0_9']['n_episodes']} (longest run {result['episodes']['shock_index_gt_0_9']['longest_run_points']} points/{result['episodes']['shock_index_gt_0_9']['longest_run_minutes']:.1f} min), HR>100={result['episodes']['heart_rate_gt_100_bpm']['n_episodes']} (longest {result['episodes']['heart_rate_gt_100_bpm']['longest_run_points']} points/{result['episodes']['heart_rate_gt_100_bpm']['longest_run_minutes']:.1f} min), SBP<80={result['episodes']['systolic_bp_lt_80_mmHg']['n_episodes']} (longest {result['episodes']['systolic_bp_lt_80_mmHg']['longest_run_points']} points/{result['episodes']['systolic_bp_lt_80_mmHg']['longest_run_minutes']:.1f} min), MAP<65={result['episodes']['map_lt_65_mmHg']['n_episodes']} (longest {result['episodes']['map_lt_65_mmHg']['longest_run_points']} points/{result['episodes']['map_lt_65_mmHg']['longest_run_minutes']:.1f} min).'

plt.close()