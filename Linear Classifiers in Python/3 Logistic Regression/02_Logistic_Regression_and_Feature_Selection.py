# # 6/3/2020
# In this exercise we'll perform feature selection on the movie review sentiment data set using L1 regularization. The features and targets are already loaded for you in X_train and y_train.

# We'll search for the best value of C using scikit-learn's GridSearchCV(), which was covered in the prerequisite course.

# Specify L1 regularization
lr = LogisticRegression(penalty= "l1")

# Instantiate the GridSearchCV object and run the search
searcher = GridSearchCV(lr, {'C':[0.001, 0.01, 0.1, 1, 10]})
searcher.fit(X_train, y_train)

# Report the best parameters
print("Best CV params", searcher.best_params_)

# Find the number of nonzero coefficients (selected features)
best_lr = searcher.best_estimator_
coefs = best_lr.coef_
print("Total number of features:", coefs.size)
print("Number of selected features:", np.count_nonzero(coefs))

# <script.py> output:
#     Best CV params {'C': 1}
#     Total number of features: 2500
#     Number of selected features: 1220