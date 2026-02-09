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
def _to_arrays(ts_list):
    t = np.array([x[0] for x in ts_list], dtype=object)
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _median_dt_minutes(t):
    if len(t) < 2:
        return np.nan
    dts = []
    for i in range(1, len(t)):
        dt = (t[i] - t[i - 1]).total_seconds() / 60.0
        if np.isfinite(dt) and dt > 0:
            dts.append(dt)
    return float(np.median(dts)) if len(dts) else np.nan

def _build_common_grid(t1, t2, max_dt_min=2.0):
    t_min = max(min(t1), min(t2))
    t_max = min(max(t1), max(t2))
    if t_max <= t_min:
        return None
    dt1 = _median_dt_minutes(t1)
    dt2 = _median_dt_minutes(t2)
    dt_candidates = [d for d in [dt1, dt2] if np.isfinite(d) and d > 0]
    dt = min(dt_candidates) if dt_candidates else 1.0
    dt = float(np.clip(dt, 0.25, max_dt_min))
    n = int(np.floor((t_max - t_min).total_seconds() / 60.0 / dt)) + 1
    if n < 10:
        return None
    grid = np.array([t_min + i * np.timedelta64(int(dt * 60), 's') for i in range(n)], dtype='datetime64[s]')
    return (grid, dt, t_min, t_max)

def _interp_to_grid(t_obj, v, grid_dt64s):
    t_sec = np.array([np.datetime64(tt, 's').astype('int64') for tt in t_obj], dtype=np.int64)
    g_sec = grid_dt64s.astype('int64')
    order = np.argsort(t_sec)
    t_sec = t_sec[order]
    v = v[order]
    uniq_t, inv = np.unique(t_sec, return_inverse=True)
    if len(uniq_t) != len(t_sec):
        sums = np.zeros(len(uniq_t), dtype=float)
        counts = np.zeros(len(uniq_t), dtype=float)
        np.add.at(sums, inv, v)
        np.add.at(counts, inv, 1.0)
        v = sums / np.maximum(counts, 1.0)
        t_sec = uniq_t
    if len(t_sec) < 2:
        return None
    y = np.interp(g_sec.astype(float), t_sec.astype(float), v.astype(float))
    return y

def _zscore(x):
    x = np.asarray(x, dtype=float)
    mu = np.nanmean(x)
    sd = np.nanstd(x, ddof=0)
    if not np.isfinite(sd) or sd == 0:
        return x * 0.0
    return (x - mu) / sd

def _xcorr_lags(x, y, max_lag_samples):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = min(len(x), len(y))
    x = x[:n]
    y = y[:n]
    xz = _zscore(x)
    yz = _zscore(y)
    lags = np.arange(-max_lag_samples, max_lag_samples + 1, dtype=int)
    r = np.full(lags.shape, np.nan, dtype=float)
    p = np.full(lags.shape, np.nan, dtype=float)
    n_eff = np.zeros(lags.shape, dtype=int)
    for i, k in enumerate(lags):
        if k < 0:
            xs = xz[:k]
            ys = yz[-k:]
        elif k > 0:
            xs = xz[k:]
            ys = yz[:-k]
        else:
            xs = xz
            ys = yz
        m = min(len(xs), len(ys))
        n_eff[i] = int(m)
        if m >= 10:
            rr, pp = stats.pearsonr(xs[:m], ys[:m])
            r[i] = float(rr)
            p[i] = float(pp)
    return (lags, r, p, n_eff)
t_spo2, v_spo2 = _to_arrays(spo2)
t_rr, v_rr = _to_arrays(respiratory_rate)
grid_info = _build_common_grid(t_spo2, t_rr, max_dt_min=2.0)
if grid_info is None:
    result = {'status': 'insufficient_overlap', 'message': 'Not enough overlapping time between SpO2 and RR to compute cross-correlation on a common grid.', 'max_lag_minutes': 20, 'best_lag_minutes': None, 'best_r': None, 'best_p_value': None}
    interpretation = 'Insufficient overlapping SpO2 and RR time-series coverage to assess lagged coupling within ±20 minutes.'
