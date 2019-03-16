'''
ANOVA Testing 
    
Anova is statistical method used to test differences 
between two or more means. 
'''

# ----- ANOVA Introduction ------
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#Exam anxieties percent of primary, high school and university students

primary = np.array([51.36372405, 44.96944041, 49.43648441, 45.84584407, 45.76670682,
       56.04033356, 60.85163656, 39.16790361, 36.90132329, 43.58084076])
high = np.array([56.65674765, 55.92724431, 42.32435143, 50.19137162, 48.91784081,
       48.11598035, 50.91298812, 47.46134988, 42.76947742, 36.86738678])
university = np.array([60.03609029, 56.94733648, 57.77026852, 47.29851926, 54.21559389,
       57.74008243, 50.92416154, 53.47770749, 55.62968872, 59.42984391])

primary_mean = np.mean(primary)
high_mean = np.mean(high)
university_mean = np.mean(university)
print("Primary Mean: ", primary_mean)
print("High School Mean: ", high_mean)
print("University Mean: ", university_mean)

total_mean = (primary_mean + high_mean + university_mean)/3
print("\nTotal Mean:", total_mean)


sns.kdeplot(primary)
sns.kdeplot(high)
sns.kdeplot(university)
plt.title("Visualizing Primary, High School and University Anxiety")
plt.xlabel("Anxiety Percent")
plt.ylabel("Count Percent")
plt.show()

f_value = stats.f_oneway(primary, high, university)
f_value = f_value[0]
print("F-value: ",f_value)

# F-value is 5.523 
#----------------------------------------

#---- F-Distribution (critical value) -----

# Here we will find critical value and compare with f-value

# degrees of freedom for groups
group = 2 # 3-1 = 2
# degrees of freedom for error
error = 27 # (10 sample - 1) * 3 = 27

# error is 0.01 --> %1
critical = stats.f.ppf(q=0.99, dfn=group, dfd=error)
print("Critical Value: ",critical)

if f_value > critical:
    print("\nNull Hypothesis rejected and Alternative Hypothesis accepted")
else:
    print("\nNull Hypothesis accepted and Alternative Hypothesis rejected")

#------------------------------------------