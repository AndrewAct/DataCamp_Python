# # 7/18/2020
# Creating a confusion matrix in Python is simple. The biggest challenge will be making sure you understand the orientation of the matrix. This exercise makes sure you understand the sklearn implementation of confusion matrices. Here, you have created a random forest model using the tic_tac_toe dataset rfc to predict outcomes of 0 (loss) or 1 (a win) for Player One.

# Note: If you read about confusion matrices on another website or for another programming language, the values might be reversed.

from sklearn.metrics import confusion_matrix

# Create predictions
test_predictions = rfc.predict(X_test)

# Create and print the confusion matrix
cm = confusion_matrix(y_test, test_predictions)
print(cm)

# Print the true positives (actual 1s that were predicted 1s)
print("The number of true positives is: {}".format(cm[1, 1]))