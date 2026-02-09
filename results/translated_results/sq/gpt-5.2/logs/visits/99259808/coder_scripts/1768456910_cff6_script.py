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
# CORRUPTED VAR REMOVED: plot_event-locked_desaturation_episodes:_spo₂_time_axis_with_segments_<92%_and_<88%_highlighted,_overlaid_with_hr_and_rr_on_the_same_time_axis. = None
# CORRUPTED VAR REMOVED: create_an_episode_summary_table_for_each_spo₂_<92%_event:_start/end_time,_nadir_spo₂,_minutes_below_92%_and_88%,_δhr_and_δrr_from_2_minutes_pre-event_baseline_to_event_nadir. = None
# CORRUPTED VAR REMOVED: plot_coupling_diagnostics:_rolling_correlation_(and_best-lag_cross-correlation_within_±2_minutes)_for_spo₂_vs_rr_and_spo₂_vs_hr_using_a_10–20_sample_window_(or_nearest_to_5_minutes),_to_identify_consistent_physiologic_co-movement_vs_artifact. = None

# --- Generated Code Starts Here ---
def _to_arrays(ts_list):
    t = [x[0] for x in ts_list]
    v = np.array([float(x[1]) for x in ts_list], dtype=float)
    return (t, v)

def _nearest_value_at_or_before(t_list, v_arr, t_query):
    n = len(t_list)
    if n == 0:
        return (np.nan, None)
    lo, hi = (0, n - 1)
    if t_query < t_list[0]:
        return (np.nan, None)
    while lo <= hi:
        mid = (lo + hi) // 2
        if t_list[mid] <= t_query:
            lo = mid + 1
        else:
            hi = mid - 1
    idx = hi
    return (float(v_arr[idx]), idx)

def _values_in_window(t_list, v_arr, t_start, t_end):
    n = len(t_list)
    if n == 0:
        return ([], np.array([], dtype=float))
    lo, hi = (0, n)
    while lo < hi:
        mid = (lo + hi) // 2
        if t_list[mid] < t_start:
            lo = mid + 1
        else:
            hi = mid
    left = lo
    lo, hi = (left, n)
    while lo < hi:
        mid = (lo + hi) // 2
        if t_list[mid] <= t_end:
            lo = mid + 1
        else:
            hi = mid
    right = lo
    return (t_list[left:right], v_arr[left:right])

def _minutes(dt):
    return dt.total_seconds() / 60.0

def _compute_event_metrics(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, start_time, end_time, nadir_idx, recovery_threshold=95.0):
    nadir_time = spo2_t[nadir_idx]
    nadir_spo2 = float(spo2_v[nadir_idx])
    ev_t, ev_v = _values_in_window(spo2_t, spo2_v, start_time, end_time)
    if len(ev_v) >= 2:
        d = np.diff(ev_v)
        max_abs_delta = float(np.max(np.abs(d)))
    else:
        max_abs_delta = np.nan
    post_end = nadir_time + (end_time - start_time)
    cap_end = nadir_time
    try:
        from datetime import timedelta
        cap_end = nadir_time
    except Exception:
        cap_end = nadir_time
    t_recover = np.nan
    for j in range(nadir_idx, len(spo2_t)):
        if spo2_t[j] < nadir_time:
            continue
        dt_min = _minutes(spo2_t[j] - nadir_time)
        if dt_min > 30.0:
            break
        if float(spo2_v[j]) >= recovery_threshold:
            t_recover = float(dt_min)
            break
    t_baseline = nadir_time
    try:
        import datetime as _dt
    except Exception:
        pass
    target_dt_min = -2.0
    base_time = None
    for j in range(nadir_idx, -1, -1):
        dt_min = _minutes(spo2_t[j] - nadir_time)
        if dt_min <= target_dt_min:
            base_time = spo2_t[j]
            break
    if base_time is None:
        if nadir_idx > 0:
            base_time = spo2_t[nadir_idx - 1]
        else:
            base_time = nadir_time
    hr_base, _ = _nearest_value_at_or_before(hr_t, hr_v, base_time)
    rr_base, _ = _nearest_value_at_or_before(rr_t, rr_v, base_time)
    hr_nadir, _ = _nearest_value_at_or_before(hr_t, hr_v, nadir_time)
    rr_nadir, _ = _nearest_value_at_or_before(rr_t, rr_v, nadir_time)
    d_hr = float(hr_nadir - hr_base) if np.isfinite(hr_base) and np.isfinite(hr_nadir) else np.nan
    d_rr = float(rr_nadir - rr_base) if np.isfinite(rr_base) and np.isfinite(rr_nadir) else np.nan
    return {'start_time': start_time, 'end_time': end_time, 'nadir_time': nadir_time, 'nadir_spo2': nadir_spo2, 'max_abs_delta_spo2': max_abs_delta, 't_recover_to_95_min': t_recover, 'd_hr_baseline2m_to_nadir': d_hr, 'd_rr_baseline2m_to_nadir': d_rr}

