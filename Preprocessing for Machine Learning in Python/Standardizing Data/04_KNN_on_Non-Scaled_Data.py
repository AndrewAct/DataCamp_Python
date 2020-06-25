# # 6/24/2020
# Let's first take a look at the accuracy of a K-nearest neighbors model on the wine dataset without standardizing the data. The knn model as well as the X and y data and labels sets have been created already. Most of this process of creating models in scikit-learn should look familiar to you.

# Split the dataset and labels into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Fit the k-nearest neighbors model to the training data
knn.fit(X_train, y_train)

# Score the model on the test data
print(knn.score(X_test, y_test))

# <script.py> output:
#     0.6444444444444445
