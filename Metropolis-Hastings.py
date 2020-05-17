import matplotlib.pyplot as plt
import scipy.stats as sts
import numpy as np

def f(x):
    Z = 24.44321494051954
    if abs(x) > 7:
        return 0
    elif abs(x) > 3:
        return 3 * (1 - (x / 7) ** 2) ** 0.5 / Z
    elif abs(x) > 1:
        return (
            (3-abs(x)) / 2 -
            3/7 * 10**0.5 * ((3-x**2 + 2*abs(x))**0.5-2)
            ) / Z
    elif abs(x) > 0.75:
        return (9-8 * abs(x)) / Z
    elif abs(x) > 0.5:
        return (3 * abs(x) + 0.75) / Z
    else:
        return 2.25 / Z

def q(x):
    return sts.norm.rvs(x,2)

def MCMC(f,q):
    x = np.random.uniform(-5,5)
    result = []
    for t in range(1,200001):
        xt = q(x) # generate potential next sample using proposal distribution
        alpha = f(xt)/f(x) # calculate acceptance
        if np.random.random() < min(1,alpha):
            x = xt
        if t % 100 == 0:
            result.append(x)
    return result

results = MCMC(f,q)
xs = np.linspace(-10,10,500)
ys = [f(x) for x in xs]
plt.figure(figsize=(10,5))
plt.hist(results,density=True,bins=50)
plt.plot(xs,ys)
plt.xlim(-8,8)
plt.show()