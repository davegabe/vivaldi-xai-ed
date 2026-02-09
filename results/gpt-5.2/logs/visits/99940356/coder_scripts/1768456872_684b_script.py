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

# --- Generated Code Starts Here ---
def _to_arrays(series):
    t = np.array([x[0] for x in series], dtype=object)
    v = np.array([float(x[1]) for x in series], dtype=float)
    return (t, v)

def _median_or_nan(x):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    return float(np.nan) if x.size == 0 else float(np.median(x))

def _nearest_value(ts, t_query):
    if ts is None or len(ts) == 0:
        return np.nan
    times = [x[0] for x in ts]
    lo, hi = (0, len(times) - 1)
    if t_query <= times[0]:
        return float(ts[0][1])
    if t_query >= times[-1]:
        return float(ts[-1][1])
    while lo <= hi:
        mid = (lo + hi) // 2
        if times[mid] < t_query:
            lo = mid + 1
        elif times[mid] > t_query:
            hi = mid - 1
        else:
            return float(ts[mid][1])
    i1, i2 = (hi, lo)
    dt1 = abs((t_query - times[i1]).total_seconds())
    dt2 = abs((times[i2] - t_query).total_seconds())
    return float(ts[i1][1]) if dt1 <= dt2 else float(ts[i2][1])

def _time_deltas_minutes(t_sorted):
    n = len(t_sorted)
    if n == 0:
        return np.array([], dtype=float)
    if n == 1:
        return np.array([0.0], dtype=float)
    dur = np.zeros(n, dtype=float)
    for i in range(n):
        if i == 0:
            dur[i] = (t_sorted[1] - t_sorted[0]).total_seconds() / 60.0 / 2.0
        elif i == n - 1:
            dur[i] = (t_sorted[-1] - t_sorted[-2]).total_seconds() / 60.0 / 2.0
        else:
            dur[i] = ((t_sorted[i] - t_sorted[i - 1]).total_seconds() + (t_sorted[i + 1] - t_sorted[i]).total_seconds()) / 60.0 / 2.0
    dur = np.clip(dur, 0.0, None)
    return dur
sbp_map = {t: float(v) for t, v in systolic_bp}
dbp_map = {t: float(v) for t, v in diastolic_bp}
common_times = sorted(set(sbp_map.keys()).intersection(dbp_map.keys()))
use_nearest_dbp = False
if len(common_times) == 0:
    common_times = [t for t, _ in systolic_bp]
    use_nearest_dbp = True
times = []
sbp_vals = []
dbp_vals = []
hr_vals = []
temp_vals = []
for t in common_times:
    sbp = sbp_map.get(t, np.nan)
    if use_nearest_dbp:
        dbp = _nearest_value(diastolic_bp, t)
    else:
        dbp = dbp_map.get(t, np.nan)
    if np.isnan(sbp) or np.isnan(dbp):
        continue
    times.append(t)
    sbp_vals.append(float(sbp))
    dbp_vals.append(float(dbp))
    hr_vals.append(float(_nearest_value(heart_rate, t)))
    temp_vals.append(float(_nearest_value(temperature, t)))
times = np.array(times, dtype=object)
sbp_vals = np.array(sbp_vals, dtype=float)
dbp_vals = np.array(dbp_vals, dtype=float)
hr_vals = np.array(hr_vals, dtype=float)
temp_vals = np.array(temp_vals, dtype=float)
pp_vals = sbp_vals - dbp_vals
map_vals = (sbp_vals + 2.0 * dbp_vals) / 3.0
pp_cut = float(np.median(pp_vals)) if pp_vals.size > 0 else np.nan
low_map = map_vals < 65.0
wide_pp = pp_vals >= pp_cut
quad = np.empty(pp_vals.shape[0], dtype=object)
quad[np.where(low_map & ~wide_pp)[0]] = 'Low MAP<65 & Narrow PP'
quad[np.where(low_map & wide_pp)[0]] = 'Low MAP<65 & Wide PP'
quad[np.where(~low_map & ~wide_pp)[0]] = 'MAP≥65 & Narrow PP'
quad[np.where(~low_map & wide_pp)[0]] = 'MAP≥65 & Wide PP'
order = np.argsort(times)
times_s = times[order]
pp_s = pp_vals[order]
map_s = map_vals[order]
hr_s = hr_vals[order]
temp_s = temp_vals[order]
quad_s = quad[order]
dur_min = _time_deltas_minutes(times_s)
total_time_min = float(np.sum(dur_min)) if dur_min.size > 0 else 0.0
quad_names = ['Low MAP<65 & Narrow PP', 'Low MAP<65 & Wide PP', 'MAP≥65 & Narrow PP', 'MAP≥65 & Wide PP']
summary_rows = []
for qn in quad_names:
    idx = np.where(quad_s == qn)[0]
    tmin = float(np.sum(dur_min[idx])) if idx.size > 0 else 0.0
    pct = 100.0 * tmin / total_time_min if total_time_min > 0 else 0.0
    med_hr = _median_or_nan(hr_s[idx]) if idx.size > 0 else float(np.nan)
    med_temp = _median_or_nan(temp_s[idx]) if idx.size > 0 else float(np.nan)
    npts = int(idx.size)
    summary_rows.append({'quadrant': qn, 'n_points': npts, 'time_minutes': tmin, 'time_percent': pct, 'median_hr_bpm': med_hr, 'median_temp_c': med_temp})
