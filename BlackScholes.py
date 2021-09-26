import numpy as np 
from math import log, sqrt, pi, exp
from scipy.stats import norm 
import math


## define two functions, d1 and d2 in Black-Scholes model
def d1(S,K1,T,r,sigma):
    return(log(S/K1)+(r+sigma**2/2.0)* (T) )/sigma*sqrt(T)
def d2(S,K,T,r,sigma):
  return (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
#     return d1(S,K1,T,r,sigma)-sigma*sqrt(T)


## define the call options price function
def bs_call(S,K1,T,r,sigma):
        return S*norm.cdf(d1(S,K1,T,r,sigma))-K1*exp(-r*T)*norm.cdf(d1(S,K1,T,r,sigma)-sigma*np.sqrt(T))
  
## define the put options price function
def bs_put(S,K,T,r,sigma):
  d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
  d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
  print(d2)
  return (K * np.exp(-r * T) * norm.cdf(-d2, 0.0, 1.0) - S * norm.cdf(-d1, 0.0, 1.0))
#     return K2*exp(-r*T)-S+bs_call(S,K1,K2,T,r,sigma)


d1x = d1(214.7,225,0.94,.0059,.2206)
print(d1x)
bsc = bs_call(214.7,225,0.94,.0059,.2206)
print(bsc)

bsp = bs_put(50, 100, 1, 0.05, 0.25)
print(bsp)


