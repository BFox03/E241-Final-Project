import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as sm

data = pd.read_excel('Life Expectancy Data.xlsx')
print("This data is a {} type \n".format(type(data)))

print("First 5 rows of data:")
print(data.head())

rows, columns = data.shape
print("\nThis data has {} and {}\n".format(rows, columns))

namesOfColumns = data.columns
print("The columns in this file are \n{}\n".format(namesOfColumns))

columnPop = data['Population']
print("Data for \'Population\' is\n{}\n".format(columnPop))

print("First 5 rows of \'Population\'")
print(columnPop.head())

columnPop.replace([0, 99999999999999], np.nan, inplace = True)
print("\nMax of \'Population\' after replacing:\n{}\n".format(columnPop.max()))

print("A description about \'Population\':\n{}\n".format(columnPop.describe()))

plt.hist(columnPop.dropna(),bins=10)
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()

# Count the number of houses with and without a waterfront
waterfront_counts = data['Waterfront'].value_counts()
# Create a bar plot
plt.bar(waterfront_counts.index, waterfront_counts.values)
# Set labels and title
plt.xticks([0, 1], ['No Waterfront', 'Waterfront'])
plt.ylabel('Number of Houses')
plt.title('Number of Houses With and Without Waterfront in NY Housing Dataset')
# Show the plot
plt.show()