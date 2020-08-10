import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

# Setting number of iterations to display
ITERATIONS = 10

# Defining the stochastic matrices
#
#M = np.array([[0,                   0.5*(0.745 + 0.495), 0.5*(0.255 + 0.505)], 
#              [0.5*(0.255 + 0.505), 0,                   0.5*(0.745 + 0.495)], 
#              [0.5*(0.095 + 0.495), 0.5*(0.905 + 0.505), 0]])

M = np.array([[0.8, 0.6], 
               [0.2, 0.4] ])

v = np.array([1, 0])


(A, B) = np.zeros((2, ITERATIONS))
# Iterating until the desired convergence for the eigenvector
for i in range(ITERATIONS):
    A[i], B[i] = v[0], v[1]
    v = np.dot(M, v)

# Plotting data
x = np.arange(ITERATIONS)
plt.scatter(x, A, label = "$S^{(A)}$", s= 25)
plt.scatter(x, B, label = "$S^{(B)}$", s = 25)
plt.xlabel("step")
plt.ylabel("probabilities")
plt.legend()
plt.show()
