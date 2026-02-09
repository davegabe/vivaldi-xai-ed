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
plot_event-locked_desaturation_episodes:_spo₂_time_axis_with_segments_<92%_and_<88%_highlighted,_overlaid_with_hr_and_rr_on_the_same_time_axis. = None
create_an_episode_summary_table_for_each_spo₂_<92%_event:_start/end_time,_nadir_spo₂,_minutes_below_92%_and_88%,_δhr_and_δrr_from_2_minutes_pre-event_baseline_to_event_nadir. = None
plot_coupling_diagnostics:_rolling_correlation_(and_best-lag_cross-correlation_within_±2_minutes)_for_spo₂_vs_rr_and_spo₂_vs_hr_using_a_10–20_sample_window_(or_nearest_to_5_minutes),_to_identify_consistent_physiologic_co-movement_vs_artifact. = None

# --- Generated Code Starts Here ---
result = {}
interpretation = {}

def _to_arrays(series):
    if series is None or len(series) == 0:
        return (np.array([]), np.array([]))
    t = np.array([x[0] for x in series], dtype=object)
    v = np.array([float(x[1]) for x in series], dtype=float)
    return (t, v)

def _interp_nearest(tq, t_src, v_src, max_gap_minutes=None):
    tq = np.array(list(tq), dtype=object)
    if tq.size == 0 or t_src.size == 0:
        return np.full(tq.shape, np.nan, dtype=float)
    out = np.full(tq.shape, np.nan, dtype=float)
    for i, t in enumerate(tq):
        j = int(np.argmin(np.array([abs((ts - t).total_seconds()) for ts in t_src], dtype=float)))
        dt_min = abs((t_src[j] - t).total_seconds()) / 60.0
        if max_gap_minutes is None or dt_min <= max_gap_minutes:
            out[i] = float(v_src[j])
    return out

def _step_hold(t_src, v_src, t_grid):
    if t_src.size == 0 or t_grid.size == 0:
        return np.full(t_grid.shape, np.nan, dtype=float)
    out = np.full(t_grid.shape, np.nan, dtype=float)
    j = 0
    last = np.nan
    for i, tg in enumerate(t_grid):
        while j < t_src.size and t_src[j] <= tg:
            last = float(v_src[j])
            j += 1
        out[i] = last
    return out

def _run_lengths(mask):
    mask = np.asarray(mask, dtype=bool)
    if mask.size == 0:
        return []
    d = np.diff(mask.astype(int))
    starts = np.where(d == 1)[0] + 1
    ends = np.where(d == -1)[0]
    if mask[0]:
        starts = np.r_[0, starts]
    if mask[-1]:
        ends = np.r_[ends, mask.size - 1]
    return list(zip(starts.tolist(), ends.tolist()))
t_hr, v_hr = _to_arrays(heart_rate)
t_sp, v_sp = _to_arrays(spo2)
t_rr, v_rr = _to_arrays(respiratory_rate)
t_sbp, v_sbp = _to_arrays(systolic_bp)
t_dbp, v_dbp = _to_arrays(diastolic_bp)
bp_pairs = []
if t_sbp.size and t_dbp.size:
    for i in range(t_sbp.size):
        j = int(np.argmin(np.array([abs((td - t_sbp[i]).total_seconds()) for td in t_dbp], dtype=float)))
        dt = abs((t_dbp[j] - t_sbp[i]).total_seconds()) / 60.0
        if dt <= 5.0:
            sbp = float(v_sbp[i])
            dbp = float(v_dbp[j])
            map_i = (sbp + 2.0 * dbp) / 3.0
            bp_pairs.append((t_sbp[i], sbp, dbp, map_i))
if not bp_pairs and t_dbp.size:
    for i in range(t_dbp.size):
        bp_pairs.append((t_dbp[i], np.nan, float(v_dbp[i]), np.nan))