result = {'pp_cut_mmhg_median': pp_cut, 'total_time_minutes_est': total_time_min, 'quadrant_summary': summary_rows, 'n_phase_points': int(pp_s.size), 'map_threshold_low': 65.0}
fig, ax = plt.subplots(1, 1, figsize=(10, 7))
if hr_s.size > 0 and np.all(np.isnan(hr_s)):
    sizes = np.full_like(hr_s, 40.0, dtype=float)
else:
    hr_min = float(np.nanmin(hr_s)) if hr_s.size > 0 else 0.0
    hr_max = float(np.nanmax(hr_s)) if hr_s.size > 0 else 1.0
    if not np.isfinite(hr_min) or not np.isfinite(hr_max) or hr_max <= hr_min:
        sizes = np.full_like(hr_s, 50.0, dtype=float)
    else:
        sizes = 30.0 + 170.0 * (np.clip(hr_s, hr_min, hr_max) - hr_min) / (hr_max - hr_min)
sc = ax.scatter(pp_s, map_s, c=temp_s, s=sizes, cmap='viridis', alpha=0.85, edgecolors='none')
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Temperature (°C)')
ax.axhline(65.0, color='crimson', linestyle='--', linewidth=1.5, label='MAP 65 mmHg threshold')
if np.isfinite(pp_cut):
    ax.axvline(pp_cut, color='dimgray', linestyle='--', linewidth=1.5, label=f'PP median split ({pp_cut:.1f} mmHg)')
if pp_s.size > 0 and map_s.size > 0:
    xmin, xmax = (float(np.nanmin(pp_s)), float(np.nanmax(pp_s)))
    ymin, ymax = (float(np.nanmin(map_s)), float(np.nanmax(map_s)))
    xr = xmax - xmin if xmax > xmin else 1.0
    yr = ymax - ymin if ymax > ymin else 1.0
    x_left = xmin + 0.05 * xr
    x_right = xmin + 0.55 * xr if np.isfinite(pp_cut) else xmin + 0.55 * xr
    x_split = pp_cut if np.isfinite(pp_cut) else xmin + 0.5 * xr
    x_left = min(x_left, x_split - 0.02 * xr)
    x_right = max(x_right, x_split + 0.02 * xr)
    y_low = ymin + 0.1 * yr
    y_high = ymin + 0.65 * yr
    y_split = 65.0
    ax.text(x_left, y_split - 0.03 * yr, 'Low MAP\nNarrow PP', color='crimson', fontsize=10, va='top', ha='left')
    ax.text(x_right, y_split - 0.03 * yr, 'Low MAP\nWide PP', color='crimson', fontsize=10, va='top', ha='left')
    ax.text(x_left, y_split + 0.03 * yr, 'MAP≥65\nNarrow PP', color='black', fontsize=10, va='bottom', ha='left')
    ax.text(x_right, y_split + 0.03 * yr, 'MAP≥65\nWide PP', color='black', fontsize=10, va='bottom', ha='left')
ax.set_title('Phase-Space: Pulse Pressure (SBP-DBP) vs MAP\nColor=Temperature, Size=Heart Rate')
ax.set_xlabel('Pulse Pressure (mmHg)')
ax.set_ylabel('MAP (mmHg)')
ax.grid(True, alpha=0.25)
ax.legend(loc='best', frameon=True)
save_plot('phase_space_pp_vs_map_temp_hr.png', fig=fig)
fig2, ax2 = plt.subplots(1, 1, figsize=(11, 3.8))
ax2.axis('off')
table_cols = ['Quadrant', 'N', 'Time (min)', 'Time (%)', 'Median HR (bpm)', 'Median Temp (°C)']
table_data = []
for row in summary_rows:
    table_data.append([row['quadrant'], f'{row['n_points']}', f'{row['time_minutes']:.1f}', f'{row['time_percent']:.1f}', 'NA' if not np.isfinite(row['median_hr_bpm']) else f'{row['median_hr_bpm']:.1f}', 'NA' if not np.isfinite(row['median_temp_c']) else f'{row['median_temp_c']:.2f}'])
tbl = ax2.table(cellText=table_data, colLabels=table_cols, loc='center', cellLoc='left', colLoc='left')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1, 1.4)
ax2.set_title(f'Quadrant Summary (MAP threshold 65 mmHg; PP split at median {pp_cut:.1f} mmHg)')
save_plot('phase_space_quadrant_summary_table.png', fig=fig2)
low_map_time = next((r['time_minutes'] for r in summary_rows if r['quadrant'] == 'Low MAP<65 & Narrow PP'), 0.0) + next((r['time_minutes'] for r in summary_rows if r['quadrant'] == 'Low MAP<65 & Wide PP'), 0.0)
low_map_pct = 100.0 * low_map_time / total_time_min if total_time_min > 0 else 0.0
interpretation = f'Phase-space hemodynamics: estimated {low_map_time:.1f} min ({low_map_pct:.1f}%) spent with MAP<65 mmHg, with pulse pressure split at median {pp_cut:.1f} mmHg; points are temperature-colored (°C) and HR-sized (bpm) to contextualize febrile, higher-HR states during low-perfusion quadrants.'

plt.close()