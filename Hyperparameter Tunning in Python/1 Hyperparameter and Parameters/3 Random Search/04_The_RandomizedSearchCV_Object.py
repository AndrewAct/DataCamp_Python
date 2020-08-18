# # 8/17/2020
# Just like the GridSearchCV library from Scikit Learn, RandomizedSearchCV provides many useful features to assist with efficiently undertaking a random search. You're going to create a RandomizedSearchCV object, making the small adjustment needed from the GridSearchCV object.

# The desired options are:

# A default Gradient Boosting Classifier Estimator
# 5-fold cross validation
# Use accuracy to score the models
# Use 4 cores for processing in parallel
# Ensure you refit the best model and return training scores
# Randomly sample 10 models
# The hyperparameter grid should be for learning_rate (150 values between 0.1 and 2) and min_samples_leaf (all values between and including 20 and 64).

# You will have available X_train & y_train datasets.

# Create a parameter grid as specified in the context above.
# Create a RandomizedSearchCV object as outlined in the context above.
# Fit the RandomizedSearchCV object to the training data.
# Print the values chosen by the modeling process for both hyperparameters.

# Create the parameter grid
param_grid = {'learning_rate': np.linspace(0.1,2,150), 'min_samples_leaf': list(range(20,65))} 

# Create a random search object
random_GBM_class = RandomizedSearchCV(
    estimator = GradientBoostingClassifier(),
    param_distributions = param_grid,
    n_iter = 10,
    scoring='accuracy', n_jobs=4, cv = 5, refit=True, return_train_score = True)

# Fit to the training data
random_GBM_class.fit(X_train, y_train)

# Print the values used for both hyperparameters
print(random_GBM_class.cv_results_['param_learning_rate'])
print(random_GBM_class.cv_results_['param_min_samples_leaf'])

# <script.py> output:
#     [1.1073825503355705 1.0691275167785235 0.4697986577181208
#      1.2476510067114095 1.5664429530201343 1.7577181208053692
#      1.859731543624161 1.5791946308724834 0.5463087248322147
#      1.7577181208053692]
#     [47 54 61 30 63 32 60 43 38 27]