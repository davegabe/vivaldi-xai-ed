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
visit_id = '99385901'
age = 80
gender = 'M'
ethnicity = 'White (Non-Hispanic/Non-Latino)'
heart_rate = [(datetime.datetime(2251, 9, 14, 4, 46, 21), 104.0), (datetime.datetime(2251, 9, 14, 5, 5, 21), 100.181818181818), (datetime.datetime(2251, 9, 14, 5, 6, 21), 96.8474576271186), (datetime.datetime(2251, 9, 14, 5, 7, 21), 96.8620689655172), (datetime.datetime(2251, 9, 14, 5, 8, 21), 98.2033898305085), (datetime.datetime(2251, 9, 14, 5, 9, 21), 97.2758620689655), (datetime.datetime(2251, 9, 14, 5, 10, 21), 96.8135593220339), (datetime.datetime(2251, 9, 14, 5, 11, 21), 97.406779661017), (datetime.datetime(2251, 9, 14, 5, 12, 21), 96.8793103448276), (datetime.datetime(2251, 9, 14, 5, 13, 21), 96.0), (datetime.datetime(2251, 9, 14, 5, 14, 21), 93.5172413793104), (datetime.datetime(2251, 9, 14, 5, 15, 21), 92.0508474576271), (datetime.datetime(2251, 9, 14, 5, 16, 21), 91.9491525423729), (datetime.datetime(2251, 9, 14, 5, 17, 21), 91.6034482758621), (datetime.datetime(2251, 9, 14, 5, 18, 21), 92.3389830508475), (datetime.datetime(2251, 9, 14, 5, 19, 21), 91.9655172413793), (datetime.datetime(2251, 9, 14, 5, 20, 21), 90.406779661017), (datetime.datetime(2251, 9, 14, 5, 21, 21), 90.6949152542373), (datetime.datetime(2251, 9, 14, 5, 22, 21), 91.4310344827586), (datetime.datetime(2251, 9, 14, 5, 23, 21), 89.5762711864407), (datetime.datetime(2251, 9, 14, 5, 24, 21), 89.9827586206897), (datetime.datetime(2251, 9, 14, 5, 25, 21), 90.7118644067797), (datetime.datetime(2251, 9, 14, 5, 26, 21), 89.271186440678), (datetime.datetime(2251, 9, 14, 5, 27, 21), 90.2241379310345), (datetime.datetime(2251, 9, 14, 5, 28, 21), 91.0169491525424), (datetime.datetime(2251, 9, 14, 5, 29, 21), 90.948275862069), (datetime.datetime(2251, 9, 14, 5, 30, 21), 92.1186440677966), (datetime.datetime(2251, 9, 14, 5, 31, 21), 92.3103448275862), (datetime.datetime(2251, 9, 14, 5, 32, 21), 90.7966101694915), (datetime.datetime(2251, 9, 14, 5, 33, 21), 91.3898305084746), (datetime.datetime(2251, 9, 14, 5, 34, 21), 91.6724137931035), (datetime.datetime(2251, 9, 14, 5, 35, 21), 91.1694915254237), (datetime.datetime(2251, 9, 14, 5, 36, 21), 91.3620689655172), (datetime.datetime(2251, 9, 14, 5, 37, 21), 91.7457627118644), (datetime.datetime(2251, 9, 14, 5, 38, 21), 91.5762711864407), (datetime.datetime(2251, 9, 14, 5, 39, 21), 94.5344827586207), (datetime.datetime(2251, 9, 14, 5, 40, 21), 94.9661016949152), (datetime.datetime(2251, 9, 14, 5, 41, 21), 95.4655172413793), (datetime.datetime(2251, 9, 14, 5, 42, 21), 95.135593220339), (datetime.datetime(2251, 9, 14, 5, 43, 21), 96.0847457627119), (datetime.datetime(2251, 9, 14, 5, 44, 21), 96.2586206896552), (datetime.datetime(2251, 9, 14, 5, 45, 21), 97.0677966101695), (datetime.datetime(2251, 9, 14, 5, 46, 21), 92.6206896551724), (datetime.datetime(2251, 9, 14, 5, 47, 21), 92.0508474576271), (datetime.datetime(2251, 9, 14, 5, 48, 21), 90.5762711864407), (datetime.datetime(2251, 9, 14, 5, 49, 21), 96.3965517241379), (datetime.datetime(2251, 9, 14, 5, 50, 21), 95.9661016949152), (datetime.datetime(2251, 9, 14, 5, 51, 21), 96.0862068965517), (datetime.datetime(2251, 9, 14, 5, 52, 21), 96.6949152542373), (datetime.datetime(2251, 9, 14, 5, 53, 21), 97.0862068965517), (datetime.datetime(2251, 9, 14, 5, 54, 21), 98.2203389830508), (datetime.datetime(2251, 9, 14, 5, 55, 21), 98.5762711864407), (datetime.datetime(2251, 9, 14, 5, 56, 21), 96.551724137931), (datetime.datetime(2251, 9, 14, 5, 57, 21), 96.9152542372881), (datetime.datetime(2251, 9, 14, 5, 58, 21), 96.8813559322034), (datetime.datetime(2251, 9, 14, 5, 59, 21), 96.3103448275862), (datetime.datetime(2251, 9, 14, 6, 0, 21), 97.1864406779661), (datetime.datetime(2251, 9, 14, 6, 1, 21), 95.6034482758621), (datetime.datetime(2251, 9, 14, 6, 2, 21), 96.1864406779661), (datetime.datetime(2251, 9, 14, 6, 3, 21), 96.551724137931), (datetime.datetime(2251, 9, 14, 6, 4, 21), 97.2033898305085), (datetime.datetime(2251, 9, 14, 6, 5, 21), 96.8793103448276), (datetime.datetime(2251, 9, 14, 6, 6, 21), 98.3050847457627), (datetime.datetime(2251, 9, 14, 6, 7, 21), 97.4915254237288), (datetime.datetime(2251, 9, 14, 6, 8, 21), 98.448275862069), (datetime.datetime(2251, 9, 14, 6, 9, 21), 97.9830508474576), (datetime.datetime(2251, 9, 14, 6, 10, 21), 98.5254237288136), (datetime.datetime(2251, 9, 14, 6, 11, 21), 98.8448275862069), (datetime.datetime(2251, 9, 14, 6, 12, 21), 97.5423728813559), (datetime.datetime(2251, 9, 14, 6, 13, 21), 95.6724137931034), (datetime.datetime(2251, 9, 14, 6, 14, 21), 96.3050847457627), (datetime.datetime(2251, 9, 14, 6, 15, 21), 97.8135593220339), (datetime.datetime(2251, 9, 14, 6, 16, 21), 97.1896551724138), (datetime.datetime(2251, 9, 14, 6, 17, 21), 96.9661016949152), (datetime.datetime(2251, 9, 14, 6, 18, 21), 95.4310344827586), (datetime.datetime(2251, 9, 14, 6, 19, 21), 95.0508474576271), (datetime.datetime(2251, 9, 14, 6, 20, 21), 94.3220338983051), (datetime.datetime(2251, 9, 14, 6, 21, 21), 96.3620689655172), (datetime.datetime(2251, 9, 14, 6, 22, 21), 96.4576271186441), (datetime.datetime(2251, 9, 14, 6, 23, 21), 94.2931034482759), (datetime.datetime(2251, 9, 14, 6, 24, 21), 94.3559322033899), (datetime.datetime(2251, 9, 14, 6, 25, 21), 90.9830508474576), (datetime.datetime(2251, 9, 14, 6, 26, 21), 90.8793103448276), (datetime.datetime(2251, 9, 14, 6, 27, 21), 92.0), (datetime.datetime(2251, 9, 14, 6, 32, 21), 97.0), (datetime.datetime(2251, 9, 14, 6, 37, 21), 91.0), (datetime.datetime(2251, 9, 14, 6, 42, 21), 93.0), (datetime.datetime(2251, 9, 14, 6, 47, 21), 72.0), (datetime.datetime(2251, 9, 14, 6, 52, 21), 95.0), (datetime.datetime(2251, 9, 14, 6, 57, 21), 72.0), (datetime.datetime(2251, 9, 14, 7, 2, 21), 96.0), (datetime.datetime(2251, 9, 14, 7, 5, 21), 93.0), (datetime.datetime(2251, 9, 14, 7, 7, 21), 95.0), (datetime.datetime(2251, 9, 14, 7, 12, 21), 96.0), (datetime.datetime(2251, 9, 14, 7, 17, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 22, 21), 96.0), (datetime.datetime(2251, 9, 14, 7, 27, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 32, 21), 96.0), (datetime.datetime(2251, 9, 14, 7, 37, 21), 97.0), (datetime.datetime(2251, 9, 14, 7, 42, 21), 98.0), (datetime.datetime(2251, 9, 14, 7, 47, 21), 95.0), (datetime.datetime(2251, 9, 14, 7, 52, 21), 96.0), (datetime.datetime(2251, 9, 14, 7, 57, 21), 97.0), (datetime.datetime(2251, 9, 14, 8, 2, 21), 95.0), (datetime.datetime(2251, 9, 14, 8, 7, 21), 99.0), (datetime.datetime(2251, 9, 14, 8, 12, 21), 87.0), (datetime.datetime(2251, 9, 14, 8, 17, 21), 72.0), (datetime.datetime(2251, 9, 14, 8, 22, 21), 67.0), (datetime.datetime(2251, 9, 14, 8, 27, 21), 94.0), (datetime.datetime(2251, 9, 14, 8, 47, 21), 97.0), (datetime.datetime(2251, 9, 14, 9, 13, 21), 94.0), (datetime.datetime(2251, 9, 14, 9, 30, 21), 120.0), (datetime.datetime(2251, 9, 14, 9, 47, 21), 82.0), (datetime.datetime(2251, 9, 14, 10, 10, 21), 93.0)]
systolic_bp = [(datetime.datetime(2251, 9, 14, 4, 46, 21), 84.0), (datetime.datetime(2251, 9, 14, 5, 3, 21), 84.0), (datetime.datetime(2251, 9, 14, 5, 4, 21), 79.0), (datetime.datetime(2251, 9, 14, 5, 5, 21), 79.0), (datetime.datetime(2251, 9, 14, 5, 7, 21), 81.0), (datetime.datetime(2251, 9, 14, 5, 17, 21), 86.0), (datetime.datetime(2251, 9, 14, 5, 18, 21), 86.0), (datetime.datetime(2251, 9, 14, 5, 41, 21), 93.0), (datetime.datetime(2251, 9, 14, 5, 43, 21), 84.0), (datetime.datetime(2251, 9, 14, 5, 47, 21), 84.0), (datetime.datetime(2251, 9, 14, 5, 48, 21), 81.0), (datetime.datetime(2251, 9, 14, 5, 53, 21), 80.0), (datetime.datetime(2251, 9, 14, 5, 58, 21), 86.0), (datetime.datetime(2251, 9, 14, 6, 3, 21), 83.0), (datetime.datetime(2251, 9, 14, 6, 8, 21), 93.0), (datetime.datetime(2251, 9, 14, 6, 13, 21), 75.0), (datetime.datetime(2251, 9, 14, 6, 17, 21), 77.0), (datetime.datetime(2251, 9, 14, 6, 20, 21), 77.0), (datetime.datetime(2251, 9, 14, 6, 22, 21), 75.0), (datetime.datetime(2251, 9, 14, 6, 23, 21), 75.0), (datetime.datetime(2251, 9, 14, 6, 27, 21), 94.0), (datetime.datetime(2251, 9, 14, 6, 32, 21), 94.0), (datetime.datetime(2251, 9, 14, 6, 37, 21), 94.0), (datetime.datetime(2251, 9, 14, 6, 42, 21), 77.0), (datetime.datetime(2251, 9, 14, 6, 47, 21), 95.0), (datetime.datetime(2251, 9, 14, 6, 52, 21), 94.0), (datetime.datetime(2251, 9, 14, 6, 57, 21), 87.0), (datetime.datetime(2251, 9, 14, 7, 2, 21), 110.0), (datetime.datetime(2251, 9, 14, 7, 5, 21), 98.0), (datetime.datetime(2251, 9, 14, 7, 7, 21), 72.0), (datetime.datetime(2251, 9, 14, 7, 12, 21), 85.0), (datetime.datetime(2251, 9, 14, 7, 17, 21), 89.0), (datetime.datetime(2251, 9, 14, 7, 22, 21), 93.0), (datetime.datetime(2251, 9, 14, 7, 27, 21), 84.0), (datetime.datetime(2251, 9, 14, 7, 32, 21), 91.0), (datetime.datetime(2251, 9, 14, 7, 37, 21), 91.0), (datetime.datetime(2251, 9, 14, 7, 47, 21), 88.0), (datetime.datetime(2251, 9, 14, 9, 13, 21), 122.0)]
diastolic_bp = [(datetime.datetime(2251, 9, 14, 4, 46, 21), 37.0), (datetime.datetime(2251, 9, 14, 5, 3, 21), 37.0), (datetime.datetime(2251, 9, 14, 5, 4, 21), 62.0), (datetime.datetime(2251, 9, 14, 5, 5, 21), 62.0), (datetime.datetime(2251, 9, 14, 5, 7, 21), 54.0), (datetime.datetime(2251, 9, 14, 5, 17, 21), 55.0), (datetime.datetime(2251, 9, 14, 5, 18, 21), 55.0), (datetime.datetime(2251, 9, 14, 5, 43, 21), 57.0), (datetime.datetime(2251, 9, 14, 5, 47, 21), 43.0), (datetime.datetime(2251, 9, 14, 5, 48, 21), 53.0), (datetime.datetime(2251, 9, 14, 5, 53, 21), 51.0), (datetime.datetime(2251, 9, 14, 5, 58, 21), 55.0), (datetime.datetime(2251, 9, 14, 6, 3, 21), 55.0), (datetime.datetime(2251, 9, 14, 6, 13, 21), 53.0), (datetime.datetime(2251, 9, 14, 6, 17, 21), 43.0), (datetime.datetime(2251, 9, 14, 6, 20, 21), 43.0), (datetime.datetime(2251, 9, 14, 6, 22, 21), 51.0), (datetime.datetime(2251, 9, 14, 6, 23, 21), 51.0), (datetime.datetime(2251, 9, 14, 6, 27, 21), 57.0), (datetime.datetime(2251, 9, 14, 6, 32, 21), 56.0), (datetime.datetime(2251, 9, 14, 6, 37, 21), 55.0), (datetime.datetime(2251, 9, 14, 6, 42, 21), 56.0), (datetime.datetime(2251, 9, 14, 6, 47, 21), 43.0), (datetime.datetime(2251, 9, 14, 6, 52, 21), 44.0), (datetime.datetime(2251, 9, 14, 6, 57, 21), 43.0), (datetime.datetime(2251, 9, 14, 7, 2, 21), 51.0), (datetime.datetime(2251, 9, 14, 7, 5, 21), 49.0), (datetime.datetime(2251, 9, 14, 7, 7, 21), 44.0), (datetime.datetime(2251, 9, 14, 7, 12, 21), 56.0), (datetime.datetime(2251, 9, 14, 7, 17, 21), 56.0), (datetime.datetime(2251, 9, 14, 7, 22, 21), 52.0), (datetime.datetime(2251, 9, 14, 7, 27, 21), 57.0), (datetime.datetime(2251, 9, 14, 7, 32, 21), 55.0), (datetime.datetime(2251, 9, 14, 7, 37, 21), 61.0), (datetime.datetime(2251, 9, 14, 7, 47, 21), 52.0), (datetime.datetime(2251, 9, 14, 9, 13, 21), 60.0)]
spo2 = [(datetime.datetime(2251, 9, 14, 4, 46, 21), 92.0), (datetime.datetime(2251, 9, 14, 5, 5, 21), 92.0), (datetime.datetime(2251, 9, 14, 5, 7, 21), 93.0), (datetime.datetime(2251, 9, 14, 5, 12, 21), 94.0), (datetime.datetime(2251, 9, 14, 5, 17, 21), 92.0), (datetime.datetime(2251, 9, 14, 5, 22, 21), 93.0), (datetime.datetime(2251, 9, 14, 5, 27, 21), 96.0), (datetime.datetime(2251, 9, 14, 5, 32, 21), 97.0), (datetime.datetime(2251, 9, 14, 6, 13, 21), 95.0), (datetime.datetime(2251, 9, 14, 6, 17, 21), 95.0), (datetime.datetime(2251, 9, 14, 6, 22, 21), 95.0), (datetime.datetime(2251, 9, 14, 6, 27, 21), 96.0), (datetime.datetime(2251, 9, 14, 6, 32, 21), 98.0), (datetime.datetime(2251, 9, 14, 6, 37, 21), 98.0), (datetime.datetime(2251, 9, 14, 6, 42, 21), 97.0), (datetime.datetime(2251, 9, 14, 6, 47, 21), 96.0), (datetime.datetime(2251, 9, 14, 6, 52, 21), 95.0), (datetime.datetime(2251, 9, 14, 6, 57, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 2, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 5, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 7, 21), 93.0), (datetime.datetime(2251, 9, 14, 7, 12, 21), 92.0), (datetime.datetime(2251, 9, 14, 7, 17, 21), 96.0), (datetime.datetime(2251, 9, 14, 7, 22, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 27, 21), 95.0), (datetime.datetime(2251, 9, 14, 7, 32, 21), 95.0), (datetime.datetime(2251, 9, 14, 7, 37, 21), 93.0), (datetime.datetime(2251, 9, 14, 7, 42, 21), 95.0), (datetime.datetime(2251, 9, 14, 7, 47, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 52, 21), 94.0), (datetime.datetime(2251, 9, 14, 7, 57, 21), 96.0), (datetime.datetime(2251, 9, 14, 8, 2, 21), 95.0), (datetime.datetime(2251, 9, 14, 8, 7, 21), 95.0), (datetime.datetime(2251, 9, 14, 8, 12, 21), 95.0), (datetime.datetime(2251, 9, 14, 8, 17, 21), 93.0), (datetime.datetime(2251, 9, 14, 8, 22, 21), 95.0), (datetime.datetime(2251, 9, 14, 8, 27, 21), 95.0), (datetime.datetime(2251, 9, 14, 8, 47, 21), 93.0), (datetime.datetime(2251, 9, 14, 9, 13, 21), 94.0), (datetime.datetime(2251, 9, 14, 9, 30, 21), 95.0), (datetime.datetime(2251, 9, 14, 9, 47, 21), 96.0), (datetime.datetime(2251, 9, 14, 10, 10, 21), 95.0)]
respiratory_rate = [(datetime.datetime(2251, 9, 14, 4, 46, 21), 18.0), (datetime.datetime(2251, 9, 14, 5, 5, 21), 19.2), (datetime.datetime(2251, 9, 14, 5, 6, 21), 19.5593220338983), (datetime.datetime(2251, 9, 14, 5, 7, 21), 21.4655172413793), (datetime.datetime(2251, 9, 14, 5, 8, 21), 20.3559322033898), (datetime.datetime(2251, 9, 14, 5, 9, 21), 25.6724137931035), (datetime.datetime(2251, 9, 14, 5, 10, 21), 17.7118644067797), (datetime.datetime(2251, 9, 14, 5, 11, 21), 17.6610169491525), (datetime.datetime(2251, 9, 14, 5, 12, 21), 21.1034482758621), (datetime.datetime(2251, 9, 14, 5, 13, 21), 23.0169491525424), (datetime.datetime(2251, 9, 14, 5, 14, 21), 22.1724137931035), (datetime.datetime(2251, 9, 14, 5, 15, 21), 23.2881355932203), (datetime.datetime(2251, 9, 14, 5, 16, 21), 23.3898305084746), (datetime.datetime(2251, 9, 14, 5, 17, 21), 22.6379310344828), (datetime.datetime(2251, 9, 14, 5, 18, 21), 24.6949152542373), (datetime.datetime(2251, 9, 14, 5, 19, 21), 25.448275862069), (datetime.datetime(2251, 9, 14, 5, 20, 21), 23.5423728813559), (datetime.datetime(2251, 9, 14, 5, 21, 21), 23.2033898305085), (datetime.datetime(2251, 9, 14, 5, 22, 21), 20.051724137931), (datetime.datetime(2251, 9, 14, 5, 23, 21), 21.3559322033898), (datetime.datetime(2251, 9, 14, 5, 24, 21), 18.6379310344828), (datetime.datetime(2251, 9, 14, 5, 25, 21), 19.8135593220339), (datetime.datetime(2251, 9, 14, 5, 26, 21), 22.6779661016949), (datetime.datetime(2251, 9, 14, 5, 27, 21), 23.8620689655172), (datetime.datetime(2251, 9, 14, 5, 28, 21), 21.1694915254237), (datetime.datetime(2251, 9, 14, 5, 29, 21), 21.7241379310345), (datetime.datetime(2251, 9, 14, 5, 30, 21), 20.3898305084746), (datetime.datetime(2251, 9, 14, 5, 31, 21), 22.4827586206897), (datetime.datetime(2251, 9, 14, 5, 32, 21), 23.6440677966102), (datetime.datetime(2251, 9, 14, 5, 33, 21), 22.9152542372881), (datetime.datetime(2251, 9, 14, 5, 34, 21), 22.6034482758621), (datetime.datetime(2251, 9, 14, 5, 35, 21), 21.6440677966102), (datetime.datetime(2251, 9, 14, 5, 36, 21), 20.7758620689655), (datetime.datetime(2251, 9, 14, 5, 37, 21), 19.3728813559322), (datetime.datetime(2251, 9, 14, 5, 38, 21), 17.2033898305085), (datetime.datetime(2251, 9, 14, 5, 39, 21), 21.6896551724138), (datetime.datetime(2251, 9, 14, 5, 40, 21), 20.3389830508475), (datetime.datetime(2251, 9, 14, 5, 41, 21), 21.3965517241379), (datetime.datetime(2251, 9, 14, 5, 42, 21), 22.1186440677966), (datetime.datetime(2251, 9, 14, 5, 43, 21), 20.6610169491525), (datetime.datetime(2251, 9, 14, 5, 44, 21), 13.5344827586207), (datetime.datetime(2251, 9, 14, 5, 45, 21), 21.2372881355932), (datetime.datetime(2251, 9, 14, 5, 46, 21), 22.9655172413793), (datetime.datetime(2251, 9, 14, 5, 47, 21), 23.0677966101695), (datetime.datetime(2251, 9, 14, 5, 48, 21), 27.5254237288136), (datetime.datetime(2251, 9, 14, 5, 49, 21), 27.2068965517241), (datetime.datetime(2251, 9, 14, 5, 50, 21), 23.3389830508475), (datetime.datetime(2251, 9, 14, 5, 51, 21), 24.0), (datetime.datetime(2251, 9, 14, 5, 52, 21), 23.7457627118644), (datetime.datetime(2251, 9, 14, 5, 53, 21), 27.0), (datetime.datetime(2251, 9, 14, 5, 54, 21), 25.1186440677966), (datetime.datetime(2251, 9, 14, 5, 55, 21), 22.3050847457627), (datetime.datetime(2251, 9, 14, 5, 56, 21), 24.2586206896552), (datetime.datetime(2251, 9, 14, 5, 57, 21), 24.1525423728814), (datetime.datetime(2251, 9, 14, 5, 58, 21), 25.0338983050848), (datetime.datetime(2251, 9, 14, 5, 59, 21), 23.2413793103448), (datetime.datetime(2251, 9, 14, 6, 0, 21), 21.7457627118644), (datetime.datetime(2251, 9, 14, 6, 1, 21), 17.5344827586207), (datetime.datetime(2251, 9, 14, 6, 2, 21), 16.3559322033898), (datetime.datetime(2251, 9, 14, 6, 3, 21), 20.5344827586207), (datetime.datetime(2251, 9, 14, 6, 4, 21), 22.2372881355932), (datetime.datetime(2251, 9, 14, 6, 5, 21), 21.0), (datetime.datetime(2251, 9, 14, 6, 6, 21), 21.2372881355932), (datetime.datetime(2251, 9, 14, 6, 7, 21), 24.9661016949153), (datetime.datetime(2251, 9, 14, 6, 8, 21), 26.5), (datetime.datetime(2251, 9, 14, 6, 9, 21), 22.0677966101695), (datetime.datetime(2251, 9, 14, 6, 10, 21), 22.9830508474576), (datetime.datetime(2251, 9, 14, 6, 11, 21), 22.5862068965517), (datetime.datetime(2251, 9, 14, 6, 12, 21), 24.1016949152542), (datetime.datetime(2251, 9, 14, 6, 13, 21), 24.1896551724138), (datetime.datetime(2251, 9, 14, 6, 14, 21), 24.2033898305085), (datetime.datetime(2251, 9, 14, 6, 15, 21), 23.3389830508475), (datetime.datetime(2251, 9, 14, 6, 16, 21), 18.6206896551724), (datetime.datetime(2251, 9, 14, 6, 17, 21), 20.4576271186441), (datetime.datetime(2251, 9, 14, 6, 18, 21), 22.5862068965517), (datetime.datetime(2251, 9, 14, 6, 19, 21), 23.728813559322), (datetime.datetime(2251, 9, 14, 6, 20, 21), 25.2542372881356), (datetime.datetime(2251, 9, 14, 6, 21, 21), 19.0), (datetime.datetime(2251, 9, 14, 6, 22, 21), 22.4237288135593), (datetime.datetime(2251, 9, 14, 6, 23, 21), 24.7758620689655), (datetime.datetime(2251, 9, 14, 6, 24, 21), 20.6610169491525), (datetime.datetime(2251, 9, 14, 6, 25, 21), 20.6949152542373), (datetime.datetime(2251, 9, 14, 6, 26, 21), 23.8793103448276), (datetime.datetime(2251, 9, 14, 6, 27, 21), 23.0), (datetime.datetime(2251, 9, 14, 6, 32, 21), 20.0), (datetime.datetime(2251, 9, 14, 6, 37, 21), 24.0), (datetime.datetime(2251, 9, 14, 6, 42, 21), 24.0), (datetime.datetime(2251, 9, 14, 6, 47, 21), 21.0), (datetime.datetime(2251, 9, 14, 6, 52, 21), 24.0), (datetime.datetime(2251, 9, 14, 6, 57, 21), 24.0), (datetime.datetime(2251, 9, 14, 7, 2, 21), 28.0), (datetime.datetime(2251, 9, 14, 7, 5, 21), 22.0), (datetime.datetime(2251, 9, 14, 7, 7, 21), 25.0), (datetime.datetime(2251, 9, 14, 7, 12, 21), 24.0), (datetime.datetime(2251, 9, 14, 7, 17, 21), 19.0), (datetime.datetime(2251, 9, 14, 7, 22, 21), 23.0), (datetime.datetime(2251, 9, 14, 7, 27, 21), 21.0), (datetime.datetime(2251, 9, 14, 7, 32, 21), 25.0), (datetime.datetime(2251, 9, 14, 7, 37, 21), 22.0), (datetime.datetime(2251, 9, 14, 7, 42, 21), 15.0), (datetime.datetime(2251, 9, 14, 7, 47, 21), 19.0), (datetime.datetime(2251, 9, 14, 7, 52, 21), 23.0), (datetime.datetime(2251, 9, 14, 7, 57, 21), 21.0), (datetime.datetime(2251, 9, 14, 8, 2, 21), 25.0), (datetime.datetime(2251, 9, 14, 8, 7, 21), 17.0), (datetime.datetime(2251, 9, 14, 8, 12, 21), 23.0), (datetime.datetime(2251, 9, 14, 8, 17, 21), 20.0), (datetime.datetime(2251, 9, 14, 8, 22, 21), 21.0), (datetime.datetime(2251, 9, 14, 8, 27, 21), 25.0), (datetime.datetime(2251, 9, 14, 8, 47, 21), 23.0), (datetime.datetime(2251, 9, 14, 9, 13, 21), 18.0), (datetime.datetime(2251, 9, 14, 9, 30, 21), 20.0), (datetime.datetime(2251, 9, 14, 9, 47, 21), 18.0), (datetime.datetime(2251, 9, 14, 10, 10, 21), 19.0)]
temperature = [(datetime.datetime(2251, 9, 14, 4, 46, 21), 38.5), (datetime.datetime(2251, 9, 14, 5, 5, 21), 39.05555555555556), (datetime.datetime(2251, 9, 14, 6, 42, 21), 36.5), (datetime.datetime(2251, 9, 14, 6, 47, 21), 37.72222222222222), (datetime.datetime(2251, 9, 14, 6, 52, 21), 38.0), (datetime.datetime(2251, 9, 14, 6, 57, 21), 38.22222222222222), (datetime.datetime(2251, 9, 14, 7, 2, 21), 38.27777777777778), (datetime.datetime(2251, 9, 14, 7, 5, 21), 38.27777777777778), (datetime.datetime(2251, 9, 14, 7, 7, 21), 38.388888888888886), (datetime.datetime(2251, 9, 14, 7, 12, 21), 38.388888888888886), (datetime.datetime(2251, 9, 14, 7, 17, 21), 38.388888888888886), (datetime.datetime(2251, 9, 14, 7, 22, 21), 38.27777777777778), (datetime.datetime(2251, 9, 14, 7, 27, 21), 38.27777777777778), (datetime.datetime(2251, 9, 14, 7, 32, 21), 38.27777777777778), (datetime.datetime(2251, 9, 14, 7, 37, 21), 38.22222222222222), (datetime.datetime(2251, 9, 14, 7, 42, 21), 38.22222222222222), (datetime.datetime(2251, 9, 14, 7, 47, 21), 38.22222222222222), (datetime.datetime(2251, 9, 14, 7, 52, 21), 38.22222222222222), (datetime.datetime(2251, 9, 14, 7, 57, 21), 38.111111111111114), (datetime.datetime(2251, 9, 14, 8, 2, 21), 38.111111111111114), (datetime.datetime(2251, 9, 14, 8, 7, 21), 38.111111111111114), (datetime.datetime(2251, 9, 14, 8, 12, 21), 38.111111111111114), (datetime.datetime(2251, 9, 14, 8, 17, 21), 38.111111111111114), (datetime.datetime(2251, 9, 14, 8, 22, 21), 38.111111111111114), (datetime.datetime(2251, 9, 14, 8, 27, 21), 38.0), (datetime.datetime(2251, 9, 14, 8, 47, 21), 37.72222222222222), (datetime.datetime(2251, 9, 14, 9, 13, 21), 37.77777777777778), (datetime.datetime(2251, 9, 14, 9, 30, 21), 37.72222222222222), (datetime.datetime(2251, 9, 14, 9, 47, 21), 37.611111111111114), (datetime.datetime(2251, 9, 14, 10, 10, 21), 37.611111111111114)]
# Previous Results
shock_index = 1.212
shock_index_interpretation = 'HIGH (1.21), significantly above normal (0.5-0.7). Suggests decompensated shock, immediate intervention needed.'
map_value = 63.0
map_interpretation = 'LOW (63 mmHg), below critical threshold of 65 mmHg. Indicates inadequate organ perfusion pressure.'
pulse_pressure = 27.0
qsofa_score = 2
qsofa_interpretation = 'High Risk (Score 2/3). Criteria met: SBP=81, RR=26. Associated with poor outcomes in sepsis.'
sirs = 1
spo2_trend = {'first': np.float64(92.0), 'last': np.float64(95.0), 'min': 92.0, 'mean': 94.6, 'slope': np.float64(0.011), 'r_squared': np.float64(0.008), 'trend_pct': np.float64(0.48)}
hr_volatility = {'dispersion_ms': 46.9, 'rmssd_ms': 55.83, 'hr_std_bpm': 5.9, 'hr_range_bpm': 53.0, 'n_samples': 114, 'data_density': 'sparse'}
triage_vital_panel = 'Attached'

