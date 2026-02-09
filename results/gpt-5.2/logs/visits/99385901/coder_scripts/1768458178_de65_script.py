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
def _extract_xy(ts):
    if ts is None or len(ts) == 0:
        return (np.array([]), np.array([]))
    t = np.array([p[0] for p in ts], dtype=object)
    v = np.array([float(p[1]) for p in ts], dtype=float)
    return (t, v)

def _nn_align(base_times, query_times, query_vals, max_abs_minutes):
    if len(base_times) == 0 or len(query_times) == 0:
        return (np.array([], dtype=int), np.array([], dtype=int), np.array([], dtype=float), np.array([], dtype=float))
    bt = np.array([dt.timestamp() for dt in base_times], dtype=float)
    qt = np.array([dt.timestamp() for dt in query_times], dtype=float)
    idx_base = []
    idx_query = []
    dmins = []
    for i, tsec in enumerate(bt):
        j = int(np.searchsorted(qt, tsec))
        cand = []
        if 0 <= j < len(qt):
            cand.append(j)
        if 0 <= j - 1 < len(qt):
            cand.append(j - 1)
        if len(cand) == 0:
            continue
        best_j = min(cand, key=lambda k: abs(qt[k] - tsec))
        dm = abs(qt[best_j] - tsec) / 60.0
        if dm <= max_abs_minutes:
            idx_base.append(i)
            idx_query.append(best_j)
            dmins.append(dm)
    if len(idx_base) == 0:
        return (np.array([], dtype=int), np.array([], dtype=int), np.array([], dtype=float), np.array([], dtype=float))
    idx_base = np.array(idx_base, dtype=int)
    idx_query = np.array(idx_query, dtype=int)
    dmins = np.array(dmins, dtype=float)
    return (idx_base, idx_query, dmins, query_vals[idx_query])

