# # 8/17/2020
# The GridSearchCV module from Scikit Learn provides many useful features to assist with efficiently undertaking a grid search. You will now put your learning into practice by creating a GridSearchCV object with certain parameters.

# The desired options are:

# A Random Forest Estimator, with the split criterion as 'entropy'
# 5-fold cross validation
# The hyperparameters max_depth (2, 4, 8, 15) and max_features ('auto' vs 'sqrt')
# Use roc_auc to score the models
# Use 4 cores for processing in parallel
# Ensure you refit the best model and return training scores
# You will have available X_train, X_test, y_train & y_test datasets.

# Create a Random Forest Classifier with specified criterion
rf_class = RandomForestClassifier(criterion='entropy')

# Create the parameter grid
param_grid = {'max_depth': [2, 4, 8, 15], 'max_features': ['auto', 'sqrt']} 

# Create a GridSearchCV object
grid_rf_class = GridSearchCV(
    estimator=rf_class,
    param_grid=param_grid,
    scoring= 'roc_auc',
    n_jobs=4,
    cv=5,
    refit=True, return_train_score=True)
print(grid_rf_class)

# <script.py> output:
#     GridSearchCV(cv=5, error_score='raise-deprecating',
#            estimator=RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
#                 max_depth=None, max_features='auto', max_leaf_nodes=None,
#                 min_impurity_decrease=0.0, min_impurity_split=None,
#                 min_samples_leaf=1, min_samples_split=2,
#                 min_weight_fraction_leaf=0.0, n_estimators='warn', n_jobs=None,
#                 oob_score=False, random_state=None, verbose=0,
#                 warm_start=False),
#            fit_params=None, iid='warn', n_jobs=4,
#            param_grid={'max_depth': [2, 4, 8, 15], 'max_features': ['auto', 'sqrt']},
#            pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
#            scoring='roc_auc', verbose=0)