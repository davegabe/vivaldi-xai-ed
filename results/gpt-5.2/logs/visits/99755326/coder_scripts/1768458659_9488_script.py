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
create_hr_tachogram_with_10‑min_rolling_coefficient_of_variation_and_hr_density/histogram;_report_%_time_in_hr_bins_120–140_and_140–160_to_assess_narrowband_“locked-in”_rhythm_vs_wandering_sinus_tachy. = None
detect_spo2_desaturation_events_(<92%_for_≥30s,_merge_gaps_<60s);_for_each_event,_generate_event‑locked_curves_of_spo2,_rr,_and_hr_from_−10_to_+10_min_and_classify_rr_response_(drop/rise/none). = None
compute_lagged_cross-correlation_between_spo2_and_rr/hr_(±10_min_lags)_plus_a_spo2_vs_rr_scatter_colored_by_time_to_distinguish_artifact_vs_hypoventilation/obstruction_vs_v/q_mismatch_patterns. = None
create_hr_vs_sbp_scatter_colored_by_time_with_an_overlaid_trajectory_line_(connect_points_in_time_order)_to_detect_looping/branching_patterns_suggestive_of_paroxysmal_dysrhythmia_or_evolving_shock. = None
plot_synchronized_time_series_of_hr,_sbp,_dbp_with_derived_shock_index_(hr/sbp)_and_pulse_pressure_(sbp−dbp),_including_5–10_min_rolling_median_for_shock_index_and_pulse_pressure. = None
for_each_detected_spo2<92%_event,_plot_event-locked_traces_(−10_to_+10_min)_of_spo2_and_rr_variability_(rolling_variance_or_rmssd)_to_screen_for_patterned_respiratory_instability_despite_normal/high_rr. = None

# --- Generated Code Starts Here ---
def _to_arrays(ts):
    if ts is None or len(ts) == 0:
        return (np.array([]), np.array([]))
    t = np.array([x[0] for x in ts], dtype=object)
    v = np.array([float(x[1]) for x in ts], dtype=float)
    return (t, v)

def _rolling_window_stats(times, values, window_minutes=2.0):
    n = len(values)
    if n == 0:
        return (np.array([]), np.array([]), np.array([]), np.array([]), np.array([]))
    med = np.full(n, np.nan, dtype=float)
    q1 = np.full(n, np.nan, dtype=float)
    q3 = np.full(n, np.nan, dtype=float)
    iqr = np.full(n, np.nan, dtype=float)
    mad = np.full(n, np.nan, dtype=float)
    for i in range(n):
        ti = times[i]
        half = window_minutes / 2.0
        dt_min = np.array([abs((tj - ti).total_seconds()) / 60.0 for tj in times], dtype=float)
        mask = dt_min <= half
        w = values[mask]
        if w.size >= 3:
            m = np.median(w)
            med[i] = m
            q1i = np.percentile(w, 25)
            q3i = np.percentile(w, 75)
            q1[i] = q1i
            q3[i] = q3i
            iqr[i] = q3i - q1i
            mad[i] = np.median(np.abs(w - m))
        elif w.size > 0:
            m = np.median(w)
            med[i] = m
            q1[i] = np.nan
            q3[i] = np.nan
            iqr[i] = np.nan
            mad[i] = np.median(np.abs(w - m))
    return (med, q1, q3, iqr, mad)

def _time_weighted_pct_within(times, values, center, tol=3.0):
    """
    Percent time (duration-weighted) where |value - center| <= tol.
    Uses segment weighting between midpoints; robust to irregular sampling.
    Returns (pct, total_minutes, within_minutes, mask_segments)
    """
    n = len(values)
    if n == 0:
        return (np.nan, 0.0, 0.0, np.array([], dtype=bool))
    if n == 1:
        within = abs(values[0] - center[0]) <= tol if np.isfinite(center[0]) else False
        return (100.0 if within else 0.0, 0.0, 0.0, np.array([], dtype=bool))
    dt = np.array([(times[i + 1] - times[i]).total_seconds() / 60.0 for i in range(n - 1)], dtype=float)
    dt = np.where(dt > 0, dt, 0.0)
    c0 = center[:-1]
    c1 = center[1:]
    v0 = values[:-1]
    v1 = values[1:]
    valid = np.isfinite(c0) & np.isfinite(c1)
    if not np.any(valid):
        return (np.nan, 0.0, 0.0, np.array([], dtype=bool))
    cseg = 0.5 * (c0 + c1)
    vseg = 0.5 * (v0 + v1)
    within = np.abs(vseg - cseg) <= tol
    denom = float(np.sum(dt[valid]))
    numer = float(np.sum(dt[valid & within]))
    pct = numer / denom * 100.0 if denom > 0 else np.nan
    return (pct, denom, numer, valid & within)
