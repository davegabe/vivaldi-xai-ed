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
visit_id = '99973518'
age = 56
gender = 'M'
ethnicity = 'Other (Hispanic/Latino)'
heart_rate = [(datetime.datetime(2215, 7, 20, 16, 29, 49), 97.7457627118644), (datetime.datetime(2215, 7, 20, 16, 30, 49), 98.7586206896552), (datetime.datetime(2215, 7, 20, 16, 31, 49), 100.745762711864), (datetime.datetime(2215, 7, 20, 16, 32, 49), 100.64406779661), (datetime.datetime(2215, 7, 20, 16, 33, 49), 99.0172413793104), (datetime.datetime(2215, 7, 20, 16, 34, 49), 97.2881355932203), (datetime.datetime(2215, 7, 20, 16, 35, 49), 96.6271186440678), (datetime.datetime(2215, 7, 20, 16, 36, 49), 96.7758620689655), (datetime.datetime(2215, 7, 20, 16, 37, 49), 97.0338983050848), (datetime.datetime(2215, 7, 20, 16, 38, 49), 96.8793103448276), (datetime.datetime(2215, 7, 20, 16, 39, 49), 96.3389830508475), (datetime.datetime(2215, 7, 20, 16, 40, 49), 95.9491525423729), (datetime.datetime(2215, 7, 20, 16, 41, 49), 96.8448275862069), (datetime.datetime(2215, 7, 20, 16, 42, 49), 96.2372881355932), (datetime.datetime(2215, 7, 20, 16, 43, 49), 96.6896551724138), (datetime.datetime(2215, 7, 20, 16, 44, 49), 97.2542372881356), (datetime.datetime(2215, 7, 20, 16, 45, 49), 96.1864406779661), (datetime.datetime(2215, 7, 20, 16, 46, 49), 96.0517241379311), (datetime.datetime(2215, 7, 20, 16, 47, 49), 96.5932203389831), (datetime.datetime(2215, 7, 20, 16, 48, 49), 97.551724137931), (datetime.datetime(2215, 7, 20, 16, 49, 49), 95.4237288135593), (datetime.datetime(2215, 7, 20, 16, 50, 49), 95.9322033898305), (datetime.datetime(2215, 7, 20, 16, 51, 49), 96.5862068965517), (datetime.datetime(2215, 7, 20, 16, 52, 49), 95.8983050847458), (datetime.datetime(2215, 7, 20, 16, 53, 49), 95.948275862069), (datetime.datetime(2215, 7, 20, 17, 18, 49), 86.0), (datetime.datetime(2215, 7, 20, 17, 23, 49), 88.0), (datetime.datetime(2215, 7, 20, 17, 33, 49), 87.0), (datetime.datetime(2215, 7, 20, 17, 48, 49), 85.0), (datetime.datetime(2215, 7, 20, 17, 53, 49), 85.0), (datetime.datetime(2215, 7, 20, 18, 3, 49), 84.0), (datetime.datetime(2215, 7, 20, 18, 18, 49), 80.0), (datetime.datetime(2215, 7, 20, 18, 42, 49), 80.0), (datetime.datetime(2215, 7, 20, 18, 48, 49), 80.0), (datetime.datetime(2215, 7, 20, 19, 13, 49), 76.0), (datetime.datetime(2215, 7, 20, 19, 18, 49), 77.0), (datetime.datetime(2215, 7, 20, 19, 20, 49), 77.0), (datetime.datetime(2215, 7, 20, 19, 30, 49), 89.0), (datetime.datetime(2215, 7, 20, 19, 40, 49), 83.0), (datetime.datetime(2215, 7, 20, 19, 48, 49), 84.0), (datetime.datetime(2215, 7, 20, 19, 50, 49), 80.0), (datetime.datetime(2215, 7, 20, 20, 0, 49), 81.0), (datetime.datetime(2215, 7, 20, 20, 18, 49), 76.0), (datetime.datetime(2215, 7, 20, 20, 21, 49), 75.0), (datetime.datetime(2215, 7, 20, 20, 36, 49), 76.0), (datetime.datetime(2215, 7, 20, 20, 49, 49), 73.0), (datetime.datetime(2215, 7, 20, 20, 50, 49), 69.0), (datetime.datetime(2215, 7, 20, 20, 55, 49), 70.0), (datetime.datetime(2215, 7, 20, 21, 0, 49), 73.0), (datetime.datetime(2215, 7, 20, 21, 2, 49), 73.0), (datetime.datetime(2215, 7, 20, 21, 48, 49), 78.0), (datetime.datetime(2215, 7, 20, 21, 54, 49), 79.0), (datetime.datetime(2215, 7, 20, 22, 18, 49), 75.0), (datetime.datetime(2215, 7, 20, 22, 23, 49), 75.0)]
systolic_bp = [(datetime.datetime(2215, 7, 20, 16, 29, 49), 92.0), (datetime.datetime(2215, 7, 20, 16, 34, 49), 83.0), (datetime.datetime(2215, 7, 20, 16, 35, 49), 83.0), (datetime.datetime(2215, 7, 20, 16, 39, 49), 90.0), (datetime.datetime(2215, 7, 20, 16, 40, 49), 90.0), (datetime.datetime(2215, 7, 20, 16, 44, 49), 85.0), (datetime.datetime(2215, 7, 20, 16, 49, 49), 94.0), (datetime.datetime(2215, 7, 20, 16, 54, 49), 82.0), (datetime.datetime(2215, 7, 20, 17, 18, 49), 102.0), (datetime.datetime(2215, 7, 20, 17, 23, 49), 86.0), (datetime.datetime(2215, 7, 20, 17, 33, 49), 92.0), (datetime.datetime(2215, 7, 20, 17, 53, 49), 84.0), (datetime.datetime(2215, 7, 20, 18, 3, 49), 86.0), (datetime.datetime(2215, 7, 20, 18, 18, 49), 84.0), (datetime.datetime(2215, 7, 20, 18, 42, 49), 81.0), (datetime.datetime(2215, 7, 20, 18, 48, 49), 75.0), (datetime.datetime(2215, 7, 20, 19, 13, 49), 87.0), (datetime.datetime(2215, 7, 20, 19, 20, 49), 91.0), (datetime.datetime(2215, 7, 20, 19, 30, 49), 119.0), (datetime.datetime(2215, 7, 20, 19, 40, 49), 94.0), (datetime.datetime(2215, 7, 20, 19, 50, 49), 89.0), (datetime.datetime(2215, 7, 20, 20, 0, 49), 82.0), (datetime.datetime(2215, 7, 20, 20, 18, 49), 79.0), (datetime.datetime(2215, 7, 20, 20, 21, 49), 77.0), (datetime.datetime(2215, 7, 20, 20, 36, 49), 71.0), (datetime.datetime(2215, 7, 20, 20, 49, 49), 67.0), (datetime.datetime(2215, 7, 20, 20, 50, 49), 71.0), (datetime.datetime(2215, 7, 20, 20, 55, 49), 80.0), (datetime.datetime(2215, 7, 20, 21, 0, 49), 105.0), (datetime.datetime(2215, 7, 20, 21, 2, 49), 120.0), (datetime.datetime(2215, 7, 20, 21, 48, 49), 84.0), (datetime.datetime(2215, 7, 20, 21, 54, 49), 92.0), (datetime.datetime(2215, 7, 20, 22, 18, 49), 87.0), (datetime.datetime(2215, 7, 20, 22, 23, 49), 108.0)]
diastolic_bp = [(datetime.datetime(2215, 7, 20, 16, 29, 49), 66.0), (datetime.datetime(2215, 7, 20, 16, 34, 49), 64.0), (datetime.datetime(2215, 7, 20, 16, 35, 49), 64.0), (datetime.datetime(2215, 7, 20, 16, 39, 49), 60.0), (datetime.datetime(2215, 7, 20, 16, 40, 49), 60.0), (datetime.datetime(2215, 7, 20, 16, 44, 49), 61.0), (datetime.datetime(2215, 7, 20, 16, 49, 49), 84.0), (datetime.datetime(2215, 7, 20, 16, 54, 49), 67.0), (datetime.datetime(2215, 7, 20, 17, 18, 49), 61.0), (datetime.datetime(2215, 7, 20, 17, 23, 49), 61.0), (datetime.datetime(2215, 7, 20, 17, 33, 49), 66.0), (datetime.datetime(2215, 7, 20, 17, 53, 49), 59.0), (datetime.datetime(2215, 7, 20, 18, 3, 49), 58.0), (datetime.datetime(2215, 7, 20, 18, 18, 49), 57.0), (datetime.datetime(2215, 7, 20, 18, 42, 49), 58.0), (datetime.datetime(2215, 7, 20, 18, 48, 49), 61.0), (datetime.datetime(2215, 7, 20, 19, 13, 49), 64.0), (datetime.datetime(2215, 7, 20, 19, 20, 49), 67.0), (datetime.datetime(2215, 7, 20, 19, 30, 49), 90.0), (datetime.datetime(2215, 7, 20, 19, 40, 49), 57.0), (datetime.datetime(2215, 7, 20, 19, 50, 49), 50.0), (datetime.datetime(2215, 7, 20, 20, 0, 49), 56.0), (datetime.datetime(2215, 7, 20, 20, 18, 49), 60.0), (datetime.datetime(2215, 7, 20, 20, 21, 49), 59.0), (datetime.datetime(2215, 7, 20, 20, 36, 49), 44.0), (datetime.datetime(2215, 7, 20, 20, 49, 49), 39.0), (datetime.datetime(2215, 7, 20, 20, 50, 49), 42.0), (datetime.datetime(2215, 7, 20, 20, 55, 49), 62.0), (datetime.datetime(2215, 7, 20, 21, 0, 49), 88.0), (datetime.datetime(2215, 7, 20, 21, 2, 49), 103.0), (datetime.datetime(2215, 7, 20, 21, 48, 49), 52.0), (datetime.datetime(2215, 7, 20, 21, 54, 49), 52.0), (datetime.datetime(2215, 7, 20, 22, 18, 49), 56.0), (datetime.datetime(2215, 7, 20, 22, 23, 49), 71.0)]
spo2 = [(datetime.datetime(2215, 7, 20, 16, 29, 49), 94.5593220338983), (datetime.datetime(2215, 7, 20, 16, 30, 49), 94.8620689655172), (datetime.datetime(2215, 7, 20, 16, 31, 49), 90.7627118644068), (datetime.datetime(2215, 7, 20, 16, 32, 49), 89.0677966101695), (datetime.datetime(2215, 7, 20, 16, 33, 49), 90.66), (datetime.datetime(2215, 7, 20, 16, 34, 49), 91.5762711864407), (datetime.datetime(2215, 7, 20, 16, 35, 49), 92.0), (datetime.datetime(2215, 7, 20, 16, 36, 49), 92.6206896551724), (datetime.datetime(2215, 7, 20, 16, 37, 49), 92.0169491525424), (datetime.datetime(2215, 7, 20, 16, 38, 49), 92.0877192982456), (datetime.datetime(2215, 7, 20, 16, 39, 49), 94.3389830508475), (datetime.datetime(2215, 7, 20, 16, 40, 49), 94.7627118644068), (datetime.datetime(2215, 7, 20, 16, 41, 49), 94.5689655172414), (datetime.datetime(2215, 7, 20, 16, 42, 49), 94.8813559322034), (datetime.datetime(2215, 7, 20, 16, 43, 49), 94.7954545454546), (datetime.datetime(2215, 7, 20, 16, 44, 49), 94.5263157894737), (datetime.datetime(2215, 7, 20, 16, 45, 49), 94.0), (datetime.datetime(2215, 7, 20, 16, 46, 49), 94.0), (datetime.datetime(2215, 7, 20, 16, 47, 49), 94.0), (datetime.datetime(2215, 7, 20, 16, 48, 49), 95.6724137931034), (datetime.datetime(2215, 7, 20, 16, 49, 49), 92.6440677966102), (datetime.datetime(2215, 7, 20, 16, 50, 49), 90.4237288135593), (datetime.datetime(2215, 7, 20, 16, 51, 49), 92.7931034482759), (datetime.datetime(2215, 7, 20, 16, 52, 49), 92.5423728813559), (datetime.datetime(2215, 7, 20, 16, 53, 49), 92.0862068965517), (datetime.datetime(2215, 7, 20, 17, 12, 49), 94.0), (datetime.datetime(2215, 7, 20, 17, 18, 49), 98.0), (datetime.datetime(2215, 7, 20, 17, 23, 49), 98.0), (datetime.datetime(2215, 7, 20, 17, 33, 49), 93.0), (datetime.datetime(2215, 7, 20, 17, 48, 49), 94.0), (datetime.datetime(2215, 7, 20, 17, 53, 49), 96.0), (datetime.datetime(2215, 7, 20, 18, 3, 49), 96.0), (datetime.datetime(2215, 7, 20, 18, 18, 49), 96.0), (datetime.datetime(2215, 7, 20, 18, 42, 49), 96.0), (datetime.datetime(2215, 7, 20, 18, 48, 49), 96.0), (datetime.datetime(2215, 7, 20, 19, 13, 49), 97.0), (datetime.datetime(2215, 7, 20, 19, 18, 49), 96.0), (datetime.datetime(2215, 7, 20, 19, 20, 49), 96.0), (datetime.datetime(2215, 7, 20, 19, 30, 49), 97.0), (datetime.datetime(2215, 7, 20, 19, 40, 49), 97.0), (datetime.datetime(2215, 7, 20, 19, 48, 49), 97.0), (datetime.datetime(2215, 7, 20, 19, 50, 49), 96.0), (datetime.datetime(2215, 7, 20, 20, 0, 49), 96.0), (datetime.datetime(2215, 7, 20, 20, 11, 49), 96.0), (datetime.datetime(2215, 7, 20, 20, 18, 49), 96.0), (datetime.datetime(2215, 7, 20, 20, 21, 49), 97.0), (datetime.datetime(2215, 7, 20, 20, 36, 49), 100.0), (datetime.datetime(2215, 7, 20, 20, 49, 49), 95.0), (datetime.datetime(2215, 7, 20, 20, 50, 49), 97.0), (datetime.datetime(2215, 7, 20, 20, 55, 49), 95.0), (datetime.datetime(2215, 7, 20, 21, 0, 49), 96.0), (datetime.datetime(2215, 7, 20, 21, 2, 49), 96.0), (datetime.datetime(2215, 7, 20, 21, 48, 49), 100.0), (datetime.datetime(2215, 7, 20, 21, 54, 49), 100.0), (datetime.datetime(2215, 7, 20, 22, 18, 49), 100.0), (datetime.datetime(2215, 7, 20, 22, 23, 49), 100.0)]
respiratory_rate = [(datetime.datetime(2215, 7, 20, 16, 29, 49), 22.1864406779661), (datetime.datetime(2215, 7, 20, 16, 30, 49), 23.7241379310345), (datetime.datetime(2215, 7, 20, 16, 31, 49), 26.728813559322), (datetime.datetime(2215, 7, 20, 16, 32, 49), 28.1016949152542), (datetime.datetime(2215, 7, 20, 16, 33, 49), 27.6896551724138), (datetime.datetime(2215, 7, 20, 16, 34, 49), 24.4237288135593), (datetime.datetime(2215, 7, 20, 16, 35, 49), 26.7118644067797), (datetime.datetime(2215, 7, 20, 16, 36, 49), 22.2068965517241), (datetime.datetime(2215, 7, 20, 16, 37, 49), 22.8474576271187), (datetime.datetime(2215, 7, 20, 16, 38, 49), 22.0344827586207), (datetime.datetime(2215, 7, 20, 16, 39, 49), 21.1186440677966), (datetime.datetime(2215, 7, 20, 16, 40, 49), 22.4915254237288), (datetime.datetime(2215, 7, 20, 16, 41, 49), 22.2586206896552), (datetime.datetime(2215, 7, 20, 16, 42, 49), 22.6271186440678), (datetime.datetime(2215, 7, 20, 16, 43, 49), 21.7931034482759), (datetime.datetime(2215, 7, 20, 16, 44, 49), 22.3389830508475), (datetime.datetime(2215, 7, 20, 16, 45, 49), 20.6779661016949), (datetime.datetime(2215, 7, 20, 16, 46, 49), 22.1724137931035), (datetime.datetime(2215, 7, 20, 16, 47, 49), 25.8305084745763), (datetime.datetime(2215, 7, 20, 16, 48, 49), 25.5689655172414), (datetime.datetime(2215, 7, 20, 16, 49, 49), 24.4915254237288), (datetime.datetime(2215, 7, 20, 16, 50, 49), 23.4406779661017), (datetime.datetime(2215, 7, 20, 16, 51, 49), 23.5), (datetime.datetime(2215, 7, 20, 16, 52, 49), 22.406779661017), (datetime.datetime(2215, 7, 20, 16, 53, 49), 23.2413793103448), (datetime.datetime(2215, 7, 20, 17, 18, 49), 34.0), (datetime.datetime(2215, 7, 20, 17, 23, 49), 20.0), (datetime.datetime(2215, 7, 20, 17, 33, 49), 27.0), (datetime.datetime(2215, 7, 20, 17, 48, 49), 20.0), (datetime.datetime(2215, 7, 20, 17, 53, 49), 20.0), (datetime.datetime(2215, 7, 20, 18, 3, 49), 22.0), (datetime.datetime(2215, 7, 20, 18, 18, 49), 17.0), (datetime.datetime(2215, 7, 20, 18, 42, 49), 19.0), (datetime.datetime(2215, 7, 20, 18, 48, 49), 18.0), (datetime.datetime(2215, 7, 20, 19, 13, 49), 19.0), (datetime.datetime(2215, 7, 20, 19, 18, 49), 17.0), (datetime.datetime(2215, 7, 20, 19, 20, 49), 18.0), (datetime.datetime(2215, 7, 20, 19, 30, 49), 26.0), (datetime.datetime(2215, 7, 20, 19, 40, 49), 25.0), (datetime.datetime(2215, 7, 20, 19, 48, 49), 29.0), (datetime.datetime(2215, 7, 20, 19, 50, 49), 26.0), (datetime.datetime(2215, 7, 20, 20, 0, 49), 32.0), (datetime.datetime(2215, 7, 20, 20, 11, 49), 27.0), (datetime.datetime(2215, 7, 20, 20, 18, 49), 22.0), (datetime.datetime(2215, 7, 20, 20, 21, 49), 26.0), (datetime.datetime(2215, 7, 20, 20, 36, 49), 32.0), (datetime.datetime(2215, 7, 20, 20, 49, 49), 22.0), (datetime.datetime(2215, 7, 20, 20, 50, 49), 19.0), (datetime.datetime(2215, 7, 20, 20, 55, 49), 26.0), (datetime.datetime(2215, 7, 20, 21, 0, 49), 24.0), (datetime.datetime(2215, 7, 20, 21, 2, 49), 32.0), (datetime.datetime(2215, 7, 20, 21, 48, 49), 24.0), (datetime.datetime(2215, 7, 20, 21, 54, 49), 25.0), (datetime.datetime(2215, 7, 20, 22, 18, 49), 23.0), (datetime.datetime(2215, 7, 20, 22, 23, 49), 25.0)]
temperature = [(datetime.datetime(2215, 7, 20, 16, 35, 49), 38.27777777777778), (datetime.datetime(2215, 7, 20, 17, 23, 49), 37.888888888888886), (datetime.datetime(2215, 7, 20, 17, 33, 49), 37.888888888888886), (datetime.datetime(2215, 7, 20, 17, 48, 49), 37.888888888888886), (datetime.datetime(2215, 7, 20, 17, 53, 49), 37.888888888888886), (datetime.datetime(2215, 7, 20, 18, 3, 49), 37.77777777777778), (datetime.datetime(2215, 7, 20, 18, 18, 49), 37.611111111111114), (datetime.datetime(2215, 7, 20, 18, 42, 49), 37.3), (datetime.datetime(2215, 7, 20, 18, 48, 49), 37.27777777777778), (datetime.datetime(2215, 7, 20, 19, 13, 49), 37.099999999999994), (datetime.datetime(2215, 7, 20, 19, 18, 49), 37.111111111111114), (datetime.datetime(2215, 7, 20, 19, 20, 49), 37.111111111111114), (datetime.datetime(2215, 7, 20, 19, 30, 49), 37.0), (datetime.datetime(2215, 7, 20, 19, 40, 49), 36.888888888888886), (datetime.datetime(2215, 7, 20, 19, 48, 49), 36.888888888888886), (datetime.datetime(2215, 7, 20, 19, 50, 49), 36.888888888888886), (datetime.datetime(2215, 7, 20, 20, 0, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 20, 11, 49), 36.8), (datetime.datetime(2215, 7, 20, 20, 18, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 20, 21, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 20, 36, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 20, 49, 49), 36.888888888888886), (datetime.datetime(2215, 7, 20, 20, 50, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 20, 55, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 21, 0, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 21, 2, 49), 36.77777777777778), (datetime.datetime(2215, 7, 20, 21, 48, 49), 36.72222222222222), (datetime.datetime(2215, 7, 20, 21, 54, 49), 36.72222222222222), (datetime.datetime(2215, 7, 20, 22, 18, 49), 36.7), (datetime.datetime(2215, 7, 20, 22, 23, 49), 36.7)]
# Previous Results
shock_index = 1.1
shock_index_interpretation = 'HIGH (1.10), significantly above normal (0.5-0.7). Suggests decompensated shock, immediate intervention needed.'
map_value = 72.7
map_interpretation = 'Normal (73 mmHg), within reference range 65-100 mmHg. Adequate perfusion pressure maintained.'
pulse_pressure = 26.0
qsofa_score = 2
qsofa_interpretation = 'High Risk (Score 2/3). Criteria met: SBP=92, RR=22. Associated with poor outcomes in sepsis.'
sirs = 1
spo2_trend = {'first': np.float64(94.6), 'last': np.float64(100.0), 'min': 89.1, 'mean': 95.1, 'slope': np.float64(0.118), 'r_squared': np.float64(0.578), 'trend_pct': np.float64(7.07)}
hr_volatility = {'dispersion_ms': 81.05, 'rmssd_ms': 26.18, 'hr_std_bpm': 9.81, 'hr_range_bpm': 31.7, 'n_samples': 54, 'data_density': 'sparse'}
triage_vital_panel = 'Attached'