bp_pairs = sorted(bp_pairs, key=lambda x: x[0])
t_bp = np.array([x[0] for x in bp_pairs], dtype=object) if bp_pairs else np.array([], dtype=object)
map_bp = np.array([x[3] for x in bp_pairs], dtype=float) if bp_pairs else np.array([], dtype=float)
t_grid = t_sp
sp_grid = v_sp
hr_on_sp = _interp_nearest(t_grid, t_hr, v_hr, max_gap_minutes=5.0)
rr_on_sp = _interp_nearest(t_grid, t_rr, v_rr, max_gap_minutes=5.0)
valid = np.isfinite(sp_grid) & np.isfinite(hr_on_sp) & np.isfinite(rr_on_sp)
sp_v = sp_grid[valid]
hr_v = hr_on_sp[valid]
rr_v = rr_on_sp[valid]
t_v = t_grid[valid]
hr_on_bp = _interp_nearest(t_bp, t_hr, v_hr, max_gap_minutes=10.0) if t_bp.size else np.array([], dtype=float)
sp_on_bp = _interp_nearest(t_bp, t_sp, v_sp, max_gap_minutes=10.0) if t_bp.size else np.array([], dtype=float)
rr_on_bp = _interp_nearest(t_bp, t_rr, v_rr, max_gap_minutes=10.0) if t_bp.size else np.array([], dtype=float)
episodes = []
if t_sp.size >= 2:
    desat_mask = v_sp < 92.0
    segs = _run_lengths(desat_mask)
    for s, e in segs:
        dur_min = (t_sp[e] - t_sp[s]).total_seconds() / 60.0 if e > s else 0.0
        nadir = float(np.min(v_sp[s:e + 1]))
        episodes.append((dur_min, s, e, nadir))
episodes = sorted(episodes, key=lambda x: (x[0], -x[3]), reverse=True)
top_eps = episodes[:3]
fig1, ax1 = plt.subplots(1, 1, figsize=(10, 7))
if sp_v.size:
    sc = ax1.scatter(sp_v, hr_v, c=rr_v, cmap='viridis', s=22, alpha=0.75, edgecolors='none')
    cbar = plt.colorbar(sc, ax=ax1)
    cbar.set_label('Respiratory rate (breaths/min)')
else:
    ax1.text(0.5, 0.5, 'Insufficient aligned HR/SpO₂/RR samples for phase-space', ha='center', va='center', transform=ax1.transAxes)
if t_bp.size and np.any(np.isfinite(sp_on_bp)) and np.any(np.isfinite(hr_on_bp)):
    vbpm = np.isfinite(sp_on_bp) & np.isfinite(hr_on_bp)
    ax1.scatter(sp_on_bp[vbpm], hr_on_bp[vbpm], s=90, facecolors='none', edgecolors='black', linewidths=1.4, marker='o', label='BP timestamps (nearest HR/SpO₂)')
    if map_bp.size and np.any(np.isfinite(map_bp[vbpm])):
        for x, y, m in zip(sp_on_bp[vbpm], hr_on_bp[vbpm], map_bp[vbpm]):
            if np.isfinite(m):
                ax1.annotate(f'{m:.0f}', (x, y), textcoords='offset points', xytext=(4, 4), fontsize=8, color='black', alpha=0.85)
ax1.set_xlabel('SpO₂ (%)')
ax1.set_ylabel('Heart rate (bpm)')
ax1.set_title('Hemodynamic–respiratory phase-space: HR vs SpO₂ (colored by RR)\nBP timestamps overlaid (marker labels = MAP mmHg when available)')
ax1.grid(True, alpha=0.25)
ax1.legend(loc='best', frameon=True)
save_plot('phase_space_hr_spo2_colored_by_rr_with_bp_markers.png', fig=fig1)
n_ep = len(top_eps)
if n_ep == 0:
    fig2, ax = plt.subplots(1, 1, figsize=(12, 3.5))
    ax.text(0.5, 0.5, 'No SpO₂ <92% episodes detected for desaturation-window composite', ha='center', va='center', transform=ax.transAxes)
    ax.axis('off')
    save_plot('desat_window_composite_with_step_hold_map.png', fig=fig2)
