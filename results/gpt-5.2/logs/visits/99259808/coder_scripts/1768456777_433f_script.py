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
visit_id = '99259808'
age = 69
gender = 'F'
ethnicity = 'White (Non-Hispanic/Non-Latino)'
heart_rate = [(datetime.datetime(2204, 6, 15, 8, 57, 53), 88.0), (datetime.datetime(2204, 6, 15, 8, 58, 53), 74.1578947368421), (datetime.datetime(2204, 6, 15, 8, 59, 53), 68.6379310344828), (datetime.datetime(2204, 6, 15, 9, 0, 53), 67.864406779661), (datetime.datetime(2204, 6, 15, 9, 1, 53), 71.6379310344828), (datetime.datetime(2204, 6, 15, 9, 2, 53), 70.1016949152542), (datetime.datetime(2204, 6, 15, 9, 3, 53), 71.4310344827586), (datetime.datetime(2204, 6, 15, 9, 4, 53), 72.6071428571429), (datetime.datetime(2204, 6, 15, 9, 5, 53), 71.3898305084746), (datetime.datetime(2204, 6, 15, 9, 6, 53), 72.1052631578947), (datetime.datetime(2204, 6, 15, 9, 7, 53), 70.8305084745763), (datetime.datetime(2204, 6, 15, 9, 8, 53), 69.2333333333333), (datetime.datetime(2204, 6, 15, 9, 9, 53), 68.9827586206897), (datetime.datetime(2204, 6, 15, 9, 10, 53), 70.8135593220339), (datetime.datetime(2204, 6, 15, 9, 11, 53), 69.8620689655173), (datetime.datetime(2204, 6, 15, 9, 12, 53), 68.4406779661017), (datetime.datetime(2204, 6, 15, 9, 13, 53), 69.6440677966102), (datetime.datetime(2204, 6, 15, 9, 14, 53), 68.3965517241379), (datetime.datetime(2204, 6, 15, 9, 15, 53), 66.3389830508475), (datetime.datetime(2204, 6, 15, 9, 16, 53), 66.8965517241379), (datetime.datetime(2204, 6, 15, 9, 17, 53), 68.6610169491526), (datetime.datetime(2204, 6, 15, 9, 18, 53), 69.9830508474576), (datetime.datetime(2204, 6, 15, 9, 19, 53), 65.4137931034483), (datetime.datetime(2204, 6, 15, 9, 20, 53), 61.9137931034483), (datetime.datetime(2204, 6, 15, 9, 21, 53), 58.4237288135593), (datetime.datetime(2204, 6, 15, 9, 22, 53), 61.0677966101695), (datetime.datetime(2204, 6, 15, 9, 23, 53), 68.2542372881356), (datetime.datetime(2204, 6, 15, 9, 24, 53), 64.5172413793104), (datetime.datetime(2204, 6, 15, 9, 25, 53), 65.9322033898305), (datetime.datetime(2204, 6, 15, 9, 26, 53), 61.7068965517241), (datetime.datetime(2204, 6, 15, 9, 27, 53), 56.9152542372881), (datetime.datetime(2204, 6, 15, 9, 28, 53), 60.5254237288136), (datetime.datetime(2204, 6, 15, 9, 29, 53), 62.6896551724138), (datetime.datetime(2204, 6, 15, 9, 30, 53), 59.4915254237288), (datetime.datetime(2204, 6, 15, 9, 31, 53), 66.0175438596491), (datetime.datetime(2204, 6, 15, 9, 32, 53), 60.6333333333333), (datetime.datetime(2204, 6, 15, 9, 33, 53), 66.2586206896552), (datetime.datetime(2204, 6, 15, 9, 34, 53), 70.1016949152542), (datetime.datetime(2204, 6, 15, 9, 35, 53), 66.5084745762712), (datetime.datetime(2204, 6, 15, 9, 36, 53), 66.4137931034483), (datetime.datetime(2204, 6, 15, 9, 37, 53), 62.7796610169492), (datetime.datetime(2204, 6, 15, 9, 38, 53), 65.2931034482759), (datetime.datetime(2204, 6, 15, 9, 39, 53), 66.4237288135593), (datetime.datetime(2204, 6, 15, 9, 40, 53), 56.7966101694915), (datetime.datetime(2204, 6, 15, 9, 41, 53), 68.9655172413793), (datetime.datetime(2204, 6, 15, 9, 42, 53), 69.9152542372881), (datetime.datetime(2204, 6, 15, 9, 43, 53), 68.948275862069), (datetime.datetime(2204, 6, 15, 9, 44, 53), 68.2033898305085), (datetime.datetime(2204, 6, 15, 9, 45, 53), 67.4915254237288), (datetime.datetime(2204, 6, 15, 9, 46, 53), 69.7241379310345), (datetime.datetime(2204, 6, 15, 9, 47, 53), 69.3728813559322), (datetime.datetime(2204, 6, 15, 9, 48, 53), 70.9137931034483), (datetime.datetime(2204, 6, 15, 9, 49, 53), 69.0847457627119), (datetime.datetime(2204, 6, 15, 9, 50, 53), 69.3559322033898), (datetime.datetime(2204, 6, 15, 9, 51, 53), 72.3965517241379), (datetime.datetime(2204, 6, 15, 9, 52, 53), 70.625), (datetime.datetime(2204, 6, 15, 9, 53, 53), 70.0740740740741), (datetime.datetime(2204, 6, 15, 9, 54, 53), 71.8333333333333), (datetime.datetime(2204, 6, 15, 9, 55, 53), 72.551724137931), (datetime.datetime(2204, 6, 15, 9, 56, 53), 71.2758620689655), (datetime.datetime(2204, 6, 15, 9, 57, 53), 68.8666666666667), (datetime.datetime(2204, 6, 15, 9, 58, 53), 72.8275862068966), (datetime.datetime(2204, 6, 15, 9, 59, 53), 75.2413793103448), (datetime.datetime(2204, 6, 15, 10, 0, 53), 72.1379310344828), (datetime.datetime(2204, 6, 15, 10, 1, 53), 71.3333333333333), (datetime.datetime(2204, 6, 15, 10, 2, 53), 71.2758620689655), (datetime.datetime(2204, 6, 15, 10, 3, 53), 72.6896551724138), (datetime.datetime(2204, 6, 15, 10, 4, 53), 74.1666666666667), (datetime.datetime(2204, 6, 15, 10, 5, 53), 69.7586206896552), (datetime.datetime(2204, 6, 15, 10, 6, 53), 71.2758620689655), (datetime.datetime(2204, 6, 15, 10, 7, 53), 70.8965517241379), (datetime.datetime(2204, 6, 15, 10, 8, 53), 73.5666666666667), (datetime.datetime(2204, 6, 15, 10, 9, 53), 83.3103448275862), (datetime.datetime(2204, 6, 15, 10, 10, 53), 72.8275862068966), (datetime.datetime(2204, 6, 15, 10, 11, 53), 72.3), (datetime.datetime(2204, 6, 15, 10, 12, 53), 73.1034482758621), (datetime.datetime(2204, 6, 15, 10, 13, 53), 74.5172413793104), (datetime.datetime(2204, 6, 15, 10, 14, 53), 73.2666666666667), (datetime.datetime(2204, 6, 15, 10, 15, 53), 74.6206896551724), (datetime.datetime(2204, 6, 15, 10, 16, 53), 73.7391304347826), (datetime.datetime(2204, 6, 15, 10, 17, 53), 77.2758620689655), (datetime.datetime(2204, 6, 15, 10, 18, 53), 74.8), (datetime.datetime(2204, 6, 15, 10, 19, 53), 74.5862068965517), (datetime.datetime(2204, 6, 15, 10, 20, 53), 73.5862068965517), (datetime.datetime(2204, 6, 15, 10, 21, 53), 79.8666666666667), (datetime.datetime(2204, 6, 15, 10, 22, 53), 74.8965517241379), (datetime.datetime(2204, 6, 15, 10, 23, 53), 73.1818181818182), (datetime.datetime(2204, 6, 15, 10, 46, 53), 69.8571428571429), (datetime.datetime(2204, 6, 15, 10, 47, 53), 74.9830508474576), (datetime.datetime(2204, 6, 15, 10, 48, 53), 72.4745762711864), (datetime.datetime(2204, 6, 15, 10, 49, 53), 71.4347826086957), (datetime.datetime(2204, 6, 15, 10, 50, 53), 65.5), (datetime.datetime(2204, 6, 15, 10, 51, 53), 68.4827586206897), (datetime.datetime(2204, 6, 15, 10, 52, 53), 67.271186440678), (datetime.datetime(2204, 6, 15, 10, 53, 53), 70.1016949152542), (datetime.datetime(2204, 6, 15, 10, 54, 53), 73.5172413793104), (datetime.datetime(2204, 6, 15, 10, 55, 53), 69.406779661017), (datetime.datetime(2204, 6, 15, 10, 56, 53), 64.7272727272727), (datetime.datetime(2204, 6, 15, 10, 59, 53), 65.0), (datetime.datetime(2204, 6, 15, 11, 0, 53), 69.3863636363636), (datetime.datetime(2204, 6, 15, 11, 1, 53), 70.1864406779661), (datetime.datetime(2204, 6, 15, 11, 2, 53), 69.1896551724138), (datetime.datetime(2204, 6, 15, 11, 3, 53), 67.728813559322), (datetime.datetime(2204, 6, 15, 11, 4, 53), 71.135593220339), (datetime.datetime(2204, 6, 15, 11, 5, 53), 69.1896551724138), (datetime.datetime(2204, 6, 15, 11, 6, 53), 70.6440677966102), (datetime.datetime(2204, 6, 15, 11, 7, 53), 69.448275862069), (datetime.datetime(2204, 6, 15, 11, 8, 53), 68.3898305084746), (datetime.datetime(2204, 6, 15, 11, 9, 53), 67.8983050847458), (datetime.datetime(2204, 6, 15, 11, 10, 53), 68.3103448275862), (datetime.datetime(2204, 6, 15, 11, 11, 53), 68.0169491525424), (datetime.datetime(2204, 6, 15, 11, 12, 53), 71.1206896551724), (datetime.datetime(2204, 6, 15, 11, 13, 53), 67.3389830508475), (datetime.datetime(2204, 6, 15, 11, 14, 53), 69.075), (datetime.datetime(2204, 6, 15, 11, 16, 53), 69.4166666666667), (datetime.datetime(2204, 6, 15, 11, 17, 53), 69.0169491525424), (datetime.datetime(2204, 6, 15, 11, 18, 53), 70.475), (datetime.datetime(2204, 6, 15, 11, 19, 53), 72.1694915254237), (datetime.datetime(2204, 6, 15, 11, 20, 53), 70.0), (datetime.datetime(2204, 6, 15, 11, 21, 53), 71.0), (datetime.datetime(2204, 6, 15, 11, 22, 53), 67.0), (datetime.datetime(2204, 6, 15, 11, 23, 53), 72.0), (datetime.datetime(2204, 6, 15, 11, 24, 53), 70.0), (datetime.datetime(2204, 6, 15, 11, 25, 53), 72.0), (datetime.datetime(2204, 6, 15, 11, 26, 53), 62.0), (datetime.datetime(2204, 6, 15, 11, 27, 53), 68.0), (datetime.datetime(2204, 6, 15, 11, 28, 53), 70.0), (datetime.datetime(2204, 6, 15, 11, 29, 53), 70.0), (datetime.datetime(2204, 6, 15, 11, 30, 53), 69.0), (datetime.datetime(2204, 6, 15, 11, 31, 53), 64.0), (datetime.datetime(2204, 6, 15, 11, 32, 53), 70.0), (datetime.datetime(2204, 6, 15, 11, 33, 53), 69.0), (datetime.datetime(2204, 6, 15, 11, 34, 53), 70.0), (datetime.datetime(2204, 6, 15, 11, 35, 53), 57.0), (datetime.datetime(2204, 6, 15, 11, 36, 53), 74.0), (datetime.datetime(2204, 6, 15, 11, 37, 53), 66.0), (datetime.datetime(2204, 6, 15, 11, 38, 53), 69.0), (datetime.datetime(2204, 6, 15, 11, 39, 53), 70.0), (datetime.datetime(2204, 6, 15, 11, 40, 53), 62.0), (datetime.datetime(2204, 6, 15, 11, 41, 53), 71.0), (datetime.datetime(2204, 6, 15, 11, 42, 53), 67.0), (datetime.datetime(2204, 6, 15, 11, 43, 53), 72.0), (datetime.datetime(2204, 6, 15, 11, 44, 53), 68.0), (datetime.datetime(2204, 6, 15, 11, 45, 53), 71.0), (datetime.datetime(2204, 6, 15, 11, 46, 53), 67.0), (datetime.datetime(2204, 6, 15, 11, 47, 53), 68.0)]
systolic_bp = [(datetime.datetime(2204, 6, 15, 8, 57, 53), 115.0), (datetime.datetime(2204, 6, 15, 8, 58, 53), 115.0), (datetime.datetime(2204, 6, 15, 9, 7, 53), 118.0), (datetime.datetime(2204, 6, 15, 9, 10, 53), 118.0), (datetime.datetime(2204, 6, 15, 9, 13, 53), 122.0), (datetime.datetime(2204, 6, 15, 9, 18, 53), 131.0), (datetime.datetime(2204, 6, 15, 9, 21, 53), 128.0), (datetime.datetime(2204, 6, 15, 9, 22, 53), 109.0), (datetime.datetime(2204, 6, 15, 9, 23, 53), 109.0), (datetime.datetime(2204, 6, 15, 9, 27, 53), 119.0), (datetime.datetime(2204, 6, 15, 9, 28, 53), 119.0), (datetime.datetime(2204, 6, 15, 9, 32, 53), 110.0), (datetime.datetime(2204, 6, 15, 9, 33, 53), 110.0), (datetime.datetime(2204, 6, 15, 9, 35, 53), 115.0), (datetime.datetime(2204, 6, 15, 9, 36, 53), 115.0), (datetime.datetime(2204, 6, 15, 9, 37, 53), 119.0), (datetime.datetime(2204, 6, 15, 9, 38, 53), 119.0), (datetime.datetime(2204, 6, 15, 9, 43, 53), 123.0), (datetime.datetime(2204, 6, 15, 9, 48, 53), 131.0), (datetime.datetime(2204, 6, 15, 9, 52, 53), 113.0), (datetime.datetime(2204, 6, 15, 9, 53, 53), 113.0), (datetime.datetime(2204, 6, 15, 9, 57, 53), 104.0), (datetime.datetime(2204, 6, 15, 9, 58, 53), 104.0), (datetime.datetime(2204, 6, 15, 10, 2, 53), 127.0), (datetime.datetime(2204, 6, 15, 10, 3, 53), 127.0), (datetime.datetime(2204, 6, 15, 10, 7, 53), 140.0), (datetime.datetime(2204, 6, 15, 10, 8, 53), 140.0), (datetime.datetime(2204, 6, 15, 10, 12, 53), 97.0), (datetime.datetime(2204, 6, 15, 10, 13, 53), 97.0), (datetime.datetime(2204, 6, 15, 10, 17, 53), 103.0), (datetime.datetime(2204, 6, 15, 10, 18, 53), 103.0), (datetime.datetime(2204, 6, 15, 10, 47, 53), 113.0), (datetime.datetime(2204, 6, 15, 10, 48, 53), 113.0), (datetime.datetime(2204, 6, 15, 10, 59, 53), 123.0), (datetime.datetime(2204, 6, 15, 11, 0, 53), 123.0), (datetime.datetime(2204, 6, 15, 11, 7, 53), 115.0), (datetime.datetime(2204, 6, 15, 11, 8, 53), 115.0), (datetime.datetime(2204, 6, 15, 11, 16, 53), 120.0), (datetime.datetime(2204, 6, 15, 11, 22, 53), 129.0)]
diastolic_bp = [(datetime.datetime(2204, 6, 15, 8, 57, 53), 92.0), (datetime.datetime(2204, 6, 15, 8, 58, 53), 92.0), (datetime.datetime(2204, 6, 15, 9, 7, 53), 67.0), (datetime.datetime(2204, 6, 15, 9, 10, 53), 67.0), (datetime.datetime(2204, 6, 15, 9, 13, 53), 57.0), (datetime.datetime(2204, 6, 15, 9, 18, 53), 81.0), (datetime.datetime(2204, 6, 15, 9, 21, 53), 107.0), (datetime.datetime(2204, 6, 15, 9, 22, 53), 85.0), (datetime.datetime(2204, 6, 15, 9, 23, 53), 85.0), (datetime.datetime(2204, 6, 15, 9, 27, 53), 82.0), (datetime.datetime(2204, 6, 15, 9, 28, 53), 82.0), (datetime.datetime(2204, 6, 15, 9, 32, 53), 58.0), (datetime.datetime(2204, 6, 15, 9, 33, 53), 58.0), (datetime.datetime(2204, 6, 15, 9, 35, 53), 61.0), (datetime.datetime(2204, 6, 15, 9, 36, 53), 61.0), (datetime.datetime(2204, 6, 15, 9, 37, 53), 63.0), (datetime.datetime(2204, 6, 15, 9, 38, 53), 63.0), (datetime.datetime(2204, 6, 15, 9, 43, 53), 66.0), (datetime.datetime(2204, 6, 15, 9, 48, 53), 65.0), (datetime.datetime(2204, 6, 15, 9, 52, 53), 76.0), (datetime.datetime(2204, 6, 15, 9, 53, 53), 76.0), (datetime.datetime(2204, 6, 15, 9, 57, 53), 86.0), (datetime.datetime(2204, 6, 15, 9, 58, 53), 86.0), (datetime.datetime(2204, 6, 15, 10, 2, 53), 75.0), (datetime.datetime(2204, 6, 15, 10, 3, 53), 75.0), (datetime.datetime(2204, 6, 15, 10, 7, 53), 117.0), (datetime.datetime(2204, 6, 15, 10, 8, 53), 117.0), (datetime.datetime(2204, 6, 15, 10, 12, 53), 46.0), (datetime.datetime(2204, 6, 15, 10, 13, 53), 46.0), (datetime.datetime(2204, 6, 15, 10, 17, 53), 69.0), (datetime.datetime(2204, 6, 15, 10, 18, 53), 69.0), (datetime.datetime(2204, 6, 15, 10, 47, 53), 70.0), (datetime.datetime(2204, 6, 15, 10, 48, 53), 70.0), (datetime.datetime(2204, 6, 15, 10, 59, 53), 69.0), (datetime.datetime(2204, 6, 15, 11, 0, 53), 69.0), (datetime.datetime(2204, 6, 15, 11, 7, 53), 79.0), (datetime.datetime(2204, 6, 15, 11, 8, 53), 79.0), (datetime.datetime(2204, 6, 15, 11, 16, 53), 79.0), (datetime.datetime(2204, 6, 15, 11, 22, 53), 78.0)]
spo2 = [(datetime.datetime(2204, 6, 15, 8, 56, 53), 99.1875), (datetime.datetime(2204, 6, 15, 8, 57, 53), 98.2093023255814), (datetime.datetime(2204, 6, 15, 8, 58, 53), 97.85), (datetime.datetime(2204, 6, 15, 8, 59, 53), 98.3333333333333), (datetime.datetime(2204, 6, 15, 9, 0, 53), 99.3898305084746), (datetime.datetime(2204, 6, 15, 9, 1, 53), 99.5172413793104), (datetime.datetime(2204, 6, 15, 9, 2, 53), 98.6949152542373), (datetime.datetime(2204, 6, 15, 9, 3, 53), 98.6851851851852), (datetime.datetime(2204, 6, 15, 9, 4, 53), 98.8636363636364), (datetime.datetime(2204, 6, 15, 9, 5, 53), 86.0), (datetime.datetime(2204, 6, 15, 9, 6, 53), 99.1929824561404), (datetime.datetime(2204, 6, 15, 9, 7, 53), 99.2881355932203), (datetime.datetime(2204, 6, 15, 9, 8, 53), 99.0), (datetime.datetime(2204, 6, 15, 9, 9, 53), 98.0344827586207), (datetime.datetime(2204, 6, 15, 9, 10, 53), 99.8135593220339), (datetime.datetime(2204, 6, 15, 9, 11, 53), 99.5517241379311), (datetime.datetime(2204, 6, 15, 9, 12, 53), 99.0), (datetime.datetime(2204, 6, 15, 9, 13, 53), 99.9152542372881), (datetime.datetime(2204, 6, 15, 9, 14, 53), 99.6896551724138), (datetime.datetime(2204, 6, 15, 9, 15, 53), 99.6610169491525), (datetime.datetime(2204, 6, 15, 9, 16, 53), 99.6896551724138), (datetime.datetime(2204, 6, 15, 9, 17, 53), 99.5593220338983), (datetime.datetime(2204, 6, 15, 9, 18, 53), 99.8305084745763), (datetime.datetime(2204, 6, 15, 9, 19, 53), 99.2758620689655), (datetime.datetime(2204, 6, 15, 9, 20, 53), 99.4655172413793), (datetime.datetime(2204, 6, 15, 9, 21, 53), 98.4406779661017), (datetime.datetime(2204, 6, 15, 9, 22, 53), 97.8135593220339), (datetime.datetime(2204, 6, 15, 9, 23, 53), 95.406779661017), (datetime.datetime(2204, 6, 15, 9, 24, 53), 99.8103448275862), (datetime.datetime(2204, 6, 15, 9, 25, 53), 99.1525423728814), (datetime.datetime(2204, 6, 15, 9, 26, 53), 99.4137931034483), (datetime.datetime(2204, 6, 15, 9, 27, 53), 97.6949152542373), (datetime.datetime(2204, 6, 15, 9, 28, 53), 97.135593220339), (datetime.datetime(2204, 6, 15, 9, 29, 53), 98.8448275862069), (datetime.datetime(2204, 6, 15, 9, 30, 53), 98.4745762711864), (datetime.datetime(2204, 6, 15, 9, 31, 53), 95.2105263157895), (datetime.datetime(2204, 6, 15, 9, 32, 53), 99.65), (datetime.datetime(2204, 6, 15, 9, 33, 53), 99.6551724137931), (datetime.datetime(2204, 6, 15, 9, 34, 53), 98.7796610169492), (datetime.datetime(2204, 6, 15, 9, 35, 53), 99.9661016949153), (datetime.datetime(2204, 6, 15, 9, 36, 53), 99.6034482758621), (datetime.datetime(2204, 6, 15, 9, 37, 53), 99.2542372881356), (datetime.datetime(2204, 6, 15, 9, 38, 53), 96.1379310344828), (datetime.datetime(2204, 6, 15, 9, 39, 53), 99.406779661017), (datetime.datetime(2204, 6, 15, 9, 40, 53), 97.271186440678), (datetime.datetime(2204, 6, 15, 9, 41, 53), 95.7931034482759), (datetime.datetime(2204, 6, 15, 9, 42, 53), 98.3559322033899), (datetime.datetime(2204, 6, 15, 9, 43, 53), 99.2758620689655), (datetime.datetime(2204, 6, 15, 9, 44, 53), 99.4237288135593), (datetime.datetime(2204, 6, 15, 9, 45, 53), 99.6271186440678), (datetime.datetime(2204, 6, 15, 9, 46, 53), 99.1206896551724), (datetime.datetime(2204, 6, 15, 9, 47, 53), 98.5593220338983), (datetime.datetime(2204, 6, 15, 9, 48, 53), 99.2758620689655), (datetime.datetime(2204, 6, 15, 9, 49, 53), 98.4237288135593), (datetime.datetime(2204, 6, 15, 9, 50, 53), 99.6101694915254), (datetime.datetime(2204, 6, 15, 9, 51, 53), 99.7586206896552), (datetime.datetime(2204, 6, 15, 9, 52, 53), 99.375), (datetime.datetime(2204, 6, 15, 9, 53, 53), 99.1851851851852), (datetime.datetime(2204, 6, 15, 9, 54, 53), 99.1), (datetime.datetime(2204, 6, 15, 9, 55, 53), 99.0), (datetime.datetime(2204, 6, 15, 9, 56, 53), 96.875), (datetime.datetime(2204, 6, 15, 9, 57, 53), 99.96), (datetime.datetime(2204, 6, 15, 9, 58, 53), 98.0), (datetime.datetime(2204, 6, 15, 9, 59, 53), 98.1904761904762), (datetime.datetime(2204, 6, 15, 10, 0, 53), 99.448275862069), (datetime.datetime(2204, 6, 15, 10, 1, 53), 98.9333333333333), (datetime.datetime(2204, 6, 15, 10, 2, 53), 99.2758620689655), (datetime.datetime(2204, 6, 15, 10, 3, 53), 99.0689655172414), (datetime.datetime(2204, 6, 15, 10, 4, 53), 99.1), (datetime.datetime(2204, 6, 15, 10, 5, 53), 98.6896551724138), (datetime.datetime(2204, 6, 15, 10, 6, 53), 99.0689655172414), (datetime.datetime(2204, 6, 15, 10, 7, 53), 98.7241379310345), (datetime.datetime(2204, 6, 15, 10, 8, 53), 99.0666666666667), (datetime.datetime(2204, 6, 15, 10, 9, 53), 98.6206896551724), (datetime.datetime(2204, 6, 15, 10, 10, 53), 98.2758620689655), (datetime.datetime(2204, 6, 15, 10, 11, 53), 98.0666666666667), (datetime.datetime(2204, 6, 15, 10, 12, 53), 97.3448275862069), (datetime.datetime(2204, 6, 15, 10, 13, 53), 97.4827586206897), (datetime.datetime(2204, 6, 15, 10, 14, 53), 97.7666666666667), (datetime.datetime(2204, 6, 15, 10, 15, 53), 97.4827586206897), (datetime.datetime(2204, 6, 15, 10, 16, 53), 98.1724137931035), (datetime.datetime(2204, 6, 15, 10, 17, 53), 97.7241379310345), (datetime.datetime(2204, 6, 15, 10, 18, 53), 98.4615384615385), (datetime.datetime(2204, 6, 15, 10, 19, 53), 97.8571428571429), (datetime.datetime(2204, 6, 15, 10, 20, 53), 96.7586206896552), (datetime.datetime(2204, 6, 15, 10, 21, 53), 96.95), (datetime.datetime(2204, 6, 15, 10, 22, 53), 98.0689655172414), (datetime.datetime(2204, 6, 15, 10, 23, 53), 98.0), (datetime.datetime(2204, 6, 15, 10, 46, 53), 96.1086956521739), (datetime.datetime(2204, 6, 15, 10, 47, 53), 95.406779661017), (datetime.datetime(2204, 6, 15, 10, 48, 53), 97.1694915254237), (datetime.datetime(2204, 6, 15, 10, 49, 53), 97.21875), (datetime.datetime(2204, 6, 15, 10, 50, 53), 96.7222222222222), (datetime.datetime(2204, 6, 15, 10, 51, 53), 95.0689655172414), (datetime.datetime(2204, 6, 15, 10, 52, 53), 96.6949152542373), (datetime.datetime(2204, 6, 15, 10, 53, 53), 94.9661016949152), (datetime.datetime(2204, 6, 15, 10, 54, 53), 96.2586206896552), (datetime.datetime(2204, 6, 15, 10, 55, 53), 97.5932203389831), (datetime.datetime(2204, 6, 15, 10, 56, 53), 97.0), (datetime.datetime(2204, 6, 15, 11, 0, 53), 95.3658536585366), (datetime.datetime(2204, 6, 15, 11, 1, 53), 97.3559322033898), (datetime.datetime(2204, 6, 15, 11, 2, 53), 94.8965517241379), (datetime.datetime(2204, 6, 15, 11, 3, 53), 97.271186440678), (datetime.datetime(2204, 6, 15, 11, 4, 53), 97.2033898305085), (datetime.datetime(2204, 6, 15, 11, 5, 53), 96.7758620689655), (datetime.datetime(2204, 6, 15, 11, 6, 53), 97.6101694915254), (datetime.datetime(2204, 6, 15, 11, 7, 53), 97.6724137931035), (datetime.datetime(2204, 6, 15, 11, 8, 53), 96.6779661016949), (datetime.datetime(2204, 6, 15, 11, 9, 53), 96.4915254237288), (datetime.datetime(2204, 6, 15, 11, 10, 53), 96.8103448275862), (datetime.datetime(2204, 6, 15, 11, 11, 53), 95.9152542372881), (datetime.datetime(2204, 6, 15, 11, 12, 53), 96.0517241379311), (datetime.datetime(2204, 6, 15, 11, 13, 53), 98.0), (datetime.datetime(2204, 6, 15, 11, 14, 53), 95.8), (datetime.datetime(2204, 6, 15, 11, 16, 53), 98.625), (datetime.datetime(2204, 6, 15, 11, 17, 53), 97.1186440677966), (datetime.datetime(2204, 6, 15, 11, 18, 53), 96.0862068965517), (datetime.datetime(2204, 6, 15, 11, 19, 53), 97.9830508474576), (datetime.datetime(2204, 6, 15, 11, 20, 53), 95.0), (datetime.datetime(2204, 6, 15, 11, 21, 53), 97.0), (datetime.datetime(2204, 6, 15, 11, 22, 53), 96.0), (datetime.datetime(2204, 6, 15, 11, 23, 53), 99.0), (datetime.datetime(2204, 6, 15, 11, 24, 53), 95.0), (datetime.datetime(2204, 6, 15, 11, 25, 53), 96.0), (datetime.datetime(2204, 6, 15, 11, 26, 53), 98.0), (datetime.datetime(2204, 6, 15, 11, 27, 53), 99.0), (datetime.datetime(2204, 6, 15, 11, 28, 53), 98.0), (datetime.datetime(2204, 6, 15, 11, 29, 53), 98.0), (datetime.datetime(2204, 6, 15, 11, 30, 53), 99.0), (datetime.datetime(2204, 6, 15, 11, 31, 53), 98.0), (datetime.datetime(2204, 6, 15, 11, 32, 53), 100.0), (datetime.datetime(2204, 6, 15, 11, 33, 53), 94.0), (datetime.datetime(2204, 6, 15, 11, 34, 53), 99.0), (datetime.datetime(2204, 6, 15, 11, 35, 53), 95.0), (datetime.datetime(2204, 6, 15, 11, 36, 53), 92.0), (datetime.datetime(2204, 6, 15, 11, 37, 53), 95.0), (datetime.datetime(2204, 6, 15, 11, 38, 53), 99.0), (datetime.datetime(2204, 6, 15, 11, 39, 53), 97.0), (datetime.datetime(2204, 6, 15, 11, 40, 53), 97.0), (datetime.datetime(2204, 6, 15, 11, 41, 53), 96.0), (datetime.datetime(2204, 6, 15, 11, 42, 53), 97.0), (datetime.datetime(2204, 6, 15, 11, 43, 53), 98.0), (datetime.datetime(2204, 6, 15, 11, 44, 53), 97.0), (datetime.datetime(2204, 6, 15, 11, 45, 53), 98.0), (datetime.datetime(2204, 6, 15, 11, 46, 53), 99.0), (datetime.datetime(2204, 6, 15, 11, 47, 53), 98.0)]
respiratory_rate = [(datetime.datetime(2204, 6, 15, 8, 57, 53), 15.6666666666667), (datetime.datetime(2204, 6, 15, 8, 58, 53), 14.0338983050847), (datetime.datetime(2204, 6, 15, 8, 59, 53), 13.4827586206897), (datetime.datetime(2204, 6, 15, 9, 0, 53), 15.9661016949153), (datetime.datetime(2204, 6, 15, 9, 1, 53), 16.7068965517241), (datetime.datetime(2204, 6, 15, 9, 2, 53), 16.7457627118644), (datetime.datetime(2204, 6, 15, 9, 3, 53), 19.4237288135593), (datetime.datetime(2204, 6, 15, 9, 4, 53), 17.7068965517241), (datetime.datetime(2204, 6, 15, 9, 5, 53), 19.4915254237288), (datetime.datetime(2204, 6, 15, 9, 6, 53), 15.7894736842105), (datetime.datetime(2204, 6, 15, 9, 7, 53), 16.3559322033898), (datetime.datetime(2204, 6, 15, 9, 8, 53), 16.3833333333333), (datetime.datetime(2204, 6, 15, 9, 9, 53), 15.3275862068966), (datetime.datetime(2204, 6, 15, 9, 10, 53), 17.8813559322034), (datetime.datetime(2204, 6, 15, 9, 11, 53), 16.1896551724138), (datetime.datetime(2204, 6, 15, 9, 12, 53), 16.0847457627119), (datetime.datetime(2204, 6, 15, 9, 13, 53), 15.3220338983051), (datetime.datetime(2204, 6, 15, 9, 14, 53), 15.9310344827586), (datetime.datetime(2204, 6, 15, 9, 15, 53), 14.8813559322034), (datetime.datetime(2204, 6, 15, 9, 16, 53), 16.2068965517241), (datetime.datetime(2204, 6, 15, 9, 17, 53), 15.6610169491525), (datetime.datetime(2204, 6, 15, 9, 18, 53), 16.1864406779661), (datetime.datetime(2204, 6, 15, 9, 19, 53), 16.0), (datetime.datetime(2204, 6, 15, 9, 20, 53), 15.7241379310345), (datetime.datetime(2204, 6, 15, 9, 21, 53), 14.5762711864407), (datetime.datetime(2204, 6, 15, 9, 22, 53), 16.0847457627119), (datetime.datetime(2204, 6, 15, 9, 23, 53), 15.6101694915254), (datetime.datetime(2204, 6, 15, 9, 24, 53), 14.8793103448276), (datetime.datetime(2204, 6, 15, 9, 25, 53), 14.6271186440678), (datetime.datetime(2204, 6, 15, 9, 26, 53), 17.3448275862069), (datetime.datetime(2204, 6, 15, 9, 27, 53), 15.7118644067797), (datetime.datetime(2204, 6, 15, 9, 28, 53), 16.4237288135593), (datetime.datetime(2204, 6, 15, 9, 29, 53), 16.0), (datetime.datetime(2204, 6, 15, 9, 30, 53), 17.5423728813559), (datetime.datetime(2204, 6, 15, 9, 31, 53), 13.859649122807), (datetime.datetime(2204, 6, 15, 9, 32, 53), 14.3833333333333), (datetime.datetime(2204, 6, 15, 9, 33, 53), 14.4310344827586), (datetime.datetime(2204, 6, 15, 9, 34, 53), 14.5762711864407), (datetime.datetime(2204, 6, 15, 9, 35, 53), 15.3389830508475), (datetime.datetime(2204, 6, 15, 9, 36, 53), 15.4827586206897), (datetime.datetime(2204, 6, 15, 9, 37, 53), 15.4406779661017), (datetime.datetime(2204, 6, 15, 9, 38, 53), 14.7758620689655), (datetime.datetime(2204, 6, 15, 9, 39, 53), 13.5423728813559), (datetime.datetime(2204, 6, 15, 9, 40, 53), 15.3050847457627), (datetime.datetime(2204, 6, 15, 9, 41, 53), 16.4310344827586), (datetime.datetime(2204, 6, 15, 9, 42, 53), 14.271186440678), (datetime.datetime(2204, 6, 15, 9, 43, 53), 15.551724137931), (datetime.datetime(2204, 6, 15, 9, 44, 53), 13.7058823529412), (datetime.datetime(2204, 6, 15, 9, 45, 53), 10.5789473684211), (datetime.datetime(2204, 6, 15, 9, 46, 53), 14.8275862068966), (datetime.datetime(2204, 6, 15, 9, 47, 53), 17.4745762711864), (datetime.datetime(2204, 6, 15, 9, 48, 53), 15.6206896551724), (datetime.datetime(2204, 6, 15, 9, 49, 53), 15.0677966101695), (datetime.datetime(2204, 6, 15, 9, 50, 53), 15.5084745762712), (datetime.datetime(2204, 6, 15, 9, 51, 53), 16.8793103448276), (datetime.datetime(2204, 6, 15, 9, 52, 53), 14.7291666666667), (datetime.datetime(2204, 6, 15, 9, 53, 53), 15.2222222222222), (datetime.datetime(2204, 6, 15, 9, 54, 53), 15.7666666666667), (datetime.datetime(2204, 6, 15, 9, 55, 53), 15.2758620689655), (datetime.datetime(2204, 6, 15, 9, 56, 53), 16.0344827586207), (datetime.datetime(2204, 6, 15, 9, 57, 53), 14.9333333333333), (datetime.datetime(2204, 6, 15, 9, 58, 53), 17.5172413793103), (datetime.datetime(2204, 6, 15, 9, 59, 53), 18.2413793103448), (datetime.datetime(2204, 6, 15, 10, 0, 53), 14.6551724137931), (datetime.datetime(2204, 6, 15, 10, 1, 53), 14.4666666666667), (datetime.datetime(2204, 6, 15, 10, 2, 53), 14.7931034482759), (datetime.datetime(2204, 6, 15, 10, 3, 53), 14.6206896551724), (datetime.datetime(2204, 6, 15, 10, 4, 53), 15.3666666666667), (datetime.datetime(2204, 6, 15, 10, 5, 53), 14.4827586206897), (datetime.datetime(2204, 6, 15, 10, 6, 53), 14.8275862068966), (datetime.datetime(2204, 6, 15, 10, 7, 53), 14.7241379310345), (datetime.datetime(2204, 6, 15, 10, 8, 53), 14.7), (datetime.datetime(2204, 6, 15, 10, 9, 53), 15.2413793103448), (datetime.datetime(2204, 6, 15, 10, 10, 53), 15.0344827586207), (datetime.datetime(2204, 6, 15, 10, 11, 53), 17.2), (datetime.datetime(2204, 6, 15, 10, 12, 53), 16.8275862068966), (datetime.datetime(2204, 6, 15, 10, 13, 53), 16.9310344827586), (datetime.datetime(2204, 6, 15, 10, 14, 53), 16.2666666666667), (datetime.datetime(2204, 6, 15, 10, 15, 53), 15.1724137931034), (datetime.datetime(2204, 6, 15, 10, 16, 53), 17.1724137931035), (datetime.datetime(2204, 6, 15, 10, 17, 53), 18.3103448275862), (datetime.datetime(2204, 6, 15, 10, 18, 53), 16.7), (datetime.datetime(2204, 6, 15, 10, 19, 53), 21.5862068965517), (datetime.datetime(2204, 6, 15, 10, 20, 53), 17.0344827586207), (datetime.datetime(2204, 6, 15, 10, 21, 53), 17.8666666666667), (datetime.datetime(2204, 6, 15, 10, 22, 53), 16.8965517241379), (datetime.datetime(2204, 6, 15, 10, 23, 53), 16.4166666666667), (datetime.datetime(2204, 6, 15, 10, 36, 53), 17.0), (datetime.datetime(2204, 6, 15, 10, 37, 53), 17.0), (datetime.datetime(2204, 6, 15, 10, 38, 53), 17.0), (datetime.datetime(2204, 6, 15, 10, 46, 53), 18.0576923076923), (datetime.datetime(2204, 6, 15, 10, 47, 53), 15.2542372881356), (datetime.datetime(2204, 6, 15, 10, 48, 53), 15.1186440677966), (datetime.datetime(2204, 6, 15, 10, 49, 53), 16.0), (datetime.datetime(2204, 6, 15, 10, 50, 53), 18.1333333333333), (datetime.datetime(2204, 6, 15, 10, 51, 53), 15.2068965517241), (datetime.datetime(2204, 6, 15, 10, 52, 53), 16.7627118644068), (datetime.datetime(2204, 6, 15, 10, 53, 53), 15.3050847457627), (datetime.datetime(2204, 6, 15, 10, 54, 53), 15.551724137931), (datetime.datetime(2204, 6, 15, 10, 55, 53), 14.9322033898305), (datetime.datetime(2204, 6, 15, 10, 56, 53), 15.6111111111111), (datetime.datetime(2204, 6, 15, 10, 57, 53), 16.0), (datetime.datetime(2204, 6, 15, 10, 59, 53), 16.0), (datetime.datetime(2204, 6, 15, 11, 0, 53), 11.4594594594595), (datetime.datetime(2204, 6, 15, 11, 1, 53), 16.2203389830508), (datetime.datetime(2204, 6, 15, 11, 2, 53), 15.7413793103448), (datetime.datetime(2204, 6, 15, 11, 3, 53), 15.6949152542373), (datetime.datetime(2204, 6, 15, 11, 4, 53), 14.9491525423729), (datetime.datetime(2204, 6, 15, 11, 5, 53), 15.551724137931), (datetime.datetime(2204, 6, 15, 11, 6, 53), 15.6949152542373), (datetime.datetime(2204, 6, 15, 11, 7, 53), 15.3103448275862), (datetime.datetime(2204, 6, 15, 11, 8, 53), 15.3389830508475), (datetime.datetime(2204, 6, 15, 11, 9, 53), 14.7457627118644), (datetime.datetime(2204, 6, 15, 11, 10, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 11, 53), 16.5932203389831), (datetime.datetime(2204, 6, 15, 11, 12, 53), 15.8103448275862), (datetime.datetime(2204, 6, 15, 11, 13, 53), 14.4576271186441), (datetime.datetime(2204, 6, 15, 11, 14, 53), 16.0), (datetime.datetime(2204, 6, 15, 11, 16, 53), 16.4444444444444), (datetime.datetime(2204, 6, 15, 11, 17, 53), 15.5254237288136), (datetime.datetime(2204, 6, 15, 11, 18, 53), 15.8863636363636), (datetime.datetime(2204, 6, 15, 11, 19, 53), 14.5932203389831), (datetime.datetime(2204, 6, 15, 11, 20, 53), 17.0), (datetime.datetime(2204, 6, 15, 11, 21, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 22, 53), 17.0), (datetime.datetime(2204, 6, 15, 11, 23, 53), 14.0), (datetime.datetime(2204, 6, 15, 11, 24, 53), 18.0), (datetime.datetime(2204, 6, 15, 11, 25, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 26, 53), 14.0), (datetime.datetime(2204, 6, 15, 11, 27, 53), 14.0), (datetime.datetime(2204, 6, 15, 11, 28, 53), 17.0), (datetime.datetime(2204, 6, 15, 11, 29, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 30, 53), 12.0), (datetime.datetime(2204, 6, 15, 11, 31, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 32, 53), 14.0), (datetime.datetime(2204, 6, 15, 11, 33, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 34, 53), 16.0), (datetime.datetime(2204, 6, 15, 11, 35, 53), 18.0), (datetime.datetime(2204, 6, 15, 11, 36, 53), 18.0), (datetime.datetime(2204, 6, 15, 11, 37, 53), 16.0), (datetime.datetime(2204, 6, 15, 11, 38, 53), 16.0), (datetime.datetime(2204, 6, 15, 11, 39, 53), 17.0), (datetime.datetime(2204, 6, 15, 11, 40, 53), 14.0), (datetime.datetime(2204, 6, 15, 11, 41, 53), 18.0), (datetime.datetime(2204, 6, 15, 11, 42, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 43, 53), 13.0), (datetime.datetime(2204, 6, 15, 11, 44, 53), 15.0), (datetime.datetime(2204, 6, 15, 11, 45, 53), 13.0), (datetime.datetime(2204, 6, 15, 11, 46, 53), 13.0), (datetime.datetime(2204, 6, 15, 11, 47, 53), 18.0)]
temperature = [(datetime.datetime(2204, 6, 15, 8, 57, 53), 34.888888888888886), (datetime.datetime(2204, 6, 15, 11, 19, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 20, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 21, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 22, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 23, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 24, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 25, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 26, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 27, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 28, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 29, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 30, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 31, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 32, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 33, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 34, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 35, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 36, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 37, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 38, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 39, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 40, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 41, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 42, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 43, 53), 35.0), (datetime.datetime(2204, 6, 15, 11, 44, 53), 35.111111111111114), (datetime.datetime(2204, 6, 15, 11, 45, 53), 35.111111111111114), (datetime.datetime(2204, 6, 15, 11, 46, 53), 35.111111111111114), (datetime.datetime(2204, 6, 15, 11, 47, 53), 35.111111111111114)]
# Previous Results
shock_index = 0.607
shock_index_interpretation = 'Normal (0.61), within reference range 0.5-0.7. No hemodynamic instability indicated.'
map_value = 84.0
map_interpretation = 'Normal (84 mmHg), within reference range 65-100 mmHg. Adequate perfusion pressure maintained.'
pulse_pressure = 51.0
qsofa_score = 1
qsofa_interpretation = 'Moderate Risk (Score 1/3). Criteria met: SBP=97. Monitor closely.'
sirs = 1
spo2_trend = {'first': np.float64(99.2), 'last': np.float64(98.0), 'min': 86.0, 'mean': 97.9, 'slope': np.float64(-0.0154), 'r_squared': np.float64(0.133), 'trend_pct': np.float64(-2.26)}
hr_volatility = {'dispersion_ms': 56.35, 'rmssd_ms': 54.75, 'hr_std_bpm': 4.38, 'hr_range_bpm': 31.2, 'n_samples': 146, 'data_density': 'sparse'}
triage_vital_panel = 'Attached'

