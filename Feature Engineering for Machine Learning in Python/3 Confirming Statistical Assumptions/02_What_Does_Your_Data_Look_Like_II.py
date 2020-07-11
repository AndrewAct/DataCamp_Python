# # 7/7/2020
# In the previous exercise you looked at the distribution of individual columns. While this is a good start, a more detailed view of how different features interact with each other may be useful as this can impact your decision on what to transform and how.

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns

# Plot pairwise relationships
sns.pairplot(so_numeric_df)

# Show plot
plt.show()

# Print summary statistics
print(so_numeric_df.describe())

# <script.py> output:
#            ConvertedSalary         Age  Years Experience
#     count     9.990000e+02  999.000000        999.000000
#     mean      6.161746e+04   36.003003          9.961962
#     std       1.760924e+05   13.255127          4.878129
#     min       0.000000e+00   18.000000          0.000000
#     25%       0.000000e+00   25.000000          7.000000
#     50%       2.712000e+04   35.000000         10.000000
#     75%       7.000000e+04   45.000000         13.000000
#     max       2.000000e+06   83.000000         27.000000