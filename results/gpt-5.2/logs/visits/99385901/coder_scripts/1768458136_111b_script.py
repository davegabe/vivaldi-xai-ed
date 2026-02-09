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
create_a_time-aligned_phase-space_scatter_of_hr_vs_map_with_points_colored_by_time_(or_temperature_if_available)_and_annotate_regions_where_map<65_and/or_hr>110. = None
detect_tachycardia_runs_where_hr>120_for_≥3_consecutive_samples;_overlay_these_episodes_on_map_(or_sbp)_time_series_to_quantify_concurrent_hypotension_(e.g.,_%_of_episodes_with_map<65_within_±2_samples). = None
compute_rolling-window_(10–15_min)_pearson_correlation_between_hr_and_map;_plot_correlation_vs_time_and_flag_intervals_with_strong_inverse_coupling_(e.g.,_r<-0.5). = None
calculate_burden_on_bp-sampled_points:_%_with_map<65,_%_with_pp≤30,_and_%_with_map<65_&_pp≤30_simultaneously;_also_compute_the_longest_consecutive_run_(in_minutes)_of_bp_samples_with_map<65_(use_sample_timestamps). = None
plot_rr_vs_spo₂_scatter_time-aligned_(nearest-neighbor_within_a_small_window),_colored_by_time,_and_flag/report_proportion_of_points_with_rr≥24_while_spo₂≥94_vs_points_with_rr≥24_and_spo₂<94_(disproportionate_drive_vs_hypoxemia-coupled). = None
plot_phase-space:_pulse_pressure_(sbp−dbp)_vs_map,_points_time-aligned_to_bp_samples_and_colored_by_temperature_(temp),_and_report_clustering_of_low_map_with_narrow_pp. = None

# --- Generated Code Starts Here ---
def _to_arrays(ts_vals):
    t = [tv[0] for tv in ts_vals]
    v = [float(tv[1]) for tv in ts_vals]
    return (t, np.asarray(v, dtype=float))

def _nearest_within_window(target_times, source_times, source_values, window_min=30.0):
    n_src = len(source_times)
    if n_src == 0:
        return (np.full(len(target_times), np.nan), np.full(len(target_times), np.nan))
    out_vals = np.full(len(target_times), np.nan)
    out_dt_min = np.full(len(target_times), np.nan)
    j = 0
    for i, tt in enumerate(target_times):
        while j + 1 < n_src and source_times[j + 1] <= tt:
            j += 1
        best_j = j
        best_abs = abs((source_times[best_j] - tt).total_seconds()) / 60.0
        if j + 1 < n_src:
            cand_abs = abs((source_times[j + 1] - tt).total_seconds()) / 60.0
            if cand_abs < best_abs:
                best_j = j + 1
                best_abs = cand_abs
        if best_abs <= window_min:
            out_vals[i] = float(source_values[best_j])
            out_dt_min[i] = float((source_times[best_j] - tt).total_seconds() / 60.0)
    return (out_vals, out_dt_min)

def _lagged_corr(x, y, lag_steps):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    r = np.full(len(lag_steps), np.nan, dtype=float)
    for k, lag in enumerate(lag_steps):
        if lag == 0:
            xs, ys = (x, y)
        elif lag > 0:
            if lag >= n:
                continue
            xs, ys = (x[:-lag], y[lag:])
        else:
            L = -lag
            if L >= n:
                continue
            xs, ys = (x[L:], y[:-L])
        m = np.isfinite(xs) & np.isfinite(ys)
        if m.sum() >= 5:
            xs2 = xs[m]
            ys2 = ys[m]
            if np.std(xs2) > 0 and np.std(ys2) > 0:
                r[k] = np.corrcoef(xs2, ys2)[0, 1]
    return r
