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
compute_and_plot_cross-correlation_(lag_±20_min)_between_spo2_and_hr_to_assess_reflex_tachycardia_timing_relative_to_hypoxemia_(episodic_obstruction)_vs_sustained_hr-rr_coupling_independent_of_spo2_(pe/shock). = None
plot_time-aligned_trajectories_of_shock_index,_sbp,_map,_and_pulse_pressure_with_a_30-min_rolling_minimum_sbp_overlay_to_detect_progressive_hypotension/occult_shock_despite_preserved_map_and_to_see_whether_si_spikes_cluster_around_hypoxemia/tachypnea_episodes. = None
compute_and_plot_cross-correlation_(lag_±20_min)_between_spo2_and_rr_to_test_whether_desaturation_events_precede/reactively_increase_rr_(airway_events)_vs_persistent_tachypnea_without_spo2_coupling_(pe/shock). = None

# --- Generated Code Starts Here ---
result = {}
interpretation = ''

def _to_arrays(ts_list):
    t = [x[0] for x in ts_list]
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _minutes_between(t1, t2):
    return (t2 - t1).total_seconds() / 60.0

def _nearest_match_indices(t_src, t_ref):
    idxs = []
    j = 0
    n = len(t_ref)
    for i in range(len(t_src)):
        ti = t_src[i]
        while j + 1 < n and abs((t_ref[j + 1] - ti).total_seconds()) <= abs((t_ref[j] - ti).total_seconds()):
            j += 1
        idxs.append(j)
    return np.array(idxs, dtype=int)

def _rolling_corr_by_time(t, x, y, window_min):
    n = len(t)
    r = np.full(n, np.nan, dtype=float)
    count = np.zeros(n, dtype=int)
    left = 0
    for i in range(n):
        while left < i and _minutes_between(t[left], t[i]) > window_min:
            left += 1
        xs = x[left:i + 1]
        ys = y[left:i + 1]
        k = len(xs)
        count[i] = k
        if k >= 3 and np.nanstd(xs) > 0 and (np.nanstd(ys) > 0):
            r[i] = float(np.corrcoef(xs, ys)[0, 1])
    return (r, count)

def _time_deltas_minutes(t):
    n = len(t)
    if n == 0:
        return np.array([], dtype=float)
    dt = np.zeros(n, dtype=float)
    if n == 1:
        dt[0] = 0.0
        return dt
    for i in range(n):
        if i == 0:
            dt[i] = _minutes_between(t[0], t[1])
        elif i == n - 1:
            dt[i] = _minutes_between(t[n - 2], t[n - 1])
        else:
            dt[i] = 0.5 * _minutes_between(t[i - 1], t[i + 1])
    dt[dt < 0] = 0.0
    return dt
t_rr, rr = _to_arrays(respiratory_rate)
t_sp, sp = _to_arrays(spo2)
if len(t_rr) < 3 or len(t_sp) < 3:
    result = {'n_matched': 0, 'message': 'Insufficient RR or SpO2 samples to compute rolling coupling.'}
    interpretation = 'Insufficient paired RR–SpO2 data to quantify tachypnea–oxygenation coupling.'