# --- Generated Code Starts Here ---
result = {}
interpretation = {}

def _extract(series):
    t = [x[0] for x in series]
    v = [float(x[1]) for x in series]
    return (t, v)

def _pair_by_nearest(t_ref, v_ref, t_other, v_other, tol_min=2.0):
    pairs_t = []
    pairs_ref = []
    pairs_other = []
    j = 0
    n_other = len(t_other)
    for i in range(len(t_ref)):
        tr = t_ref[i]
        while j + 1 < n_other and t_other[j + 1] <= tr:
            j += 1
        best_k = None
        best_dt = None
        for k in (j, j + 1):
            if 0 <= k < n_other:
                dt_min = abs((t_other[k] - tr).total_seconds()) / 60.0
                if best_dt is None or dt_min < best_dt:
                    best_dt = dt_min
                    best_k = k
        if best_k is not None and best_dt is not None and (best_dt <= tol_min):
            pairs_t.append(tr)
            pairs_ref.append(v_ref[i])
            pairs_other.append(v_other[best_k])
    return (pairs_t, np.array(pairs_ref, dtype=float), np.array(pairs_other, dtype=float))

def _rolling_corr(x, y, win):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = min(len(x), len(y))
    x = x[:n]
    y = y[:n]
    if n < max(3, win):
        return np.array([], dtype=float)
    out = np.full(n, np.nan, dtype=float)
    for i in range(win - 1, n):
        xs = x[i - win + 1:i + 1]
        ys = y[i - win + 1:i + 1]
        if np.nanstd(xs) == 0.0 or np.nanstd(ys) == 0.0:
            out[i] = np.nan
        else:
            out[i] = np.corrcoef(xs, ys)[0, 1]
    return out

