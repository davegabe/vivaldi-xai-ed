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
result = {}
interpretation = {}

def _to_arrays(ts_list):
    t = [x[0] for x in ts_list]
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _minutes_since(t0, t_list):
    return np.array([(ti - t0).total_seconds() / 60.0 for ti in t_list], dtype=float)

def _interp_at(x_src, y_src, x_new):
    x_src = np.asarray(x_src, dtype=float)
    y_src = np.asarray(y_src, dtype=float)
    x_new = np.asarray(x_new, dtype=float)
    m = np.isfinite(x_src) & np.isfinite(y_src)
    x_src = x_src[m]
    y_src = y_src[m]
    if x_src.size < 2:
        return np.full_like(x_new, np.nan, dtype=float)
    order = np.argsort(x_src)
    x_src = x_src[order]
    y_src = y_src[order]
    y = np.interp(x_new, x_src, y_src)
    y[(x_new < x_src[0]) | (x_new > x_src[-1])] = np.nan
    return y

def _rolling_min_irregular(x, y, window_min=30.0):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    out = np.full_like(y, np.nan, dtype=float)
    if x.size == 0:
        return out
    j0 = 0
    for i in range(x.size):
        while j0 < i and x[i] - x[j0] > window_min:
            j0 += 1
        w = y[j0:i + 1]
        w = w[np.isfinite(w)]
        out[i] = np.min(w) if w.size else np.nan
    return out
all_ts = []
for series in (heart_rate, systolic_bp, diastolic_bp, spo2, respiratory_rate, temperature):
    if isinstance(series, list) and len(series) > 0:
        all_ts.extend([t for t, _ in series])
