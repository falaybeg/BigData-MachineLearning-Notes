'''
04 - What is Statistics ?
'''

# ------- Central Limit Theorem -------
import numpy as np 
import matplotlib.pyplot as plt 

population = np.random.random_integers(10, size = 100000)
plt.title("Distribution of Population")
plt.hist(population)
plt.show()
mean  = np.mean(population)
print("Population Mean: ", mean)

import random 
mean_sample = []
for i in range(10000):
    sample = random.randrange(5,10)
    mean_sample.append(np.mean(random.sample(list(population),sample)))
plt.title("Mean of Sample")
plt.hist(mean_sample, bins=50, color="red")

plt.hist(population, alpha=0.5, density=True)
plt.hist(mean_sample, bins=50, alpha=0.5, color="red")
plt.title("Central Limit Theorem")
plt.show()
#------------------------------------------

# ------- Standard Error -------
# population mean = 100 and std = 15 
mean = 100 
std = 15 

# Sampling n= 10 and sample_mean = 104. 
# So can we say this 10 person is from population 
n = 10 
sample_mean = 104 

SE = 15 / 10**(1/2)
SE = round(SE,3)
print("Standard Error: ",SE)
print("These 10 people are from population with %68 between ",(mean-SE)," and ",(mean+SE))            
#---------------------------------------


# ------ Hypothesis Testing -------
import pandas as pd 
from scipy import stats

# From our  cancer dataset
# Null Hypothesis: relationship between radius_mean and area_mean is zero in tumor population 
# Alternative Hypothesis:  relationship between radius_mean and area_mean is not zero in tumor population 

data = pd.read_csv("CancerCellData.csv")
radius_mean = data.radius_mean 
area_mean = data.area_mean 

statistics, p_value = stats.ttest_rel(radius_mean, area_mean)
print("P-value: ",p_value)

# Consequently Null Hypothesis says that p-value must be zero 
# But the result shows that p-values = 1.52 and Null Hypothesis rejected.
# Between radius_mean and area_mean have relationship so Alternative hypothesis is accepted 


# ----- T-Distribution ------

import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

# creating of two datasets
sample1 = np.array([14.67230258, 14.5984991 , 14.99997003, 14.83541808, 15.42533116,
       15.42023888, 15.0614731 , 14.43906856, 15.40888636, 14.87811941,
       14.93932134, 15.04271942, 14.96311939, 14.0379782 , 14.10980817,
       15.23184029])

sample2 = np.array([15.23658167, 15.30058977, 15.49836851, 15.03712277, 14.72393502,
       14.97462198, 15.0381114 , 15.18667258, 15.5914418 , 15.44854406,
       15.54645152, 14.89288726, 15.36069141, 15.18758271, 14.48270754,
       15.28841374])

print("--- Sample 1 ---")
print("Mean 1: ",np.mean(sample1))    
print("Standard Deviation: ", np.std(sample1))
print("Variance: ",np.var(sample1))

print("\n--- Sample 2 ---")
print("Mean : ",np.mean(sample2))    
print("Standard Deviation: ", np.std(sample2))
print("Variance: ",np.var(sample2))

# Visualizing of two datasets
sns.kdeplot(sample1)
sns.kdeplot(sample2)
plt.show()

# calculating of T-VALUE
t_value = np.abs(np.mean(sample1)-np.mean(sample2))/np.sqrt(np.var(sample1)/len(sample1) + np.var(sample2)/len(sample2))
print("t-value: ",t_value)

# Consequently we can say that t-value is 2.337 and we compare with critical value 
# At t-table critical value is 2.04 and we can say that t-value is higher than critical-value 
# So Null Hypothesis is rejected. 
#------------------------------------------
