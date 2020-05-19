# 5/18/2020
# Import the necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

# Create the classifier: logreg
logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = logreg.predict(X_test)

# Compute and print the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# <script.py> output:
#     [[176  30]
#      [ 35  67]]
#                  precision    recall  f1-score   support
    
#               0       0.83      0.85      0.84       206
#               1       0.69      0.66      0.67       102
    
#     avg / total       0.79      0.79      0.79       308