def _pearsonr_safe(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x = x[mask]
    y = y[mask]
    if len(x) < 3:
        return (np.nan, np.nan, 0)
    if np.std(x) == 0.0 or np.std(y) == 0.0:
        return (np.nan, np.nan, len(x))
    r, p = stats.pearsonr(x, y)
    return (float(r), float(p), int(len(x)))

def _best_lag_xcorr(t_spo2, v_spo2, t_other, v_other, max_lag_min=2.0, step_s=10.0, pair_tol_min=0.5):
    lags_min = np.arange(-max_lag_min, max_lag_min + 1e-09, step_s / 60.0, dtype=float)
    best = {'lag_min': np.nan, 'r': np.nan, 'p': np.nan, 'n_pairs': 0}
    all_r = []
    all_n = []
    for lag in lags_min:
        t_shift = [ti + np.timedelta64(int(round(lag * 60.0)), 's') for ti in t_other]
        lag_td = t_other[0] - t_other[0]
        try:
            import_fail = False
        except Exception:
            import_fail = True
        if len(t_other) == 0:
            continue
        try:
            delta0 = t_other[0] - t_other[0]
            td_cls = delta0.__class__
            lag_td = td_cls(seconds=float(lag * 60.0))
            t_shift = [ti + lag_td for ti in t_other]
        except Exception:
            t_shift = t_other
        tp, xs, ys = _pair_by_nearest(t_spo2, v_spo2, t_shift, v_other, tol_min=pair_tol_min)
        r, p, n = _pearsonr_safe(xs, ys)
        all_r.append(r)
        all_n.append(n)
        if n > 0 and np.isfinite(r):
            if not np.isfinite(best['r']) or abs(r) > abs(best['r']) or (abs(r) == abs(best['r']) and n > best['n_pairs']):
                best = {'lag_min': float(lag), 'r': float(r), 'p': float(p), 'n_pairs': int(n)}
    return (lags_min, np.array(all_r, dtype=float), np.array(all_n, dtype=int), best)

def _suggest_window_by_5min(t_pairs, default_win=15):
    if len(t_pairs) < 3:
        return int(default_win)
    dts = []
    for i in range(1, len(t_pairs)):
        dts.append((t_pairs[i] - t_pairs[i - 1]).total_seconds() / 60.0)
    dts = np.array(dts, dtype=float)
    dts = dts[np.isfinite(dts) & (dts > 0)]
    if len(dts) == 0:
        return int(default_win)
    med_dt = float(np.median(dts))
    if med_dt <= 0:
        return int(default_win)
    target = 5.0 / med_dt
    cand = [10, 12, 15, 18, 20]
    win = min(cand, key=lambda w: abs(w - target))
    return int(win)

def _summarize_coupling(name, best_lag, roll_corr, win, n_pairs):
    rr = best_lag['r']
    lag = best_lag['lag_min']
    if np.isfinite(rr):
        strength = 'weak'
        if abs(rr) >= 0.7:
            strength = 'strong'
        elif abs(rr) >= 0.4:
            strength = 'moderate'
        direction = 'positive' if rr > 0 else 'negative'
        roll_med = float(np.nanmedian(roll_corr)) if len(roll_corr) else np.nan
        roll_iqr = float(np.nanpercentile(roll_corr, 75) - np.nanpercentile(roll_corr, 25)) if len(roll_corr) else np.nan
        roll_text = ''
        if np.isfinite(roll_med) and np.isfinite(roll_iqr):
            roll_text = f' Rolling corr median {roll_med:.2f} (IQR {roll_iqr:.2f}) with window {win} samples.'
        return f'{name}: best-lag cross-correlation within ±2 min is {strength} {direction} (r={rr:.2f}) at lag {lag:+.2f} min (n={n_pairs}).{roll_text} Interpreting consistent co-movement vs artifact depends on stability of rolling correlation and plausible directionality.'
    else:
        return f'{name}: insufficient paired data for reliable coupling (n={n_pairs}); rolling correlation window {win} samples may be unstable, favoring artifact/nonstationarity assessment.'
t_spo2, v_spo2 = _extract(spo2)
t_rr, v_rr = _extract(respiratory_rate)
t_hr, v_hr = _extract(heart_rate)
t_p_rr, x_sp_rr, y_rr = _pair_by_nearest(t_spo2, v_spo2, t_rr, v_rr, tol_min=2.0)
t_p_hr, x_sp_hr, y_hr = _pair_by_nearest(t_spo2, v_spo2, t_hr, v_hr, tol_min=2.0)
win_rr = _suggest_window_by_5min(t_p_rr, default_win=15)
win_hr = _suggest_window_by_5min(t_p_hr, default_win=15)
roll_rr = _rolling_corr(x_sp_rr, y_rr, win_rr)
roll_hr = _rolling_corr(x_sp_hr, y_hr, win_hr)
lags_rr, r_by_lag_rr, n_by_lag_rr, best_rr = _best_lag_xcorr(t_spo2, v_spo2, t_rr, v_rr, max_lag_min=2.0, step_s=10.0, pair_tol_min=0.5)
lags_hr, r_by_lag_hr, n_by_lag_hr, best_hr = _best_lag_xcorr(t_spo2, v_spo2, t_hr, v_hr, max_lag_min=2.0, step_s=10.0, pair_tol_min=0.5)
fig, axes = plt.subplots(2, 1, sharex=False, figsize=(10, 7))
axes[0].plot(t_p_rr, roll_rr, color='tab:blue', linewidth=1.5)
axes[0].axhline(0.0, color='black', linewidth=0.8, alpha=0.6)
axes[0].set_title(f'Rolling correlation (window={win_rr} samples): SpO₂ vs RR (paired within ±2 min)')
axes[0].set_ylabel('Pearson r')
axes[0].set_ylim(-1.05, 1.05)
axes[0].grid(True, alpha=0.25)
axes[1].plot(t_p_hr, roll_hr, color='tab:purple', linewidth=1.5)
axes[1].axhline(0.0, color='black', linewidth=0.8, alpha=0.6)
axes[1].set_title(f'Rolling correlation (window={win_hr} samples): SpO₂ vs HR (paired within ±2 min)')
axes[1].set_ylabel('Pearson r')
axes[1].set_ylim(-1.05, 1.05)
axes[1].grid(True, alpha=0.25)
plt.tight_layout()
save_plot('coupling_rolling_correlation.png', fig=fig)
fig2, axes2 = plt.subplots(2, 1, sharex=True, figsize=(10, 7))
axes2[0].plot(lags_rr, r_by_lag_rr, color='tab:blue', linewidth=1.5)
if np.isfinite(best_rr['r']):
    axes2[0].axvline(best_rr['lag_min'], color='tab:red', linestyle='--', linewidth=1.2)
    axes2[0].scatter([best_rr['lag_min']], [best_rr['r']], color='tab:red', zorder=3)
axes2[0].axhline(0.0, color='black', linewidth=0.8, alpha=0.6)
axes2[0].set_title('Best-lag cross-correlation (SpO₂ vs RR) within ±2 min')
axes2[0].set_ylabel('Pearson r')
axes2[0].set_ylim(-1.05, 1.05)
axes2[0].grid(True, alpha=0.25)
axes2[1].plot(lags_hr, r_by_lag_hr, color='tab:purple', linewidth=1.5)
if np.isfinite(best_hr['r']):
    axes2[1].axvline(best_hr['lag_min'], color='tab:red', linestyle='--', linewidth=1.2)
    axes2[1].scatter([best_hr['lag_min']], [best_hr['r']], color='tab:red', zorder=3)
axes2[1].axhline(0.0, color='black', linewidth=0.8, alpha=0.6)
axes2[1].set_title('Best-lag cross-correlation (SpO₂ vs HR) within ±2 min')
axes2[1].set_xlabel('Lag (minutes)  [positive = other occurs later than SpO₂]')
axes2[1].set_ylabel('Pearson r')
axes2[1].set_ylim(-1.05, 1.05)
axes2[1].grid(True, alpha=0.25)
plt.tight_layout()
save_plot('coupling_best_lag_xcorr.png', fig=fig2)
result = {'spo2_rr': {'paired_n': int(len(x_sp_rr)), 'rolling_window_samples': int(win_rr), 'rolling_corr': {'median': float(np.nanmedian(roll_rr)) if len(roll_rr) else np.nan, 'iqr': float(np.nanpercentile(roll_rr, 75) - np.nanpercentile(roll_rr, 25)) if len(roll_rr) else np.nan, 'min': float(np.nanmin(roll_rr)) if len(roll_rr) else np.nan, 'max': float(np.nanmax(roll_rr)) if len(roll_rr) else np.nan}, 'best_lag_xcorr': best_rr, 'lag_scan': {'lags_min': lags_rr, 'r_by_lag': r_by_lag_rr, 'n_pairs_by_lag': n_by_lag_rr}}, 'spo2_hr': {'paired_n': int(len(x_sp_hr)), 'rolling_window_samples': int(win_hr), 'rolling_corr': {'median': float(np.nanmedian(roll_hr)) if len(roll_hr) else np.nan, 'iqr': float(np.nanpercentile(roll_hr, 75) - np.nanpercentile(roll_hr, 25)) if len(roll_hr) else np.nan, 'min': float(np.nanmin(roll_hr)) if len(roll_hr) else np.nan, 'max': float(np.nanmax(roll_hr)) if len(roll_hr) else np.nan}, 'best_lag_xcorr': best_hr, 'lag_scan': {'lags_min': lags_hr, 'r_by_lag': r_by_lag_hr, 'n_pairs_by_lag': n_by_lag_hr}}}
interpretation = {'spo2_vs_rr_coupling': _summarize_coupling('SpO₂ vs RR', best_rr, roll_rr, win_rr, int(len(x_sp_rr))), 'spo2_vs_hr_coupling': _summarize_coupling('SpO₂ vs HR', best_hr, roll_hr, win_hr, int(len(x_sp_hr)))}

plt.close()