def _extract_desat_events(spo2_series, threshold=92.0, merge_gap_minutes=1.0):
    spo2_t, spo2_v = _to_arrays(spo2_series)
    n = len(spo2_v)
    if n == 0:
        return ([], spo2_t, spo2_v)
    below = spo2_v < threshold
    events = []
    i = 0
    while i < n:
        if not below[i]:
            i += 1
            continue
        start_i = i
        while i + 1 < n and below[i + 1]:
            i += 1
        end_i = i
        start_time = spo2_t[start_i]
        end_time = spo2_t[end_i]
        j = end_i + 1
        while j < n:
            if below[j]:
                gap_min = _minutes(spo2_t[j] - end_time)
                if gap_min <= merge_gap_minutes:
                    k = j
                    while k + 1 < n and below[k + 1]:
                        k += 1
                    end_i = k
                    end_time = spo2_t[end_i]
                    j = end_i + 1
                    continue
            break
        events.append((start_i, end_i, start_time, end_time))
        i = end_i + 1
    return (events, spo2_t, spo2_v)

def _align_window(t_list, v_arr, t0, pre_min=10.0, post_min=10.0):
    t_start = t0
    t_end = t0
    times = []
    vals = []
    for t, v in zip(t_list, v_arr):
        dtm = _minutes(t - t0)
        if dtm < -pre_min or dtm > post_min:
            continue
        times.append(dtm)
        vals.append(float(v))
    if len(vals) == 0:
        return (np.array([], dtype=float), np.array([], dtype=float))
    return (np.array(times, dtype=float), np.array(vals, dtype=float))
spo2_t, spo2_v = _to_arrays(spo2)
hr_t, hr_v = _to_arrays(heart_rate)
rr_t, rr_v = _to_arrays(respiratory_rate)
events, spo2_t, spo2_v = _extract_desat_events(spo2, threshold=92.0, merge_gap_minutes=1.0)
event_summaries = []
aligned = []

def _baseline_median(t_rel, v, lo=-10.0, hi=-2.0):
    m = (t_rel >= lo) & (t_rel <= hi)
    if np.any(m):
        return float(np.median(v[m]))
    return float(np.median(v)) if len(v) else np.nan
for start_i, end_i, start_time, end_time in events:
    seg = spo2_v[start_i:end_i + 1]
    if len(seg) == 0:
        continue
    local_nadir_offset = int(np.argmin(seg))
    nadir_idx = start_i + local_nadir_offset
    nadir_time = spo2_t[nadir_idx]
    met = _compute_event_metrics(spo2_t, spo2_v, hr_t, hr_v, rr_t, rr_v, start_time, end_time, nadir_idx, recovery_threshold=95.0)
    met['event_index'] = len(event_summaries) + 1
    event_summaries.append(met)
    pre_min, post_min = (10.0, 10.0)
    t_sp, v_sp = _align_window(spo2_t, spo2_v, nadir_time, pre_min=pre_min, post_min=post_min)
    t_hr, v_hr = _align_window(hr_t, hr_v, nadir_time, pre_min=pre_min, post_min=post_min)
    t_rr, v_rr = _align_window(rr_t, rr_v, nadir_time, pre_min=pre_min, post_min=post_min)
    sp_base = _baseline_median(t_sp, v_sp, lo=-10.0, hi=-2.0) if len(v_sp) else np.nan
    hr_base = _baseline_median(t_hr, v_hr, lo=-10.0, hi=-2.0) if len(v_hr) else np.nan
    rr_base = _baseline_median(t_rr, v_rr, lo=-10.0, hi=-2.0) if len(v_rr) else np.nan
    sp_norm = v_sp - sp_base if len(v_sp) and np.isfinite(sp_base) else np.array([], dtype=float)
    hr_norm = v_hr - hr_base if len(v_hr) and np.isfinite(hr_base) else np.array([], dtype=float)
    rr_norm = v_rr - rr_base if len(v_rr) and np.isfinite(rr_base) else np.array([], dtype=float)
    aligned.append({'event_index': met['event_index'], 'nadir_time': nadir_time, 'spo2_t_rel_min': t_sp, 'spo2_delta': sp_norm, 'hr_t_rel_min': t_hr, 'hr_delta': hr_norm, 'rr_t_rel_min': t_rr, 'rr_delta': rr_norm, 'nadir_spo2': met['nadir_spo2'], 'max_abs_delta_spo2': met['max_abs_delta_spo2'], 't_recover_to_95_min': met['t_recover_to_95_min']})