else:
    fig2, axes = plt.subplots(n_ep, 1, figsize=(12, 3.6 * n_ep), sharex=False)
    if n_ep == 1:
        axes = [axes]
    for k, (dur_min, s, e, nadir) in enumerate(top_eps):
        ax = axes[k]
        t_start = t_sp[s]
        t_end = t_sp[e]
        w0 = t_start - np.timedelta64(10, 'm') if isinstance(t_start, np.datetime64) else t_start - __import__('datetime').timedelta(minutes=10)
        w1 = t_end + np.timedelta64(15, 'm') if isinstance(t_end, np.datetime64) else t_end + __import__('datetime').timedelta(minutes=15)

        def _window(t, v):
            if t.size == 0:
                return (np.array([], dtype=object), np.array([], dtype=float))
            m = np.array([ti >= w0 and ti <= w1 for ti in t], dtype=bool)
            return (t[m], v[m])
        tw_sp, vw_sp = _window(t_sp, v_sp)
        tw_hr, vw_hr = _window(t_hr, v_hr)
        tw_rr, vw_rr = _window(t_rr, v_rr)
        tw_bp = np.array([ti for ti in t_bp if ti >= w0 and ti <= w1], dtype=object) if t_bp.size else np.array([], dtype=object)
        mw_bp = np.array([map_bp[i] for i in range(map_bp.size) if t_bp[i] >= w0 and t_bp[i] <= w1], dtype=float) if t_bp.size else np.array([], dtype=float)
        t_plot = tw_sp if tw_sp.size else tw_hr if tw_hr.size else tw_rr if tw_rr.size else tw_bp
        if t_plot.size == 0:
            ax.text(0.5, 0.5, 'No data in selected window', ha='center', va='center', transform=ax.transAxes)
            ax.axis('off')
            continue
        map_step = _step_hold(t_bp, map_bp, t_plot) if t_bp.size else np.full(t_plot.shape, np.nan, dtype=float)
        if tw_sp.size:
            ax.plot(tw_sp, vw_sp, color='#1f77b4', linewidth=1.8, label='SpO₂ (%)')
            ax.fill_between(tw_sp, vw_sp, 92.0, where=vw_sp < 92.0, color='#1f77b4', alpha=0.12, step=None)
            ax.axhline(92.0, color='#1f77b4', linestyle='--', linewidth=1.0, alpha=0.6)
            ax.fill_between(tw_sp, vw_sp, 88.0, where=vw_sp < 88.0, color='crimson', alpha=0.1, step=None)
            ax.axhline(88.0, color='crimson', linestyle='--', linewidth=1.0, alpha=0.5)
        ax2 = ax.twinx()
        if tw_hr.size:
            ax2.plot(tw_hr, vw_hr, color='#ff7f0e', linewidth=1.4, alpha=0.9, label='HR (bpm)')
        if tw_rr.size:
            ax2.plot(tw_rr, vw_rr, color='#2ca02c', linewidth=1.4, alpha=0.85, label='RR (br/min)')
        ax3 = ax.twinx()
        ax3.spines['right'].set_position(('axes', 1.1))
        ax3.set_frame_on(True)
        ax3.patch.set_visible(False)
        for spn in ax3.spines.values():
            spn.set_visible(True)
        if np.any(np.isfinite(map_step)):
            ax3.step(t_plot, map_step, where='post', color='black', linewidth=1.6, alpha=0.8, label='MAP step-hold (mmHg)')
        if tw_bp.size and mw_bp.size:
            vb = np.isfinite(mw_bp)
            if np.any(vb):
                ax3.scatter(tw_bp[vb], mw_bp[vb], color='black', s=28, marker='x', linewidths=1.2, label='BP measurement (MAP)')
        ax.axvspan(t_start, t_end, color='gray', alpha=0.12, label='SpO₂<92% episode')
        ax.set_ylabel('SpO₂ (%)')
        ax2.set_ylabel('HR (bpm) / RR (breaths/min)')
        ax3.set_ylabel('MAP (mmHg)')
        ax.set_title(f'Desaturation-window composite #{k + 1}: duration {dur_min:.1f} min, nadir SpO₂ {nadir:.0f}%')
        ax.grid(True, alpha=0.22)
        h1, l1 = ax.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        h3, l3 = ax3.get_legend_handles_labels()
        seen = set()
        handles = []
        labels = []
        for h, lab in list(zip(h1, l1)) + list(zip(h2, l2)) + list(zip(h3, l3)):
            if lab not in seen and lab.strip() != '':
                handles.append(h)
                labels.append(lab)
                seen.add(lab)
        ax.legend(handles, labels, loc='upper left', frameon=True, fontsize=9)
    fig2.tight_layout()
    save_plot('desat_window_composite_with_step_hold_map.png', fig=fig2)
result['shock_index'] = float(shock_index)
result['map_value_mmHg'] = float(map_value)
result['pulse_pressure_mmHg'] = float(pulse_pressure)
result['qsofa_score'] = int(qsofa_score)
result['sirs'] = int(sirs)
result['spo2_trend'] = spo2_trend
result['hr_volatility'] = hr_volatility
result['plots'] = {'phase_space': 'phase_space_hr_spo2_colored_by_rr_with_bp_markers.png', 'desat_window_composite': 'desat_window_composite_with_step_hold_map.png'}
interpretation['shock_index'] = shock_index_interpretation
interpretation['map'] = map_interpretation
interpretation['qsofa'] = qsofa_interpretation
interpretation['desaturation_summary'] = f'SpO₂ shows intermittent desaturation with nadir {spo2_trend.get('min', np.nan):.0f}% and overall trend slope {float(spo2_trend.get('slope', np.nan)):.4f} %/sample; phase-space and desat-window composites saved to evaluate coupling with RR/HR and coincident MAP step-holds.'

plt.close()