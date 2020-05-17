
import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import root

def calculate_q(k):
    return root(lambda q: q - np.exp(k * (q-1)), 0).x[0]

k = np.linspace(1,10,50)
q = []
for i in k:
    q.append(calculate_q(i))

plt.plot(k,q)
plt.xlabel('k')
plt.ylabel('q')
plt.show()

n = 1000
plt.plot(k,[n*(1-j) for j in q])
plt.xlabel('k')
plt.ylabel('Size of LCC')
plt.show()

