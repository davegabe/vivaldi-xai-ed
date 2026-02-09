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
def _to_arrays(ts_list):
    t = [x[0] for x in ts_list]
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _minutes_between(t1, t2):
    return (t2 - t1).total_seconds() / 60.0

def _value_at_or_before(t_list, v_arr, t_query):
    lo, hi = (0, len(t_list) - 1)
    if hi < 0 or t_list[0] > t_query:
        return np.nan
    if t_list[hi] <= t_query:
        return float(v_arr[hi])
    while lo <= hi:
        mid = (lo + hi) // 2
        if t_list[mid] <= t_query:
            lo = mid + 1
        else:
            hi = mid - 1
    idx = hi
    return float(v_arr[idx]) if idx >= 0 else np.nan

def _event_metrics(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, threshold, min_duration_s=30.0, merge_gap_s=60.0):
    events = []
    n = len(spo2_t)
    if n < 2:
        return events
    merge_gap_min = merge_gap_s / 60.0
    min_dur_min = min_duration_s / 60.0
    in_event = False
    start_idx = None
    last_below_idx = None

    def close_event(s_idx, e_idx):
        t_start = spo2_t[s_idx]
        t_end = spo2_t[e_idx]
        duration_min = max(0.0, _minutes_between(t_start, t_end))
        if duration_min < min_dur_min:
            return
        seg_v = spo2_v[s_idx:e_idx + 1]
        min_spo2 = float(np.nanmin(seg_v)) if len(seg_v) else np.nan
        depth = float(threshold - min_spo2) if np.isfinite(min_spo2) else np.nan
        baseline_window_start = t_start - (t_start - t_start)
        t_minus5 = t_start + (spo2_t[0] - spo2_t[0])
        idxs_baseline = []
        for k in range(n):
            dt = _minutes_between(spo2_t[k], t_start)
            if 1.0 <= dt <= 5.0:
                idxs_baseline.append(k)
        if idxs_baseline:
            spo2_baseline = float(np.nanmean(spo2_v[idxs_baseline]))
        else:
            spo2_baseline = _value_at_or_before(spo2_t, spo2_v, t_start)
        if not np.isfinite(spo2_baseline):
            spo2_baseline = np.nan
        spo2_event_mean = float(np.nanmean(seg_v)) if len(seg_v) else np.nan

        def baseline_mean_for_stream(stream_t, stream_v):
            vals = []
            for k in idxs_baseline:
                val = _value_at_or_before(stream_t, stream_v, spo2_t[k])
                if np.isfinite(val):
                    vals.append(val)
            if vals:
                return float(np.mean(vals))
            return _value_at_or_before(stream_t, stream_v, t_start)
        hr_baseline = baseline_mean_for_stream(hr_t, hr_v)
        rr_baseline = baseline_mean_for_stream(rr_t, rr_v)
        hr_vals = []
        rr_vals = []
        for k in range(s_idx, e_idx + 1):
            hv = _value_at_or_before(hr_t, hr_v, spo2_t[k])
            rv = _value_at_or_before(rr_t, rr_v, spo2_t[k])
            if np.isfinite(hv):
                hr_vals.append(hv)
            if np.isfinite(rv):
                rr_vals.append(rv)
        hr_event_mean = float(np.mean(hr_vals)) if hr_vals else np.nan
        rr_event_mean = float(np.mean(rr_vals)) if rr_vals else np.nan
        d_hr = float(hr_event_mean - hr_baseline) if np.isfinite(hr_event_mean) and np.isfinite(hr_baseline) else np.nan
        d_rr = float(rr_event_mean - rr_baseline) if np.isfinite(rr_event_mean) and np.isfinite(rr_baseline) else np.nan
        events.append({'threshold': float(threshold), 'start_time': t_start, 'end_time': t_end, 'duration_min': float(duration_min), 'min_spo2': float(min_spo2) if np.isfinite(min_spo2) else np.nan, 'depth_pct_points': float(depth) if np.isfinite(depth) else np.nan, 'spo2_baseline': float(spo2_baseline) if np.isfinite(spo2_baseline) else np.nan, 'spo2_event_mean': float(spo2_event_mean) if np.isfinite(spo2_event_mean) else np.nan, 'hr_baseline_bpm': float(hr_baseline) if np.isfinite(hr_baseline) else np.nan, 'hr_event_mean_bpm': float(hr_event_mean) if np.isfinite(hr_event_mean) else np.nan, 'd_hr_bpm': float(d_hr) if np.isfinite(d_hr) else np.nan, 'rr_baseline_brpm': float(rr_baseline) if np.isfinite(rr_baseline) else np.nan, 'rr_event_mean_brpm': float(rr_event_mean) if np.isfinite(rr_event_mean) else np.nan, 'd_rr_brpm': float(d_rr) if np.isfinite(d_rr) else np.nan})
    for i in range(n):
        is_below = np.isfinite(spo2_v[i]) and spo2_v[i] < threshold
        if not in_event:
            if is_below:
                in_event = True
                start_idx = i
                last_below_idx = i
        elif is_below:
            last_below_idx = i
        else:
            gap_min = _minutes_between(spo2_t[last_below_idx], spo2_t[i])
            if gap_min <= merge_gap_min:
                continue
            close_event(start_idx, last_below_idx)
            in_event = False
            start_idx = None
            last_below_idx = None
    if in_event and start_idx is not None and (last_below_idx is not None):
        close_event(start_idx, last_below_idx)
    return events

