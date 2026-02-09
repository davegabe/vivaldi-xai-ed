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
visit_id = '99755326'
age = 49
gender = 'F'
ethnicity = 'Other (Hispanic/Latino)'
heart_rate = [(datetime.datetime(2218, 10, 22, 16, 58, 2), 127.375), (datetime.datetime(2218, 10, 22, 16, 59, 2), 130.140350877193), (datetime.datetime(2218, 10, 22, 17, 0, 2), 133.050847457627), (datetime.datetime(2218, 10, 22, 17, 1, 2), 138.203389830508), (datetime.datetime(2218, 10, 22, 17, 2, 2), 138.810344827586), (datetime.datetime(2218, 10, 22, 17, 3, 2), 140.881355932203), (datetime.datetime(2218, 10, 22, 17, 4, 2), 139.810344827586), (datetime.datetime(2218, 10, 22, 17, 5, 2), 136.64406779661), (datetime.datetime(2218, 10, 22, 17, 6, 2), 136.338983050847), (datetime.datetime(2218, 10, 22, 17, 7, 2), 136.810344827586), (datetime.datetime(2218, 10, 22, 17, 8, 2), 139.881355932203), (datetime.datetime(2218, 10, 22, 17, 9, 2), 139.258620689655), (datetime.datetime(2218, 10, 22, 17, 10, 2), 138.661016949153), (datetime.datetime(2218, 10, 22, 17, 11, 2), 141.620689655172), (datetime.datetime(2218, 10, 22, 17, 12, 2), 148.915254237288), (datetime.datetime(2218, 10, 22, 17, 13, 2), 156.627118644068), (datetime.datetime(2218, 10, 22, 17, 14, 2), 158.672413793103), (datetime.datetime(2218, 10, 22, 17, 15, 2), 154.949152542373), (datetime.datetime(2218, 10, 22, 17, 16, 2), 157.172413793103), (datetime.datetime(2218, 10, 22, 17, 17, 2), 154.101694915254), (datetime.datetime(2218, 10, 22, 17, 18, 2), 150.152542372881), (datetime.datetime(2218, 10, 22, 17, 19, 2), 146.310344827586), (datetime.datetime(2218, 10, 22, 17, 20, 2), 142.813559322034), (datetime.datetime(2218, 10, 22, 17, 21, 2), 141.086206896552), (datetime.datetime(2218, 10, 22, 17, 22, 2), 141.813559322034), (datetime.datetime(2218, 10, 22, 17, 23, 2), 141.610169491525), (datetime.datetime(2218, 10, 22, 17, 24, 2), 140.055555555556), (datetime.datetime(2218, 10, 22, 17, 25, 2), 137.728813559322), (datetime.datetime(2218, 10, 22, 17, 26, 2), 140.5), (datetime.datetime(2218, 10, 22, 17, 27, 2), 140.983050847458), (datetime.datetime(2218, 10, 22, 17, 28, 2), 137.016949152542), (datetime.datetime(2218, 10, 22, 17, 29, 2), 135.48275862069), (datetime.datetime(2218, 10, 22, 17, 30, 2), 133.338983050847), (datetime.datetime(2218, 10, 22, 17, 31, 2), 131.137931034483), (datetime.datetime(2218, 10, 22, 17, 32, 2), 129.796610169492), (datetime.datetime(2218, 10, 22, 17, 33, 2), 129.271186440678), (datetime.datetime(2218, 10, 22, 17, 34, 2), 128.98275862069), (datetime.datetime(2218, 10, 22, 17, 35, 2), 130.0), (datetime.datetime(2218, 10, 22, 17, 36, 2), 133.603448275862), (datetime.datetime(2218, 10, 22, 17, 37, 2), 132.949152542373), (datetime.datetime(2218, 10, 22, 17, 38, 2), 133.220338983051), (datetime.datetime(2218, 10, 22, 17, 39, 2), 137.98275862069), (datetime.datetime(2218, 10, 22, 17, 40, 2), 137.474576271186), (datetime.datetime(2218, 10, 22, 17, 41, 2), 134.51724137931), (datetime.datetime(2218, 10, 22, 17, 42, 2), 130.898305084746), (datetime.datetime(2218, 10, 22, 17, 43, 2), 128.396551724138), (datetime.datetime(2218, 10, 22, 17, 44, 2), 127.457627118644), (datetime.datetime(2218, 10, 22, 17, 45, 2), 126.64406779661), (datetime.datetime(2218, 10, 22, 17, 46, 2), 126.948275862069), (datetime.datetime(2218, 10, 22, 17, 47, 2), 127.0), (datetime.datetime(2218, 10, 22, 17, 48, 2), 127.258620689655), (datetime.datetime(2218, 10, 22, 17, 49, 2), 127.06779661017), (datetime.datetime(2218, 10, 22, 17, 50, 2), 127.0), (datetime.datetime(2218, 10, 22, 17, 51, 2), 127.206896551724), (datetime.datetime(2218, 10, 22, 17, 52, 2), 126.610169491525), (datetime.datetime(2218, 10, 22, 17, 53, 2), 126.0), (datetime.datetime(2218, 10, 22, 17, 54, 2), 125.830508474576), (datetime.datetime(2218, 10, 22, 17, 55, 2), 126.0), (datetime.datetime(2218, 10, 22, 17, 56, 2), 125.0), (datetime.datetime(2218, 10, 22, 17, 57, 2), 125.0), (datetime.datetime(2218, 10, 22, 17, 58, 2), 126.0), (datetime.datetime(2218, 10, 22, 17, 59, 2), 125.0), (datetime.datetime(2218, 10, 22, 18, 0, 2), 125.0), (datetime.datetime(2218, 10, 22, 18, 1, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 2, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 3, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 4, 2), 123.0), (datetime.datetime(2218, 10, 22, 18, 5, 2), 123.0), (datetime.datetime(2218, 10, 22, 18, 6, 2), 123.0), (datetime.datetime(2218, 10, 22, 18, 7, 2), 123.0), (datetime.datetime(2218, 10, 22, 18, 8, 2), 123.0), (datetime.datetime(2218, 10, 22, 18, 9, 2), 123.0), (datetime.datetime(2218, 10, 22, 18, 10, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 11, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 12, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 13, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 14, 2), 125.0), (datetime.datetime(2218, 10, 22, 18, 15, 2), 125.0), (datetime.datetime(2218, 10, 22, 18, 16, 2), 125.0), (datetime.datetime(2218, 10, 22, 18, 17, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 18, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 19, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 20, 2), 124.0), (datetime.datetime(2218, 10, 22, 18, 21, 2), 124.0)]
systolic_bp = [(datetime.datetime(2218, 10, 22, 17, 0, 2), 127.0), (datetime.datetime(2218, 10, 22, 17, 1, 2), 127.0), (datetime.datetime(2218, 10, 22, 17, 2, 2), 127.0), (datetime.datetime(2218, 10, 22, 17, 5, 2), 100.0), (datetime.datetime(2218, 10, 22, 17, 6, 2), 100.0), (datetime.datetime(2218, 10, 22, 17, 10, 2), 120.0), (datetime.datetime(2218, 10, 22, 17, 11, 2), 120.0), (datetime.datetime(2218, 10, 22, 17, 14, 2), 129.0), (datetime.datetime(2218, 10, 22, 17, 15, 2), 123.0), (datetime.datetime(2218, 10, 22, 17, 16, 2), 123.0), (datetime.datetime(2218, 10, 22, 17, 20, 2), 119.0), (datetime.datetime(2218, 10, 22, 17, 21, 2), 119.0), (datetime.datetime(2218, 10, 22, 17, 25, 2), 138.0), (datetime.datetime(2218, 10, 22, 17, 26, 2), 138.0), (datetime.datetime(2218, 10, 22, 17, 30, 2), 125.0), (datetime.datetime(2218, 10, 22, 17, 31, 2), 125.0), (datetime.datetime(2218, 10, 22, 17, 35, 2), 118.0), (datetime.datetime(2218, 10, 22, 17, 36, 2), 118.0), (datetime.datetime(2218, 10, 22, 17, 40, 2), 137.0), (datetime.datetime(2218, 10, 22, 17, 41, 2), 137.0), (datetime.datetime(2218, 10, 22, 17, 45, 2), 111.0), (datetime.datetime(2218, 10, 22, 17, 46, 2), 111.0), (datetime.datetime(2218, 10, 22, 17, 50, 2), 115.0), (datetime.datetime(2218, 10, 22, 17, 51, 2), 115.0), (datetime.datetime(2218, 10, 22, 17, 55, 2), 109.0), (datetime.datetime(2218, 10, 22, 18, 0, 2), 111.0), (datetime.datetime(2218, 10, 22, 18, 5, 2), 108.0), (datetime.datetime(2218, 10, 22, 18, 10, 2), 105.0), (datetime.datetime(2218, 10, 22, 18, 15, 2), 114.0), (datetime.datetime(2218, 10, 22, 18, 20, 2), 108.0), (datetime.datetime(2218, 10, 22, 18, 21, 2), 107.0)]
diastolic_bp = [(datetime.datetime(2218, 10, 22, 17, 0, 2), 117.0), (datetime.datetime(2218, 10, 22, 17, 1, 2), 117.0), (datetime.datetime(2218, 10, 22, 17, 2, 2), 117.0), (datetime.datetime(2218, 10, 22, 17, 5, 2), 72.0), (datetime.datetime(2218, 10, 22, 17, 6, 2), 72.0), (datetime.datetime(2218, 10, 22, 17, 10, 2), 77.0), (datetime.datetime(2218, 10, 22, 17, 11, 2), 77.0), (datetime.datetime(2218, 10, 22, 17, 15, 2), 75.0), (datetime.datetime(2218, 10, 22, 17, 16, 2), 75.0), (datetime.datetime(2218, 10, 22, 17, 20, 2), 78.0), (datetime.datetime(2218, 10, 22, 17, 21, 2), 78.0), (datetime.datetime(2218, 10, 22, 17, 25, 2), 92.0), (datetime.datetime(2218, 10, 22, 17, 26, 2), 92.0), (datetime.datetime(2218, 10, 22, 17, 30, 2), 65.0), (datetime.datetime(2218, 10, 22, 17, 31, 2), 65.0), (datetime.datetime(2218, 10, 22, 17, 35, 2), 69.0), (datetime.datetime(2218, 10, 22, 17, 36, 2), 69.0), (datetime.datetime(2218, 10, 22, 17, 40, 2), 81.0), (datetime.datetime(2218, 10, 22, 17, 41, 2), 81.0), (datetime.datetime(2218, 10, 22, 17, 45, 2), 62.0), (datetime.datetime(2218, 10, 22, 17, 46, 2), 62.0), (datetime.datetime(2218, 10, 22, 17, 50, 2), 63.0), (datetime.datetime(2218, 10, 22, 17, 51, 2), 63.0), (datetime.datetime(2218, 10, 22, 17, 55, 2), 58.0), (datetime.datetime(2218, 10, 22, 18, 0, 2), 60.0), (datetime.datetime(2218, 10, 22, 18, 5, 2), 64.0), (datetime.datetime(2218, 10, 22, 18, 10, 2), 61.0), (datetime.datetime(2218, 10, 22, 18, 15, 2), 62.0), (datetime.datetime(2218, 10, 22, 18, 20, 2), 61.0), (datetime.datetime(2218, 10, 22, 18, 21, 2), 58.0)]
spo2 = [(datetime.datetime(2218, 10, 22, 16, 57, 2), 92.7659574468085), (datetime.datetime(2218, 10, 22, 16, 58, 2), 91.8305084745763), (datetime.datetime(2218, 10, 22, 16, 59, 2), 92.0517241379311), (datetime.datetime(2218, 10, 22, 17, 0, 2), 92.4166666666667), (datetime.datetime(2218, 10, 22, 17, 1, 2), 84.125), (datetime.datetime(2218, 10, 22, 17, 2, 2), 87.0), (datetime.datetime(2218, 10, 22, 17, 3, 2), 97.7457627118644), (datetime.datetime(2218, 10, 22, 17, 4, 2), 97.0689655172414), (datetime.datetime(2218, 10, 22, 17, 5, 2), 96.406779661017), (datetime.datetime(2218, 10, 22, 17, 6, 2), 98.1186440677966), (datetime.datetime(2218, 10, 22, 17, 7, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 8, 2), 99.1864406779661), (datetime.datetime(2218, 10, 22, 17, 9, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 10, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 11, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 12, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 13, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 14, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 15, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 16, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 17, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 18, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 19, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 20, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 23, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 24, 2), 98.9722222222223), (datetime.datetime(2218, 10, 22, 17, 25, 2), 98.2881355932203), (datetime.datetime(2218, 10, 22, 17, 26, 2), 98.9310344827586), (datetime.datetime(2218, 10, 22, 17, 27, 2), 99.0508474576271), (datetime.datetime(2218, 10, 22, 17, 28, 2), 99.8305084745763), (datetime.datetime(2218, 10, 22, 17, 29, 2), 99.9655172413793), (datetime.datetime(2218, 10, 22, 17, 30, 2), 98.1525423728814), (datetime.datetime(2218, 10, 22, 17, 31, 2), 97.8103448275862), (datetime.datetime(2218, 10, 22, 17, 32, 2), 98.406779661017), (datetime.datetime(2218, 10, 22, 17, 33, 2), 99.1694915254237), (datetime.datetime(2218, 10, 22, 17, 34, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 35, 2), 99.271186440678), (datetime.datetime(2218, 10, 22, 17, 36, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 37, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 38, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 39, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 40, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 41, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 42, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 43, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 44, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 45, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 46, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 47, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 48, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 49, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 50, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 51, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 52, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 53, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 54, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 55, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 56, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 57, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 58, 2), 99.0), (datetime.datetime(2218, 10, 22, 17, 59, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 0, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 1, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 2, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 3, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 4, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 5, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 6, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 7, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 8, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 9, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 10, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 11, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 12, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 13, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 14, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 15, 2), 99.0), (datetime.datetime(2218, 10, 22, 18, 16, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 17, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 18, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 19, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 20, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 21, 2), 98.0)]
respiratory_rate = [(datetime.datetime(2218, 10, 22, 16, 58, 2), 27.0), (datetime.datetime(2218, 10, 22, 16, 59, 2), 21.5490196078431), (datetime.datetime(2218, 10, 22, 17, 0, 2), 19.6440677966102), (datetime.datetime(2218, 10, 22, 17, 1, 2), 29.2542372881356), (datetime.datetime(2218, 10, 22, 17, 2, 2), 20.3275862068966), (datetime.datetime(2218, 10, 22, 17, 3, 2), 20.5423728813559), (datetime.datetime(2218, 10, 22, 17, 4, 2), 17.7241379310345), (datetime.datetime(2218, 10, 22, 17, 5, 2), 18.7796610169492), (datetime.datetime(2218, 10, 22, 17, 6, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 7, 2), 18.1206896551724), (datetime.datetime(2218, 10, 22, 17, 8, 2), 26.6610169491526), (datetime.datetime(2218, 10, 22, 17, 9, 2), 17.1379310344828), (datetime.datetime(2218, 10, 22, 17, 10, 2), 18.8135593220339), (datetime.datetime(2218, 10, 22, 17, 11, 2), 12.5945945945946), (datetime.datetime(2218, 10, 22, 17, 12, 2), 13.6), (datetime.datetime(2218, 10, 22, 17, 13, 2), 22.6949152542373), (datetime.datetime(2218, 10, 22, 17, 14, 2), 26.2931034482759), (datetime.datetime(2218, 10, 22, 17, 15, 2), 27.0677966101695), (datetime.datetime(2218, 10, 22, 17, 16, 2), 22.1551724137931), (datetime.datetime(2218, 10, 22, 17, 17, 2), 19.1694915254237), (datetime.datetime(2218, 10, 22, 17, 18, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 19, 2), 21.2413793103448), (datetime.datetime(2218, 10, 22, 17, 20, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 21, 2), 19.2586206896552), (datetime.datetime(2218, 10, 22, 17, 22, 2), 19.8305084745763), (datetime.datetime(2218, 10, 22, 17, 23, 2), 19.2203389830508), (datetime.datetime(2218, 10, 22, 17, 24, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 25, 2), 20.0338983050848), (datetime.datetime(2218, 10, 22, 17, 26, 2), 16.6206896551724), (datetime.datetime(2218, 10, 22, 17, 27, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 28, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 29, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 30, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 31, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 32, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 33, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 34, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 35, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 36, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 37, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 38, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 39, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 40, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 41, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 42, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 43, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 44, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 45, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 46, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 47, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 48, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 49, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 50, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 51, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 52, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 53, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 54, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 55, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 56, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 57, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 58, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 59, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 0, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 1, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 2, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 3, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 4, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 5, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 6, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 7, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 8, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 9, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 10, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 11, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 12, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 13, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 14, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 15, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 16, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 17, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 18, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 19, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 20, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 21, 2), 20.0)]
temperature = [(datetime.datetime(2218, 10, 22, 17, 2, 2), 36.5), (datetime.datetime(2218, 10, 22, 17, 35, 2), 36.22222222222222), (datetime.datetime(2218, 10, 22, 17, 40, 2), 36.0), (datetime.datetime(2218, 10, 22, 17, 45, 2), 35.888888888888886), (datetime.datetime(2218, 10, 22, 17, 50, 2), 35.888888888888886), (datetime.datetime(2218, 10, 22, 17, 55, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 17, 56, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 17, 57, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 17, 58, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 17, 59, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 18, 0, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 18, 1, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 18, 2, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 18, 3, 2), 35.77777777777778), (datetime.datetime(2218, 10, 22, 18, 4, 2), 35.72222222222222), (datetime.datetime(2218, 10, 22, 18, 5, 2), 35.72222222222222), (datetime.datetime(2218, 10, 22, 18, 6, 2), 35.72222222222222), (datetime.datetime(2218, 10, 22, 18, 7, 2), 35.72222222222222), (datetime.datetime(2218, 10, 22, 18, 8, 2), 35.72222222222222), (datetime.datetime(2218, 10, 22, 18, 9, 2), 35.72222222222222), (datetime.datetime(2218, 10, 22, 18, 10, 2), 35.72222222222222), (datetime.datetime(2218, 10, 22, 18, 11, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 12, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 13, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 14, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 15, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 16, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 17, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 18, 2), 35.611111111111114), (datetime.datetime(2218, 10, 22, 18, 19, 2), 35.5), (datetime.datetime(2218, 10, 22, 18, 20, 2), 35.5), (datetime.datetime(2218, 10, 22, 18, 21, 2), 35.5)]
# Previous Results
shock_index = 1.048
shock_index_interpretation = 'HIGH (1.05), significantly above normal (0.5-0.7). Suggests decompensated shock, immediate intervention needed.'
map_value = 120.3
map_interpretation = 'Elevated (120 mmHg), above reference range (65-100 mmHg). Consider hypertensive state.'
pulse_pressure = 10.0
qsofa_score = 2
qsofa_interpretation = 'High Risk (Score 2/3). Criteria met: SBP=100, RR=27. Associated with poor outcomes in sepsis.'
sirs = 2
spo2_trend = {'first': np.float64(92.8), 'last': np.float64(98.0), 'min': 84.1, 'mean': 98.2, 'slope': np.float64(0.0429), 'r_squared': np.float64(0.17), 'trend_pct': np.float64(3.65)}
hr_volatility = {'dispersion_ms': 29.56, 'rmssd_ms': 6.54, 'hr_std_bpm': 9.18, 'hr_range_bpm': 35.7, 'n_samples': 84, 'data_density': 'moderate'}
triage_vital_panel = 'Attached'

