# # 6/25/2020
# Now that we have run PCA on the wine dataset, let's try training a model with it.

# Split the transformed X and the y labels into training and test sets
X_wine_train, X_wine_test, y_wine_train, y_wine_test = train_test_split(transformed_X, y)

# Fit knn to the training data
knn.fit(X_wine_train, y_wine_train)

# Score knn on the test data and print it out
print(knn.score(X_wine_test, y_wine_test))

# <script.py> output:
#     0.6444444444444445