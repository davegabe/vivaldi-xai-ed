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
def _to_arrays(ts_list):
    t = [x[0] for x in ts_list]
    v = [float(x[1]) for x in ts_list]
    return (t, np.asarray(v, dtype=float))
t_sbp, v_sbp = _to_arrays(systolic_bp)
t_dbp, v_dbp = _to_arrays(diastolic_bp)

def _pair_by_nearest(t1, v1, t2, v2, max_dt_min=15.0):
    i = j = 0
    out_t, out_v1, out_v2 = ([], [], [])
    while i < len(t1) and j < len(t2):
        dt = (t1[i] - t2[j]).total_seconds()
        if abs(dt) <= max_dt_min * 60.0:
            out_t.append(t1[i] if abs(dt) <= abs((t2[j] - t1[i]).total_seconds()) else t2[j])
            out_v1.append(v1[i])
            out_v2.append(v2[j])
            i += 1
            j += 1
        elif dt < 0:
            i += 1
        else:
            j += 1
    return (out_t, np.asarray(out_v1, dtype=float), np.asarray(out_v2, dtype=float))
t_pair, sbp_p, dbp_p = _pair_by_nearest(t_sbp, v_sbp, t_dbp, v_dbp, max_dt_min=15.0)
pp = sbp_p - dbp_p
map_arr = (sbp_p + 2.0 * dbp_p) / 3.0
t_temp, v_temp = _to_arrays(temperature)

def _nearest_values(t_query, t_ref, v_ref):
    if len(t_ref) == 0:
        return np.full(len(t_query), np.nan, dtype=float)
    out = np.empty(len(t_query), dtype=float)
    j = 0
    for i, tq in enumerate(t_query):
        while j + 1 < len(t_ref) and abs((t_ref[j + 1] - tq).total_seconds()) <= abs((t_ref[j] - tq).total_seconds()):
            j += 1
        out[i] = v_ref[j]
    return out
temp_p = _nearest_values(t_pair, t_temp, v_temp)
valid = np.isfinite(pp) & np.isfinite(dbp_p) & np.isfinite(map_arr)
if np.any(np.isfinite(temp_p)):
    valid = valid & np.isfinite(temp_p)
dbp_v = dbp_p[valid]
pp_v = pp[valid]
map_v = map_arr[valid]
temp_v = temp_p[valid] if np.any(np.isfinite(temp_p)) else np.full(np.sum(valid), np.nan, dtype=float)

def _time_weighted_percentages(t, cond_a, cond_b, cond_c):
    if len(t) < 2:
        w = np.zeros(len(t), dtype=float)
    else:
        w = np.asarray([(t[i + 1] - t[i]).total_seconds() / 60.0 for i in range(len(t) - 1)] + [0.0], dtype=float)
        w = np.clip(w, 0.0, np.inf)
    total = float(np.sum(w))
    if total <= 0:
        n = float(len(t)) if len(t) else 1.0
        return {'A_map_lt_65_dbp_lt_45_pp_ge_30_pct': 100.0 * float(np.mean(cond_a)) if len(t) else 0.0, 'B_map_lt_65_pp_lt_30_pct': 100.0 * float(np.mean(cond_b)) if len(t) else 0.0, 'C_map_ge_65_pct': 100.0 * float(np.mean(cond_c)) if len(t) else 0.0, 'method': 'point-proportion'}
    return {'A_map_lt_65_dbp_lt_45_pp_ge_30_pct': 100.0 * float(np.sum(w[cond_a]) / total), 'B_map_lt_65_pp_lt_30_pct': 100.0 * float(np.sum(w[cond_b]) / total), 'C_map_ge_65_pct': 100.0 * float(np.sum(w[cond_c]) / total), 'method': 'time-weighted'}
cond_map_lt_65 = map_v < 65.0
cond_map_ge_65 = ~cond_map_lt_65
cond_a = cond_map_lt_65 & (dbp_v < 45.0) & (pp_v >= 30.0)
cond_b = cond_map_lt_65 & (pp_v < 30.0)
cond_c = cond_map_ge_65
t_valid = [t_pair[i] for i, ok in enumerate(valid) if ok]
bin_pcts = _time_weighted_percentages(t_valid, cond_a, cond_b, cond_c)
fig, ax = plt.subplots(figsize=(8, 6))
hb = ax.hexbin(dbp_v, pp_v, gridsize=25, cmap='Greys', mincnt=1, linewidths=0.2)
cb1 = fig.colorbar(hb, ax=ax)
cb1.set_label('Count (density)')
if np.any(np.isfinite(temp_v)):
    hb_t = ax.hexbin(dbp_v, pp_v, C=temp_v, reduce_C_function=np.nanmean, gridsize=25, cmap='coolwarm', mincnt=1, alpha=0.7, linewidths=0.0)
    cb2 = fig.colorbar(hb_t, ax=ax)
    cb2.set_label('Temperature (°C) mean per hex')
ax.set_xlabel('Diastolic BP (mmHg)')
ax.set_ylabel('Pulse Pressure (mmHg)')
ax.set_title('DBP vs Pulse Pressure (density with temperature overlay)')
ax.axhline(30.0, color='k', linestyle='--', linewidth=1)
ax.axvline(45.0, color='k', linestyle='--', linewidth=1)
ax.text(45.5, 30.5, 'DBP=45 / PP=30', fontsize=9, va='bottom', ha='left')
save_plot('dbp_vs_pulse_pressure_hexbin_temp.png', fig=fig)
result = {'n_paired_points': int(len(t_valid)), 'bin_percentages': bin_pcts, 'phenotype_definitions': {'A': '(MAP<65 & DBP<45 & PP≥30)', 'B': '(MAP<65 & PP<30)', 'C': '(MAP≥65)'}, 'plot_file': 'dbp_vs_pulse_pressure_hexbin_temp.png'}
interpretation = f'Phenotype time distribution (method={bin_pcts.get('method')}): {bin_pcts['A_map_lt_65_dbp_lt_45_pp_ge_30_pct']:.1f}% in MAP<65 with low DBP (<45) and wide PP (≥30), {bin_pcts['B_map_lt_65_pp_lt_30_pct']:.1f}% in MAP<65 with narrow PP (<30), and {bin_pcts['C_map_ge_65_pct']:.1f}% with MAP≥65 (adequate perfusion pressure).'

plt.close()