def _lagged_coupling(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, lag_min, baseline_minutes=5.0):
    d_spo2 = []
    d_hr = []
    d_rr = []
    t_used = []
    for i in range(len(spo2_t)):
        t0 = spo2_t[i]
        target_idx = None
        best_time = None
        for j in range(i - 1, -1, -1):
            dt = _minutes_between(spo2_t[j], t0)
            if dt >= baseline_minutes:
                target_idx = j
                best_time = spo2_t[j]
                break
        if target_idx is None:
            continue
        spo2_base = spo2_v[target_idx]
        if not np.isfinite(spo2_base) or not np.isfinite(spo2_v[i]):
            continue
        desired_offset = -lag_min
        closest_k = None
        closest_abs = None
        for k in range(max(0, i - 200), min(len(spo2_t), i + 200)):
            off = _minutes_between(spo2_t[k], t0)
            absdiff = abs(off - desired_offset)
            if closest_abs is None or absdiff < closest_abs:
                closest_abs = absdiff
                closest_k = k
        if closest_k is None or closest_abs is None or closest_abs > 2.5:
            t_query = t0
        else:
            t_query = spo2_t[closest_k]
        hr_now = _value_at_or_before(hr_t, hr_v, t_query)
        rr_now = _value_at_or_before(rr_t, rr_v, t_query)
        hr_base = _value_at_or_before(hr_t, hr_v, best_time)
        rr_base = _value_at_or_before(rr_t, rr_v, best_time)
        if not (np.isfinite(hr_now) and np.isfinite(hr_base) and np.isfinite(rr_now) and np.isfinite(rr_base)):
            continue
        d_spo2.append(float(spo2_v[i] - spo2_base))
        d_hr.append(float(hr_now - hr_base))
        d_rr.append(float(rr_now - rr_base))
        t_used.append(t0)
    d_spo2 = np.array(d_spo2, dtype=float)
    d_hr = np.array(d_hr, dtype=float)
    d_rr = np.array(d_rr, dtype=float)

    def corr(x, y):
        m = np.isfinite(x) & np.isfinite(y)
        if m.sum() < 5:
            return {'r': np.nan, 'p': np.nan, 'n': int(m.sum())}
        r, p = stats.pearsonr(x[m], y[m])
        return {'r': float(r), 'p': float(p), 'n': int(m.sum())}
    return {'lag_min': float(lag_min), 'n_pairs': int(len(d_spo2)), 'corr_dHR_dSpO2': corr(d_hr, d_spo2), 'corr_dRR_dSpO2': corr(d_rr, d_spo2), 'dSpO2_mean': float(np.nanmean(d_spo2)) if len(d_spo2) else np.nan, 'dHR_mean': float(np.nanmean(d_hr)) if len(d_hr) else np.nan, 'dRR_mean': float(np.nanmean(d_rr)) if len(d_rr) else np.nan}
spo2_t, spo2_v = _to_arrays(spo2)
hr_t, hr_v = _to_arrays(heart_rate)
rr_t, rr_v = _to_arrays(respiratory_rate)
events_94 = _event_metrics(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, threshold=94.0, min_duration_s=30.0, merge_gap_s=60.0)
events_92 = _event_metrics(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, threshold=92.0, min_duration_s=30.0, merge_gap_s=60.0)

def _scatter_depth_duration(events, threshold, color_key, title_suffix, filename):
    if not events:
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.set_title(f'SpO2 Desaturation Events (<{int(threshold)}%): none detected')
        ax.set_xlabel('Duration (min)')
        ax.set_ylabel('Depth below threshold (percentage points)')
        ax.grid(True, alpha=0.3)
        save_plot(filename, fig=fig)
        return
    durations = np.array([e['duration_min'] for e in events], dtype=float)
    depths = np.array([e['depth_pct_points'] for e in events], dtype=float)
    colors = np.array([e[color_key] for e in events], dtype=float)
    fig, ax = plt.subplots(figsize=(8, 6))
    sc = ax.scatter(durations, depths, c=colors, cmap='coolwarm', s=70, edgecolor='k', linewidth=0.4, alpha=0.9)
    cb = fig.colorbar(sc, ax=ax)
    if color_key == 'd_hr_bpm':
        cb.set_label('ΔHR (bpm): event mean − pre-event baseline')
    else:
        cb.set_label('ΔRR (brpm): event mean − pre-event baseline')
    ax.set_title(f'SpO2 Desaturation Events <{int(threshold)}%: Depth vs Duration ({title_suffix})')
    ax.set_xlabel('Duration (min)')
    ax.set_ylabel(f'Depth below {int(threshold)}% (percentage points)')
    ax.grid(True, alpha=0.3)
    save_plot(filename, fig=fig)