else:
    tolerance_min = 5.0
    idx_near = _nearest_match_indices(t_rr, t_sp)
    sp_matched = sp[idx_near]
    dt_min = np.array([abs(_minutes_between(t_rr[i], t_sp[idx_near[i]])) for i in range(len(t_rr))], dtype=float)
    keep = dt_min <= tolerance_min
    t = [t_rr[i] for i in range(len(t_rr)) if keep[i]]
    rr_m = rr[keep]
    sp_m = sp_matched[keep]
    if len(t) < 10:
        tolerance_min2 = 10.0
        keep2 = dt_min <= tolerance_min2
        t = [t_rr[i] for i in range(len(t_rr)) if keep2[i]]
        rr_m = rr[keep2]
        sp_m = sp_matched[keep2]
        tolerance_used = tolerance_min2
    else:
        tolerance_used = tolerance_min
    n = len(t)
    r10, n10 = _rolling_corr_by_time(t, rr_m, sp_m, window_min=10.0)
    r15, n15 = _rolling_corr_by_time(t, rr_m, sp_m, window_min=15.0)
    rr_hi = rr_m >= 28.0
    sp_ok = sp_m >= 94.0
    dt = _time_deltas_minutes(t)
    total_time = float(np.nansum(dt)) if n > 0 else 0.0
    q1 = rr_hi & sp_ok
    q2 = rr_hi & ~sp_ok
    q3 = ~rr_hi & sp_ok
    q4 = ~rr_hi & ~sp_ok

    def _pct(mask):
        if total_time <= 0:
            return np.nan
        return 100.0 * float(np.nansum(dt[mask])) / total_time
    dwell = {'RR>=28 & SpO2>=94 (%)': _pct(q1), 'RR>=28 & SpO2<94 (%)': _pct(q2), 'RR<28 & SpO2>=94 (%)': _pct(q3), 'RR<28 & SpO2<94 (%)': _pct(q4), 'total_dwell_minutes': total_time}

    def _nan_stats(a):
        a = np.array(a, dtype=float)
        a = a[np.isfinite(a)]
        if a.size == 0:
            return {'mean': np.nan, 'median': np.nan, 'min': np.nan, 'max': np.nan, 'n': 0}
        return {'mean': float(np.mean(a)), 'median': float(np.median(a)), 'min': float(np.min(a)), 'max': float(np.max(a)), 'n': int(a.size)}
    corr_stats = {'rolling_corr_10min': _nan_stats(r10), 'rolling_corr_15min': _nan_stats(r15), 'n_matched': int(n), 'match_tolerance_min': float(tolerance_used)}
    if n > 0:
        elapsed = np.array([_minutes_between(t[0], ti) for ti in t], dtype=float)
        fig, axes = plt.subplots(2, 1, figsize=(10, 9), sharex=False, constrained_layout=True)
        ax = axes[0]
        sc = ax.scatter(sp_m, rr_m, c=elapsed, cmap='viridis', s=28, alpha=0.9, edgecolors='none')
        cbar = plt.colorbar(sc, ax=ax)
        cbar.set_label('Elapsed time (min)')
        ax.set_title('Phase-space: RR vs SpO₂ (colored by time)')
        ax.set_xlabel('SpO₂ (%)')
        ax.set_ylabel('Respiratory Rate (breaths/min)')
        ax.axvline(94.0, color='black', lw=1, ls='--')
        ax.axhline(28.0, color='black', lw=1, ls='--')
        txt = f'RR≥28 & SpO₂≥94: {dwell['RR>=28 & SpO2>=94 (%)']:.1f}%\nRR≥28 & SpO₂<94: {dwell['RR>=28 & SpO2<94 (%)']:.1f}%\nRR<28 & SpO₂≥94: {dwell['RR<28 & SpO2>=94 (%)']:.1f}%\nRR<28 & SpO₂<94: {dwell['RR<28 & SpO2<94 (%)']:.1f}%'
        ax.text(0.99, 0.01, txt, transform=ax.transAxes, ha='right', va='bottom', fontsize=10, bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='0.3', alpha=0.9))
        ax2 = axes[1]
        ax2.plot(elapsed, r10, lw=1.8, label='Rolling corr (10 min)')
        ax2.plot(elapsed, r15, lw=1.8, label='Rolling corr (15 min)')
        ax2.axhline(0.0, color='black', lw=1)
        ax2.set_title('Rolling coupling: corr(RR, SpO₂) over time')
        ax2.set_xlabel('Elapsed time from first matched sample (min)')
        ax2.set_ylabel('Correlation')
        ax2.set_ylim(-1.05, 1.05)
        ax2.legend(loc='best')
        ax2_t = ax2.twinx()
        ax2_t.plot(elapsed, n15, color='0.5', lw=1.0, alpha=0.5, label='N in 15-min window')
        ax2_t.set_ylabel('Window N')
        ax2_t.set_ylim(0, max(5, int(np.nanmax(n15) if np.isfinite(np.nanmax(n15)) else 5)))
        save_plot('rr_spo2_phase_space_and_rolling_corr.png', fig=fig)
    result = {'matched_series': {'n_matched': int(n), 'match_tolerance_min': float(tolerance_used), 'rr_bpm': rr_m, 'spo2_pct': sp_m}, 'dwell_time_quadrants': dwell, 'coupling': corr_stats, 'thresholds': {'RR_high_bpm': 28.0, 'SpO2_ok_pct': 94.0}, 'plot_file': 'rr_spo2_phase_space_and_rolling_corr.png'}
    disproportionate = dwell['RR>=28 & SpO2>=94 (%)']
    hypox_tach = dwell['RR>=28 & SpO2<94 (%)']
    corr15_mean = corr_stats['rolling_corr_15min']['mean']
    interpretation = f'RR–SpO₂ coupling shows mean 15-min rolling corr={corr15_mean:.2f} with dwell time RR≥28 & SpO₂≥94 at {disproportionate:.1f}% vs RR≥28 & SpO₂<94 at {hypox_tach:.1f}%, quantifying the burden of tachypnea disproportionate to hypoxemia.'

plt.close()