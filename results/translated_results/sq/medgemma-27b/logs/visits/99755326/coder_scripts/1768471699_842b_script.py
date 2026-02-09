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
respiratory_rate = [(datetime.datetime(2218, 10, 22, 16, 58, 2), 27.0), (datetime.datetime(2218, 10, 22, 16, 59, 2), 21.5490196078431), (datetime.datetime(2218, 10, 22, 17, 0, 2), 19.6440677966102), (datetime.datetime(2218, 10, 22, 17, 1, 2), 29.2542372881356), (datetime.datetime(2218, 10, 22, 17, 2, 2), 20.3275862068966), (datetime.datetime(2218, 10, 22, 17, 3, 2), 20.5423728813559), (datetime.datetime(2218, 10, 22, 17, 4, 2), 17.7241379310345), (datetime.datetime(2218, 10, 22, 17, 5, 2), 18.7796610169492), (datetime.datetime(2218, 10, 22, 17, 6, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 7, 2), 18.1206896551724), (datetime.datetime(2218, 10, 22, 17, 8, 2), 26.6610169491526), (datetime.datetime(2218, 10, 22, 17, 9, 2), 17.1379310344828), (datetime.datetime(2218, 10, 22, 17, 10, 2), 18.8135593220339), (datetime.datetime(2218, 10, 22, 17, 11, 2), 12.5945945945946), (datetime.datetime(2218, 10, 22, 17, 12, 2), 13.6), (datetime.datetime(2218, 10, 22, 17, 13, 2), 22.6949152542373), (datetime.datetime(2218, 10, 22, 17, 14, 2), 26.2931034482759), (datetime.datetime(2218, 10, 22, 17, 15, 2), 27.0677966101695), (datetime.datetime(2218, 10, 22, 17, 16, 2), 22.1551724137931), (datetime.datetime(2218, 10, 22, 17, 17, 2), 19.1694915254237), (datetime.datetime(2218, 10, 22, 17, 18, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 19, 2), 21.2413793103448), (datetime.datetime(2218, 10, 22, 17, 20, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 21, 2), 19.2586206896552), (datetime.datetime(2218, 10, 22, 17, 22, 2), 19.8305084745763), (datetime.datetime(2218, 10, 22, 17, 23, 2), 19.2203389830508), (datetime.datetime(2218, 10, 22, 17, 24, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 25, 2), 20.0338983050848), (datetime.datetime(2218, 10, 22, 17, 26, 2), 16.6206896551724), (datetime.datetime(2218, 10, 22, 17, 27, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 28, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 29, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 30, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 31, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 32, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 33, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 34, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 35, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 36, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 37, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 38, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 39, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 40, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 41, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 42, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 43, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 44, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 45, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 46, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 47, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 48, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 49, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 50, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 51, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 52, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 53, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 54, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 55, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 56, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 57, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 58, 2), 20.0), (datetime.datetime(2218, 10, 22, 17, 59, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 0, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 1, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 2, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 3, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 4, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 5, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 6, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 7, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 8, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 9, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 10, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 11, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 12, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 13, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 14, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 15, 2), 20.0), (datetime.datetime(2218, 10, 22, 18, 16, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 17, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 18, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 19, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 20, 2), 98.0), (datetime.datetime(2218, 10, 22, 18, 21, 2), 98.0)]
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
import numpy as np
from datetime import datetime, timedelta
time_hr = [t for t, v in heart_rate]
hr_values = [v for t, v in heart_rate]
time_diffs = [(t2 - t1).total_seconds() / 60.0 for t1, t2 in zip(time_hr[:-1], time_hr[1:])]
cumulative_time = [0.0]
for diff in time_diffs:
    cumulative_time.append(cumulative_time[-1] + diff)
window_size_minutes = 5
window_size_samples = int(len(hr_values) / (time_diffs[0] if len(time_diffs) > 0 else 1)) if len(hr_values) > 0 else 0
if window_size_samples < 1:
    window_size_samples = 1
if window_size_samples > len(hr_values):
    window_size_samples = len(hr_values)
if window_size_samples == 0:
    window_size_samples = 1
rolling_std = np.convolve(hr_values, np.ones(window_size_samples), mode='valid') / window_size_samples
rolling_time = cumulative_time[len(cumulative_time) - len(rolling_std):]
plt.figure(figsize=(12, 6))
plt.plot(rolling_time, rolling_std)
plt.xlabel('Koha (minuta)')
plt.ylabel('Devijimi Standard Rrotullues i Rrahjeve të Zemrës (rrahje/min)')
plt.title('Volatiliteti i Rrahjeve të Zemrës Gjatë Kohës')
plt.grid(True)
save_plot('hr_volatility.png')

