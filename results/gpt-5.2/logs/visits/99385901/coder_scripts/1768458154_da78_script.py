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
def _to_arrays(ts_list):
    if ts_list is None or len(ts_list) == 0:
        return (np.array([]), np.array([]))
    t = np.array([x[0] for x in ts_list], dtype=object)
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _interp_uniform(t_obj, v, dt_sec=5.0):
    if len(t_obj) < 3:
        return (np.array([]), np.array([]), np.nan)
    t_sec = np.array([(ti - t_obj[0]).total_seconds() for ti in t_obj], dtype=float)
    if not np.all(np.isfinite(t_sec)) or not np.all(np.isfinite(v)):
        mask = np.isfinite(t_sec) & np.isfinite(v)
        t_sec = t_sec[mask]
        v = v[mask]
    if len(t_sec) < 3:
        return (np.array([]), np.array([]), np.nan)
    order = np.argsort(t_sec)
    t_sec = t_sec[order]
    v = v[order]
    uniq = np.concatenate([[True], np.diff(t_sec) > 0])
    t_sec = t_sec[uniq]
    v = v[uniq]
    if len(t_sec) < 3:
        return (np.array([]), np.array([]), np.nan)
    duration = t_sec[-1] - t_sec[0]
    if not np.isfinite(duration) or duration < 60.0:
        return (np.array([]), np.array([]), np.nan)
    t_uniform = np.arange(t_sec[0], t_sec[-1] + 1e-09, float(dt_sec))
    v_uniform = np.interp(t_uniform, t_sec, v)
    fs = 1.0 / float(dt_sec)
    return (t_uniform, v_uniform, fs)

