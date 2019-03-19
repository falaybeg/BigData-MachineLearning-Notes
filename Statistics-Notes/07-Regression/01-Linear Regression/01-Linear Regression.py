'''
Linear Regression
'''
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
# Load dataset
df = pd.read_csv("linear_regression_dataset.csv")

# Dataset is visualized by using Scatter Plot 
plt.scatter(df["Experience"], df["Salary"])
plt.title("Scatter Plot graphics for Experience and Salary", fontsize=14)
plt.xlabel("Experience (year)", fontsize=14)
plt.ylabel("Salary", fontsize= 14)
#Scatter Plot graph shows us that salary increases according to experience year
plt.show()

# Linear Regression is defined from sklearn library 
from sklearn.linear_model import LinearRegression
# Created a instance from LinearRegression() class for prediction
linear_regression = LinearRegression()

# X and Y values is transformed to numpy array and reshaped for model
xset = df["Experience"].values.reshape(-1,1)
yset = df["Salary"].values.reshape(-1,1)


# Fit process is carried out
linear_regression.fit(xset,yset)

# Manuel Prediction method ______________________
# y = b0 + b1*x

b0 = linear_regression.predict(np.array([[0]]))
b1 = linear_regression.coef_

# We found constant and coefficieny/slope 
# We are going to predict salary in 11th year
experience = 11 
y = b0 + b1*experience
print("b0 : ",b0,"\nb1 : ",b1)
print("Salary  (manual method) : ",y.item(0))
#_________________________________________________


# Automatic Prediction method -----------------------

salary = linear_regression.predict(np.array([[11]]))
print("Salary (function method): ",salary.item(0))



experienceYear = np.array([0,1,2,3,5,7,10,11,15,18,20]).reshape(-1,1)
predictedSalary = linear_regression.predict(experienceYear)

plt.scatter(xset,yset)
plt.plot(experienceYear, predictedSalary, color="red" )
plt.xlabel("Experience (Year)", fontsize=14)
plt.ylabel("Salary",fontsize=14)
plt.show()
#_________________________________________________
