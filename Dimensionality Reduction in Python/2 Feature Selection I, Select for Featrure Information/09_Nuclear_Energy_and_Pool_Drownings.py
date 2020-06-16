# # 6/15/2020
# The dataset that has been pre-loaded for you as weird_df contains actual data provided by the US Centers for Disease Control & Prevention and Department of Energy.

# Let's see if we can find a pattern.

# Seaborn has been pre-loaded as sns and matplotlib.pyplot as plt.

# Print the first five lines of weird_df
print(weird_df.head())
# <script.py> output:
#        pool_drownings  nuclear_energy
#     0             421           728.3
#     1             465           753.9
#     2             494           768.8
#     3             538           780.1
#     4             430           763.7

# Put nuclear energy production on the x-axis and the number of pool drownings on the y-axis
sns.scatterplot(x='nuclear_energy', y= 'pool_drownings', data= weird_df)
plt.show()

# Print out the correlation matrix of weird_df
print(weird_df.corr())

# <script.py> output:
#                     pool_drownings  nuclear_energy
#     pool_drownings        1.000000        0.901179
#     nuclear_energy        0.901179        1.000000