# --- Generated Code Starts Here ---
import numpy as _np

def _extract_series(ts_list):
    if ts_list is None or len(ts_list) == 0:
        return ([], _np.array([], dtype=float))
    t = [x[0] for x in ts_list]
    v = _np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _find_runs(mask, min_len=3):
    runs = []
    n = len(mask)
    i = 0
    while i < n:
        if bool(mask[i]):
            j = i
            while j < n and bool(mask[j]):
                j += 1
            if j - i >= min_len:
                runs.append((i, j - 1))
            i = j
        else:
            i += 1
    return runs
hr_t, hr_v = _extract_series(heart_rate)
sbp_t, sbp_v = _extract_series(systolic_bp)
dbp_t, dbp_v = _extract_series(diastolic_bp)
map_t = []
map_v = _np.array([], dtype=float)
if len(sbp_t) > 0 and len(dbp_t) > 0 and (len(sbp_t) == len(dbp_t)) and all((sbp_t[i] == dbp_t[i] for i in range(len(sbp_t)))):
    map_t = sbp_t
    map_v = (sbp_v + 2.0 * dbp_v) / 3.0
elif len(sbp_t) > 0:
    map_t = sbp_t
    map_v = sbp_v / 3.0 + 50.0
episodes = []
if len(hr_v) > 0:
    tachy_mask = hr_v > 120.0
    runs = _find_runs(tachy_mask, min_len=3)
    use_map = len(map_v) > 0
    if not use_map:
        map_t = sbp_t
        map_v = sbp_v
    for start_i, end_i in runs:
        ep = {'start_idx': int(start_i), 'end_idx': int(end_i), 'n_samples': int(end_i - start_i + 1), 'start_time': hr_t[start_i], 'end_time': hr_t[end_i], 'hr_max': float(_np.max(hr_v[start_i:end_i + 1])), 'hr_mean': float(_np.mean(hr_v[start_i:end_i + 1])), 'hypotension_present': False, 'hypotension_metric': 'MAP' if use_map else 'SBP', 'hypotension_threshold': 65.0 if use_map else 90.0, 'min_hypotension_value_in_window': None, 'window_n_samples': 0}
        if len(map_t) > 0:
            w_start = max(0, start_i - 2)
            w_end = min(len(hr_t) - 1, end_i + 2)
            t0 = hr_t[w_start]
            t1 = hr_t[w_end]
            idxs = []
            for k, tk in enumerate(map_t):
                if tk >= t0 and tk <= t1:
                    idxs.append(k)
            ep['window_n_samples'] = int(len(idxs))
            if len(idxs) > 0:
                vals = map_v[_np.array(idxs, dtype=int)]
                vmin = float(_np.min(vals))
                ep['min_hypotension_value_in_window'] = vmin
                if use_map:
                    ep['hypotension_present'] = bool(_np.any(vals < 65.0))
                else:
                    ep['hypotension_present'] = bool(_np.any(vals < 90.0))
        episodes.append(ep)
