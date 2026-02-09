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
from datetime import datetime

def _extract_xy_temp(heart_rate, systolic_bp, temperature, max_time_diff_min=30.0):
    hr_t = [t for t, v in heart_rate]
    hr_v = np.array([v for t, v in heart_rate], dtype=float)
    sbp_t = [t for t, v in systolic_bp]
    sbp_v = np.array([v for t, v in systolic_bp], dtype=float)
    tmp_t = [t for t, v in temperature]
    tmp_v = np.array([v for t, v in temperature], dtype=float)
    x_hr = []
    y_sbp = []
    c_tmp = []
    dt_hr_min = []
    dt_tmp_min = []
    for i, t_sbp in enumerate(sbp_t):
        j_hr = int(np.argmin([abs((t - t_sbp).total_seconds()) for t in hr_t]))
        dthr = abs((hr_t[j_hr] - t_sbp).total_seconds()) / 60.0
        j_tmp = int(np.argmin([abs((t - t_sbp).total_seconds()) for t in tmp_t]))
        dttmp = abs((tmp_t[j_tmp] - t_sbp).total_seconds()) / 60.0
        if dthr <= max_time_diff_min and dttmp <= max_time_diff_min:
            x_hr.append(hr_v[j_hr])
            y_sbp.append(sbp_v[i])
            c_tmp.append(tmp_v[j_tmp])
            dt_hr_min.append(dthr)
            dt_tmp_min.append(dttmp)
    return (np.array(x_hr, dtype=float), np.array(y_sbp, dtype=float), np.array(c_tmp, dtype=float), np.array(dt_hr_min, dtype=float), np.array(dt_tmp_min, dtype=float))
x_hr, y_sbp, c_tmp, dt_hr_min, dt_tmp_min = _extract_xy_temp(heart_rate=heart_rate, systolic_bp=systolic_bp, temperature=temperature, max_time_diff_min=30.0)
n_pairs = int(x_hr.size)

