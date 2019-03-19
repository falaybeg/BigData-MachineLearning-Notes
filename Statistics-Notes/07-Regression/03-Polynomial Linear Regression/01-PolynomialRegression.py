'''
Polynomial Linear Regression

It is used when between variables don't have linear relationship.
We will firstly apply Linear Regression for understanding differences between Polynomial and Linear Regressions
'''
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

df = pd.read_csv("polynomial_data.csv")

# --- Linear Regression ---
xset = df["CarPrice"].values.reshape(-1,1) # car price
yset = df["MaxSpeed"].values.reshape(-1,1) # max speed

plt.scatter(xset, yset)
plt.ylabel("Max Speed", fontsize = 14)
plt.xlabel("Car Price", fontsize = 14)



lr = LinearRegression()
lr.fit(xset, yset)
 
y_head = lr.predict(xset)
plt.plot(xset, y_head, color="green", label="Linear Line")
# Although the line fitted with minimum MSE (mean squared error), the result shows that MSE value is high 

carPrice = np.array([[10000]])
predicted = lr.predict(carPrice)

# Predicted result will show that the car speed can't be 686 km/h.
# In this case is used Polynomial Regression.
print("Price is 10000 and Predicted Max Speed: {}\n".format(round(predicted.item(0),2)))
#_______________________________________________________________


# ------- Polynomial Regression ------
# Here we will apply Polynomial Regression and will see differences 

# Polynomial library is imported
from sklearn.preprocessing import PolynomialFeatures

# x^2 --> here 2 is our degree,
polynomial_regression = PolynomialFeatures(degree = 2)
# If we increase degree level the prediction will be more efficient
#polynomial_regression = PolynomialFeatures(degree = 4)

# here X (car price) is transformed to polynomial feature.
# Here we find X values and X^2 values
x_polynomial = polynomial_regression.fit_transform(xset)

# after creating x^2 feature we apply normal Linear Regression
linear_regression2 = LinearRegression()
# Here we fit our line as a curve line
linear_regression2.fit(x_polynomial, yset)
y_head_polynomial = linear_regression2.predict(x_polynomial)

plt.plot(xset,y_head_polynomial, color="red", label="Polynomial Line")
plt.legend()
plt.show()
#_________________________________________________________
