'''

'''
import numpy as np 
from scipy import stats

sample = np.random.randint(1,10000,50)

# --- Central Tendency (Mean, Median, Mode) -----
print("------ Central Tendency ------")
print("Mean: ", np.mean(sample))
print("Median: ",np.median(sample))
print("Mode: ",stats.mode(sample))
print("-----------------------------------")


# ----- Dispersion (Range, Varianve, Standard Deviation) -----
print("------ Dispersion using Function ------")
print("Range: ", (np.max(sample)-np.min(sample)))
print("Variance: ",np.var(sample))
print("Standard Deviation: ",np.std(sample))

print("--------Dispersion without function----------")
variance = sum((sample - np.mean(sample))**2)/len(sample)
print("Variance: ",variance)
standardev = np.sqrt(variance)
print("Standard Deviation: ",standardev)
print("---------------------------------------------\n")
#------------------------------------------------------------------------

# --------- Quartiles ---------
import pandas as pd 
import seaborn as sns

# Load dataset using Pandas library
data = pd.read_csv("data.csv")
data = data.drop(['Unnamed: 32','id'],axis = 1)
print(data.head())

data_bening = data[data["diagnosis"] == "B"]
data_malignant = data[data["diagnosis"] == "M"]

# Get description of the dataset
desc= data_bening["radius_mean"].describe()
# Get quartiles values
Q1 = desc[4]
Q3 = desc[6]
IQR = Q3 - Q1
print("Q1: ",Q1)
print("Q3: ",Q3)    
print("IQR: ",IQR)

# calculate lower and upper bounds for finding outlier values
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
print("Lower Bound: ", lower_bound)
print("Upper Bound: ",upper_bound)
print("Anything outside this range is an outlier: (", lower_bound ,",", upper_bound,")")
data_bening[data_bening.radius_mean < lower_bound].radius_mean
print("Outliers: ",data_bening[(data_bening["radius_mean"] < lower_bound) | (data_bening["radius_mean"]  > upper_bound)].radius_mean.values)

# Visualizing dataset using boxplot 
melted_data = pd.melt(data, id_vars = "diagnosis", value_vars=["radius_mean"])
sns.boxplot(x="value", y="variable", hue="diagnosis", data=melted_data)
#------------------------------------------------------------------------

# ----- Bivariate, Correlation and Covariance -----
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
data = pd.read_csv("data.csv")

# Correlation Map between dataset variables/columns
f,ax = plt.subplots(figsize = (18,18))
sns.heatmap(data.corr(), annot=True, linewidth=0.5, fmt=".1f",ax=ax)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.title("Corelation Map")
plt.show()

# Visualizing correlation between two variables using regression plot
sns.jointplot(data["radius_mean"], data["area_mean"], kind="regg")
sns.jointplot(data["radius_mean"], data["radius_se"], kind="regg")

# Visualizing multiple variable correlation by using GridPlot 
sns.set(style="white")
df = data.loc[:,["radius_mean","area_mean","radius_se","area_se"]]
g = sns.PairGrid(df, diag_sharey = False)
g.map_lower(sns.kdeplot,cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot,lw =3)
plt.show()
#------------------------------------------------------------------------

# ----- Covariance -----
np.cov(data.radius_mean,data.area_mean)
print("Covariance between radius mean and area mean: ",data.radius_mean.cov(data.area_mean))
print("Covariance between radius mean and fractal dimension se: ",data.radius_mean.cov(data.fractal_dimension_se))
fig, axs = plt.subplots(1, 2)
axs[0].scatter(data.radius_mean, data.area_mean)
axs[1].scatter(data.fractal_dimension_se, data.radius_mean)
plt.show()
#------------------------------------------------------------------------


# ------- Pearson Correlation Coefficient ------
import pandas as pd 
import seaborn as sns

data = pd.read_csv("data.csv")

# Calculating Pearson Coefficient 
p1 = data.loc[:,["area_mean", "radius_mean"]].corr(method="pearson")
p2 = data.radius_mean.cov(data.area_mean)/(data.radius_mean.std()*data.area_mean.std())
print("\n----- Pearson Correlation DataFrame -----")
print(p1)
print("\nPearson Coefficient: ", p2)

p3 = data.loc[:,["area_mean", "radius_mean", "concavity_mean", "perimeter_mean"]].corr(method="pearson")
print("\n----- Multiple Pearson Correlation DataFrame -----")
print(p3)

#sns.jointplot(data.radius_mean, data.area_mean, kind="regg")
#sns.jointplot(data.radius_mean, data.concavity_mean, kind="regg")

#------------------------------------------------------------------------

# ----- Spearman Rank Coefficient (It is less impressed from outliers) -----

# here we ranked our variables and calculated spearman value
ranked_data = data.rank()
spearman_correlation = ranked_data.loc[:,["area_mean","radius_mean"]].corr(method="pearson")
print("\nSpearman's Correlation: ",spearman_correlation)
#--------------------------------------------------------------------------

# ----- Effective Size -----
import pandas as pd 
import numpy as np
# here dataset loaded
data = pd.read_csv("data.csv")

# Bening and Malignant cancer were splitted
data_malignant = data[data["diagnosis"] == "M"]
data_bening = data[data["diagnosis"] == "B"]

mean_diff = data_malignant.radius_mean.mean() - data_bening.radius_mean.mean()
print("Difference (M1 - M2): ", mean_diff)

variance_malignant = data_malignant.radius_mean.var()
variance_bening = data_bening.radius_mean.var()
var_pooled = (len(data_bening)*variance_malignant + len(data_malignant)*variance_bening)/ float(len(data_bening) + len(data_malignant))
var_pooled = np.sqrt(var_pooled)
print("Denominator sqrt[(s1^2/n1) + (s2^2/n2)] : ",var_pooled)

effective_size = mean_diff/var_pooled
print("Effective Size: ", effective_size)

# The result will be 1.92 and it means that groups are different from each other 
#--------------------------------------------------------------------------


