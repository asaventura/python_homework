import numpy as np


a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
a_mean = a.mean(axis=0)
a_centered = a - a_mean
a_centered_sp = a_centered.T[0].dot(a_centered.T[1])

print(a_mean)
print(a_centered)
print(a_centered_sp)
print(a_centered_sp / (len(a) - 1))
print(np.cov(a.T))