def _pearsonr_safe(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    m = np.isfinite(x) & np.isfinite(y)
    x = x[m]
    y = y[m]
    if len(x) < 3:
        return (np.nan, np.nan, int(len(x)))
    if np.std(x) == 0 or np.std(y) == 0:
        return (np.nan, np.nan, int(len(x)))
    r, p = stats.pearsonr(x, y)
    return (float(r), float(p), int(len(x)))

def _map_from_bp(sbp_list, dbp_list, max_abs_minutes=5.0):
    st, sv = _extract_xy(sbp_list)
    dt, dv = _extract_xy(dbp_list)
    if len(st) == 0 or len(dt) == 0:
        return (np.array([], dtype=object), np.array([], dtype=float))
    idx_s, idx_d, dmins, aligned_dbp = _nn_align(st, dt, dv, max_abs_minutes=max_abs_minutes)
    if len(idx_s) == 0:
        return (np.array([], dtype=object), np.array([], dtype=float))
    sbp_al = sv[idx_s]
    dbp_al = aligned_dbp
    map_al = (sbp_al + 2.0 * dbp_al) / 3.0
    times_al = st[idx_s]
    return (times_al, map_al)

def _temp_slope_at_map_times(map_times, temp_times, temp_vals, window_minutes=20.0):
    if len(map_times) == 0 or len(temp_times) == 0:
        return (np.array([], dtype=float), np.array([], dtype=int))
    mt = np.array([dt.timestamp() for dt in map_times], dtype=float)
    tt = np.array([dt.timestamp() for dt in temp_times], dtype=float)
    tv = np.asarray(temp_vals, dtype=float)
    slopes = np.full(len(map_times), np.nan, dtype=float)
    ns = np.zeros(len(map_times), dtype=int)
    halfwin = window_minutes * 60.0
    for i, tsec in enumerate(mt):
        m = np.abs(tt - tsec) <= halfwin
        n = int(np.sum(m))
        ns[i] = n
        if n < 3:
            continue
        x = (tt[m] - tsec) / 60.0
        y = tv[m]
        try:
            b = np.polyfit(x, y, 1)[0]
            slopes[i] = float(b)
        except Exception:
            slopes[i] = np.nan
    return (slopes, ns)
map_times, map_series = _map_from_bp(systolic_bp, diastolic_bp, max_abs_minutes=5.0)
temp_times, temp_vals = _extract_xy(temperature)
lags = np.arange(-60, 61, 1, dtype=int)
r_vals = np.full_like(lags, np.nan, dtype=float)
p_vals = np.full_like(lags, np.nan, dtype=float)
n_pairs = np.zeros_like(lags, dtype=int)
max_match_minutes = 5.0
if len(map_times) > 0 and len(temp_times) > 0:
    mt_sec = np.array([dt.timestamp() for dt in map_times], dtype=float)
    tt_sec = np.array([dt.timestamp() for dt in temp_times], dtype=float)
    order_t = np.argsort(tt_sec)
    tt_sec = tt_sec[order_t]
    tv = temp_vals[order_t]
    for k, lag in enumerate(lags):
        shifted_mt_sec = mt_sec + lag * 60.0
        idx_temp = []
        idx_map = []
        for i, tsec in enumerate(shifted_mt_sec):
            j = int(np.searchsorted(tt_sec, tsec))
            cand = []
            if 0 <= j < len(tt_sec):
                cand.append(j)
            if 0 <= j - 1 < len(tt_sec):
                cand.append(j - 1)
            if len(cand) == 0:
                continue
            best_j = min(cand, key=lambda q: abs(tt_sec[q] - tsec))
            dm = abs(tt_sec[best_j] - tsec) / 60.0
            if dm <= max_match_minutes:
                idx_map.append(i)
                idx_temp.append(best_j)
        if len(idx_map) < 3:
            continue
        x_temp = tv[np.array(idx_temp, dtype=int)]
        y_map = map_series[np.array(idx_map, dtype=int)]
        r, p, n = _pearsonr_safe(x_temp, y_map)
        r_vals[k] = r
        p_vals[k] = p
        n_pairs[k] = n
if np.all(~np.isfinite(r_vals)):
    peak_idx = None
    peak_lag = None
    peak_r = np.nan
    peak_p = np.nan
    peak_n = 0
else:
    peak_idx = int(np.nanargmax(np.abs(r_vals)))
    peak_lag = int(lags[peak_idx])
    peak_r = float(r_vals[peak_idx])
    peak_p = float(p_vals[peak_idx]) if np.isfinite(p_vals[peak_idx]) else np.nan
    peak_n = int(n_pairs[peak_idx])
n_aligned_pairs = 0
idx_m, idx_t, dmins0, temp_at_map = _nn_align(map_times, temp_times, temp_vals, max_abs_minutes=10.0)
n_aligned_pairs = int(len(idx_m))
if n_aligned_pairs > 0:
    map_t0 = map_times[idx_m]
    map_v0 = map_series[idx_m]
    slopes, slope_ns = _temp_slope_at_map_times(map_t0, temp_times, temp_vals, window_minutes=20.0)
    hypot = map_v0 < 65.0
    rising = np.isfinite(slopes) & (slopes > 0)
    falling = np.isfinite(slopes) & (slopes < 0)
    n_hypot = int(np.sum(hypot))
    n_hypot_rising = int(np.sum(hypot & rising))
    n_hypot_falling = int(np.sum(hypot & falling))
    n_hypot_flat = int(np.sum(hypot & np.isfinite(slopes) & (slopes == 0)))
    n_hypot_unsure = int(np.sum(hypot & ~np.isfinite(slopes)))
    pct_rising = 100.0 * n_hypot_rising / n_hypot if n_hypot > 0 else np.nan
    pct_falling = 100.0 * n_hypot_falling / n_hypot if n_hypot > 0 else np.nan
    pct_unsure = 100.0 * n_hypot_unsure / n_hypot if n_hypot > 0 else np.nan
    if n_hypot > 0 and np.isfinite(pct_rising) and np.isfinite(pct_falling):
        if pct_rising > pct_falling + 10.0:
            cluster_label = 'clusters more on rising temperature'
        elif pct_falling > pct_rising + 10.0:
            cluster_label = 'clusters more on falling temperature'
        else:
            cluster_label = 'no clear preference for rising vs falling temperature'
    else:
        cluster_label = 'insufficient data to assess clustering'
else:
    n_hypot = 0
    n_hypot_rising = 0
    n_hypot_falling = 0
    n_hypot_flat = 0
    n_hypot_unsure = 0
    pct_rising = np.nan
    pct_falling = np.nan
    pct_unsure = np.nan
    cluster_label = 'insufficient aligned MAP-Temp data'
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(lags, r_vals, color='tab:blue', lw=2)
ax.axhline(0, color='black', lw=1, alpha=0.6)
ax.set_xlim(-60, 60)
ax.set_xlabel('Lag (minutes): Temp(t) vs MAP(t + lag)')
ax.set_ylabel('Pearson r')
ax.set_title('Lagged cross-correlation: Temperature vs MAP (nearest-neighbor aligned)')
if peak_idx is not None and np.isfinite(peak_r):
    ax.scatter([peak_lag], [peak_r], color='tab:red', zorder=5)
    txt = f'Peak |r|={abs(peak_r):.3f} (r={peak_r:.3f}) at lag {peak_lag} min\nn={peak_n}'
    if np.isfinite(peak_p):
        txt += f', p={peak_p:.3g}'
    ax.annotate(txt, xy=(peak_lag, peak_r), xytext=(peak_lag + (8 if peak_lag <= 0 else -35), peak_r + (0.12 if peak_r <= 0 else -0.18)), arrowprops=dict(arrowstyle='->', lw=1), fontsize=9, bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='0.7', alpha=0.9))
