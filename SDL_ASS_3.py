
# Assignment_No:3
""" Title - write python code that loads any data set (from www.data.gov.in) & plot the graph.
"""

# importing library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file

df = pd.read_csv('Salary.csv')
print(df.head(5))        # print the dataset of first five data

# show column name in the dataset
print(df.columns)

# show the index in dataset
print(df.index)

# statistical operation
print(df.describe())

# compute pairwise Pearson coefficient of columns
print(df.corr())

# find min value of dataset
print(df.min(axis =0))

# find max value of dataset
print(df.max())

print(df.any)

# show mode of dataset
print(df.mode(axis =0))

print(df.std(axis=0))

# show count of dataset
print(df.count(axis=0))
# show shape of dataset
print(df.shape)


# Data visualization

# 1 Plot Bar graph on dataset

df.plot.bar(label='Salary''YearsExperience',width=2.5)
plt.legend()
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Bar_graph')
plt.show()

# 2 plot histogram
df.plot.hist( histtype='bar',rwidth=0.8)
plt.xlabel('Salary')
plt.ylabel('Years of experience')
plt.title("Histogram")
plt.legend()
plt.show()

# 3 Scatter_plot
x='Salary'
y='YearsExperience'
df.plot.scatter(x,y, label='Empyloee data', color ='red')
plt.xlabel('Salary')
plt.ylabel('YearsExperience')
plt.title('Scatter_plot')
plt.legend()
plt.show()



#  4 plot

df.plot(label='Graph',color='purple')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.title('Growth')
plt.legend()
plt.show()

# 5 Box plot
df.plot.box()
plt.ylabel('Salary')
plt.title('Box_Bar')
plt.legend()
plt.show()






