'''
Multiple Linear Regression
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("multiple_regression_dataset.csv")

xset = df.iloc[:,[0,2]].values
yset = df.Salary.values.reshape(-1,1)


multiple_regression = LinearRegression()
multiple_regression.fit(xset, yset)


b0 = multiple_regression.intercept_
bresult = multiple_regression.coef_
b1 = bresult.item(0)
b2 = bresult.item(1)


print("b0: {}\nb1: {}\nb2: {}".format(b0.item(0),b1,b2))

# here predicted Salary according to input values (experience and age)
experience_age = np.array([[5,35],[10,40],[20,45],[30,55]])
predictedSalary = multiple_regression.predict(experience_age)


result = np.column_stack((experience_age,predictedSalary))
count = 1
for i  in result:
    print("\n--- ",count,".Predicted ---")
    print("Experience: {}\nAge: {},\nSalary: {}".format(i[0],i[1],round(i[2],2)))
    count += 1