cluster_note = f'MAP<65 clustering: rising {n_hypot_rising}/{n_hypot} ({pct_rising:.1f}%), falling {n_hypot_falling}/{n_hypot} ({pct_falling:.1f}%), unsure {n_hypot_unsure}/{n_hypot} ({pct_unsure:.1f}%)\nConclusion: {cluster_label}'
ax.text(0.01, 0.01, cluster_note, transform=ax.transAxes, va='bottom', ha='left', fontsize=9, bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='0.7', alpha=0.9))
ax.grid(True, alpha=0.25)
save_plot('temp_map_lagged_cross_correlation.png', fig=fig)
result = {'lags_min': lags.tolist(), 'pearson_r': [None if not np.isfinite(v) else float(v) for v in r_vals], 'p_value': [None if not np.isfinite(v) else float(v) for v in p_vals], 'n_pairs': [int(v) for v in n_pairs], 'peak': {'lag_min': None if peak_lag is None else int(peak_lag), 'r': None if not np.isfinite(peak_r) else float(peak_r), 'p': None if not np.isfinite(peak_p) else float(peak_p), 'n_pairs': int(peak_n), 'selection': 'max absolute Pearson r over lags [-60, +60] minutes', 'alignment': f'nearest-neighbor Temp to lag-shifted MAP timestamps within ±{max_match_minutes:.1f} min'}, 'map65_clustering_vs_temp_slope': {'map_alignment': 'nearest-neighbor Temp to MAP timestamps within ±10 min', 'temp_slope_method': 'local linear fit within ±20 min window around each MAP timestamp; slope in °C/min', 'n_aligned_pairs': int(n_aligned_pairs), 'n_map_lt_65': int(n_hypot), 'n_map_lt_65_rising_temp': int(n_hypot_rising), 'n_map_lt_65_falling_temp': int(n_hypot_falling), 'n_map_lt_65_flat_temp': int(n_hypot_flat), 'n_map_lt_65_unsure_slope': int(n_hypot_unsure), 'pct_map_lt_65_rising_temp': None if not np.isfinite(pct_rising) else float(pct_rising), 'pct_map_lt_65_falling_temp': None if not np.isfinite(pct_falling) else float(pct_falling), 'pct_map_lt_65_unsure_slope': None if not np.isfinite(pct_unsure) else float(pct_unsure), 'conclusion': cluster_label}, 'provided_context': {'map_value_state': float(map_value), 'map_interpretation_state': str(map_interpretation), 'shock_index_state': float(shock_index), 'shock_index_interpretation_state': str(shock_index_interpretation)}, 'plot_file': 'temp_map_lagged_cross_correlation.png'}
if peak_lag is None or not np.isfinite(peak_r):
    interpretation = 'Insufficient overlapping Temperature–MAP data to compute a reliable lagged cross-correlation across ±60 minutes; MAP<65 clustering vs temperature direction cannot be determined from available aligned pairs.'
else:
    direction = 'positive' if peak_r > 0 else 'negative'
    interpretation = f'Temperature–MAP coupling shows a peak {direction} correlation at lag {peak_lag} min (r={peak_r:.3f}, n={peak_n}' + (f', p={peak_p:.3g}' if np.isfinite(peak_p) else '') + f'); MAP<65 {cluster_label} based on local temperature slope classification.'

plt.close()