sbp_t, sbp_v = _to_arrays(systolic_bp)
dbp_t, dbp_v = _to_arrays(diastolic_bp)
dbp_near_v, dbp_near_dt = _nearest_within_window(sbp_t, dbp_t, dbp_v, window_min=5.0)
pp_v = sbp_v - dbp_near_v
pp_t = np.asarray(sbp_t, dtype=object)
valid_pp = np.isfinite(pp_v)
pp_t = pp_t[valid_pp]
pp_v = pp_v[valid_pp]
temp_t, temp_v = _to_arrays(temperature)
temp_at_bp, temp_dt_min = _nearest_within_window(pp_t.tolist(), temp_t, temp_v, window_min=30.0)
m_pair = np.isfinite(pp_v) & np.isfinite(temp_at_bp)
pp_t2 = pp_t[m_pair]
pp2 = pp_v[m_pair]
temp2 = temp_at_bp[m_pair]
temp_dt2 = temp_dt_min[m_pair]
if len(pp_t2) >= 6:
    t0 = pp_t2[0]
    minutes = np.array([(t - t0).total_seconds() / 60.0 for t in pp_t2], dtype=float)
    t_end = minutes.max()
    grid = np.arange(0.0, t_end + 1.0, 1.0, dtype=float)
    order = np.argsort(minutes)
    minutes_s = minutes[order]
    pp_s = pp2[order]
    temp_s = temp2[order]
    uniq_t, uniq_idx = np.unique(minutes_s, return_index=True)
    pp_u = pp_s[uniq_idx]
    temp_u = temp_s[uniq_idx]
    pp_g = np.interp(grid, uniq_t, pp_u, left=np.nan, right=np.nan)
    temp_g = np.interp(grid, uniq_t, temp_u, left=np.nan, right=np.nan)
    finite_g = np.isfinite(pp_g) & np.isfinite(temp_g)
    lag_steps = np.arange(-60, 61, 1, dtype=int)
    r_lags = _lagged_corr(pp_g, temp_g, lag_steps)
    finite_r = np.isfinite(r_lags)
    if finite_r.any():
        peak_idx = np.nanargmax(np.abs(r_lags))
        peak_lag_min = int(lag_steps[peak_idx])
        peak_r = float(r_lags[peak_idx])
    else:
        peak_idx = None
        peak_lag_min = None
        peak_r = np.nan
else:
    lag_steps = np.arange(-60, 61, 1, dtype=int)
    r_lags = np.full(len(lag_steps), np.nan)
    peak_idx = None
    peak_lag_min = None
    peak_r = np.nan
    grid = np.array([])
    pp_g = np.array([])
    temp_g = np.array([])
pp_narrow_mask = np.isfinite(pp2) & (pp2 <= 30.0) & np.isfinite(temp_dt2)
narrow_lags = temp_dt2[pp_narrow_mask]
all_lags = temp_dt2[np.isfinite(temp_dt2)]
fig, axes = plt.subplots(2, 1, figsize=(10, 8), constrained_layout=True)
ax = axes[0]
ax.axhline(0, color='0.7', lw=1)
ax.plot(lag_steps, r_lags, color='tab:blue', lw=2)
ax.set_xlim(-60, 60)
ax.set_xlabel('Lag (min)  [positive: Temp leads PP; negative: Temp lags PP]')
ax.set_ylabel('Pearson r')
ax.set_title('Lagged cross-correlation: Temperature vs Pulse Pressure (nearest-neighbor aligned)')
if peak_lag_min is not None and np.isfinite(peak_r):
    ax.axvline(peak_lag_min, color='tab:red', lw=2, alpha=0.8)
    ax.scatter([peak_lag_min], [peak_r], color='tab:red', zorder=5)
    ax.annotate(f'peak |r|={abs(peak_r):.3f}\nr={peak_r:.3f}\nlag={peak_lag_min:+d} min', xy=(peak_lag_min, peak_r), xytext=(peak_lag_min + (5 if peak_lag_min < 30 else -25), peak_r + (0.1 if peak_r < 0.6 else -0.2)), arrowprops=dict(arrowstyle='->', color='tab:red', lw=1), fontsize=10)
ax2 = axes[1]
bins = np.arange(-30, 31, 2, dtype=float)
if len(all_lags) > 0:
    ax2.hist(all_lags, bins=bins, alpha=0.35, color='0.5', label='All BP–Temp pair lags')