t0 = min(all_ts) if all_ts else None
hr_t, hr_v = _to_arrays(heart_rate)
sbp_t, sbp_v = _to_arrays(systolic_bp)
dbp_t, dbp_v = _to_arrays(diastolic_bp)
spo2_t, spo2_v = _to_arrays(spo2)
rr_t, rr_v = _to_arrays(respiratory_rate)
hr_x = _minutes_since(t0, hr_t) if t0 else np.array([], dtype=float)
sbp_x = _minutes_since(t0, sbp_t) if t0 else np.array([], dtype=float)
dbp_x = _minutes_since(t0, dbp_t) if t0 else np.array([], dtype=float)
spo2_x = _minutes_since(t0, spo2_t) if t0 else np.array([], dtype=float)
rr_x = _minutes_since(t0, rr_t) if t0 else np.array([], dtype=float)
grid_x = sbp_x.copy()
hr_on_sbp = _interp_at(hr_x, hr_v, grid_x)
dbp_on_sbp = _interp_at(dbp_x, dbp_v, grid_x)
si = np.full_like(grid_x, np.nan, dtype=float)
map_series = np.full_like(grid_x, np.nan, dtype=float)
pp = np.full_like(grid_x, np.nan, dtype=float)
valid = np.isfinite(hr_on_sbp) & np.isfinite(sbp_v) & (sbp_v > 0)
si[valid] = hr_on_sbp[valid] / sbp_v[valid]
valid_map = np.isfinite(sbp_v) & np.isfinite(dbp_on_sbp)
map_series[valid_map] = (sbp_v[valid_map] + 2.0 * dbp_on_sbp[valid_map]) / 3.0
valid_pp = np.isfinite(sbp_v) & np.isfinite(dbp_on_sbp)
pp[valid_pp] = sbp_v[valid_pp] - dbp_on_sbp[valid_pp]
sbp_rollmin30 = _rolling_min_irregular(sbp_x, sbp_v, window_min=30.0)
spo2_on_grid = _interp_at(spo2_x, spo2_v, grid_x)
rr_on_grid = _interp_at(rr_x, rr_v, grid_x)
fig, axes = plt.subplots(4, 1, sharex=True, figsize=(12, 10), constrained_layout=True)
ax = axes[0]
ax.plot(grid_x, si, color='black', lw=1.5, label='Shock Index (HR/SBP)')
ax.axhline(0.7, color='orange', ls='--', lw=1, alpha=0.8, label='SI 0.7')
ax.axhline(1.0, color='red', ls='--', lw=1, alpha=0.8, label='SI 1.0')
m_hypox = np.isfinite(spo2_on_grid) & (spo2_on_grid < 92.0)
m_tachy = np.isfinite(rr_on_grid) & (rr_on_grid >= 22.0)
ax.scatter(grid_x[m_hypox], si[m_hypox], s=18, color='steelblue', alpha=0.7, label='SpO2 < 92% (në kohë)')
ax.scatter(grid_x[m_tachy], si[m_tachy], s=18, color='purple', alpha=0.5, label='RR ≥ 22 (në kohë)')
ax.set_ylabel('SI (pa njësi)')
ax.set_title('Kohë-e-përputhur hemodinamika me mbivendosje minimale rrotulluese SBP')
ax.grid(True, alpha=0.25)
ax.legend(loc='upper right', fontsize=8, ncol=2, frameon=False)
ax = axes[1]
ax.plot(sbp_x, sbp_v, marker='o', ms=3, lw=1.0, color='tab:red', label='SBP')
ax.plot(sbp_x, sbp_rollmin30, lw=2.0, color='tab:red', alpha=0.35, label='SBP min rrotullues (30 min)')
ax.axhline(75, color='red', ls='--', lw=1, alpha=0.8, label='SBP 75 (pragu i paralajmërimit)')
ax.axhline(90, color='orange', ls='--', lw=1, alpha=0.6, label='SBP 90')
ax.set_ylabel('SBP (mmHg)')
ax.grid(True, alpha=0.25)
ax.legend(loc='upper right', fontsize=8, ncol=2, frameon=False)
ax = axes[2]
ax.plot(grid_x, map_series, marker='o', ms=3, lw=1.0, color='tab:green', label='MAP (i derivuar)')
ax.axhline(65, color='orange', ls='--', lw=1, alpha=0.8, label='MAP 65')
ax.axhline(60, color='red', ls='--', lw=1, alpha=0.8, label='MAP 60')
ax.set_ylabel('MAP (mmHg)')
ax.grid(True, alpha=0.25)
ax.legend(loc='upper right', fontsize=8, ncol=2, frameon=False)
ax = axes[3]
ax.plot(grid_x, pp, marker='o', ms=3, lw=1.0, color='tab:blue', label='Presioni Pulsues (SBP-DBP)')
ax.axhline(25, color='orange', ls='--', lw=1, alpha=0.8, label='PP 25 (i ulët)')
ax.set_ylabel('PP (mmHg)')
ax.set_xlabel('Minuta që nga jetësoreja e parë e regjistruar')
ax.grid(True, alpha=0.25)
ax.legend(loc='upper right', fontsize=8, ncol=2, frameon=False)
save_plot('hemodynamics_si_sbp_map_pp_with_sbp_rollmin30.png', fig=fig)
result['shock_index'] = shock_index
result['map_value'] = map_value
result['pulse_pressure'] = pulse_pressure
result['qsofa_score'] = qsofa_score
result['spo2_trend'] = spo2_trend
result['hr_volatility'] = hr_volatility
result['plot_file'] = 'hemodynamics_si_sbp_map_pp_with_sbp_rollmin30.png'
result['sbp_rolling_min30_min'] = float(np.nanmin(sbp_rollmin30)) if sbp_rollmin30.size and np.any(np.isfinite(sbp_rollmin30)) else np.nan
result['sbp_min'] = float(np.nanmin(sbp_v)) if sbp_v.size and np.any(np.isfinite(sbp_v)) else np.nan
result['si_max_on_sbp_grid'] = float(np.nanmax(si)) if si.size and np.any(np.isfinite(si)) else np.nan
interpretation['shock_index'] = shock_index_interpretation
interpretation['map'] = map_interpretation
interpretation['qsofa'] = qsofa_interpretation
interpretation['pulse_pressure'] = f'Presioni i pulsit {pulse_pressure:.0f} mmHg është i ulët-ngushtë, gjë që mund të pasqyrojë vëllim të zvogëluar të goditjes/vasokonstriksion dhe mund të mbështesë shokun fshehur kur çiftëzohet me indeks të lartë të shokut.'
if np.isfinite(result['sbp_rolling_min30_min']):
    interpretation['sbp_rolling_min30'] = f'Minimumi rrotullues 30-min SBP arriti {result['sbp_rolling_min30_min']:.0f} mmHg, duke ndihmuar në identifikimin e episodeve progresive të hipotensionit edhe nëse MAP-i momental duket i ruajtur.'
else:
    interpretation['sbp_rolling_min30'] = 'Minimumi rrotullues 30-min SBP nuk mundi të llogaritej (të dhëna të pamjaftueshme SBP).'

plt.close()