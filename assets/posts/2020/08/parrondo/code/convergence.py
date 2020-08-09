import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

# Setting number of iterations to display
ITERATIONS = 50

# Defining the stochastic matrices
#
#M = np.array([[0,                   0.5*(0.745 + 0.495), 0.5*(0.255 + 0.505)], 
#              [0.5*(0.255 + 0.505), 0,                   0.5*(0.745 + 0.495)], 
#              [0.5*(0.095 + 0.495), 0.5*(0.905 + 0.505), 0]])

M = np.array([[0, 0.745, 0.255], 
               [0.255, 0, 0.745], 
               [0.095, 0.905, 0]])

v = np.array([0, 0, 1])


(A, B, C) = np.zeros((3, ITERATIONS))
# Iterating until the desired convergence for the eigenvector
for i in range(ITERATIONS):
    A[i], B[i], C[i] = v[0], v[1], v[2]
    v = np.dot(v, M)

# Plotting data
x = np.arange(ITERATIONS)
plt.scatter(x, A, label = "$\pi_1$", s= 15)
plt.scatter(x, B, label = "$\pi_2$", s = 15)
plt.scatter(x, C, label = "$\pi_3$", s = 15)
plt.xlabel("i")
plt.legend()
plt.show()
