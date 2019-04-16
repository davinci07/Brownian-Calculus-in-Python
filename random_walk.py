from math import sqrt
from scipy.stats import norm
import numpy as np




def symmetric_random_walk(m,d):
    out = []
    for i in range(d):
        #for k in range(n):
        #    x += norm.rvs(scale=delta**2*dt)
        x = np.cumsum(2*np.random.binomial(1,.5,m)-1)
        out.append(x[len(x)-1])
    return (out)
        
        




print(symmetric_random_walk(100,1000))
