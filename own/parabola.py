import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1, 1, 1],
    [4, 2, 1],
    [9, 3, 1]
])

b = np.array([1, 2, 0])

# Solve
a, b_coef, c = np.linalg.solve(A, b)

print(a, b_coef, c)

## Define points (1, 1), (2, 2), (3, 0)
xx = np.array([1, 2, 3])
yy = np.array([1, 2, 0])

## Generate 100 numbers
x = np.linspace(0, 4, 100)

## Define the parabola equation
f = lambda t: a*t**2+b_coef*t+c

## Draw the points
plt.plot(xx, yy, '*')
plt.plot(x, f(x))

## Show the chart
plt.show()