# # 6/26/2020
# In this exercise, you'll practice plotting the values of two time series without the time component.

# Two DataFrames, data and data2 are available in your workspace.

# Unless otherwise noted, assume that all required packages are loaded with their common aliases throughout this course.

# Note: This course assumes some familiarity with time series data, as well as how to use them in data analytics pipelines. 

# Print the first 5 rows of data
print(data.head())

# <script.py> output:
#     symbol  data_values
#     0        214.009998
#     1        214.379993
#     2        210.969995
#     3        210.580000
#     4        211.980005

# Print the first 5 rows of data2
print(data2.head())

# <script.py> output:
#        data_values
#     0    -0.006928
#     1    -0.007929
#     2    -0.008900
#     3    -0.009815
#     4    -0.010653

# Plot the time series in each dataset
fig, axs = plt.subplots(2, 1, figsize=(5, 10))
data.iloc[:1000].plot(y='data_values', ax=axs[0])
data2.iloc[:1000].plot(y='data_values', ax=axs[1])
plt.show()