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
def _to_arrays(ts_list):
    if not ts_list:
        return (np.array([]), np.array([]))
    t = np.array([x[0] for x in ts_list], dtype=object)
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _nearest_at_or_before(t_arr, v_arr, t0):
    if t_arr.size == 0:
        return (None, np.nan)
    idx = np.searchsorted(t_arr, t0, side='right') - 1
    if idx < 0:
        return (None, np.nan)
    return (int(idx), float(v_arr[idx]))

def _window_min(t_arr, v_arr, t_end, lookback_min):
    if t_arr.size == 0:
        return np.nan
    t_start = t_end - np.timedelta64(int(round(lookback_min * 60)), 's')
    left = np.searchsorted(t_arr, t_start, side='right')
    right = np.searchsorted(t_arr, t_end, side='right')
    if right <= left:
        return np.nan
    return float(np.nanmin(v_arr[left:right]))

def _window_max(t_arr, v_arr, t_end, lookback_min):
    if t_arr.size == 0:
        return np.nan
    t_start = t_end - np.timedelta64(int(round(lookback_min * 60)), 's')
    left = np.searchsorted(t_arr, t_start, side='right')
    right = np.searchsorted(t_arr, t_end, side='right')
    if right <= left:
        return np.nan
    return float(np.nanmax(v_arr[left:right]))

def _time_to_npdt(t_obj_arr):
    if t_obj_arr.size == 0:
        return np.array([], dtype='datetime64[s]')
    out = np.empty(t_obj_arr.size, dtype='datetime64[s]')
    for i, dt in enumerate(t_obj_arr):
        out[i] = np.datetime64(dt)
    return out
t_hr_obj, hr = _to_arrays(heart_rate)
t_sbp_obj, sbp = _to_arrays(systolic_bp)
t_dbp_obj, dbp = _to_arrays(diastolic_bp)
t_temp_obj, temp = _to_arrays(temperature)
t_hr = _time_to_npdt(t_hr_obj)
t_sbp = _time_to_npdt(t_sbp_obj)
t_dbp = _time_to_npdt(t_dbp_obj)
t_temp = _time_to_npdt(t_temp_obj)

def _sort_by_time(t, v):
    if t.size == 0:
        return (t, v)
    order = np.argsort(t)
    return (t[order], v[order])
t_hr, hr = _sort_by_time(t_hr, hr)
t_sbp, sbp = _sort_by_time(t_sbp, sbp)
t_dbp, dbp = _sort_by_time(t_dbp, dbp)
t_temp, temp = _sort_by_time(t_temp, temp)
bp_times = np.unique(np.concatenate([t_sbp, t_dbp])) if t_sbp.size + t_dbp.size > 0 else np.array([], dtype='datetime64[s]')
map_ts = np.full(bp_times.shape, np.nan, dtype=float)
pp_ts = np.full(bp_times.shape, np.nan, dtype=float)
sbp_at = np.full(bp_times.shape, np.nan, dtype=float)
dbp_at = np.full(bp_times.shape, np.nan, dtype=float)
for i, t0 in enumerate(bp_times):
    _, sbp0 = _nearest_at_or_before(t_sbp, sbp, t0)
    _, dbp0 = _nearest_at_or_before(t_dbp, dbp, t0)
    sbp_at[i] = sbp0
    dbp_at[i] = dbp0
    if np.isfinite(sbp0) and np.isfinite(dbp0):
        map_ts[i] = (sbp0 + 2.0 * dbp0) / 3.0
        pp_ts[i] = sbp0 - dbp0
hr_std = float(np.nanstd(hr)) if hr.size else np.nan
step_thr = max(15.0, 1.5 * hr_std) if np.isfinite(hr_std) else 15.0
max_gap_min = 20.0
event_idx = []
event_t = []
event_delta = []
event_dir = []
event_hr = []
if t_hr.size >= 2:
    dt_min = (t_hr[1:] - t_hr[:-1]).astype('timedelta64[s]').astype(float) / 60.0
    dhr = hr[1:] - hr[:-1]
    for i in range(1, t_hr.size):
        gap = dt_min[i - 1]
        delta = dhr[i - 1]
        if np.isfinite(gap) and gap > 0 and (gap <= max_gap_min) and np.isfinite(delta):
            if abs(delta) >= step_thr:
                event_idx.append(i)
                event_t.append(t_hr[i])
                event_delta.append(float(delta))
                event_dir.append(1 if delta > 0 else -1)
                event_hr.append(float(hr[i]))
event_t = np.array(event_t, dtype='datetime64[s]')
event_delta = np.array(event_delta, dtype=float)
event_dir = np.array(event_dir, dtype=int)
event_hr = np.array(event_hr, dtype=float)
lookback_bp_min = 15.0
event_map = np.full(event_t.shape, np.nan, dtype=float)
event_sbp = np.full(event_t.shape, np.nan, dtype=float)
event_dbp = np.full(event_t.shape, np.nan, dtype=float)
flag_map65 = np.zeros(event_t.shape, dtype=bool)
flag_sbp_drop20 = np.zeros(event_t.shape, dtype=bool)
for i, t0 in enumerate(event_t):
    _, sbp0 = _nearest_at_or_before(t_sbp, sbp, t0)
    _, dbp0 = _nearest_at_or_before(t_dbp, dbp, t0)
    event_sbp[i] = sbp0
    event_dbp[i] = dbp0
    if np.isfinite(sbp0) and np.isfinite(dbp0):
        m = (sbp0 + 2.0 * dbp0) / 3.0
        event_map[i] = m
        flag_map65[i] = m < 65.0
    else:
        flag_map65[i] = False
    if np.isfinite(sbp0):
        sbp_prev_max = _window_max(t_sbp, sbp, t0, lookback_bp_min)
        if np.isfinite(sbp_prev_max):
            flag_sbp_drop20[i] = sbp_prev_max - sbp0 >= 20.0
        else:
            flag_sbp_drop20[i] = False
    else:
        flag_sbp_drop20[i] = False
