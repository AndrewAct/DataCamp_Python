# # 8/17/2020
# You will now visualize the first random search undertaken, construct a tighter grid and check the results. You will have available:

# results_df - a DataFrame that has the hyperparameter combination and the resulting accuracy of all 500 trials. Only the hyperparameters that had the strongest visualizations from the previous exercise are included (max_depth and learn_rate)
# visualize_first() - This function takes no arguments but will visualize each of your hyperparameters against accuracy for your first random search.

# Use the provided function to visualize the first results
visualize_first()

# Use the provided function to visualize the first results
# visualize_first()

# Create some combinations lists & combine:
max_depth_list = list(range(1,21))
learn_rate_list = np.linspace(0.001,1,50)

# Call the function to visualize the second results
visualize_second()