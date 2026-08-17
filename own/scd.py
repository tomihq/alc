## This will work as it's an SCD. Expected to return: (-3, 2, 2)
import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1, 1, 0],
    [0, -1, 1],
    [0, 0 , 1]
])

b = np.array([-1, 0, 2])

x, y, z = np.linalg.solve(A, b)

print(x, y, z)