n_episodes = len(episodes)
n_with_hypo = int(sum((1 for e in episodes if e['hypotension_present'])))
pct_with_hypo = float(100.0 * n_with_hypo / n_episodes) if n_episodes > 0 else _np.nan
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 7))
if len(hr_t) > 0:
    ax1.plot(hr_t, hr_v, color='tab:red', linewidth=1.5, label='Heart Rate (bpm)')
    ax1.axhline(120.0, color='tab:red', linestyle='--', linewidth=1.0, alpha=0.7, label='HR > 120 threshold')
    for e in episodes:
        ax1.axvspan(e['start_time'], e['end_time'], color='tab:red', alpha=0.15)
    ax1.set_ylabel('HR (bpm)')
    ax1.legend(loc='upper right')
else:
    ax1.text(0.5, 0.5, 'No heart_rate data available', ha='center', va='center', transform=ax1.transAxes)
    ax1.set_ylabel('HR (bpm)')
if len(map_t) > 0:
    if len(sbp_t) > 0 and len(dbp_t) > 0 and (len(sbp_t) == len(dbp_t)) and all((sbp_t[i] == dbp_t[i] for i in range(len(sbp_t)))):
        ax2.plot(map_t, map_v, color='tab:blue', linewidth=1.5, label='MAP (mmHg)')
        ax2.axhline(65.0, color='tab:blue', linestyle='--', linewidth=1.0, alpha=0.7, label='MAP 65 mmHg threshold')
        for e in episodes:
            ax2.axvspan(e['start_time'], e['end_time'], color='tab:red', alpha=0.12)
        ax2.set_ylabel('MAP (mmHg)')
        ax2.legend(loc='upper right')
    else:
        ax2.plot(map_t, map_v, color='tab:purple', linewidth=1.5, label='SBP (mmHg) [used for overlay]')
        ax2.axhline(90.0, color='tab:purple', linestyle='--', linewidth=1.0, alpha=0.7, label='SBP 90 mmHg threshold')
        for e in episodes:
            ax2.axvspan(e['start_time'], e['end_time'], color='tab:red', alpha=0.12)
        ax2.set_ylabel('SBP (mmHg)')
        ax2.legend(loc='upper right')
