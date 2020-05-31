# # 5/30/2020
# We have loaded the following image using the imread() function of the image class of matplotlib.

# The RGB values are stored in a data frame, batman_df. The RGB values have been standardized used the whiten() function, stored in columns, scaled_red, scaled_blue and scaled_green.

# Construct an elbow plot with the data frame. How many dominant colors are present?

distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(batman_df[['scaled_red', 'scaled_blue', 'scaled_green']], i)
    distortions.append(distortion)

# Create a data frame with two lists, num_clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters,
                           'distortions': distortions
})

# Create a line plot of num_clusters and distortions
sns.lineplot(x= 'num_clusters', y= 'distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()