# --- Generated Code Starts Here ---
timestamps = [t for t, v in spo2]
values = [v for t, v in spo2]
n = len(values)
rolling_std = []
for i in range(n):
    start_idx = max(0, i - 4)
    window = values[start_idx:i + 1]
    if len(window) >= 2:
        rolling_std.append(np.std(window, ddof=1))
    else:
        rolling_std.append(0.0)
desaturation_events = []
in_event = False
event_start = None
event_start_idx = None
for i, (t, v) in enumerate(spo2):
    if v < 92:
        if not in_event:
            in_event = True
            event_start = t
            event_start_idx = i
    elif in_event:
        event_end = spo2[i - 1][0]
        duration_min = (event_end - event_start).total_seconds() / 60.0
        min_val = min(values[event_start_idx:i])
        min_idx = event_start_idx + values[event_start_idx:i].index(min_val)
        desaturation_events.append({'start': event_start, 'end': event_end, 'duration_min': duration_min, 'min_val': min_val, 'min_time': timestamps[min_idx]})
        in_event = False
if in_event:
    event_end = timestamps[-1]
    duration_min = (event_end - event_start).total_seconds() / 60.0
    min_val = min(values[event_start_idx:])
    min_idx = event_start_idx + values[event_start_idx:].index(min_val)
    desaturation_events.append({'start': event_start, 'end': event_end, 'duration_min': duration_min, 'min_val': min_val, 'min_time': timestamps[min_idx]})
fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.plot(timestamps, values, 'b-', linewidth=1.5, marker='o', markersize=4, label='SpO2 (%)')
ax1.axhline(y=92, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Desaturation Threshold (92%)')
ax1.axhline(y=90, color='darkred', linestyle=':', linewidth=1.5, alpha=0.7, label='Critical Threshold (90%)')
for event in desaturation_events:
    ax1.axvspan(event['start'], event['end'], alpha=0.3, color='red')
    annotation_text = f'Desat: {event['min_val']:.1f}%\nDuration: {event['duration_min']:.1f} min'
    ax1.annotate(annotation_text, xy=(event['min_time'], event['min_val']), xytext=(10, -30), textcoords='offset points', fontsize=8, color='darkred', fontweight='bold', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='red', alpha=0.8), arrowprops=dict(arrowstyle='->', color='red', lw=1))
ax1.set_xlabel('Time', fontsize=11)
ax1.set_ylabel('SpO2 (%)', color='blue', fontsize=11)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_ylim(85, 102)
ax2 = ax1.twinx()
ax2.fill_between(timestamps, rolling_std, alpha=0.3, color='orange', label='Rolling 5-pt Std Dev')
ax2.plot(timestamps, rolling_std, 'orange', linewidth=1, linestyle='-', alpha=0.7)
ax2.set_ylabel('Rolling Std Dev (%)', color='orange', fontsize=11)
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(0, max(rolling_std) * 2.5 if max(rolling_std) > 0 else 5)
plt.title(f'SpO2 Time Series with Variability Analysis\n56yo Male with Chronic Respiratory Disease | {len(desaturation_events)} Desaturation Event(s) Detected', fontsize=12, fontweight='bold')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower right', fontsize=9)
fig.autofmt_xdate()
plt.tight_layout()
save_plot('spo2_desaturation_analysis.png')
total_desat_duration = sum((e['duration_min'] for e in desaturation_events))
min_spo2_during_events = min([e['min_val'] for e in desaturation_events]) if desaturation_events else None
result = {'desaturation_events_count': len(desaturation_events), 'total_desaturation_duration_min': round(total_desat_duration, 2), 'lowest_spo2_during_desaturation': min_spo2_during_events, 'spo2_overall_min': min(values), 'spo2_overall_mean': round(np.mean(values), 2), 'max_rolling_std': round(max(rolling_std), 2), 'mean_rolling_std': round(np.mean(rolling_std), 2), 'events_detail': [{'start': str(e['start']), 'duration_min': round(e['duration_min'], 2), 'nadir_spo2': e['min_val']} for e in desaturation_events]}
interpretation = f'Patient experienced {len(desaturation_events)} desaturation episode(s) below 92% totaling {total_desat_duration:.1f} minutes, with lowest SpO2 of {min_spo2_during_events}% during events; overall SpO2 trend is IMPROVING (slope +0.118%/min) with mean 95.1%, consistent with chronic respiratory disease with acute exacerbation now stabilizing, though variability (max rolling std {max(rolling_std):.2f}%) suggests continued monitoring warranted in this high-risk tracheostomy patient.'

plt.close()