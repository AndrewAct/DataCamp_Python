# 5/26/2020
# In this exercise, you'll manually set the grid of hyperparameters that will be used to tune rf's hyperparameters and find the optimal regressor. For this purpose, you will be constructing a grid of hyperparameters and tune the number of estimators, the maximum number of features used when splitting each node and the minimum number of samples (or fraction) per leaf.

# Define the dictionary 'params_rf'
params_rf = {
             'n_estimators' : [100, 350, 500],
             'max_features' : ['log2', 'auto', 'sqrt'],
             'min_samples_leaf' : [2, 10, 30]
}