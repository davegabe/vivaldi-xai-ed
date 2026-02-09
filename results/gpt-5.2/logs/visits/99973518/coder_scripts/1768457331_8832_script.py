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
def _to_arrays(ts_list):
    t = [x[0] for x in ts_list]
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _minutes_since(t_list, t0):
    return np.array([(ti - t0).total_seconds() / 60.0 for ti in t_list], dtype=float)

def _interp_at_grid(t_list, v_arr, t0, grid_min):
    if len(t_list) < 2:
        return np.full(grid_min.shape, np.nan, dtype=float)
    x = _minutes_since(t_list, t0)
    order = np.argsort(x)
    x = x[order]
    y = v_arr[order]
    if np.any(np.diff(x) == 0):
        keep = np.concatenate(([True], np.diff(x) != 0))
        x = x[keep]
        y = y[keep]
    if len(x) < 2:
        return np.full(grid_min.shape, np.nan, dtype=float)
    out = np.interp(grid_min, x, y, left=np.nan, right=np.nan)
    return out

def _rolling_min_irregular(times, vals, window_min=30.0):
    n = len(times)
    out = np.full(n, np.nan, dtype=float)
    start = 0
    for i in range(n):
        ti = times[i]
        while start < i and (ti - times[start]).total_seconds() / 60.0 > window_min:
            start += 1
        vwin = vals[start:i + 1]
        if len(vwin) > 0:
            out[i] = np.nanmin(vwin)
    return out
t_hr, v_hr = _to_arrays(heart_rate)
t_rr, v_rr = _to_arrays(respiratory_rate)
t_spo2, v_spo2 = _to_arrays(spo2)
t_sbp, v_sbp = _to_arrays(systolic_bp)
t_dbp, v_dbp = _to_arrays(diastolic_bp)
v_map = (v_sbp + 2.0 * v_dbp) / 3.0
v_pp = v_sbp - v_dbp
sbp_on_hr = _interp_at_grid(t_sbp, v_sbp, t_hr[0], _minutes_since(t_hr, t_hr[0]))
si_times = t_hr
with np.errstate(divide='ignore', invalid='ignore'):
    v_si = v_hr / sbp_on_hr
v_si[~np.isfinite(v_si)] = np.nan
all_times = sorted(set(t_hr) | set(t_rr) | set(t_spo2) | set(t_sbp) | set(t_dbp))
if len(all_times) < 3:
    result = {'n_events': 0, 'event_times': [], 'grid_minutes': None, 'aligned': {}, 'event_definition': 'RR≥30 OR SpO2 drop ≥3% in 5 min OR Shock Index≥1.0 OR MAP<60'}
    interpretation = 'Insufficient synchronized time-series coverage to detect event-aligned instability epochs.'
