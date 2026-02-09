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
from datetime import datetime, timedelta
map_value = 66.3
map_interpretation = 'Normal (66 mmHg), within reference range 65-100 mmHg. Adequate perfusion pressure maintained.'
systolic_bp_data = [(datetime(2024, 1, 1, 0, 0), 94.0), (datetime(2024, 1, 1, 1, 0), 95.0), (datetime(2024, 1, 1, 2, 0), 96.0), (datetime(2024, 1, 1, 3, 0), 97.0), (datetime(2024, 1, 1, 4, 0), 98.0), (datetime(2024, 1, 1, 5, 0), 99.0), (datetime(2024, 1, 1, 6, 0), 100.0), (datetime(2024, 1, 1, 7, 0), 101.0), (datetime(2024, 1, 1, 8, 0), 102.0), (datetime(2024, 1, 1, 9, 0), 103.0), (datetime(2024, 1, 1, 10, 0), 104.0), (datetime(2024, 1, 1, 11, 0), 105.0), (datetime(2024, 1, 1, 12, 0), 106.0), (datetime(2024, 1, 1, 13, 0), 107.0), (datetime(2024, 1, 1, 14, 0), 108.0), (datetime(2024, 1, 1, 15, 0), 109.0), (datetime(2024, 1, 1, 16, 0), 110.0), (datetime(2024, 1, 1, 17, 0), 111.0), (datetime(2024, 1, 1, 18, 0), 112.0), (datetime(2024, 1, 1, 19, 0), 113.0), (datetime(2024, 1, 1, 20, 0), 114.0), (datetime(2024, 1, 1, 21, 0), 115.0), (datetime(2024, 1, 1, 22, 0), 116.0), (datetime(2024, 1, 1, 23, 0), 117.0)]
diastolic_bp_data = [(datetime(2024, 1, 1, 0, 0), 53.0), (datetime(2024, 1, 1, 1, 0), 54.0), (datetime(2024, 1, 1, 2, 0), 55.0), (datetime(2024, 1, 1, 3, 0), 56.0), (datetime(2024, 1, 1, 4, 0), 57.0), (datetime(2024, 1, 1, 5, 0), 58.0), (datetime(2024, 1, 1, 6, 0), 59.0), (datetime(2024, 1, 1, 7, 0), 60.0), (datetime(2024, 1, 1, 8, 0), 61.0), (datetime(2024, 1, 1, 9, 0), 62.0), (datetime(2024, 1, 1, 10, 0), 63.0), (datetime(2024, 1, 1, 11, 0), 64.0), (datetime(2024, 1, 1, 12, 0), 65.0), (datetime(2024, 1, 1, 13, 0), 66.0), (datetime(2024, 1, 1, 14, 0), 67.0), (datetime(2024, 1, 1, 15, 0), 68.0), (datetime(2024, 1, 1, 16, 0), 69.0), (datetime(2024, 1, 1, 17, 0), 70.0), (datetime(2024, 1, 1, 18, 0), 71.0), (datetime(2024, 1, 1, 19, 0), 72.0), (datetime(2024, 1, 1, 20, 0), 73.0), (datetime(2024, 1, 1, 21, 0), 74.0), (datetime(2024, 1, 1, 22, 0), 75.0), (datetime(2024, 1, 1, 23, 0), 76.0)]
map_data = []
for i in range(min(len(systolic_bp_data), len(diastolic_bp_data))):
    timestamp = systolic_bp_data[i][0]
    systolic = systolic_bp_data[i][1]
    diastolic = diastolic_bp_data[i][1]
    map_value = (systolic + 2 * diastolic) / 3
    map_data.append((timestamp, map_value))
now = datetime.now()
start_time = now - timedelta(hours=12)
filtered_map_data = [(ts, val) for ts, val in map_data if ts >= start_time]
timestamps = [ts for ts, val in filtered_map_data]
map_values = [val for ts, val in filtered_map_data]
plt.figure(figsize=(12, 6))
plt.plot(timestamps, map_values, marker='o', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Mean Arterial Pressure (mmHg)')
plt.title('Mean Arterial Pressure Trend (Last 12 Hours)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
save_plot('map_trend_last_12_hours.png')

plt.close()