t_hr, hr = _to_arrays(heart_rate)
window_min = 2.0
hr_med, hr_q1, hr_q3, hr_iqr, hr_mad = _rolling_window_stats(t_hr, hr, window_minutes=window_min)
locking_tol_bpm = 3.0
locking_index_pct, denom_min, within_min, _ = _time_weighted_pct_within(t_hr, hr, hr_med, tol=locking_tol_bpm)
fig, ax = plt.subplots(1, 1, figsize=(12, 5))
ax.plot(t_hr, hr, color='black', linewidth=1.0, alpha=0.7, label='HR (bpm)')
ax.plot(t_hr, hr_med, color='#1f77b4', linewidth=2.0, label=f'Rolling median ({window_min:.0f} min)')
if np.any(np.isfinite(hr_q1)) and np.any(np.isfinite(hr_q3)):
    ax.fill_between(t_hr, hr_q1, hr_q3, color='#1f77b4', alpha=0.2, label='Rolling IQR (25–75%)')
else:
    mad_scale = 2.9652
    lower = hr_med - mad_scale * hr_mad
    upper = hr_med + mad_scale * hr_mad
    ax.fill_between(t_hr, lower, upper, color='#1f77b4', alpha=0.2, label='Rolling MAD band (~IQR)')
ax.set_title(f'Heart Rate Tachogram with Rolling Variability Band\nLocking index: {locking_index_pct:.1f}% time within ±{locking_tol_bpm:.0f} bpm of local median')
ax.set_xlabel('Time')
ax.set_ylabel('Heart rate (bpm)')
ax.grid(True, alpha=0.25)
ax.legend(loc='best', frameon=True)
save_plot('hr_tachogram_rolling_median_iqr_mad_locking_index.png', fig=fig)
result = {'hr_n_samples': int(len(hr)), 'rolling_window_minutes': float(window_min), 'locking_tolerance_bpm': float(locking_tol_bpm), 'locking_index_pct_time': float(locking_index_pct) if np.isfinite(locking_index_pct) else None, 'locking_index_denominator_minutes': float(denom_min), 'locking_index_within_minutes': float(within_min), 'hr_local_median_summary_bpm': {'median_of_local_medians': float(np.nanmedian(hr_med)) if hr_med.size else None, 'min_local_median': float(np.nanmin(hr_med)) if np.any(np.isfinite(hr_med)) else None, 'max_local_median': float(np.nanmax(hr_med)) if np.any(np.isfinite(hr_med)) else None}, 'hr_local_iqr_summary_bpm': {'median_local_iqr': float(np.nanmedian(hr_iqr)) if np.any(np.isfinite(hr_iqr)) else None, 'max_local_iqr': float(np.nanmax(hr_iqr)) if np.any(np.isfinite(hr_iqr)) else None}, 'plot_file': 'hr_tachogram_rolling_median_iqr_mad_locking_index.png'}
if result['locking_index_pct_time'] is None:
    interpretation = 'Unable to compute HR locking index due to insufficient valid local-median coverage in the rolling window.'
else:
    li = result['locking_index_pct_time']
    if li >= 80:
        cls = 'highly locked-in'
    elif li >= 60:
        cls = 'moderately locked-in'
    else:
        cls = 'not locked-in (variable)'
    interpretation = f'HR locking index is {li:.1f}% (time-weighted) within ±{locking_tol_bpm:.0f} bpm of the 2-min local median, indicating {cls} tachycardia (less variability implies more fixed-rate tachycardia).'

plt.close()