else:
    ax2.text(0.5, 0.5, 'No MAP/SBP data available', ha='center', va='center', transform=ax2.transAxes)
    ax2.set_ylabel('MAP/SBP')
ax2.set_xlabel('Time')
plt.tight_layout()
save_plot('tachy_runs_overlay_map_sbp.png')
result = {'tachycardia_definition': 'HR>120 bpm for >=3 consecutive HR samples', 'n_hr_samples': int(len(hr_v)), 'n_episodes': int(n_episodes), 'episodes': episodes, 'concurrent_hypotension_window': 'within HR episode ±2 HR samples (time-bounded window)', 'concurrent_hypotension_metric': 'MAP<65' if len(sbp_t) > 0 and len(dbp_t) > 0 and (len(sbp_t) == len(dbp_t)) and all((sbp_t[i] == dbp_t[i] for i in range(len(sbp_t)))) else 'SBP<90 (surrogate; MAP unavailable/asynchronous)', 'n_episodes_with_concurrent_hypotension': int(n_with_hypo), 'pct_episodes_with_concurrent_hypotension': float(pct_with_hypo), 'provided_overall_map_value': float(map_value), 'provided_overall_map_interpretation': str(map_interpretation), 'provided_shock_index': float(shock_index), 'provided_shock_index_interpretation': str(shock_index_interpretation), 'provided_qsofa': int(qsofa_score), 'provided_qsofa_interpretation': str(qsofa_interpretation), 'plot_file': 'tachy_runs_overlay_map_sbp.png'}
interpretation = f'Tachycardia runs (HR>120 for ≥3 consecutive samples): {n_episodes} episode(s); {n_with_hypo}/{n_episodes} ({pct_with_hypo:.1f}%) had concurrent hypotension ({('MAP<65 mmHg' if result['concurrent_hypotension_metric'].startswith('MAP') else 'SBP<90 mmHg')}) within the episode ±2 HR samples, consistent with hemodynamic instability risk given overall MAP {map_value:.0f} mmHg ({map_interpretation}) and shock index {shock_index:.2f} ({shock_index_interpretation}).'

plt.close()