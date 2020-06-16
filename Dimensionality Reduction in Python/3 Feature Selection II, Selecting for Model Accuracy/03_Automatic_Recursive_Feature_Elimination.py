# # 6/15/2020
# Now let's automate this recursive process. Wrap a Recursive Feature Eliminator (RFE) around our logistic regression estimator and pass it the desired number of features.

# All the necessary functions and packages have been pre-loaded and the features have been scaled for you.

# Create the RFE with a LogisticRegression estimator and 3 features to select
rfe = RFE(estimator= LogisticRegression(), n_features_to_select= 3, verbose=1)

# Fits the eliminator to the data
rfe.fit(X_train, y_train)

# Print the features and their ranking (high = dropped early on)
print(dict(zip(X.columns, rfe.ranking_)))

# Print the features that are not eliminated
print(X.columns[rfe.support_])

# Calculates the test set accuracy
acc = accuracy_score(y_test, rfe.predict(X_test))
print("{0:.1%} accuracy on test set.".format(acc)) 

# <script.py> output:
#     Fitting estimator with 8 features.
#     Fitting estimator with 7 features.
#     Fitting estimator with 6 features.
#     Fitting estimator with 5 features.
#     Fitting estimator with 4 features.
#     {'diastolic': 6, 'glucose': 1, 'pregnant': 5, 'triceps': 3, 'bmi': 1, 'family': 2, 'insulin': 4, 'age': 1}
#     Index(['glucose', 'bmi', 'age'], dtype='object')
#     80.6% accuracy on test set.