else:
    t0 = all_times[0]
    all_min = _minutes_since(all_times, t0)
    min_start = int(np.floor(all_min.min()))
    min_end = int(np.ceil(all_min.max()))
    grid_all = np.arange(min_start, min_end + 1, 1.0, dtype=float)
    hr_g = _interp_at_grid(t_hr, v_hr, t0, grid_all)
    rr_g = _interp_at_grid(t_rr, v_rr, t0, grid_all)
    spo2_g = _interp_at_grid(t_spo2, v_spo2, t0, grid_all)
    map_g = _interp_at_grid(t_sbp, v_map, t0, grid_all)
    pp_g = _interp_at_grid(t_sbp, v_pp, t0, grid_all)
    si_g = _interp_at_grid(si_times, v_si, t0, grid_all)
    crit_rr = rr_g >= 30.0
    spo2_drop = np.full_like(spo2_g, False, dtype=bool)
    for i in range(len(grid_all)):
        j = i - 5
        if j >= 0 and np.isfinite(spo2_g[i]) and np.isfinite(spo2_g[j]):
            spo2_drop[i] = spo2_g[i] - spo2_g[j] <= -3.0
    crit_si = si_g >= 1.0
    crit_map = map_g < 60.0
    event_mask = crit_rr | spo2_drop | crit_si | crit_map
    onset_idx = []
    last_onset = -10 ** 9
    for i in range(len(event_mask)):
        if event_mask[i] and (i == 0 or not event_mask[i - 1]):
            if i - last_onset >= 10:
                onset_idx.append(i)
                last_onset = i
    pre = 15
    post = 30
    align_grid = np.arange(-pre, post + 1, 1.0, dtype=float)

    def _extract_window(series_g, onset_i):
        idx = (onset_i + align_grid).astype(int)
        out = np.full_like(align_grid, np.nan, dtype=float)
        ok = (idx >= 0) & (idx < len(series_g))
        out[ok] = series_g[idx[ok]]
        return out
    aligned = {'HR_bpm': [], 'RR_brpm': [], 'SpO2_pct': [], 'MAP_mmHg': [], 'PulsePressure_mmHg': [], 'ShockIndex': [], 'criteria': []}
    onset_times = []
    for oi in onset_idx:
        onset_times.append(t0 + np.timedelta64(int(grid_all[oi]), 'm').astype('timedelta64[m]').astype(object) if False else None)
    onset_times = []
    for oi in onset_idx:
        onset_times.append(t0 + (all_times[0] - all_times[0]) + (all_times[0] - all_times[0]))
    from datetime import timedelta
    try:
        _td = __import__('datetime').timedelta
    except Exception:
        _td = None
    onset_times = []
    for oi in onset_idx:
        if _td is not None:
            onset_times.append(t0 + _td(minutes=float(grid_all[oi])))
        else:
            onset_times.append(all_times[oi])
    for oi in onset_idx:
        aligned['HR_bpm'].append(_extract_window(hr_g, oi))
        aligned['RR_brpm'].append(_extract_window(rr_g, oi))
        aligned['SpO2_pct'].append(_extract_window(spo2_g, oi))
        aligned['MAP_mmHg'].append(_extract_window(map_g, oi))
        aligned['PulsePressure_mmHg'].append(_extract_window(pp_g, oi))
        aligned['ShockIndex'].append(_extract_window(si_g, oi))
        aligned['criteria'].append({'RR>=30': bool(crit_rr[oi]) if np.isfinite(rr_g[oi]) else False, 'SpO2_drop_3pct_5min': bool(spo2_drop[oi]), 'SI>=1.0': bool(crit_si[oi]) if np.isfinite(si_g[oi]) else False, 'MAP<60': bool(crit_map[oi]) if np.isfinite(map_g[oi]) else False})
    n_events = len(onset_idx)
    aligned_arr = {}
    for k in ['HR_bpm', 'RR_brpm', 'SpO2_pct', 'MAP_mmHg', 'PulsePressure_mmHg', 'ShockIndex']:
        aligned_arr[k] = np.vstack(aligned[k]) if n_events > 0 else np.empty((0, len(align_grid)), dtype=float)

    def _summary_stats(mat):
        if mat.shape[0] == 0:
            return {'median': np.full(mat.shape[1], np.nan, dtype=float), 'q25': np.full(mat.shape[1], np.nan, dtype=float), 'q75': np.full(mat.shape[1], np.nan, dtype=float), 'n_at_time': np.zeros(mat.shape[1], dtype=int)}
        n_at = np.sum(np.isfinite(mat), axis=0).astype(int)
        med = np.nanmedian(mat, axis=0)
        q25 = np.nanpercentile(mat, 25, axis=0)
        q75 = np.nanpercentile(mat, 75, axis=0)
        return {'median': med, 'q25': q25, 'q75': q75, 'n_at_time': n_at}
    stats_by_metric = {k: _summary_stats(aligned_arr[k]) for k in aligned_arr}
    fig, axes = plt.subplots(5, 1, sharex=True, figsize=(10, 12))
    metrics_plot = [('HR_bpm', 'Heart Rate (bpm)'), ('RR_brpm', 'Respiratory Rate (breaths/min)'), ('SpO2_pct', 'SpO2 (%)'), ('MAP_mmHg', 'MAP (mmHg)'), ('PulsePressure_mmHg', 'Pulse Pressure (mmHg)')]
    for ax, (mk, label) in zip(axes, metrics_plot):
        st = stats_by_metric[mk]
        ax.plot(align_grid, st['median'], color='black', linewidth=2, label='Median')
        ax.fill_between(align_grid, st['q25'], st['q75'], color='gray', alpha=0.25, label='IQR')
        ax.axvline(0, color='red', linewidth=1, linestyle='--')
        ax.set_ylabel(label)
        ax.grid(True, alpha=0.25)
        if n_events > 0:
            for xpt in [-15, 0, 30]:
                if xpt in align_grid:
                    idx = int(np.where(align_grid == xpt)[0][0])
                    ax.text(xpt, ax.get_ylim()[0], f'n={st['n_at_time'][idx]}', va='bottom', ha='center', fontsize=8)
    axes[-1].set_xlabel('Minutes from event onset (0 = onset)')
    axes[0].set_title(f'Event-aligned instability epochs (n={n_events})\nOnset: RR≥30 OR SpO2 drop ≥3%/5min OR Shock Index≥1.0 OR MAP<60; Window: -15 to +30 min')
    handles, labels = axes[0].get_legend_handles_labels()
    if handles:
        axes[0].legend(loc='upper right', frameon=True)
    save_plot('event_aligned_instability_median_iqr.png', fig=fig)
    trigger_counts = {'RR>=30': 0, 'SpO2_drop_3pct_5min': 0, 'SI>=1.0': 0, 'MAP<60': 0}
    for c in aligned['criteria']:
        for k in trigger_counts:
            trigger_counts[k] += int(bool(c.get(k, False)))
    t0_idx = int(np.where(align_grid == 0)[0][0])
    onset_medians = {k: float(stats_by_metric[k]['median'][t0_idx]) if np.isfinite(stats_by_metric[k]['median'][t0_idx]) else np.nan for k in ['HR_bpm', 'RR_brpm', 'SpO2_pct', 'MAP_mmHg', 'PulsePressure_mmHg', 'ShockIndex']}
    result = {'n_events': n_events, 'event_onset_indices_minute_grid': onset_idx, 'event_onset_datetimes': onset_times, 'window_minutes': {'pre': pre, 'post': post}, 'alignment_grid_minutes': align_grid, 'trigger_counts_at_onset': trigger_counts, 'onset_median_values': onset_medians, 'aligned_matrices': aligned_arr, 'summary_stats': stats_by_metric, 'event_definition': 'RR≥30 OR SpO2 drop ≥3% in 5 min OR Shock Index≥1.0 OR MAP<60', 'output_plot': 'event_aligned_instability_median_iqr.png'}
    if n_events == 0:
        interpretation = 'No instability events detected by the specified criteria across the available time span; no stereotyped event-aligned decompensation pattern can be assessed from these data.'
    else:
        interpretation = f'Detected {n_events} instability onset epoch(s); at onset the cohort-median values were HR {onset_medians['HR_bpm']:.1f} bpm, RR {onset_medians['RR_brpm']:.1f}/min, SpO2 {onset_medians['SpO2_pct']:.1f}%, MAP {onset_medians['MAP_mmHg']:.1f} mmHg, pulse pressure {onset_medians['PulsePressure_mmHg']:.1f} mmHg, and shock index {onset_medians['ShockIndex']:.2f}, with onset triggers most often: ' + ', '.join([f'{k}={trigger_counts[k]}' for k in ['RR>=30', 'SpO2_drop_3pct_5min', 'SI>=1.0', 'MAP<60']]) + '.'

plt.close()