def _near_bp_masks(t_uniform, t0_obj, hypot_ts_obj, window_min=10.0):
    if len(t_uniform) == 0:
        return (np.array([], dtype=bool), np.array([], dtype=bool))
    if hypot_ts_obj is None or len(hypot_ts_obj) == 0:
        near = np.zeros_like(t_uniform, dtype=bool)
        far = np.ones_like(t_uniform, dtype=bool)
        return (near, far)
    hyp_sec = np.array([(ti - t0_obj).total_seconds() for ti in hypot_ts_obj], dtype=float)
    hyp_sec = hyp_sec[np.isfinite(hyp_sec)]
    if len(hyp_sec) == 0:
        near = np.zeros_like(t_uniform, dtype=bool)
        far = np.ones_like(t_uniform, dtype=bool)
        return (near, far)
    w = float(window_min) * 60.0
    if len(hyp_sec) > 5000:
        hyp_sec = hyp_sec[::max(1, len(hyp_sec) // 5000)]
    dmin = np.min(np.abs(t_uniform[:, None] - hyp_sec[None, :]), axis=1)
    near = dmin <= w
    far = ~near
    return (near, far)

def _welch_psd(x, fs, nperseg=None, noverlap=None):
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if len(x) < 8 or not np.isfinite(fs) or fs <= 0:
        return (np.array([]), np.array([]))
    x = x - np.mean(x)
    if nperseg is None:
        nperseg = int(min(1024, max(128, 2 ** int(np.floor(np.log2(max(16, len(x) // 8)))))))
        nperseg = int(min(nperseg, len(x)))
    if nperseg < 16:
        return (np.array([]), np.array([]))
    if noverlap is None:
        noverlap = int(nperseg // 2)
    step = nperseg - noverlap
    if step <= 0:
        step = max(1, nperseg // 4)
        noverlap = nperseg - step
    if len(x) < nperseg:
        return (np.array([]), np.array([]))
    win = np.hanning(nperseg)
    scale = fs * np.sum(win ** 2)
    starts = np.arange(0, len(x) - nperseg + 1, step, dtype=int)
    if len(starts) < 2 and len(x) >= nperseg:
        starts = np.array([0], dtype=int)
    Pxx = None
    for s in starts:
        seg = x[s:s + nperseg]
        seg = seg * win
        fft = np.fft.rfft(seg)
        p = np.abs(fft) ** 2 / scale
        if Pxx is None:
            Pxx = p
        else:
            Pxx = Pxx + p
    Pxx = Pxx / float(len(starts))
    f = np.fft.rfftfreq(nperseg, d=1.0 / fs)
    return (f, Pxx)

def _dominant_peaks(f, Pxx, band_low_hz, band_high_hz, top_k=3):
    if len(f) == 0 or len(Pxx) == 0:
        return []
    mask = (f >= band_low_hz) & (f <= band_high_hz) & np.isfinite(Pxx)
    if np.sum(mask) < 5:
        return []
    fb = f[mask]
    Pb = Pxx[mask]
    peaks = []
    for i in range(1, len(Pb) - 1):
        if Pb[i] > Pb[i - 1] and Pb[i] > Pb[i + 1]:
            peaks.append((Pb[i], fb[i]))
    if len(peaks) == 0:
        j = int(np.nanargmax(Pb))
        return [(float(Pb[j]), float(fb[j]))]
    peaks.sort(key=lambda x: x[0], reverse=True)
    out = []
    for p, ff in peaks[:top_k]:
        if ff > 0 and np.isfinite(ff) and np.isfinite(p):
            out.append((float(p), float(ff)))
    return out

def _format_peak_list(peaks):
    lst = []
    for power, ff in peaks:
        if ff <= 0:
            continue
        period_s = 1.0 / ff
        lst.append({'freq_hz': ff, 'period_s': period_s, 'power': power})
    return lst

def _segment_series(x, mask):
    x = np.asarray(x, dtype=float)
    if len(x) == 0 or len(mask) != len(x):
        return np.array([])
    xm = x[mask]
    xm = xm[np.isfinite(xm)]
    return xm

def _compare_psd(t_uniform, x_uniform, fs, near_mask, far_mask, label, dt_sec, make_plot=True):
    x_near = _segment_series(x_uniform, near_mask)
    x_far = _segment_series(x_uniform, far_mask)
    min_samples_short = int(max(120.0 / dt_sec, 64))
    min_samples_long = int(max(8 * 60.0 / dt_sec, 128))
    info = {'fs_hz': float(fs) if np.isfinite(fs) else np.nan, 'dt_sec': float(dt_sec), 'n_total': int(len(x_uniform)), 'n_near': int(len(x_near)), 'n_far': int(len(x_far)), 'near_sufficient_short': bool(len(x_near) >= min_samples_short), 'far_sufficient_short': bool(len(x_far) >= min_samples_short), 'near_sufficient_long': bool(len(x_near) >= min_samples_long), 'far_sufficient_long': bool(len(x_far) >= min_samples_long)}

    def choose_nperseg(n):
        if not np.isfinite(fs) or fs <= 0:
            return None
        for target_min in [10.0, 5.0, 2.0]:
            nps = int(target_min * 60.0 * fs)
            if n >= nps and nps >= 128:
                return nps
        return None
    nps_near = choose_nperseg(len(x_near))
    nps_far = choose_nperseg(len(x_far))
    fN, pN = _welch_psd(x_near, fs, nperseg=nps_near)
    fF, pF = _welch_psd(x_far, fs, nperseg=nps_far)
    band1 = (1.0 / 120.0, 1.0 / 30.0)
    band2 = (1.0 / 600.0, 1.0 / 120.0)
    peaks_near_band1 = _dominant_peaks(fN, pN, band1[0], band1[1], top_k=3) if len(fN) else []
    peaks_near_band2 = _dominant_peaks(fN, pN, band2[0], band2[1], top_k=3) if len(fN) else []
    peaks_far_band1 = _dominant_peaks(fF, pF, band1[0], band1[1], top_k=3) if len(fF) else []
    peaks_far_band2 = _dominant_peaks(fF, pF, band2[0], band2[1], top_k=3) if len(fF) else []
    out = {'label': label, 'info': info, 'near': {'peaks_30_120s': _format_peak_list(peaks_near_band1), 'peaks_2_10min': _format_peak_list(peaks_near_band2)}, 'far': {'peaks_30_120s': _format_peak_list(peaks_far_band1), 'peaks_2_10min': _format_peak_list(peaks_far_band2)}}
    if make_plot:
        fig, ax = plt.subplots(2, 1, sharex=True, figsize=(10, 7), constrained_layout=True)
        if len(fN) and len(pN):
            ax[0].plot(fN, pN, lw=1.2, color='tab:red', label='Near hypotension (±10 min)')
            ax[0].set_yscale('log')
            ax[0].set_ylabel('PSD (log scale)')
            ax[0].set_title(f'{label}: Power Spectral Density (Welch) - Near hypotension')
            peaks_all = _dominant_peaks(fN, pN, band2[0], band1[1], top_k=5)
            for power, ff in peaks_all[:3]:
                if ff > 0:
                    ax[0].axvline(ff, color='k', alpha=0.25, lw=0.8)
                    ax[0].text(ff, max(np.nanmin(pN[np.isfinite(pN)]) * 1.2, power), f'{1.0 / ff:.0f}s', rotation=90, va='bottom', ha='right', fontsize=9)
            ax[0].legend(loc='upper right')
        else:
            ax[0].text(0.5, 0.5, 'Insufficient data for near-hypotension PSD', ha='center', va='center', transform=ax[0].transAxes)
            ax[0].set_axis_off()
        if len(fF) and len(pF):
            ax[1].plot(fF, pF, lw=1.2, color='tab:blue', label='Non-hypotension segments')
            ax[1].set_yscale('log')
            ax[1].set_xlabel('Frequency (Hz)')
            ax[1].set_ylabel('PSD (log scale)')
            ax[1].set_title(f'{label}: Power Spectral Density (Welch) - Non-hypotension')
            peaks_all = _dominant_peaks(fF, pF, band2[0], band1[1], top_k=5)
            for power, ff in peaks_all[:3]:
                if ff > 0:
                    ax[1].axvline(ff, color='k', alpha=0.25, lw=0.8)
                    ax[1].text(ff, max(np.nanmin(pF[np.isfinite(pF)]) * 1.2, power), f'{1.0 / ff:.0f}s', rotation=90, va='bottom', ha='right', fontsize=9)
            ax[1].legend(loc='upper right')
        else:
            ax[1].text(0.5, 0.5, 'Insufficient data for non-hypotension PSD', ha='center', va='center', transform=ax[1].transAxes)
            ax[1].set_axis_off()
        for a in ax:
            if a.has_data():
                a.axvspan(band2[0], band2[1], color='gold', alpha=0.12, label='2–10 min band')
                a.axvspan(band1[0], band1[1], color='limegreen', alpha=0.1, label='30–120 s band')
                a.set_xlim(0, max(band1[1] * 1.5, 0.05))
    return out
t_sbp, v_sbp = _to_arrays(systolic_bp)
t_dbp, v_dbp = _to_arrays(diastolic_bp)
hypot_ts = []
bp_map_samples = []
bp_pp_samples = []
if len(t_sbp) > 0 and len(t_dbp) > 0:
    dbp_times_sec = np.array([(ti - t_dbp[0]).total_seconds() for ti in t_dbp], dtype=float)
    for i in range(len(t_sbp)):
        ts = t_sbp[i]
        sbp = float(v_sbp[i])
        idx = int(np.argmin(np.abs(np.array([(ts - tj).total_seconds() for tj in t_dbp], dtype=float))))
        dt = abs((ts - t_dbp[idx]).total_seconds())
        if np.isfinite(dt) and dt <= 300.0 and np.isfinite(sbp) and np.isfinite(v_dbp[idx]):
            dbp = float(v_dbp[idx])
            map_i = (sbp + 2.0 * dbp) / 3.0
            pp_i = sbp - dbp
            bp_map_samples.append((ts, map_i))
            bp_pp_samples.append((ts, pp_i))
            if map_i < 65.0:
                hypot_ts.append(ts)
hypot_ts = sorted(hypot_ts)
t_hr, v_hr = _to_arrays(heart_rate)
t_sp, v_sp = _to_arrays(spo2)
dt_sec = 5.0
t_hr_u, hr_u, fs_hr = _interp_uniform(t_hr, v_hr, dt_sec=dt_sec)
t_sp_u, sp_u, fs_sp = _interp_uniform(t_sp, v_sp, dt_sec=dt_sec)
plots = []
segments_summary = {}
if len(t_hr_u) > 0:
    t0_hr = t_hr[0]
    near_hr, far_hr = _near_bp_masks(t_hr_u, t0_hr, hypot_ts, window_min=10.0)
else:
    near_hr, far_hr = (np.array([], dtype=bool), np.array([], dtype=bool))
if len(t_sp_u) > 0:
    t0_sp = t_sp[0]
    near_sp, far_sp = _near_bp_masks(t_sp_u, t0_sp, hypot_ts, window_min=10.0)
else:
    near_sp, far_sp = (np.array([], dtype=bool), np.array([], dtype=bool))
hr_psd = _compare_psd(t_hr_u, hr_u, fs_hr, near_hr, far_hr, label='Heart Rate (bpm)', dt_sec=dt_sec, make_plot=True)
save_plot('psd_hr_near_vs_far.png')
plots.append('psd_hr_near_vs_far.png')
sp_psd = _compare_psd(t_sp_u, sp_u, fs_sp, near_sp, far_sp, label='SpO₂ (%)', dt_sec=dt_sec, make_plot=True)
save_plot('psd_spo2_near_vs_far.png')
plots.append('psd_spo2_near_vs_far.png')
result = {'shock_index': shock_index, 'map_value': map_value, 'pulse_pressure': pulse_pressure, 'qsofa_score': qsofa_score, 'bp_map_hypotension_definition': 'MAP<65 mmHg computed at BP-aligned samples (SBP/DBP nearest within 5 min)', 'n_bp_map_samples': int(len(bp_map_samples)), 'n_hypotensive_bp_samples': int(len(hypot_ts)), 'hypotension_window_min': 10.0, 'resampling_dt_sec': dt_sec, 'psd': {'heart_rate': hr_psd, 'spo2': sp_psd}, 'plots': plots}

def _peak_sentence(psd_dict):

    def best_peak(peaks):
        if not peaks:
            return None
        pk = sorted(peaks, key=lambda d: d.get('power', -np.inf), reverse=True)[0]
        return pk
    near_peaks = psd_dict.get('near', {}).get('peaks_30_120s', []) + psd_dict.get('near', {}).get('peaks_2_10min', [])
    far_peaks = psd_dict.get('far', {}).get('peaks_30_120s', []) + psd_dict.get('far', {}).get('peaks_2_10min', [])
    bn = best_peak(near_peaks)
    bf = best_peak(far_peaks)

    def fmt(pk):
        if pk is None:
            return 'no dominant peak detected in 30–120 s or 2–10 min bands'
        p = pk['period_s']
        if p >= 120:
            return f'dominant periodicity ~{p / 60.0:.1f} min'
        return f'dominant periodicity ~{p:.0f} s'
    return (fmt(bn), fmt(bf))
hr_near_sent, hr_far_sent = _peak_sentence(hr_psd)
sp_near_sent, sp_far_sent = _peak_sentence(sp_psd)
interpretation = {'shock_index': shock_index_interpretation, 'map': map_interpretation, 'qsofa': qsofa_interpretation, 'spectral_cycling_summary': f'HR PSD near hypotension shows {hr_near_sent} vs non-hypotension {hr_far_sent}; SpO₂ PSD near hypotension shows {sp_near_sent} vs non-hypotension {sp_far_sent}.', 'notes': 'PSD computed on uniformly resampled (5 s) interpolated HR/SpO₂; interpret quasi-periodicity cautiously given irregular original sampling and potential motion/measurement artifacts.'}

plt.close()