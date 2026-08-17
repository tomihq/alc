## This won't work, as an infinitely many solutions system (SCI) does not have an invertible matrix."
import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [(1j), -(1+1j), 0],
    [1, -2, 1],
    [1, 2j, -1]
])

b = np.array([-1, 0, 2j])

x, y, z = np.linalg.solve(A, b)

print(x, y, z)