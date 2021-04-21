import numpy as np


a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
a_mean = a.mean(axis=0)
a_centered = a - a_mean
print(a_mean)
print(a_centered)