# --- Generated Code Starts Here ---
def _to_arrays(ts_list):
    if ts_list is None or len(ts_list) == 0:
        return (np.array([]), np.array([]))
    t = np.array([x[0] for x in ts_list], dtype=object)
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _t_to_minutes(t, t0):
    return np.array([(ti - t0).total_seconds() / 60.0 for ti in t], dtype=float)

def _interp_within_range(t_src_min, v_src, t_grid_min):
    if len(t_src_min) < 2:
        return np.full_like(t_grid_min, np.nan, dtype=float)
    order = np.argsort(t_src_min)
    t_src = t_src_min[order]
    v_src = v_src[order]
    y = np.interp(t_grid_min, t_src, v_src)
    y[(t_grid_min < t_src[0]) | (t_grid_min > t_src[-1])] = np.nan
    return y

def _lagged_corr(x, y, lag_steps):
    if lag_steps == 0:
        xs, ys = (x, y)
    elif lag_steps > 0:
        xs, ys = (x[:-lag_steps], y[lag_steps:])
    else:
        k = -lag_steps
        xs, ys = (x[k:], y[:-k])
    m = np.isfinite(xs) & np.isfinite(ys)
    n = int(np.sum(m))
    if n < 8:
        return (np.nan, n, np.nan)
    xs = xs[m]
    ys = ys[m]
    sx = np.std(xs, ddof=1)
    sy = np.std(ys, ddof=1)
    if sx == 0 or sy == 0:
        return (np.nan, n, np.nan)
    r = float(np.corrcoef(xs, ys)[0, 1])
    df = n - 2
    if df <= 0 or not np.isfinite(r) or abs(r) >= 1:
        p = np.nan
    else:
        tstat = r * np.sqrt(df / (1.0 - r * r))
        p = float(2.0 * stats.t.sf(np.abs(tstat), df))
    return (r, n, p)
