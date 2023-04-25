import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as sm

Housing = pd.read_excel('Housing.xlsx')
print("This data is a {} type \n".format(type(Housing)))

print("First 5 rows of data:")
print(Housing.head())

rows, columns = Housing.shape
print("\nThis data has {} and {}\n".format(rows, columns))

namesOfColumns = Housing.columns
print("The columns in this file are \n{}\n".format(namesOfColumns))

columnPop = Housing['price']
print("Data for \'price\' is\n{}\n".format(columnPop))

print("First 5 rows of \'price\'")
print(columnPop.head())

columnPop.replace([0, 99999999999999], np.nan, inplace = True)
print("\nMax of \'price\' after replacing:\n{}\n".format(columnPop.max()))

print("A description about \'price\':\n{}\n".format(columnPop.describe()))

#Histogram price counts
plt.hist(columnPop.dropna(),bins=10)
plt.xlabel('Price')
plt.ylabel('Houses')
plt.show()

#Bar chart bedroom counts
# Count the number of houses for each number of beds
bed_counts = Housing['bedrooms'].value_counts()
# Sort the bed_counts by index
bed_counts = bed_counts.sort_index()
# Create a bar plot
plt.bar(bed_counts.index, bed_counts.values)
# Set labels and title
plt.xlabel('Number of Beds')
plt.ylabel('Number of Houses')
plt.title('Number of Houses for Each Number of Beds in Housing Dataset')
# Show the plot
plt.show()

#Pie chart Bedroom counts
# Calculate percentage values
percentages = 100 * bed_counts / bed_counts.sum()
# Create a pie chart without percentage values displayed on the chart
labels = bed_counts.index
colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))
wedges, texts = plt.pie(bed_counts, labels=labels, colors=colors, startangle=90)
# Set title
plt.title('Percentage of Houses for Each Number of Beds in NY Housing Dataset')
# Create a legend with percentage values
legend_labels = [f'{label}: {percentage:.1f}%' for label, percentage in zip(labels, percentages)]
plt.legend(wedges, legend_labels, title="Number of Beds", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
# Show the plot
plt.show()

#Scatterplot Price vs. Area
plt.plot(Housing.area, Housing.price,'o', markersize=2)
plt.xlabel('Living Area in Square Feet')
plt.ylabel("House Price in $")
plt.show()

#Simple linear regression model
SLR=sm.ols(formula = 'Housing.price ~ Housing.area', data = Housing).fit()
SLR.summary()

# Multi-linear regression model
MLR=sm.ols(formula = 'Housing.price ~ Housing.area + Housing.bedrooms', data = Housing).fit()
MLR.summary()