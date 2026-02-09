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
def _to_arrays(ts_list):
    if ts_list is None or len(ts_list) == 0:
        return (np.array([], dtype=object), np.array([], dtype=float))
    t = np.array([x[0] for x in ts_list], dtype=object)
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _map_from_bp(sbps, dbps):
    return (sbps + 2.0 * dbps) / 3.0

def _window_center_time(t_start, t_end):
    return t_start + (t_end - t_start) / 2

def _pearsonr_safe(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.size < 3 or y.size < 3:
        return (np.nan, np.nan)
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 3:
        return (np.nan, np.nan)
    if np.nanstd(x[m]) == 0 or np.nanstd(y[m]) == 0:
        return (np.nan, np.nan)
    r, p = stats.pearsonr(x[m], y[m])
    return (float(r), float(p))

def _sec(dt0, dt1):
    return (dt1 - dt0).total_seconds()
window_minutes = 12.0
step_minutes = 2.0
min_pairs = 5
inverse_threshold = -0.5
pair_tol_seconds = 120.0
t_hr, v_hr = _to_arrays(heart_rate)
t_sbp, v_sbp = _to_arrays(systolic_bp)
t_dbp, v_dbp = _to_arrays(diastolic_bp)
all_times = []
if t_hr.size > 0:
    all_times.extend([t_hr[0], t_hr[-1]])
if t_sbp.size > 0:
    all_times.extend([t_sbp[0], t_sbp[-1]])
if t_dbp.size > 0:
    all_times.extend([t_dbp[0], t_dbp[-1]])
if len(all_times) == 0:
    result = {'window_minutes': window_minutes, 'step_minutes': step_minutes, 'min_pairs': min_pairs, 'inverse_threshold': inverse_threshold, 'n_windows': 0, 'n_flagged': 0, 'flagged_intervals': [], 'correlation_series': [], 'plot_file': None}
    interpretation = 'Insufficient data to compute rolling HR–MAP correlation.'
else:
    t_min = min(all_times)
    t_max = max(all_times)
    span_minutes = (t_max - t_min).total_seconds() / 60.0
    if span_minutes < window_minutes:
        result = {'window_minutes': window_minutes, 'step_minutes': step_minutes, 'min_pairs': min_pairs, 'inverse_threshold': inverse_threshold, 'n_windows': 0, 'n_flagged': 0, 'flagged_intervals': [], 'correlation_series': [], 'plot_file': None}
        interpretation = 'Time span is shorter than rolling window; cannot compute HR–MAP correlation.'
    else:
        step_seconds = step_minutes * 60.0
        win_seconds = window_minutes * 60.0
        n_steps = int(np.floor(((t_max - t_min).total_seconds() - win_seconds) / step_seconds)) + 1
        if n_steps < 1:
            n_steps = 1
        window_starts = [t_min + i * (t_max - t_max + (t_max - t_max)) for i in range(0)]
        window_starts = [t_min + i * __import__('datetime').timedelta(seconds=step_seconds) for i in range(n_steps)]
        td_step = t_max - t_min
        td_step = td_step - td_step
        step_td = type(td_step)(seconds=int(round(step_seconds)))
        win_td = type(td_step)(seconds=int(round(win_seconds)))
        window_starts = [t_min + i * step_td for i in range(n_steps)]

        def _slice_between(t_arr, v_arr, t0, t1):
            if t_arr.size == 0:
                return (np.array([], dtype=object), np.array([], dtype=float))
            m = (t_arr >= t0) & (t_arr <= t1)
            return (t_arr[m], v_arr[m])
        corr_times, corr_r, corr_p, n_pairs_list = ([], [], [], [])
        flagged = []
        for t0 in window_starts:
            t1 = t0 + win_td
            t_hr_w, hr_w = _slice_between(t_hr, v_hr, t0, t1)
            t_sbp_w, sbp_w = _slice_between(t_sbp, v_sbp, t0, t1)
            t_dbp_w, dbp_w = _slice_between(t_dbp, v_dbp, t0, t1)
            pairs_t = []
            pairs_map = []
            if t_sbp_w.size > 0 and t_dbp_w.size > 0:
                sbp_secs = np.array([_sec(t0, tt) for tt in t_sbp_w], dtype=float)
                dbp_secs = np.array([_sec(t0, tt) for tt in t_dbp_w], dtype=float)
                for i in range(t_sbp_w.size):
                    j = int(np.argmin(np.abs(dbp_secs - sbp_secs[i])))
                    if abs(dbp_secs[j] - sbp_secs[i]) <= pair_tol_seconds:
                        pairs_t.append(t_sbp_w[i])
                        pairs_map.append(_map_from_bp(sbp_w[i], dbp_w[j]))
                for j in range(t_dbp_w.size):
                    i = int(np.argmin(np.abs(sbp_secs - dbp_secs[j])))
                    if abs(sbp_secs[i] - dbp_secs[j]) <= pair_tol_seconds:
                        pairs_t.append(t_dbp_w[j])
                        pairs_map.append(_map_from_bp(sbp_w[i], dbp_w[j]))
                if len(pairs_t) > 0:
                    idx = np.argsort(np.array([tt.timestamp() for tt in pairs_t], dtype=float))
                    pairs_t_sorted = [pairs_t[k] for k in idx]
                    pairs_map_sorted = np.array([pairs_map[k] for k in idx], dtype=float)
                    uniq_t = []
                    uniq_map = []
                    k = 0
                    while k < len(pairs_t_sorted):
                        t_curr = pairs_t_sorted[k]
                        vals = [pairs_map_sorted[k]]
                        k2 = k + 1
                        while k2 < len(pairs_t_sorted) and pairs_t_sorted[k2] == t_curr:
                            vals.append(pairs_map_sorted[k2])
                            k2 += 1
                        uniq_t.append(t_curr)
                        uniq_map.append(float(np.nanmean(vals)))
                        k = k2
                    pairs_t = np.array(uniq_t, dtype=object)
                    pairs_map = np.array(uniq_map, dtype=float)
                else:
                    pairs_t = np.array([], dtype=object)
                    pairs_map = np.array([], dtype=float)
            else:
                pairs_t = np.array([], dtype=object)
                pairs_map = np.array([], dtype=float)
            hr_aligned = []
            map_aligned = []
            if pairs_t.size > 0 and t_hr_w.size > 0:
                hr_secs = np.array([_sec(t0, tt) for tt in t_hr_w], dtype=float)
                map_secs = np.array([_sec(t0, tt) for tt in pairs_t], dtype=float)
                for msec, mval in zip(map_secs, pairs_map):
                    i = int(np.argmin(np.abs(hr_secs - msec)))
                    if abs(hr_secs[i] - msec) <= pair_tol_seconds:
                        hr_aligned.append(float(hr_w[i]))
                        map_aligned.append(float(mval))
            hr_aligned = np.array(hr_aligned, dtype=float)
            map_aligned = np.array(map_aligned, dtype=float)
            n_pairs = int(min(hr_aligned.size, map_aligned.size))
            if n_pairs >= min_pairs:
                r, p = _pearsonr_safe(hr_aligned, map_aligned)
            else:
                r, p = (np.nan, np.nan)
            ct = _window_center_time(t0, t1)
            corr_times.append(ct)
            corr_r.append(r)
            corr_p.append(p)
            n_pairs_list.append(n_pairs)
            if np.isfinite(r) and r < inverse_threshold:
                flagged.append({'start': t0, 'end': t1, 'center_time': ct, 'r': float(r), 'p_value': float(p) if np.isfinite(p) else np.nan, 'n_pairs': n_pairs})
        fig, ax = plt.subplots(1, 1, figsize=(10, 4))
        ax.plot(corr_times, corr_r, color='black', linewidth=1.5, label='Rolling Pearson r (HR vs MAP)')
        ax.axhline(0.0, color='gray', linewidth=1.0)
        ax.axhline(inverse_threshold, color='red', linestyle='--', linewidth=1.2, label=f'Inverse threshold r<{inverse_threshold}')
        for f in flagged:
            ax.axvspan(f['start'], f['end'], color='red', alpha=0.12)
        ax.set_title(f'Rolling HR–MAP Pearson Correlation (window={window_minutes:.0f} min, step={step_minutes:.0f} min)')
        ax.set_ylabel('Pearson r')
        ax.set_xlabel('Time')
        ax.set_ylim(-1.05, 1.05)
        ax.legend(loc='lower right', frameon=True)
        ax.text(0.01, 0.02, f'Shock Index={shock_index:.3f} ({shock_index_interpretation.split('.')[0]}) | MAP={map_value:.0f} mmHg ({map_interpretation.split('.')[0]})', transform=ax.transAxes, fontsize=9, va='bottom', ha='left')
        save_plot('rolling_hr_map_correlation.png', fig=fig)
        corr_series = []
        for ct, r, p, npairs in zip(corr_times, corr_r, corr_p, n_pairs_list):
            corr_series.append({'center_time': ct, 'r': float(r) if np.isfinite(r) else np.nan, 'p_value': float(p) if np.isfinite(p) else np.nan, 'n_pairs': int(npairs)})
        valid_rs = np.array([x for x in corr_r if np.isfinite(x)], dtype=float)
        r_min = float(np.min(valid_rs)) if valid_rs.size > 0 else np.nan
        r_med = float(np.median(valid_rs)) if valid_rs.size > 0 else np.nan
        result = {'window_minutes': float(window_minutes), 'step_minutes': float(step_minutes), 'min_pairs': int(min_pairs), 'inverse_threshold': float(inverse_threshold), 'pair_tol_seconds': float(pair_tol_seconds), 'n_windows': int(len(corr_times)), 'n_windows_valid': int(valid_rs.size), 'r_min': r_min, 'r_median': r_med, 'n_flagged': int(len(flagged)), 'flagged_intervals': flagged, 'correlation_series': corr_series, 'plot_file': 'rolling_hr_map_correlation.png'}
        if valid_rs.size == 0:
            interpretation = 'Rolling HR–MAP correlation could not be computed due to insufficient paired HR and BP data within windows.'
        elif len(flagged) > 0:
            interpretation = f'Rolling HR–MAP correlation shows {len(flagged)}/{len(corr_times)} intervals with strong inverse coupling (r<{inverse_threshold}), consistent with periods of tachycardia accompanying falling perfusion pressure (MAP).'
        else:
            interpretation = f'Rolling HR–MAP correlation does not show strong inverse coupling (no windows with r<{inverse_threshold}); despite this, absolute perfusion remains low (MAP {map_value:.0f} mmHg) with elevated shock index ({shock_index:.2f}).'

plt.close()