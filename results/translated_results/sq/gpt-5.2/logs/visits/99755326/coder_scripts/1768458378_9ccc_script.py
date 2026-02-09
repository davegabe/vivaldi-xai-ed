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
def _to_arrays(series):
    if series is None or len(series) == 0:
        return (np.array([]), np.array([]))
    t = np.array([x[0] for x in series], dtype=object)
    v = np.array([float(x[1]) for x in series], dtype=float)
    return (t, v)

def _seconds_between(t2, t1):
    return (t2 - t1).total_seconds()

def _event_segments_from_spo2(spo2_series, threshold=92.0, min_duration_s=30.0, merge_gap_s=60.0):
    t, v = _to_arrays(spo2_series)
    n = len(t)
    if n < 2:
        return []
    below = v < threshold
    segments = []
    in_seg = False
    start_idx = None
    for i in range(n):
        if below[i] and (not in_seg):
            in_seg = True
            start_idx = i
        elif not below[i] and in_seg:
            end_idx = i - 1
            segments.append((start_idx, end_idx))
            in_seg = False
            start_idx = None
    if in_seg:
        segments.append((start_idx, n - 1))
    raw_events = []
    for s_idx, e_idx in segments:
        start_t = t[s_idx]
        end_t = t[e_idx]
        if e_idx + 1 < n:
            end_t = t[e_idx + 1]
        duration = _seconds_between(end_t, start_t)
        if duration >= min_duration_s:
            raw_events.append((start_t, end_t))
    if not raw_events:
        return []
    merged = [raw_events[0]]
    for st, et in raw_events[1:]:
        pst, pet = merged[-1]
        gap = _seconds_between(st, pet)
        if gap < merge_gap_s:
            merged[-1] = (pst, max(pet, et))
        else:
            merged.append((st, et))
    return merged

def _nearest_index(ts, t_target):
    if len(ts) == 0:
        return None
    t0 = ts[0]
    x = np.array([_seconds_between(ti, t0) for ti in ts], dtype=float)
    y = _seconds_between(t_target, t0)
    j = int(np.searchsorted(x, y))
    if j <= 0:
        return 0
    if j >= len(x):
        return len(x) - 1
    if abs(x[j] - y) < abs(x[j - 1] - y):
        return j
    return j - 1

def _value_at_or_near(series, t_target, max_abs_dt_s=None):
    ts, vs = _to_arrays(series)
    if len(ts) == 0:
        return np.nan
    idx = _nearest_index(ts, t_target)
    if idx is None:
        return np.nan
    dt = abs(_seconds_between(ts[idx], t_target))
    if max_abs_dt_s is not None and dt > max_abs_dt_s:
        return np.nan
    return float(vs[idx])

def _extract_event_locked(series, t_center, window_min=10.0):
    ts, vs = _to_arrays(series)
    if len(ts) == 0:
        return (np.array([]), np.array([]))
    w_s = window_min * 60.0
    rel = np.array([_seconds_between(ti, t_center) / 60.0 for ti in ts], dtype=float)
    mask = (rel >= -window_min) & (rel <= window_min)
    return (rel[mask], vs[mask])

def _classify_rr_response(rr_series, t_event_start, t_event_end, pre_min=5.0, post_min=5.0, min_delta=2.0, max_abs_dt_s=120.0):
    ts, vs = _to_arrays(rr_series)
    if len(ts) < 2:
        return ('none', np.nan, np.nan, np.nan)
    rel = np.array([_seconds_between(ti, t_event_start) / 60.0 for ti in ts], dtype=float)
    pre_mask = (rel >= -pre_min) & (rel < 0.0)
    post_mask = (rel > 0.0) & (rel <= post_min)
    pre_vals = vs[pre_mask]
    post_vals = vs[post_mask]
    if pre_vals.size == 0:
        v = _value_at_or_near(rr_series, t_event_start, max_abs_dt_s=max_abs_dt_s)
        pre_vals = np.array([]) if np.isnan(v) else np.array([v], dtype=float)
    if post_vals.size == 0:
        v = _value_at_or_near(rr_series, t_event_start, max_abs_dt_s=max_abs_dt_s)
        if np.isnan(v) or (pre_vals.size > 0 and np.isfinite(pre_vals[0]) and (abs(v - pre_vals[0]) < 1e-09)):
            v2 = _value_at_or_near(rr_series, t_event_end, max_abs_dt_s=max_abs_dt_s)
            v = v2
        post_vals = np.array([]) if np.isnan(v) else np.array([v], dtype=float)
    if pre_vals.size == 0 or post_vals.size == 0:
        return ('none', np.nan, np.nan, np.nan)
    pre_med = float(np.median(pre_vals))
    post_med = float(np.median(post_vals))
    delta = post_med - pre_med
    if delta >= min_delta:
        cls = 'rise'
    elif delta <= -min_delta:
        cls = 'drop'
    else:
        cls = 'none'
    return (cls, pre_med, post_med, float(delta))
