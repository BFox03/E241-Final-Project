import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as sm

data = pd.read_excel('Housing.xlsx')
print("This data is a {} type \n".format(type(data)))

print("First 5 rows of data:")
print(data.head())

rows, columns = data.shape
print("\nThis data has {} and {}\n".format(rows, columns))

namesOfColumns = data.columns
print("The columns in this file are \n{}\n".format(namesOfColumns))

columnPop = data['price']
print("Data for \'price\' is\n{}\n".format(columnPop))

print("First 5 rows of \'price\'")
print(columnPop.head())

columnPop.replace([0, 99999999999999], np.nan, inplace = True)
print("\nMax of \'price\' after replacing:\n{}\n".format(columnPop.max()))

print("A description about \'price\':\n{}\n".format(columnPop.describe()))

plt.hist(columnPop.dropna(),bins=10)
plt.xlabel('Price')
plt.ylabel('Houses')
plt.show()
