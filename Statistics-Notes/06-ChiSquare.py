'''
Chi-Square Analysis 

Chi-Square is a procedure for testing differences 
between observed and expected two category values.
'''

# ------- Chi-Square Analysis ------
import numpy as np 
from scipy.stats import chi2
# we have 7 computer. And their failure rates are equal to each other 
# Computer are independet with each other 

# Null Hypothesis: Statistically the failure rates are %95 meaningful 

observation = np.array([5,7,9,5,3,10,5])
total = np.sum(observation)
print("Total failure: ", total)
expected = total / len(observation)
print("Expected failure: ",expected)

# we calculate chi-square value
chi_value = np.sum(((observation - expected)**2)/expected)
print("Chi-Square Value: ",chi_value)

# here we find critical value and compare with chi-square value
critical_val = chi2.isf(0.05, expected)
print("Critical Val: ", critical_val)

if chi_value < critical_val:
    print("\nNull Hypotesis is accepted. Between observed and expected values have high correlation")
else:
    print("Null Hypothesis is rejected")