def _safe_pearsonr(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if a.size < 3 or np.nanstd(a) == 0.0 or np.nanstd(b) == 0.0:
        return (np.nan, np.nan)
    r, p = stats.pearsonr(a, b)
    return (float(r), float(p))
overall_r, overall_p = _safe_pearsonr(x_hr, y_sbp)
overall_spearman_rho, overall_spearman_p = (np.nan, np.nan)
if n_pairs >= 3 and np.nanstd(x_hr) > 0.0 and (np.nanstd(y_sbp) > 0.0):
    sr = stats.spearmanr(x_hr, y_sbp, nan_policy='omit')
    overall_spearman_rho, overall_spearman_p = (float(sr.correlation), float(sr.pvalue))
window = 5
roll_r = []
roll_p = []
roll_center = []
if n_pairs >= window:
    for i in range(n_pairs - window + 1):
        r_i, p_i = _safe_pearsonr(x_hr[i:i + window], y_sbp[i:i + window])
        roll_r.append(r_i)
        roll_p.append(p_i)
        roll_center.append(i + (window - 1) / 2.0)
roll_r = np.array(roll_r, dtype=float) if len(roll_r) else np.array([], dtype=float)
roll_p = np.array(roll_p, dtype=float) if len(roll_p) else np.array([], dtype=float)
roll_r_median = float(np.nanmedian(roll_r)) if roll_r.size else np.nan
roll_r_mean = float(np.nanmean(roll_r)) if roll_r.size else np.nan
roll_r_min = float(np.nanmin(roll_r)) if roll_r.size else np.nan
roll_r_max = float(np.nanmax(roll_r)) if roll_r.size else np.nan
if n_pairs > 0:
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    hb = ax.hexbin(x_hr, y_sbp, C=c_tmp, reduce_C_function=np.nanmean, gridsize=20, mincnt=1, cmap='inferno')
    cb = fig.colorbar(hb, ax=ax)
    cb.set_label('Temperature (°C)')
    ax.set_xlabel('Heart Rate (bpm)')
    ax.set_ylabel('Systolic BP (mmHg)')
    ax.set_title('HR vs SBP (hexbin), colored by Temperature')
    txt_lines = []
    if np.isfinite(overall_r):
        txt_lines.append(f'Overall Pearson r={overall_r:.2f} (p={overall_p:.3g})')
    else:
        txt_lines.append('Overall Pearson r=NA')
    if np.isfinite(overall_spearman_rho):
        txt_lines.append(f'Overall Spearman ρ={overall_spearman_rho:.2f} (p={overall_spearman_p:.3g})')
    else:
        txt_lines.append('Overall Spearman ρ=NA')
    if roll_r.size:
        txt_lines.append(f'Rolling (n={window}) Pearson r: median={roll_r_median:.2f}, range=[{roll_r_min:.2f},{roll_r_max:.2f}]')
    else:
        txt_lines.append(f'Rolling (n={window}) Pearson r: NA (insufficient pairs)')
    txt_lines.append(f'Paired points: {n_pairs} (tolerance ≤30 min)')
    ax.text(0.02, 0.98, '\n'.join(txt_lines), transform=ax.transAxes, va='top', ha='left', fontsize=9, bbox=dict(boxstyle='round', facecolor='white', alpha=0.85, edgecolor='0.6'))
    save_plot('hr_sbp_hexbin_temp.png', fig=fig)
fig2, ax2 = plt.subplots(1, 1, figsize=(9, 4))
if roll_r.size:
    ax2.plot(np.arange(roll_r.size), roll_r, lw=1.8, color='tab:blue')
    ax2.axhline(0.0, color='0.3', lw=1.0, ls='--')
    ax2.set_ylim(-1.05, 1.05)
    ax2.set_xlabel(f'Rolling window index (window={window})')
    ax2.set_ylabel('Pearson r (HR vs SBP)')
    ax2.set_title('Rolling HR–SBP coupling (Pearson r)')
    ax2.text(0.01, 0.02, f'median r={roll_r_median:.2f} | mean r={roll_r_mean:.2f} | range [{roll_r_min:.2f},{roll_r_max:.2f}]', transform=ax2.transAxes, va='bottom', ha='left', fontsize=9)
else:
    ax2.text(0.5, 0.5, f'Insufficient paired points for rolling r (need ≥{window}).\nPaired points: {n_pairs}', ha='center', va='center', transform=ax2.transAxes)
    ax2.set_axis_off()
save_plot('hr_sbp_rolling_correlation.png', fig=fig2)
result = {'n_pairs_hr_sbp_temp': n_pairs, 'pairing_tolerance_minutes': 30.0, 'pairing_dt_hr_minutes_summary': {'median': float(np.nanmedian(dt_hr_min)) if dt_hr_min.size else np.nan, 'max': float(np.nanmax(dt_hr_min)) if dt_hr_min.size else np.nan}, 'pairing_dt_temp_minutes_summary': {'median': float(np.nanmedian(dt_tmp_min)) if dt_tmp_min.size else np.nan, 'max': float(np.nanmax(dt_tmp_min)) if dt_tmp_min.size else np.nan}, 'overall_pearson_r_hr_vs_sbp': overall_r, 'overall_pearson_p_hr_vs_sbp': overall_p, 'overall_spearman_rho_hr_vs_sbp': overall_spearman_rho, 'overall_spearman_p_hr_vs_sbp': overall_spearman_p, 'rolling_window_n_samples': window, 'rolling_pearson_r_summary': {'median': roll_r_median, 'mean': roll_r_mean, 'min': roll_r_min, 'max': roll_r_max, 'n_windows': int(roll_r.size)}, 'provided_context_metrics': {'shock_index': shock_index, 'shock_index_interpretation': shock_index_interpretation, 'map_value': map_value, 'map_interpretation': map_interpretation, 'qsofa_score': qsofa_score, 'qsofa_interpretation': qsofa_interpretation}, 'plots_saved': ['hr_sbp_hexbin_temp.png', 'hr_sbp_rolling_correlation.png']}

def _coupling_label(r):
    if not np.isfinite(r):
        return 'indeterminate'
    ar = abs(r)
    if ar < 0.2:
        return 'minimal'
    if ar < 0.4:
        return 'weak'
    if ar < 0.6:
        return 'moderate'
    return 'strong'
interpretation = {'overall_hr_sbp_coupling': f'HR–SBP coupling overall is {_coupling_label(overall_r)} (Pearson r={overall_r:.2f}{('; p=' + format(overall_p, '.3g') if np.isfinite(overall_p) else '')}), with rolling-window (n={window}) coupling median r={roll_r_median:.2f} (range [{roll_r_min:.2f},{roll_r_max:.2f}]) across {int(roll_r.size)} windows.' if n_pairs >= 3 else f'HR–SBP coupling could not be reliably quantified due to limited paired observations (n={n_pairs}).'}

plt.close()