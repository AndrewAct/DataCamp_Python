# # 6/15/2020
# You'll again work on the Pima Indians dataset to predict whether an individual has diabetes. This time using a random forest classifier. You'll fit the model on the training data after performing the train-test split and consult the feature importance values.

# The feature and target datasets have been pre-loaded for you as X and y. Same goes for the necessary packages and functions.
# Perform a 75% training and 25% test data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=0)

# Fit the random forest model to the training data
rf = RandomForestClassifier(random_state=0)
rf.fit(X_train, y_train)

# Calculate the accuracy
acc = accuracy_score(y_test, rf.predict(X_test))

# Print the importances per feature
print(dict(zip(X.columns, rf.feature_importances_.round(2))))

# Print accuracy
print("{0:.1%} accuracy on test set.".format(acc))

# <script.py> output:
#     {'diastolic': 0.08, 'glucose': 0.21, 'pregnant': 0.09, 'triceps': 0.11, 'bmi': 0.09, 'family': 0.12, 'insulin': 0.13, 'age': 0.16}
#     77.6% accuracy on test set.