flag_instability = flag_map65 | flag_sbp_drop20
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(12, 10))
axes[0].plot(t_hr, hr, color='tab:red', lw=1.5, label='HR (bpm)')
axes[0].set_ylabel('HR (bpm)')
axes[0].grid(True, alpha=0.25)
if event_t.size > 0:
    y0, y1 = axes[0].get_ylim()
    y_raster = y0 + 0.06 * (y1 - y0)
    t_non = event_t[~flag_instability]
    t_bad = event_t[flag_instability]
    if t_non.size > 0:
        axes[0].vlines(t_non, y_raster - 0.04 * (y1 - y0), y_raster + 0.04 * (y1 - y0), color='tab:blue', lw=1.2, alpha=0.9, label='HR step-change')
    if t_bad.size > 0:
        axes[0].vlines(t_bad, y_raster - 0.06 * (y1 - y0), y_raster + 0.06 * (y1 - y0), color='k', lw=2.0, alpha=0.95, label='HR step + MAP<65 or SBP drop≥20')
    axes[0].set_ylim(y0, y1)
axes[1].plot(t_sbp, sbp, color='tab:purple', lw=1.5, label='SBP (mmHg)')
axes[1].plot(t_dbp, dbp, color='tab:green', lw=1.2, label='DBP (mmHg)')
axes[1].axhline(80.0, color='k', ls='--', lw=1.0, alpha=0.6, label='SBP 80')
axes[1].set_ylabel('BP (mmHg)')
axes[1].grid(True, alpha=0.25)
if bp_times.size > 0:
    axes[2].plot(bp_times, map_ts, color='tab:orange', lw=1.5, label='MAP (mmHg)')
    axes[2].plot(bp_times, pp_ts, color='tab:gray', lw=1.2, label='Pulse Pressure (mmHg)')
axes[2].axhline(65.0, color='k', ls='--', lw=1.0, alpha=0.6, label='MAP 65')
axes[2].set_ylabel('MAP/PP')
axes[2].grid(True, alpha=0.25)
axes[3].plot(t_temp, temp, color='tab:brown', lw=1.5, label='Temp (°C)')
axes[3].axhline(38.0, color='k', ls='--', lw=1.0, alpha=0.6, label='38.0°C')
axes[3].axhline(39.0, color='k', ls=':', lw=1.0, alpha=0.6, label='39.0°C')
axes[3].set_ylabel('Temp (°C)')
axes[3].set_xlabel('Time')
axes[3].grid(True, alpha=0.25)
for ax in axes:
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(loc='upper left', fontsize=9, frameon=False, ncol=2)
plt.suptitle('Vitals Panel with HR Step-Change Event Raster (instability highlighted)', y=0.99)
plt.tight_layout(rect=[0, 0, 1, 0.97])
save_plot('vitals_panel_event_raster.png', fig=fig)
n_events = int(event_t.size)
n_instab = int(np.sum(flag_instability)) if n_events else 0
n_map65 = int(np.sum(flag_map65)) if n_events else 0
n_sbpdrop = int(np.sum(flag_sbp_drop20)) if n_events else 0
n_hr_up = int(np.sum(event_dir == 1)) if n_events else 0
n_hr_down = int(np.sum(event_dir == -1)) if n_events else 0
longest_run = 0
if n_events > 0:
    order = np.argsort(event_t)
    t_sorted = event_t[order]
    bad_sorted = flag_instability[order]
    gaps = np.zeros(t_sorted.size, dtype=float)
    if t_sorted.size >= 2:
        gaps[1:] = (t_sorted[1:] - t_sorted[:-1]).astype('timedelta64[s]').astype(float) / 60.0
    run = 0
    for i in range(t_sorted.size):
        if not bad_sorted[i]:
            run = 0
            continue
        if i == 0 or gaps[i] <= 30.0:
            run = run + 1
        else:
            run = 1
        if run > longest_run:
            longest_run = run
result = {'plot_file': 'vitals_panel_event_raster.png', 'hr_step_threshold_bpm': float(step_thr), 'max_hr_sample_gap_min_for_step': float(max_gap_min), 'bp_lookback_min_for_sbp_drop': float(lookback_bp_min), 'n_hr_step_events': n_events, 'n_hr_step_events_up': n_hr_up, 'n_hr_step_events_down': n_hr_down, 'n_events_with_map_lt_65': n_map65, 'n_events_with_sbp_drop_ge_20': n_sbpdrop, 'n_events_with_instability_flag': n_instab, 'longest_consecutive_instability_event_run_within_30min': int(longest_run), 'uses_provided_scalar_metrics': {'shock_index': float(shock_index), 'map_value': float(map_value), 'qsofa_score': int(qsofa_score)}}
interpretation = f'Detected {n_events} HR step-change events (|ΔHR|≥{step_thr:.1f} bpm within {max_gap_min:.0f} min); {n_instab}/{n_events} were concurrent with hemodynamic concern (MAP<65 and/or SBP drop≥20 mmHg in prior {lookback_bp_min:.0f} min), supporting paroxysmal instability superimposed on baseline low pressures (MAP {map_value:.1f} mmHg; shock index {shock_index:.3f}; qSOFA {qsofa_score}).'

plt.close()