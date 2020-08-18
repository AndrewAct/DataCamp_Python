# # 8/17/2020
# Visualizing the search space of random search allows you to easily see the coverage of this technique and therefore allows you to see the effect of your sampling on the search space.

# In this exercise you will use several different samples of hyperparameter combinations and produce visualizations of the search space.

# The function sample_and_visualize_hyperparameters() takes a single argument (number of combinations to sample) and then randomly samples hyperparameter combinations, just like you did in the last exercise! The function will then visualize the combinations.

# If you want to see the function definition, you can use Python's handy inspect library, like so:

# print(inspect.getsource(sample_and_visualize_hyperparameters))

# Confirm how many hyperparameter combinations & print
number_combs = len(combinations_list)
print(number_combs)

# Sample and visualise specified combinations
for x in [50, 500, 1500]:
    sample_and_visualize_hyperparameters(x)
    
# Sample all the hyperparameter combinations & visualise
print(sample_and_visualize_hyperparameters(number_combs))

# <script.py> output:
#     2000
#     None