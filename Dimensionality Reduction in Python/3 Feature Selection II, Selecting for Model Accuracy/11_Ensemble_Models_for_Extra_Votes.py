# # 6/16/2020
# The LassoCV() model selected 26 out of 32 features. Not bad, but not a spectacular dimensionality reduction either. Let's use two more models to select the 10 features they consider most important using the Recursive Feature Eliminator (RFE).

# The standardized training and test data has been pre-loaded for you as X_train, X_test, y_train, and y_test.

from sklearn.feature_selection import RFE
from sklearn.ensemble import GradientBoostingRegressor

# Select 10 features with RFE on a GradientBoostingRegressor, drop 3 features on each step
rfe_gb = RFE(estimator=GradientBoostingRegressor(), 
             n_features_to_select=10, step=3, verbose=1)
rfe_gb.fit(X_train, y_train)

# Calculate the R squared on the test set
r_squared = rfe_gb.score(X_test, y_test)
print('The model can explain {0:.1%} of the variance in the test set'.format(r_squared))

# Assign the support array to gb_mask
gb_mask = rfe_gb.support_

# <script.py> output:
#     Fitting estimator with 32 features.
#     Fitting estimator with 29 features.
#     Fitting estimator with 26 features.
#     Fitting estimator with 23 features.
#     Fitting estimator with 20 features.
#     Fitting estimator with 17 features.
#     Fitting estimator with 14 features.
#     Fitting estimator with 11 features.
#     The model can explain 85.6% of the variance in the test set

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor

# Select 10 features with RFE on a RandomForestRegressor, drop 3 features on each step
rfe_rf = RFE(estimator= RandomForestRegressor(), 
             n_features_to_select= 10, step= 3, verbose=1)
rfe_rf.fit(X_train, y_train)

# Calculate the R squared on the test set
r_squared = rfe_rf.score(X_test, y_test)
print('The model can explain {0:.1%} of the variance in the test set'.format(r_squared))

# Assign the support array to gb_mask
rf_mask = rfe_rf.support_

# <script.py> output:
#     Fitting estimator with 32 features.
#     Fitting estimator with 29 features.
#     Fitting estimator with 26 features.
#     Fitting estimator with 23 features.
#     Fitting estimator with 20 features.
#     Fitting estimator with 17 features.
#     Fitting estimator with 14 features.
#     Fitting estimator with 11 features.
#     The model can explain 84.0% of the variance in the test set