_scatter_depth_duration(events_94, 94.0, 'd_hr_bpm', 'colored by ΔHR', 'spo2_events_lt94_depth_vs_duration_dHR.png')
_scatter_depth_duration(events_94, 94.0, 'd_rr_brpm', 'colored by ΔRR', 'spo2_events_lt94_depth_vs_duration_dRR.png')
_scatter_depth_duration(events_92, 92.0, 'd_hr_bpm', 'colored by ΔHR', 'spo2_events_lt92_depth_vs_duration_dHR.png')
_scatter_depth_duration(events_92, 92.0, 'd_rr_brpm', 'colored by ΔRR', 'spo2_events_lt92_depth_vs_duration_dRR.png')
coupling = {'minus_5_min': _lagged_coupling(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, lag_min=-5.0, baseline_minutes=5.0), 'zero_min': _lagged_coupling(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, lag_min=0.0, baseline_minutes=5.0), 'plus_5_min': _lagged_coupling(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, lag_min=5.0, baseline_minutes=5.0)}

def _event_summary(events):
    if not events:
        return {'n_events': 0}
    durs = np.array([e['duration_min'] for e in events], dtype=float)
    mins = np.array([e['min_spo2'] for e in events], dtype=float)
    depths = np.array([e['depth_pct_points'] for e in events], dtype=float)
    dhr = np.array([e['d_hr_bpm'] for e in events], dtype=float)
    drr = np.array([e['d_rr_brpm'] for e in events], dtype=float)
    return {'n_events': int(len(events)), 'duration_min_median': float(np.nanmedian(durs)), 'duration_min_max': float(np.nanmax(durs)), 'min_spo2_min': float(np.nanmin(mins)), 'depth_median_pct_points': float(np.nanmedian(depths)), 'depth_max_pct_points': float(np.nanmax(depths)), 'dHR_median_bpm': float(np.nanmedian(dhr)) if np.isfinite(dhr).any() else np.nan, 'dRR_median_brpm': float(np.nanmedian(drr)) if np.isfinite(drr).any() else np.nan}
result = {'events_lt94': events_94, 'events_lt92': events_92, 'summary_lt94': _event_summary(events_94), 'summary_lt92': _event_summary(events_92), 'lagged_coupling_deltas_vs_5min_prior': coupling, 'notes': {'event_rule': 'SpO2 < threshold for >=30s, merge gaps <60s (SpO2-series based).', 'baseline_rule': 'Pre-event baseline computed from SpO2 timestamps in [-5,-1] min (fallback LOCF at start). ΔHR/ΔRR use LOCF from their own streams.', 'lagged_rule': 'ΔSpO2, ΔHR, ΔRR computed vs values >=5 min earlier; HR/RR evaluated at approximate lagged time using nearest SpO2 timestamp (tolerance 2.5 min), else t0.'}}
n94 = result['summary_lt94'].get('n_events', 0)
n92 = result['summary_lt92'].get('n_events', 0)
min92 = result['summary_lt92'].get('min_spo2_min', np.nan)
dmax92 = result['summary_lt92'].get('depth_max_pct_points', np.nan)
durmax92 = result['summary_lt92'].get('duration_min_max', np.nan)
c0 = result['lagged_coupling_deltas_vs_5min_prior']['zero_min']['corr_dHR_dSpO2']
c_m5 = result['lagged_coupling_deltas_vs_5min_prior']['minus_5_min']['corr_dHR_dSpO2']
c_p5 = result['lagged_coupling_deltas_vs_5min_prior']['plus_5_min']['corr_dHR_dSpO2']

def _fmt_rp(d):
    r = d.get('r', np.nan)
    p = d.get('p', np.nan)
    n = d.get('n', 0)
    if not (np.isfinite(r) and np.isfinite(p)):
        return f'r=NA (n={n})'
    return f'r={r:.2f}, p={p:.3g} (n={n})'
interpretation = f'Detected {n94} SpO2 desaturation events <94% and {n92} events <92%; the <92% events reached nadir {min92:.1f}% with maximum depth {dmax92:.1f} %-points below 92% and maximum duration {durmax92:.2f} min (event-level ΔHR/ΔRR coloring provided to assess physiologic vs artifact patterns), with lagged ΔHR–ΔSpO2 coupling vs 5-min-prior baseline of {_fmt_rp(c_m5)} at −5 min, {_fmt_rp(c0)} at 0 min, and {_fmt_rp(c_p5)} at +5 min.'

plt.close()