else:
    grid_dt64s, dt_min, t_min, t_max = grid_info
    y_spo2 = _interp_to_grid(t_spo2, v_spo2, grid_dt64s)
    y_rr = _interp_to_grid(t_rr, v_rr, grid_dt64s)
    if y_spo2 is None or y_rr is None:
        result = {'status': 'insufficient_samples', 'message': 'Not enough samples after interpolation to compute cross-correlation.', 'dt_minutes': dt_min, 'max_lag_minutes': 20, 'best_lag_minutes': None, 'best_r': None, 'best_p_value': None}
        interpretation = 'Insufficient usable samples after aligning SpO2 and RR to a common time grid to assess lagged coupling within ±20 minutes.'
    else:
        max_lag_samples = int(np.round(20.0 / dt_min))
        max_lag_samples = int(np.clip(max_lag_samples, 1, max(1, len(grid_dt64s) // 4)))
        lags, rvals, pvals, n_eff = _xcorr_lags(y_spo2, y_rr, max_lag_samples)
        valid = np.isfinite(rvals) & np.isfinite(pvals) & (n_eff >= 10)
        if not np.any(valid):
            best_idx = None
            best_lag_min = None
            best_r = None
            best_p = None
            best_n = None
            best_dir = None
        else:
            idxs = np.where(valid)[0]
            best_idx = idxs[np.argmax(np.abs(rvals[idxs]))]
            best_lag_min = float(lags[best_idx] * dt_min)
            best_r = float(rvals[best_idx])
            best_p = float(pvals[best_idx])
            best_n = int(n_eff[best_idx])
            if best_lag_min > 0:
                best_dir = 'SpO2_leads_RR'
            elif best_lag_min < 0:
                best_dir = 'RR_leads_SpO2'
            else:
                best_dir = 'synchronous'
        fig, ax = plt.subplots(2, 1, sharex=False, figsize=(10, 7))
        t_minutes = (grid_dt64s - grid_dt64s[0]).astype('timedelta64[s]').astype(float) / 60.0
        ax[0].plot(t_minutes, _zscore(y_spo2), label='SpO2 (z)', linewidth=1.5)
        ax[0].plot(t_minutes, _zscore(y_rr), label='RR (z)', linewidth=1.5)
        ax[0].set_title('Aligned SpO2 and RR on Common Grid (z-scored)')
        ax[0].set_xlabel('Minutes from overlap start')
        ax[0].set_ylabel('z-score')
        ax[0].legend(loc='best')
        ax[0].grid(True, alpha=0.3)
        lag_minutes = lags.astype(float) * dt_min
        ax[1].plot(lag_minutes, rvals, color='black', linewidth=1.5)
        ax[1].axvline(0, color='gray', linewidth=1.0, alpha=0.7)
        if best_idx is not None:
            ax[1].scatter([best_lag_min], [best_r], color='red', zorder=5)
            ax[1].text(best_lag_min, best_r, f'  best r={best_r:.2f} @ {best_lag_min:.1f} min', va='center')
        ax[1].set_title('Cross-correlation: SpO2 vs RR (Pearson r) with Lag')
        ax[1].set_xlabel('Lag (minutes). Positive: SpO2 leads RR; Negative: RR leads SpO2')
        ax[1].set_ylabel('Correlation (r)')
        ax[1].grid(True, alpha=0.3)
        plt.tight_layout()
        save_plot('spo2_rr_cross_correlation.png')
        if best_idx is None:
            interpretation = 'Unable to compute a stable SpO2–RR cross-correlation within ±20 minutes due to insufficient aligned samples.'
        else:
            signif = best_p is not None and np.isfinite(best_p) and (best_p < 0.05)
            if best_r < 0:
                coupling = 'inverse coupling (desaturation associated with higher RR)'
            elif best_r > 0:
                coupling = 'positive coupling (SpO2 and RR rise/fall together)'
            else:
                coupling = 'no coupling'
            if best_dir == 'SpO2_leads_RR':
                timing = f'SpO2 changes lead RR by ~{abs(best_lag_min):.1f} min'
            elif best_dir == 'RR_leads_SPO2':
                timing = f'RR changes lead SpO2 by ~{abs(best_lag_min):.1f} min'
            elif best_dir == 'RR_leads_SpO2':
                timing = f'RR changes lead SpO2 by ~{abs(best_lag_min):.1f} min'
            else:
                timing = 'RR and SpO2 changes are synchronous (0 min lag)'
            sig_txt = 'statistically significant' if signif else 'not statistically significant'
            interpretation = f'Within ±20 min, the strongest SpO2–RR association is r={best_r:.2f} at lag {best_lag_min:.1f} min ({timing}), {sig_txt}; pattern suggests {coupling}.'
        result = {'status': 'ok', 'dt_minutes': float(dt_min), 'overlap_start': str(t_min), 'overlap_end': str(t_max), 'n_grid_samples': int(len(grid_dt64s)), 'max_lag_minutes': 20.0, 'max_lag_samples': int(max_lag_samples), 'best_lag_minutes': best_lag_min, 'best_r': best_r, 'best_p_value': best_p, 'best_n_eff': best_n if best_idx is not None else None, 'best_direction': best_dir, 'lags_minutes': lag_minutes.tolist(), 'r_values': [None if not np.isfinite(v) else float(v) for v in rvals], 'p_values': [None if not np.isfinite(v) else float(v) for v in pvals], 'n_eff': n_eff.tolist(), 'plot_file': 'spo2_rr_cross_correlation.png'}

plt.close()