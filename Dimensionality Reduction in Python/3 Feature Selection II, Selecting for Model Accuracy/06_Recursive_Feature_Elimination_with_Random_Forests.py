# # 6/15/2020
# You'll wrap a Recursive Feature Eliminator around a random forest model to remove features step by step. This method is more conservative compared to selecting features after applying a single importance threshold. Since dropping one feature can influence the relative importances of the others.

# You'll need these pre-loaded datasets: X, X_train, y_train.

# Functions and classes that have been pre-loaded for you are: RandomForestClassifier(), RFE(), train_test_split().

# Set the feature eliminator to remove 2 features on each step
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=2, step = 2, verbose=1)

# Fit the model to the training data
rfe.fit(X_train, y_train)

# Create a mask
mask = rfe.support_

# Apply the mask to the feature dataset X and print the result
reduced_X = X.loc[:, mask]
print(reduced_X.columns)

# <script.py> output:
#     Fitting estimator with 8 features.
#     Fitting estimator with 6 features.
#     Fitting estimator with 4 features.
#     Index(['glucose', 'insulin'], dtype='object')
