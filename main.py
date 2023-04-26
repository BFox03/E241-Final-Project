import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as sm

Housing = pd.read_excel('Housing.xlsx')
print("This data is a {} type \n".format(type(Housing)))

print("First 5 rows of data:")
print(Housing.head())

price = Housing['price']
area = Housing['area']
bedrooms = Housing['bedrooms']
stories = Housing['stories']
bathrooms = Housing['bathrooms']
prefarea = Housing['prefarea']
furnished = Housing['furnishingstatus']

rows, columns = Housing.shape
print("\nThis data has {} and {}\n".format(rows, columns))

namesOfColumns = Housing.columns
print("The columns in this file are \n{}\n".format(namesOfColumns))

print("A description about \'price\':\n{}\n".format(price.describe()))

#Histogram price counts
plt.hist(price.dropna(),bins=10)
plt.xlabel('Price')
plt.ylabel('Houses')
plt.title('Number of Houses per Price in Housing Dataset')
plt.show()

#Histogram bedroom counts
plt.hist(bedrooms.dropna(),bins=10)
plt.xlabel('Bedrooms')
plt.ylabel('Houses')
plt.title('Number of Houses per Bedrooms in Housing Dataset')
plt.show()

#Histogram bathroom counts
plt.hist(bathrooms.dropna(),bins=10)
plt.xlabel('Bathrooms')
plt.ylabel('Houses')
plt.title('Number of Houses per Bathrooms in Housing Dataset')
plt.show()

#Histogram prefarea counts
plt.hist(prefarea.dropna(),bins=10)
plt.xlabel('Preferred Area')
plt.ylabel('Houses')
plt.title('Number of Houses per Preferred Area in Housing Dataset')
plt.show()

#Histogram stories counts
plt.hist(stories.dropna(),bins=10)
plt.xlabel('Stories')
plt.ylabel('Houses')
plt.title('Number of Houses per Stories in Housing Dataset')
plt.show()

#Histogram Furnish counts
plt.hist(furnished.dropna(),bins=10)
plt.xlabel('Furnish Status')
plt.ylabel('Houses')
plt.title('Number of Houses per Furnish Status in Housing Dataset')
plt.show()

#Scatterplot Price vs. Area
plt.plot(Housing.area, Housing.price,'o', markersize=2)
plt.xlabel('Living Area in Square Feet')
plt.ylabel("House Price in $")
plt.title('Housing Price for Living Area in Housing Dataset')
plt.show()

#Simple linear regression model
SLR=sm.ols(formula = 'price ~ area', data = Housing).fit()
print(SLR.summary())

# Multi-linear regression model
MLR=sm.ols(formula = 'price ~ area + bedrooms', data = Housing).fit()
print(MLR.summary())