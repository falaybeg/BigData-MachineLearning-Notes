'''
--- Probability Distributions
'''

# --------- Uniform Distibution ---------
import numpy as np 
import matplotlib.pyplot as plt 

# playing dice game (results will be only from 1 to 6)

result = np.random.randint(1,7,10000)
print("Sample Space (1 to 6): ", np.unique(result))

plt.hist(result, bins=12)
plt.title("Uniform 1", fontsize = 14)
plt.ylabel("Number of outcomes", fontsize = 14)
plt.xlabel("Possible outcomes", fontsize = 14)
plt.show()
plt.hist(result, bins=6)
plt.title("Uniform 2", fontsize = 14)
plt.ylabel("Number of Outcomes", fontsize = 14)
plt.xlabel("Possible Outcomes", fontsize = 14)
plt.show()
#------------------------------------------------------


# -------- Binomial Distribution --------
import numpy as np 
import matplotlib.pyplot as plt 

#playing dice game 
n = 2 # number of trials
p = 0.5 #probability of each trial 

sample = np.random.binomial(n,p, 10000) # 10000 number of test
weights = np.ones_like(sample) / float(len(sample))
print("Weight: ", weights)
plt.hist(sample, weights=weights)
plt.title("Binomial DIstribution", fontsize = 14)
plt.xlabel("Number of Success", fontsize = 14)
plt.ylabel("Probability", fontsize = 14)
plt.show()

n = 10 
r = 4
p = 1/6
# Library solution by using scipy
from scipy.stats import binom 
print("Libarary Result: ",binom.pmf(r,n,p))

# Solution using formula 
import math 
result = (math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))*(p**r)*(1-p)**(n-r)
print("Formula Result: ",result)
#------------------------------------------------------


# -------- Poisson Distribution --------
import numpy as np 
import matplotlib.pyplot as plt 

# Average 3 vehicle in every hour
lamda = 3
sample = np.random.poisson(lamda, 500000)
weights = np.ones_like(sample)/float(len(sample))
print(weight)
plt.hist(sample, weights=weights, bins=50)
plt.title("Poisson Distribution", fontsize = 14)
plt.ylabel("Possibility", fontsize = 14)
plt.xlabel("Number of occurences", fontsize = 14)
#With %20 probability may come 2-3 vehicle in every hour
#------------------------------------------------------


# -------- Gaussian (Normal) Distribution --------
import numpy as np 
import matplotlib.pyplot as plt 

# IQ level example of people 
# mu is mean and sigma is standard deviation 
mu, sigma = 110, 20 
sample = np.random.normal(mu, sigma, 100000)
print("Mean of Sample: ", np.mean(sample))
print("Standard Deviation of Sample: ", np.std(sample))

plt.figure(figsize = (10,7))
plt.hist(sample, 100, normed=False)
plt.title("Gaussian (Normal) Distribution", fontsize = 14)
plt.xlabel("IQ Level Population", fontsize = 14)
plt.ylabel("Frequency of IQ (Count)", fontsize = 14)
plt.show()
# Consequently 60 percent of people have between 90 and 130 IQ level.
#------------------------------------------------------