if len(narrow_lags) > 0:
    ax2.hist(narrow_lags, bins=bins, alpha=0.75, color='tab:orange', label='Narrow PP≤30 mmHg pair lags')
ax2.axvline(0, color='0.2', lw=1)
ax2.set_xlim(-30, 30)
ax2.set_xlabel('Pairing lag = (Temp time − BP time), minutes')
ax2.set_ylabel('Count')
ax2.set_title('Nearest-neighbor BP–Temp pairing lag distribution (highlight: narrow pulse pressure)')
ax2.legend(loc='best', frameon=False)
save_plot('temp_pp_lagged_xcorr_and_narrow_pp_lags.png', fig=fig)
n_pairs = int(len(pp2))
n_narrow = int(np.sum(np.isfinite(pp2) & (pp2 <= 30.0)))
pct_narrow = 100.0 * n_narrow / n_pairs if n_pairs > 0 else np.nan
if len(narrow_lags) > 0:
    lag_med = float(np.nanmedian(narrow_lags))
    lag_iqr = (float(np.nanpercentile(narrow_lags, 25)), float(np.nanpercentile(narrow_lags, 75)))
else:
    lag_med = np.nan
    lag_iqr = (np.nan, np.nan)
result = {'alignment': {'bp_samples_with_pp': int(len(pp_v)), 'bp_temp_aligned_pairs': n_pairs, 'temp_window_min': 30.0, 'dbp_window_min_for_pp': 5.0, 'pair_lag_min_summary': {'all_pairs_median': float(np.nanmedian(all_lags)) if len(all_lags) else np.nan, 'all_pairs_iqr': (float(np.nanpercentile(all_lags, 25)) if len(all_lags) else np.nan, float(np.nanpercentile(all_lags, 75)) if len(all_lags) else np.nan)}}, 'pp_summary_on_aligned_pairs': {'pp_min_mmHg': float(np.nanmin(pp2)) if n_pairs else np.nan, 'pp_mean_mmHg': float(np.nanmean(pp2)) if n_pairs else np.nan, 'pp_max_mmHg': float(np.nanmax(pp2)) if n_pairs else np.nan, 'n_narrow_pp_le_30': n_narrow, 'pct_narrow_pp_le_30': float(pct_narrow) if np.isfinite(pct_narrow) else np.nan, 'narrow_pp_pair_lag_median_min': lag_med, 'narrow_pp_pair_lag_iqr_min': lag_iqr}, 'lagged_cross_correlation': {'lags_min': lag_steps.tolist(), 'r': r_lags.tolist(), 'peak_abs_r': float(abs(peak_r)) if np.isfinite(peak_r) else np.nan, 'peak_r': float(peak_r) if np.isfinite(peak_r) else np.nan, 'peak_lag_min': peak_lag_min, 'lag_sign_convention': 'corr(PP[t], Temp[t+lag]); lag>0 means Temp leads PP', 'resampling_grid_min': 1, 'lag_range_min': [-60, 60]}, 'provided_state_context_used': {'map_value_mmHg': float(map_value), 'pulse_pressure_mmHg': float(pulse_pressure), 'shock_index': float(shock_index), 'qsofa_score': int(qsofa_score)}}
if peak_lag_min is None or not np.isfinite(peak_r):
    interpretation = 'Insufficient aligned BP–temperature data to compute a reliable ±60 min lagged correlation between temperature (°C) and pulse pressure (mmHg), so no peak lag/correlation could be annotated.'
else:
    interpretation = f'Temperature–pulse pressure coupling shows a peak correlation of r={peak_r:.3f} at lag {peak_lag_min:+d} min (positive lag: temperature leads PP), with {pct_narrow:.1f}% of aligned BP samples having narrow pulse pressure ≤30 mmHg; narrow-PP BP–Temp pairing lags are centered around median {lag_med:.1f} min (IQR {lag_iqr[0]:.1f} to {lag_iqr[1]:.1f}).'

plt.close()