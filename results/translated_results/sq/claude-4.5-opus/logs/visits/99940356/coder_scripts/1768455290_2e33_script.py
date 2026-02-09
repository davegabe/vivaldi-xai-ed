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
import numpy as np
from datetime import datetime
hr_times = [t for t, v in heart_rate]
hr_values = [v for t, v in heart_rate]
sbp_times = [t for t, v in systolic_bp]
sbp_values = [v for t, v in systolic_bp]
min_time = max(min(hr_times), min(sbp_times))
max_time = min(max(hr_times), max(sbp_times))
all_times = sorted(set(hr_times + sbp_times))
all_times = [t for t in all_times if min_time <= t <= max_time]

def interpolate_at_time(times, values, target_time):
    if target_time <= times[0]:
        return values[0]
    if target_time >= times[-1]:
        return values[-1]
    for i in range(len(times) - 1):
        if times[i] <= target_time <= times[i + 1]:
            dt = (times[i + 1] - times[i]).total_seconds()
            if dt == 0:
                return values[i]
            frac = (target_time - times[i]).total_seconds() / dt
            return values[i] + frac * (values[i + 1] - values[i])
    return values[-1]
si_times = []
si_values = []
for t in all_times:
    hr_interp = interpolate_at_time(hr_times, hr_values, t)
    sbp_interp = interpolate_at_time(sbp_times, sbp_values, t)
    if sbp_interp > 0:
        si = hr_interp / sbp_interp
        si_times.append(t)
        si_values.append(si)
start_time = si_times[0]
minutes_from_start = [(t - start_time).total_seconds() / 60.0 for t in si_times]
x = np.array(minutes_from_start)
y = np.array(si_values)
slope, intercept = np.polyfit(x, y, 1)
trend_line = slope * x + intercept
ss_res = np.sum((y - trend_line) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
if slope > 0.001:
    trend_direction = 'increasing (worsening)'
elif slope < -0.001:
    trend_direction = 'decreasing (improving)'
else:
    trend_direction = 'stable'
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(minutes_from_start, si_values, 'o-', color='#2E86AB', linewidth=2, markersize=6, label='Shock Index', alpha=0.8)
ax.plot(minutes_from_start, trend_line, '--', color='#E74C3C', linewidth=2, label=f'Trend (slope: {slope * 60:.4f}/hr)')
ax.axhline(y=0.7, color='green', linestyle=':', alpha=0.7, label='Normal upper limit (0.7)')
ax.axhline(y=1.0, color='orange', linestyle=':', alpha=0.7, label='Elevated threshold (1.0)')
ax.axhspan(0, 0.7, alpha=0.1, color='green')
ax.axhspan(0.7, 1.0, alpha=0.1, color='yellow')
ax.axhspan(1.0, max(si_values) + 0.2, alpha=0.1, color='red')
ax.axhline(y=shock_index, color='purple', linestyle='-', alpha=0.5, linewidth=1.5, label=f'Current SI: {shock_index:.3f}')
ax.set_xlabel('Time from First Reading (minutes)', fontsize=11)
ax.set_ylabel('Shock Index (HR/SBP)', fontsize=11)
ax.set_title(f'Shock Index Trajectory Over Time\n82yo Male - High Risk for Sepsis', fontsize=12, fontweight='bold')
stats_text = f'Mean SI: {np.mean(si_values):.3f}\nRange: {np.min(si_values):.3f} - {np.max(si_values):.3f}\nTrend: {trend_direction}\nR²: {r_squared:.3f}'
ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=9, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.legend(loc='upper right', fontsize=9)
ax.set_ylim(0, max(si_values) + 0.3)
ax.grid(True, alpha=0.3)
plt.tight_layout()
save_plot('shock_index_trajectory.png')
si_change = si_values[-1] - si_values[0]
si_change_pct = si_change / si_values[0] * 100 if si_values[0] > 0 else 0
duration_minutes = (si_times[-1] - si_times[0]).total_seconds() / 60.0
result = {'current_shock_index': shock_index, 'mean_shock_index': round(np.mean(si_values), 3), 'min_shock_index': round(np.min(si_values), 3), 'max_shock_index': round(np.max(si_values), 3), 'trend_slope_per_hour': round(slope * 60, 4), 'trend_direction': trend_direction, 'r_squared': round(r_squared, 3), 'si_change_absolute': round(si_change, 3), 'si_change_percent': round(si_change_pct, 1), 'monitoring_duration_minutes': round(duration_minutes, 1), 'n_measurements': len(si_values)}
if shock_index >= 1.0:
    severity = 'CRITICAL: SI ≥1.0 indicates significant shock risk'
elif shock_index >= 0.7:
    severity = 'ELEVATED: SI 0.7-1.0 suggests early compensated shock'
else:
    severity = 'Normal SI range'
interpretation = f'Shock Index trajectory analysis over {duration_minutes:.0f} minutes shows {trend_direction} trend (slope: {slope * 60:.4f}/hr, R²={r_squared:.2f}). Current SI of {shock_index:.2f} is {shock_index_interpretation.split('.')[0].lower()}. In this 82yo male with severe sepsis history, orthostatic hypotension on midodrine, and active fever, the elevated SI warrants close monitoring for hemodynamic deterioration. Mean SI {np.mean(si_values):.2f} over observation period with range {np.min(si_values):.2f}-{np.max(si_values):.2f}.'

plt.close()