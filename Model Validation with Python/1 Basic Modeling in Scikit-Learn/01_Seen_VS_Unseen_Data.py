# # 7/15/2020
# Model's tend to have higher accuracy on observations they have seen before. In the candy dataset, predicting the popularity of Skittles will likely have higher accuracy than predicting the popularity of Andes Mints; Skittles is in the dataset, and Andes Mints is not.

# You've built a model based on 50 candies using the dataset X_train and need to report how accurate the model is at predicting the popularity of the 50 candies the model was built on, and the 35 candies (X_test) it has never seen. You will use the mean absolute error, mae(), as the accuracy metric.

# The model is fit using X_train and y_train
model.fit(X_train, y_train)

# Create vectors of predictions
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Train/Test Errors
train_error = mae(y_true=y_train, y_pred=train_predictions)
test_error = mae(y_true=y_test, y_pred=test_predictions)

# Print the accuracy for seen and unseen data
print("Model error on seen data: {0:.2f}.".format(train_error))
print("Model error on unseen data: {0:.2f}.".format(test_error))

# <script.py> output:
#     Model error on seen data: 3.28.
#     Model error on unseen data: 11.07.