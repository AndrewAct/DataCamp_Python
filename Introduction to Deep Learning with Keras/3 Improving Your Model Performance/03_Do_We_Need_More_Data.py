# # 8/9/2020
# It's time to check whether the digits dataset model you built benefits from more training examples!

# In order to keep code to a minimum, various things are already initialized and ready to use:

# The model you just built.
# X_train,y_train,X_test, and y_test.
# The initial_weights of your model, saved after using model.get_weights().
# A pre-defined list of training sizes: training_sizes.
# A pre-defined early stopping callback monitoring loss: early_stop.
# Two empty lists to store the evaluation results: train_accs and test_accs.
# Train your model on the different training sizes and evaluate the results on X_test. End by plotting the results with plot_results().

# The full code for this exercise can be found on the slides!

for size in training_sizes:
      	# Get a fraction of training data (we only care about the training data)
    X_train_frac, y_train_frac = X_train[:size], y_train[:size]

    # Reset the model to the initial weights and train it on the new training data fraction
    model.set_weights(initial_weights)
    model.fit(X_train_frac, y_train_frac, epochs = 50, callbacks = [early_stop])

    # Evaluate and store both: the training data fraction and the complete test set results
    train_accs.append(model.evaluate(X_train_frac, y_train_frac)[1])
    test_accs.append(model.evaluate(X_test, y_test)[1])
    
# Plot train vs test accuracies
plot_results(train_accs, test_accs)