plt.close()
plt.figure(figsize=(12, 6))
time_sbp = [t for t, v in systolic_bp]
sbp_values = [v for t, v in systolic_bp]
plt.plot(time_sbp, sbp_values, label='Sistolik BP')
time_dbp = [t for t, v in diastolic_bp]
dbp_values = [v for t, v in diastolic_bp]
plt.plot(time_dbp, dbp_values, label='Diastolik BP')
plt.xlabel('Koha')
plt.ylabel('Presioni i Gjakut (mmHg)')
plt.title('Presioni i Gjakut Gjatë Kohës')
plt.legend()
plt.grid(True)
save_plot('blood_pressure_over_time.png')

plt.close()
plt.figure(figsize=(12, 6))
time_spo2 = [t for t, v in spo2]
spo2_values = [v for t, v in spo2]
plt.plot(time_spo2, spo2_values, label='SpO2')
plt.xlabel('Koha')
plt.ylabel('Oksigjenimi i Gjakut (%)')
plt.title('Niveli i Oksigjenimit të Gjakut Gjatë Kohës')
plt.legend()
plt.grid(True)
save_plot('spo2_over_time.png')

plt.close()
plt.figure(figsize=(12, 6))
time_resp = [t for t, v in respiratory_rate]
resp_values = [v for t, v in respiratory_rate]
plt.plot(time_resp, resp_values, label='Frymemarrje')
plt.xlabel('Koha')
plt.ylabel('Numri i Frymemarrjeve (frymemarrje/min)')
plt.title('Frekuenca e Frymemarrjes Gjatë Kohës')
plt.legend()
plt.grid(True)
save_plot('respiratory_rate_over_time.png')

plt.close()
plt.figure(figsize=(12, 6))
time_temp = [t for t, v in temperature]
temp_values = [v for t, v in temperature]
plt.plot(time_temp, temp_values, label='Temperaturë')
plt.xlabel('Koha')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura Gjatë Kohës')
plt.legend()
plt.grid(True)
save_plot('temperature_over_time.png')

plt.close()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Vlerësimi i Rrezikut të Sepsisë (qSOFA)')
ax.set_xlabel('Kriteret qSOFA')
ax.set_ylabel('Vlera')
bar_labels = ['Presioni Sistolik i Gjakut (SBP)', 'Shpejtësia e Frymemarrjes (RR)', 'Statusi Mendor']
bar_values = [systolic_bp[-1][1] if systolic_bp else 0, respiratory_rate[-1][1] if respiratory_rate else 0, 0]
colors = ['red' if bar_values[0] <= 100 else 'green', 'red' if bar_values[1] >= 22 else 'green', 'green']
ax.bar(bar_labels, bar_values, color=colors)
ax.text(0, bar_values[0] + 2, f'{bar_values[0]} mmHg', ha='center', va='bottom', fontsize=9)
ax.text(1, bar_values[1] + 2, f'{bar_values[1]} /min', ha='center', va='bottom', fontsize=9)
ax.text(2, 2, 'Normal', ha='center', va='bottom', fontsize=9)
ax.axhline(y=100, color='gray', linestyle='--', linewidth=0.8, label='Pragu SBP')
ax.axhline(y=22, color='gray', linestyle='--', linewidth=0.8, label='Pragu RR')
ax.legend()
plt.tight_layout()
save_plot('qsofa_score.png')

plt.close()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Vlerësimi i Rrezikut të Sepsisë (SIRS)')
ax.set_xlabel('Kriteret SIRS')
ax.set_ylabel('Vlera')
bar_labels_sirs = ['Temperatura', 'Shpejtësia e Rrahjeve të Zemrës', 'Frekuenca e Frymemarrjes', 'Numri i Bardhë i Gjakut']
bar_values_sirs = [temperature[-1][1] if temperature else 0, heart_rate[-1][1] if heart_rate else 0, respiratory_rate[-1][1] if respiratory_rate else 0, 0]
colors_sirs = []
if temperature and temperature[-1][1] > 38 or temperature[-1][1] < 36:
    colors_sirs.append('red')
else:
    colors_sirs.append('green')
if heart_rate and heart_rate[-1][1] > 90:
    colors_sirs.append('red')
else:
    colors_sirs.append('green')
if respiratory_rate and respiratory_rate[-1][1] > 20:
    colors_sirs.append('red')
else:
    colors_sirs.append('green')
