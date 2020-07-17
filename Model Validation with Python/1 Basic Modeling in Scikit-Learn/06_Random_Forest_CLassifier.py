# # 7/16/2020
# This exercise reviews the four modeling steps discussed throughout this chapter using a random forest classification model. You will:

# Create a random forest classification model.
# Fit the model using the tic_tac_toe dataset.
# Make predictions on whether Player One will win (1) or lose (0) the current game.
# Finally, you will evaluate the overall accuracy of the model.
# Let's get started!

from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rfc = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=1111)

# Fit rfc using X_train and y_train
rfc.fit(X_train, y_train)

# Create predictions on X_test
predictions = rfc.predict(X_test)
print(predictions[0:5])

# Print model accuracy using score() and the testing data
print(rfc.score(X_test, y_test))

# <script.py> output:
#     [1 1 1 1 1]
#     0.817470664928292
