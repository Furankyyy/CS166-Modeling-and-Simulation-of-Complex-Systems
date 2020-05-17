import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

url = 'https://gist.githubusercontent.com/raquelhr/d1324510056353feeccf111d6b186a0d/raw/7b3bccc7917f3baa7ec1d919195d120083ee75e9/proctatinium_data.csv'

data = pd.read_csv(url)

t_values = np.array(data["time"], dtype=float)
count_values = np.array(data["count_rate"], dtype=float)

plt.plot(t_values,count_values)
plt.xlabel('Time')
plt.ylabel('Count rate')
plt.show()

def N(t, lambda_):
    return 32 * np.exp(-lambda_ * t)

result= []

for _ in range(10000):
    popt, popv = curve_fit(N,t_values,count_values)
    hl = np.log(2)/popt
    result.append(hl)

plt.hist(result,bins = 50,density=True)
plt.xlabel('Half Life')
plt.ylabel('Density')
plt.show()


popt, popv = curve_fit(N,t_values,count_values)
experiment = N(t_values,popt)
theory_lambda = np.log(2) / 77
theory = N(t_values,theory_lambda)

plt.plot(t_values,count_values,label='Data')
plt.plot(t_values,experiment,label='Experiment')
plt.plot(t_values,theory,label='Theory')

plt.xlabel('Time')
plt.ylabel('Count rate')
plt.legend()
plt.show()

print('Error:', np.mean(result) - 77)