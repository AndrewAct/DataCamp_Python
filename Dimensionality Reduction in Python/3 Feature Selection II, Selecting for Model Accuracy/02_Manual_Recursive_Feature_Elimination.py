# # 6/15/2020
# Now that we've created a diabetes classifier, let's see if we can reduce the number of features without hurting the model accuracy too much.

# On the second line of code the features are selected from the original dataframe. Adjust this selection.

# A StandardScaler() instance has been predefined as scaler and a LogisticRegression() one as lr.

# All necessary functions and packages have been pre-loaded too.

# Remove the feature with the lowest model coefficient
X = diabetes_df[['pregnant', 'glucose', 'triceps', 'insulin', 'bmi', 'family', 'age']]

# Performs a 25-75% train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Scales features and fits the logistic regression model
lr.fit(scaler.fit_transform(X_train), y_train)

# Calculates the accuracy on the test set and prints coefficients
acc = accuracy_score(y_test, lr.predict(scaler.transform(X_test)))
print("{0:.1%} accuracy on test set.".format(acc)) 
print(dict(zip(X.columns, abs(lr.coef_[0]).round(2))))

# 80.6% accuracy on test set.
# {'glucose': 1.23, 'pregnant': 0.05, 'triceps': 0.24, 'bmi': 0.39, 'family': 0.34, 'insulin': 0.2, 'age': 0.35}


# Remove the 2 features with the lowest model coefficients
X = diabetes_df[['glucose', 'triceps', 'bmi', 'family', 'age']]

# Performs a 25-75% train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Scales features and fits the logistic regression model
lr.fit(scaler.fit_transform(X_train), y_train)

# Calculates the accuracy on the test set and prints coefficients
acc = accuracy_score(y_test, lr.predict(scaler.transform(X_test)))
print("{0:.1%} accuracy on test set.".format(acc)) 
print(dict(zip(X.columns, abs(lr.coef_[0]).round(2))))

# script.py> output:
#     79.6% accuracy on test set.
#     {'bmi': 0.34, 'glucose': 1.13, 'family': 0.34, 'age': 0.37, 'triceps': 0.25}

# Only keep the feature with the highest coefficient
X = diabetes_df[['glucose']]

# Performs a 25-75% train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Scales features and fits the logistic regression model to the data
lr.fit(scaler.fit_transform(X_train), y_train)

# Calculates the accuracy on the test set and prints coefficients
acc = accuracy_score(y_test, lr.predict(scaler.transform(X_test)))
print("{0:.1%} accuracy on test set.".format(acc)) 
print(dict(zip(X.columns, abs(lr.coef_[0]).round(2))))

# <script.py> output:
#     76.5% accuracy on test set.
#     {'glucose': 1.27}