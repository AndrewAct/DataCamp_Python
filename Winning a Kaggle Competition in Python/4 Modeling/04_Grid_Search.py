# # 8/19/2020
# Recall that we've created a baseline Gradient Boosting model in the previous lesson. Your goal now is to find the best max_depth hyperparameter value for this Gradient Boosting model. This hyperparameter limits the number of nodes in each individual tree. You will be using K-fold cross-validation to measure the local performance of the model for each hyperparameter value.

# You're given a function get_cv_score(), which takes the train dataset and dictionary of the model parameters as arguments and returns the overall validation RMSE score over 3-fold cross-validation.

# Possible max depth values
max_depth_grid = [3, 6, 9, 12, 15]
results = {}

# For each value in the grid
for max_depth_candidate in max_depth_grid:
    # Specify parameters for the model
    params = {'max_depth': max_depth_candidate}

    # Calculate validation score for a particular hyperparameter
    validation_score = get_cv_score(train, params)

    # Save the results for each max depth value
    results[max_depth_candidate] = validation_score   
print(results)

# <script.py> output:
#     {3: 6.50509, 6: 6.52138, 9: 6.64181, 12: 6.8819, 15: 6.99156}