t_spo2, v_spo2 = _to_arrays(spo2)
t_rr, v_rr = _to_arrays(respiratory_rate)
t_hr, v_hr = _to_arrays(heart_rate)
if len(t_spo2) < 2 or (len(t_rr) < 2 and len(t_hr) < 2):
    result = {'error': 'Insufficient data for lagged cross-correlation. Need >=2 samples for SpO2 and >=2 for RR and/or HR.', 'spo2_n': int(len(t_spo2)), 'rr_n': int(len(t_rr)), 'hr_n': int(len(t_hr))}
    interpretation = 'Unable to compute lagged SpO2 cross-correlations due to insufficient time-series samples.'
else:
    t0 = min([t_spo2[0]] + ([t_rr[0]] if len(t_rr) else []) + ([t_hr[0]] if len(t_hr) else []))
    spo2_min = _t_to_minutes(t_spo2, t0)
    rr_min = _t_to_minutes(t_rr, t0) if len(t_rr) else np.array([])
    hr_min = _t_to_minutes(t_hr, t0) if len(t_hr) else np.array([])
    starts = [np.nanmin(spo2_min)]
    ends = [np.nanmax(spo2_min)]
    if len(rr_min):
        starts.append(np.nanmin(rr_min))
        ends.append(np.nanmax(rr_min))
    if len(hr_min):
        starts.append(np.nanmin(hr_min))
        ends.append(np.nanmax(hr_min))
    t_start = float(np.nanmax(starts))
    t_end = float(np.nanmin(ends))
    dt_min = 1.0 / 6.0
    if not np.isfinite(t_start) or not np.isfinite(t_end) or t_end - t_start < 20.0 + 2.0:
        result = {'error': 'Insufficient overlapping time window to evaluate ±10 minute lags robustly.', 'overlap_minutes': float(t_end - t_start) if np.isfinite(t_end - t_start) else np.nan, 'required_minutes_min': 22.0}
        interpretation = 'Overlap between SpO2 and RR/HR is too short to assess ±10 minute lagged relationships.'
    else:
        t_grid = np.arange(t_start, t_end + 1e-09, dt_min, dtype=float)
        spo2_g = _interp_within_range(spo2_min, v_spo2, t_grid)
        rr_g = _interp_within_range(rr_min, v_rr, t_grid) if len(rr_min) else np.full_like(t_grid, np.nan, dtype=float)
        hr_g = _interp_within_range(hr_min, v_hr, t_grid) if len(hr_min) else np.full_like(t_grid, np.nan, dtype=float)
        max_lag_min = 10.0
        max_lag_steps = int(round(max_lag_min / dt_min))
        lag_steps = np.arange(-max_lag_steps, max_lag_steps + 1, dtype=int)
        lag_minutes = lag_steps.astype(float) * dt_min
        rr_rows = []
        hr_rows = []
        for ls, lm in zip(lag_steps, lag_minutes):
            if len(rr_min):
                r, n, p = _lagged_corr(spo2_g, rr_g, int(ls))
                rr_rows.append((float(lm), float(r) if np.isfinite(r) else np.nan, int(n), float(p) if np.isfinite(p) else np.nan))
            if len(hr_min):
                r, n, p = _lagged_corr(spo2_g, hr_g, int(ls))
                hr_rows.append((float(lm), float(r) if np.isfinite(r) else np.nan, int(n), float(p) if np.isfinite(p) else np.nan))

        def _best(rows):
            if not rows:
                return None
            lags = np.array([r[0] for r in rows], dtype=float)
            corr = np.array([r[1] for r in rows], dtype=float)
            n = np.array([r[2] for r in rows], dtype=int)
            p = np.array([r[3] for r in rows], dtype=float)
            m = np.isfinite(corr)
            if not np.any(m):
                return {'best_lag_min': np.nan, 'best_r': np.nan, 'n': int(np.nanmax(n) if len(n) else 0), 'p_value': np.nan}
            idx = int(np.nanargmax(np.abs(corr[m])))
            sel = np.where(m)[0][idx]
            return {'best_lag_min': float(lags[sel]), 'best_r': float(corr[sel]), 'n': int(n[sel]), 'p_value': float(p[sel]) if np.isfinite(p[sel]) else np.nan}
        best_rr = _best(rr_rows) if len(rr_min) else None
        best_hr = _best(hr_rows) if len(hr_min) else None
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))
        if len(rr_rows):
            ax.plot([x[0] for x in rr_rows], [x[1] for x in rr_rows], label='SpO2 vs RR', linewidth=2)
        if len(hr_rows):
            ax.plot([x[0] for x in hr_rows], [x[1] for x in hr_rows], label='SpO2 vs HR', linewidth=2)
        ax.axvline(0, color='k', linewidth=1, alpha=0.6)
        ax.axhline(0, color='k', linewidth=1, alpha=0.2)
        ax.set_xlabel('Lag (minutes): positive means RR/HR occurs AFTER SpO2')
        ax.set_ylabel('Pearson r')
        ax.set_title('Lagged cross-correlation with SpO2 (±10 min)\n(interpolated onto common 10-second grid; no extrapolation)')
        ax.set_xlim(-max_lag_min, max_lag_min)
        ax.legend(loc='best')
        ax.grid(True, alpha=0.25)
        save_plot('lagged_cross_correlation_spo2_rr_hr.png', fig=fig)
        if len(rr_min):
            spo2_at_rr = _interp_within_range(spo2_min, v_spo2, rr_min)
            m = np.isfinite(spo2_at_rr) & np.isfinite(v_rr)
            x_rr = v_rr[m]
            y_spo2 = spo2_at_rr[m]
            c_time = rr_min[m]
        else:
            x_rr = np.array([])
            y_spo2 = np.array([])
            c_time = np.array([])
        fig2, ax2 = plt.subplots(1, 1, figsize=(8, 6))
        if len(x_rr) >= 2:
            sc = ax2.scatter(x_rr, y_spo2, c=c_time, cmap='viridis', s=35, alpha=0.85, edgecolors='none')
            cb = plt.colorbar(sc, ax=ax2)
            cb.set_label('Time (minutes since start)')
        else:
            ax2.text(0.5, 0.5, 'Insufficient paired SpO2-RR points for scatter', ha='center', va='center', transform=ax2.transAxes)
        ax2.set_xlabel('Respiratory Rate (breaths/min)')
        ax2.set_ylabel('SpO2 (%)')
        ax2.set_title('SpO2 vs RR (colored by time)\n(patterns: hypoventilation/obstruction vs V/Q mismatch vs artifact)')
        ax2.grid(True, alpha=0.25)
        save_plot('spo2_vs_rr_time_scatter.png', fig=fig2)
        result = {'settings': {'max_lag_minutes': float(max_lag_min), 'grid_dt_minutes': float(dt_min), 'grid_dt_seconds': float(dt_min * 60.0), 'overlap_window_minutes': float(t_end - t_start)}, 'spo2_rr': {'lag_corr_table': [{'lag_min': a, 'r': b, 'n': c, 'p_value': d} for a, b, c, d in rr_rows], 'best': best_rr} if len(rr_rows) else {'lag_corr_table': [], 'best': None}, 'spo2_hr': {'lag_corr_table': [{'lag_min': a, 'r': b, 'n': c, 'p_value': d} for a, b, c, d in hr_rows], 'best': best_hr} if len(hr_rows) else {'lag_corr_table': [], 'best': None}, 'scatter_spo2_vs_rr': {'n_pairs': int(len(x_rr)), 'rr_min': float(np.nanmin(x_rr)) if len(x_rr) else np.nan, 'rr_max': float(np.nanmax(x_rr)) if len(x_rr) else np.nan, 'spo2_min': float(np.nanmin(y_spo2)) if len(y_spo2) else np.nan, 'spo2_max': float(np.nanmax(y_spo2)) if len(y_spo2) else np.nan}, 'plots': ['lagged_cross_correlation_spo2_rr_hr.png', 'spo2_vs_rr_time_scatter.png']}

        def _interp_sentence(best, label):
            if best is None or not np.isfinite(best.get('best_r', np.nan)) or (not np.isfinite(best.get('best_lag_min', np.nan))):
                return f'{label}: lagged association could not be reliably estimated from available overlap.'
            r = best['best_r']
            lag = best['best_lag_min']
            n = best.get('n', None)
            p = best.get('p_value', np.nan)
            direction = 'inverse' if r < 0 else 'positive'
            ptxt = f', p={p:.3g}' if np.isfinite(p) else ''
            ntxt = f' (n={n})' if isinstance(n, (int, np.integer)) else ''
            return f'{label}: strongest {direction} correlation at lag {lag:+.2f} min with r={r:.3f}{ptxt}{ntxt}.'
        parts = []
        if len(rr_rows):
            parts.append(_interp_sentence(best_rr, 'SpO2↔RR'))
        if len(hr_rows):
            parts.append(_interp_sentence(best_hr, 'SpO2↔HR'))
        parts.append('SpO2 vs RR time-colored scatter saved to help distinguish clustered outliers (artifact) from sustained low-SpO2 patterns across RR (possible V/Q mismatch) or low RR with desaturation (possible hypoventilation/obstruction).')
        interpretation = ' '.join(parts)

plt.close()