colors_sirs.append('green')
ax.bar(bar_labels_sirs, bar_values_sirs, color=colors_sirs)
ax.text(0, bar_values_sirs[0] + 0.5, f'{bar_values_sirs[0]:.1f}°C', ha='center', va='bottom', fontsize=9)
ax.text(1, bar_values_sirs[1] + 2, f'{bar_values_sirs[1]} bpm', ha='center', va='bottom', fontsize=9)
ax.text(2, bar_values_sirs[2] + 1, f'{bar_values_sirs[2]} /min', ha='center', va='bottom', fontsize=9)
ax.text(3, 5, 'N/A', ha='center', va='bottom', fontsize=9)
ax.axhline(y=38, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Temperaturës (>38°C)')
ax.axhline(y=36, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Temperaturës (<36°C)')
ax.axhline(y=90, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Rrahjeve të Zemrës (>90 bpm)')
ax.axhline(y=20, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Frymemarrjes (>20 /min)')
ax.legend()
plt.tight_layout()
save_plot('sirs_score.png')

plt.close()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Vlerësimi i Rrezikut të Shock Index')
ax.set_xlabel('Kriteret Shock Index')
ax.set_ylabel('Vlera')
bar_labels_shock = ['Shock Index']
bar_values_shock = [shock_index]
colors_shock = ['red' if shock_index > 0.9 else 'green']
ax.bar(bar_labels_shock, bar_values_shock, color=colors_shock)
ax.text(0, bar_values_shock[0] + 0.02, f'{bar_values_shock[0]:.2f}', ha='center', va='bottom', fontsize=12)
ax.axhline(y=0.9, color='gray', linestyle='--', linewidth=0.8, label='Pragu Shock Index (>0.9)')
ax.legend()
plt.tight_layout()
save_plot('shock_index_plot.png')

plt.close()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Vlerësimi i Rrezikut të Mean Arterial Pressure (MAP)')
ax.set_xlabel('Kriteret MAP')
ax.set_ylabel('Vlera (mmHg)')
bar_labels_map = ['MAP']
bar_values_map = [map_value]
colors_map = ['red' if map_value < 65 or map_value > 100 else 'green']
ax.bar(bar_labels_map, bar_values_map, color=colors_map)
ax.text(0, bar_values_map[0] + 1, f'{bar_values_map[0]:.1f}', ha='center', va='bottom', fontsize=12)
ax.axhline(y=65, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Poshtëm MAP (<65 mmHg)')
ax.axhline(y=100, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Sipërm MAP (>100 mmHg)')
ax.legend()
plt.tight_layout()
save_plot('map_plot.png')

plt.close()
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Vlerësimi i Rrezikut të Pulse Pressure')
ax.set_xlabel('Kriteret Pulse Pressure')
ax.set_ylabel('Vlera (mmHg)')
bar_labels_pp = ['Pulse Pressure']
bar_values_pp = [pulse_pressure]
colors_pp = ['red' if pulse_pressure < 25 or pulse_pressure > 100 else 'green']
ax.bar(bar_labels_pp, bar_values_pp, color=colors_pp)
ax.text(0, bar_values_pp[0] + 1, f'{bar_values_pp[0]:.1f}', ha='center', va='bottom', fontsize=12)
ax.axhline(y=25, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Poshtëm Pulse Pressure (<25 mmHg)')
ax.axhline(y=100, color='gray', linestyle='--', linewidth=0.8, label='Pragu i Sipërm Pulse Pressure (>100 mmHg)')
ax.legend()
plt.tight_layout()
save_plot('pulse_pressure_plot.png')

plt.close()
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title('Trendi i SpO2')
ax.set_xlabel('Koha')
ax.set_ylabel('SpO2 (%)')
ax.plot(time_spo2, spo2_values, marker='o', linestyle='-', color='b', label='SpO2')
ax.axhline(y=spo2_trend['mean'], color='r', linestyle='--', label=f"Mesatarja: {spo2_trend['mean']:.1f}%")
ax.axhline(y=spo2_trend['first'], color='g', linestyle=':', label=f"Fillimi: {spo2_trend['first']:.1f}%")
ax.axhline(y=spo2_trend['last'], color='purple', linestyle=':', label=f"Fundi: {spo2_trend['last']:.1f}%")
ax.text(0.5, 0.95, f"Trendi: {spo2_trend['slope']:.2f} (R^2: {spo2_trend['r_squared']:.2f})", transform=ax.transAxes, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.5', fc='wheat', alpha=0.5))
ax.legend(loc='best')
plt.grid(True)
save_plot('spo2_trend.png')

plt.close()
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title('Volatiliteti i Rrahjeve të Zemrës')
ax.set_xlabel('Koha (minuta)')
ax.set_ylabel('Devijimi Standard i Rrahjeve të Zemrës (bpm)')
ax.plot(rolling_time, rolling_std, marker='o', linestyle='-', color='b', label='Devijimi Standard Rrotullues')
ax.text(0.5, 0.95, f"Dispersioni: {hr_volatility['dispersion_ms']:.2f} ms\nRMSSD: {hr_volatility['rmssd_ms']:.2f} ms\nStdDev: {hr_volatility['hr_std_bpm']:.2f} bpm\nRange: {hr_volatility['hr_range_bpm']:.1f} bpm\nKampione: {hr_volatility['n_samples']}\nDensitet: {hr_volatility['data_density']}", transform=ax.transAxes, ha='left', va='top', bbox=dict(boxstyle='round,pad=0.5', fc='wheat', alpha=0.5))
ax.legend(loc='best')
plt.grid(True)
save_plot('hr_volatility_details.png')

plt.close()