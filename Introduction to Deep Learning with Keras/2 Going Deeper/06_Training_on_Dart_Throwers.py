# # 8/9/2020
# Your model is now ready, just as your dataset. It's time to train!

# The coordinates features and competitors labels you just transformed have been partitioned into coord_train,coord_test and competitors_train,competitors_test.

# Your model is also loaded. Feel free to visualize your training data or model.summary() in the console.

# Let's find out who threw which dart just by looking at the board!

# Fit your model to the training data for 200 epochs
model.fit(coord_train,competitors_train,epochs = 200)

# Evaluate your model accuracy on the test data
accuracy = model.evaluate(coord_test, competitors_test)[1]

# Print accuracy
print('Accuracy:', accuracy)

