# # 7/20/2020
# For a school assignment, your professor has asked your class to create a random forest model to predict the average test score for the final exam.

# After developing an initial random forest model, you are unsatisfied with the overall accuracy. You realize that there are too many hyperparameters to choose from, and each one has a lot of possible values. You have decided to make a list of possible ranges for the hyperparameters you might use in your next model.

# Your professor has provided de-identified data for the last ten quizzes to act as the training data. There are 30 students in your class.

# Review the parameters of rfr
print(rfr.get_params())

# Maximum Depth
max_depth = [4, 8, 12]

# Minimum samples for a split
# It means the minimum number of samples required to split an internal node
min_samples_split = [2, 5, 10]

# Max features 
max_features = [4, 6, 8, 10]

# <script.py> output:
#     {'bootstrap': True, 'criterion': 'mse', 'max_depth': None, 'max_features': 'auto', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 'warn', 'n_jobs': None, 'oob_score': False, 'random_state': 1111, 'verbose': 0, 'warm_start': False}
