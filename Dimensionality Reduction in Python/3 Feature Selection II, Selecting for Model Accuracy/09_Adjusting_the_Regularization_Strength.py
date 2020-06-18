# # 6/16/2020
# Your current Lasso model has an R2 score of 84.7%. When a model applies overly powerful regularization it can suffer from high bias, hurting its predictive power.

# Let's improve the balance between predictive power and model simplicity by tweaking the alpha parameter.

# Find the highest alpha value with R-squared above 98%
# The higher alpha is, the more values would be close to zero
la = Lasso(alpha = 0.1, random_state=0)

# Fits the model and calculates performance stats
la.fit(X_train_std, y_train)
r_squared = la.score(X_test_std, y_test)
n_ignored_features = sum(la.coef_ == 0)

# Print peformance stats 
print("The model can predict {0:.1%} of the variance in the test set.".format(r_squared))
print("{} out of {} features were ignored.".format(n_ignored_features, len(la.coef_)))

# <script.py> output:
#     The model can predict 98.3% of the variance in the test set.
#     64 out of 91 features were ignored.