fig, ax = plt.subplots(3, 1, sharex=True, figsize=(10, 9))
for a in aligned:
    if len(a['spo2_t_rel_min']) and len(a['spo2_delta']):
        ax[0].plot(a['spo2_t_rel_min'], a['spo2_delta'], alpha=0.35, linewidth=1.25)
ax[0].axvline(0.0, color='k', linewidth=1.0, alpha=0.8)
ax[0].axhline(-3.0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
ax[0].set_ylabel('SpO₂ Δ nga baza (%)')
ax[0].set_title('Morfologjia e ngjarjes së deoksigjenimit SpO₂ (e rregulluar sipas pikës më të ulët; baza = mediani -10 deri në -2 min)')
for a in aligned:
    if len(a['hr_t_rel_min']) and len(a['hr_delta']):
        ax[1].plot(a['hr_t_rel_min'], a['hr_delta'], alpha=0.35, linewidth=1.25)
ax[1].axvline(0.0, color='k', linewidth=1.0, alpha=0.8)
ax[1].set_ylabel('HR Δ nga baza (bpm)')
for a in aligned:
    if len(a['rr_t_rel_min']) and len(a['rr_delta']):
        ax[2].plot(a['rr_t_rel_min'], a['rr_delta'], alpha=0.35, linewidth=1.25)
ax[2].axvline(0.0, color='k', linewidth=1.0, alpha=0.8)
ax[2].set_ylabel('RR Δ nga baza (fryrje/min)')
ax[2].set_xlabel('Minuta nga pika më e ulët e SpO₂')
n_events = len(event_summaries)
if n_events > 0:
    maxd = [e['max_abs_delta_spo2'] for e in event_summaries if np.isfinite(e['max_abs_delta_spo2'])]
    trec = [e['t_recover_to_95_min'] for e in event_summaries if np.isfinite(e['t_recover_to_95_min'])]
    txt = f'Ngjarje: {n_events}'
    if len(maxd):
        txt += f'\nMedian max |ΔSpO₂| për mostër: {float(np.median(maxd)):.2f}%'
    else:
        txt += '\nMedian max |ΔSpO₂| për mostër: NA'
    if len(trec):
        txt += f'\nKohë mediane për t\'u rikuperuar në ≥95%: {float(np.median(trec)):.1f} min'
    else:
        txt += '\nKohë mediane për t\'u rikuperuar në ≥95%: NA (brenda 30 min)'
    ax[0].text(0.98, 0.02, txt, transform=ax[0].transAxes, ha='right', va='bottom', fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='0.8'))
plt.tight_layout()
save_plot('spo2_event_morphology_aligned_overlay.png')
result = {'n_events_spo2_below_92': int(len(event_summaries)), 'event_summaries': event_summaries, 'plot_file': 'spo2_event_morphology_aligned_overlay.png'}
if len(event_summaries) == 0:
    interpretation = 'Asnjë ngjarje SpO₂ <92% nuk u zbulua; mbivendosja e morfologjisë dhe metrikave të rikuperimit nuk janë të zbatueshme.'
else:
    maxd = np.array([e['max_abs_delta_spo2'] for e in event_summaries], dtype=float)
    trec = np.array([e['t_recover_to_95_min'] for e in event_summaries], dtype=float)
    nadirs = np.array([e['nadir_spo2'] for e in event_summaries], dtype=float)
    n_recovered = int(np.sum(np.isfinite(trec)))
    interpretation = f'U zbuluan {len(event_summaries)} episode SpO₂ <92% (median nadir {float(np.nanmedian(nadirs)):.1f}%), me medianen maksimale për mostër |ΔSpO₂| {float(np.nanmedian(maxd)):.2f}% dhe {n_recovered}/{len(event_summaries)} u rikuperuan në ≥95% brenda 30 minutave (kohë mediane rikuperimi {float(np.nanmedian(trec)):.1f} min midis atyre të rikuperuarve).'

plt.close()