# # 6/13/2020
# Data visualization is a crucial step in any data exploration. Let's use Seaborn to explore some samples of the US Army ANSUR body measurement dataset.

# Two data samples have been pre-loaded as ansur_df_1 and ansur_df_2.

# Seaborn has been imported as sns.
# Remove one of the redundant features 
reduced_df = ansur_df_1.drop('body_height', axis=1)

# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(reduced_df, hue='Gender')

# Show the plot
plt.show()

# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(ansur_df_2, hue = "Gender", diag_kind='hist')


# Show the plot
plt.show()

# Remove the redundant feature
reduced_df = ansur_df_2.drop("n_legs", axis = 1)

# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(reduced_df, hue='Gender', diag_kind='hist')

# Show the plot
plt.show()