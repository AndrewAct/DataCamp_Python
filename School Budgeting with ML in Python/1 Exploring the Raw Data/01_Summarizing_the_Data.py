# # 5/24/2020
# You'll continue your EDA in this exercise by computing summary statistics for the numeric data in the dataset. 
# The data has been pre-loaded into a DataFrame called df.

# You can use df.info() in the IPython Shell to determine which columns of the data are numeric, specifically type float64.
#  You'll notice that there are two numeric columns, called FTE and Total.

# FTE: Stands for "full-time equivalent". If the budget item is associated to an employee, this number tells us the percentage of full-time that the employee works. 
# A value of 1 means the associated employee works for the school full-time. A value close to 0 means the item is associated to a part-time or contracted employee.
# Total: Stands for the total cost of the expenditure. This number tells us how much the budget item cost.
# After printing summary statistics for the numeric data, your job is to plot a histogram of the non-null FTE column to see the distribution of part-time and full-time employees in the dataset.

# This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Scikit-Learn Cheat Sheet and keep it handy!

# Print the summary statistics
print(df.describe())

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Create the histogram
plt.hist(df['FTE'].dropna())

# Add title and labels
plt.title('Distribution of %full-time \n employee works')
plt.xlabel('% of full-time')
plt.ylabel('num employees')

# Display the histogram
plt.show()

# <script.py> output:
#                   FTE         Total
#     count  449.000000  1.542000e+03
#     mean     0.493532  1.446867e+04
#     std      0.452844  7.916752e+04
#     min     -0.002369 -1.044084e+06
#     25%      0.004310  1.108111e+02
#     50%      0.440000  7.060299e+02
#     75%      1.000000  5.347760e+03
#     max      1.047222  1.367500e+06