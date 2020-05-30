# # 5/30/2020
# In the FIFA 18 dataset, various attributes of players are present. Two such attributes are:

# defending: a number which signifies the defending attributes of a player
# physical: a number which signifies the physical attributes of a player
# These are typically defense-minded players. In this exercise, you will perform clustering based on these attributes in the data.

# The following modules have been pre-loaded: kmeans, vq from scipy.cluster.vq, matplotlib.pyplot as plt, seaborn as sns. The data for this exercise is stored in a Pandas dataframe, fifa. The scaled variables are scaled_def and scaled_phy.

# Set up a random seed in numpy
random.seed([1000,2000])

# Fit the data into a k-means algorithm
cluster_centers,_ = kmeans(fifa[['scaled_def', 'scaled_phy']], 3)

# Assign cluster labels
fifa['cluster_labels'], _ = vq(fifa[['scaled_def', 'scaled_phy']], cluster_centers)

# Display cluster centers 
print(fifa[['scaled_def', 'scaled_phy', 'cluster_labels']].groupby('cluster_labels').mean())

# Create a scatter plot through seaborn
sns.scatterplot(x= 'scaled_def', y= 'scaled_phy', hue= 'cluster_labels', data=fifa)
plt.show()

# <script.py> output:
#                     scaled_def  scaled_phy
#     cluster_labels                        
#     0                     3.74        8.87
#     1                     1.87        7.08
#     2                     2.10        8.94