events = _event_segments_from_spo2(spo2, threshold=92.0, min_duration_s=30.0, merge_gap_s=60.0)
event_results = []
for k, (st, et) in enumerate(events, start=1):
    duration_s = _seconds_between(et, st)
    mid = st + (et - st) / 2
    spo2_rel, spo2_vals = _extract_event_locked(spo2, mid, window_min=10.0)
    rr_rel, rr_vals = _extract_event_locked(respiratory_rate, mid, window_min=10.0)
    hr_rel, hr_vals = _extract_event_locked(heart_rate, mid, window_min=10.0)
    spo2_t, spo2_v = _to_arrays(spo2)
    if len(spo2_t) > 0:
        in_evt = np.array([ti >= st and ti <= et for ti in spo2_t], dtype=bool)
        if np.any(in_evt):
            nadir = float(np.min(spo2_v[in_evt]))
        else:
            nadir = np.nan
    else:
        nadir = np.nan
    rr_cls, rr_pre, rr_post, rr_delta = _classify_rr_response(respiratory_rate, st, et, pre_min=5.0, post_min=5.0, min_delta=2.0, max_abs_dt_s=120.0)
    event_results.append({'event_id': k, 'start_time': st, 'end_time': et, 'duration_s': float(duration_s), 'spo2_nadir_pct': nadir, 'alignment_time': mid, 'rr_response': rr_cls, 'rr_pre_median_brpm': rr_pre, 'rr_post_median_brpm': rr_post, 'rr_delta_brpm': rr_delta, 'curves': {'spo2': {'t_min': spo2_rel, 'value': spo2_vals}, 'rr': {'t_min': rr_rel, 'value': rr_vals}, 'hr': {'t_min': hr_rel, 'value': hr_vals}}})
if len(event_results) > 0:
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(10, 10))
    ax_spo2, ax_rr, ax_hr = axes
    for ev in event_results:
        c = ev['curves']
        if c['spo2']['t_min'].size > 0:
            ax_spo2.plot(c['spo2']['t_min'], c['spo2']['value'], alpha=0.6, linewidth=1.5)
        if c['rr']['t_min'].size > 0:
            ax_rr.plot(c['rr']['t_min'], c['rr']['value'], alpha=0.6, linewidth=1.5)
        if c['hr']['t_min'].size > 0:
            ax_hr.plot(c['hr']['t_min'], c['hr']['value'], alpha=0.6, linewidth=1.5)
    ax_spo2.axvline(0, color='k', linewidth=1, alpha=0.6)
    ax_rr.axvline(0, color='k', linewidth=1, alpha=0.6)
    ax_hr.axvline(0, color='k', linewidth=1, alpha=0.6)
    ax_spo2.axhline(92.0, color='r', linestyle='--', linewidth=1, alpha=0.7)
    ax_spo2.set_ylabel('SpO2 (%)')
    ax_rr.set_ylabel('RR (brpm)')
    ax_hr.set_ylabel('HR (bpm)')
    ax_hr.set_xlabel('Kohë nga mesatarja e ngjarjes (min)')
    ax_spo2.set_title('Kurbat e ngjarjeve të kyçura të shenjave vitale rreth ngjarjeve të uljes së SpO2 (<92%)\nAfati kohor: -10 deri +10 minuta; t=0 në mesataren e ngjarjes')
    ax_spo2.set_xlim(-10, 10)
    save_plot('spo2_desat_event_locked_curves.png', fig=fig)
else:
    fig, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.axis('off')
    ax.text(0.01, 0.6, 'Nuk u zbuluan ngjarje të uljes së SpO2 (<92% për ≥30s).', fontsize=12)
    save_plot('spo2_desat_event_locked_curves.png', fig=fig)
result = {'n_events': int(len(event_results)), 'events': event_results, 'event_definition': {'spo2_threshold_pct': 92.0, 'min_duration_s': 30.0, 'merge_gap_s': 60.0, 'event_locked_window_min': 10.0, 'rr_response_definition': {'baseline_window_min': 5.0, 'post_window_min': 5.0, 'min_delta_brpm_for_change': 2.0}}, 'available_state_metrics_used': {'spo2_trend': spo2_trend, 'hr_volatility': hr_volatility, 'shock_index': shock_index, 'map_value': map_value, 'qsofa_score': qsofa_score, 'sirs': sirs}}
if result['n_events'] == 0:
    interpretation = f'Zbulimi i ngjarjeve të uljes së SpO2 nuk gjeti 0 ngjarje që plotësojnë kriteret (<92% për ≥30s, boshllëqe të bashkuara <60s); konteksti i përgjithshëm mbetet me rrezik të lartë me indeks shoku {shock_index:.3f} (LARTË), qSOFA {qsofa_score}/3, dhe hipoksemi ndërprerëse e vërejtur në trend (min {spo2_trend.get('min', np.nan)}%).'
else:
    rr_counts = {'rise': 0, 'drop': 0, 'none': 0}
    nadirs = []
    durs = []
    for ev in event_results:
        rr_counts[ev['rr_response']] = rr_counts.get(ev['rr_response'], 0) + 1
        if np.isfinite(ev['spo2_nadir_pct']):
            nadirs.append(ev['spo2_nadir_pct'])
        durs.append(ev['duration_s'])
    nadir_min = float(np.min(nadirs)) if len(nadirs) > 0 else np.nan
    dur_med = float(np.median(np.array(durs, dtype=float))) if len(durs) > 0 else np.nan
    interpretation = f'U zbuluan {result['n_events']} ngjarje(je) të uljes së SpO2 (<92% për ≥30s, boshllëqe të bashkuara <60s) me pikën më të ulët të ngjarjes {nadir_min:.1f}% dhe medianën e kohëzgjatjes {dur_med:.0f}s; klasifikimi i përgjigjes së RR: rritje={rr_counts.get('rise', 0)}, rënie={rr_counts.get('drop', 0)}, asnjë={rr_counts.get('none', 0)}.'

plt.close()