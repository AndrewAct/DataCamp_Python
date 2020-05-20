# 5/19/2020
# Setup the pipeline
steps = [('scaler', StandardScaler()),
         ('SVM', SVC())]

pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'SVM__C':[1, 10, 100],
              'SVM__gamma':[0.1, 0.01]}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 21)

# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline, param_grid= parameters)

# Fit to the training set
cv.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)

# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))

# <script.py> output:
#     Accuracy: 0.7795918367346939
#                  precision    recall  f1-score   support
    
#           False       0.83      0.85      0.84       662
#            True       0.67      0.63      0.65       318
    
#     avg / total       0.78      0.78      0.78       980
    
#     Tuned Model Parameters: {'SVM__C': 10, 'SVM__gamma': 0.1}
