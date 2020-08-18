# # 8/17/2020
# You're going to undertake the first part of a Coarse to Fine search. This involves analyzing the results of an initial random search that took place over a large search space, then deciding what would be the next logical step to make your hyperparameter search finer.

# You have available:

# combinations_list - a list of the possible hyperparameter combinations the random search was undertaken on.
# results_df - a DataFrame that has each hyperparameter combination and the resulting accuracy of all 500 trials. Each hyperparameter is a column, with the header the hyperparameter name.
# visualize_hyperparameter() - a function that takes in a column of the DataFrame (as a string) and produces a scatter plot of this column's values compared to the accuracy scores. An example call of the function would be visualize_hyperparameter('accuracy')

# Confirm (by printing out) the size of the combinations_list, justifying the need to start with a random search.
# Sort the results_df by accuracy values and print the top 10 rows. Are there clear insights? Beware a small sample size!
# Confirm (by printing out) which hyperparameters were used in this search. These are the column names in results_df.
# Call visualize_hyperparameter() with each hyperparameter in turn (max_depth, min_samples_leaf, learn_rate). Are there any trends?

# Confirm the size of the combinations_list
print(len(combinations_list))

# Sort the results_df by accuracy and print the top 10 rows
print(results_df.sort_values(by='accuracy', ascending=False).head(10))

# Confirm which hyperparameters were used in this search
print(results_df.columns)

# Call visualize_hyperparameter() with each hyperparameter in turn
visualize_hyperparameter('max_depth')
visualize_hyperparameter('min_samples_leaf')
visualize_hyperparameter('learn_rate')

# <script.py> output:
#     10000
#         max_depth  min_samples_leaf  learn_rate  accuracy
#     1          10                14    0.477450        97
#     4           6                12    0.771275        97
#     2           7                14    0.050067        96
#     3           5                12    0.023356        96
#     5          13                11    0.290470        96
#     6           6                10    0.317181        96
#     7          19                10    0.757919        96
#     8           2                16    0.931544        96
#     9          16                13    0.904832        96
#     10         12                13    0.891477        96
#     Index(['max_depth', 'min_samples_leaf', 'learn_rate', 'accuracy'], dtype='object')