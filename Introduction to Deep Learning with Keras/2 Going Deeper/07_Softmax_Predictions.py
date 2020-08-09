# # 8/9/2020
# Your recently trained model is loaded for you. This model is generalizing well!, that's why you got a high accuracy on the test set.

# Since you used the softmax activation function, for every input of 2 coordinates provided to your model there's an output vector of 4 numbers. Each of these numbers encodes the probability of a given dart being thrown by one of the 4 possible competitors.

# When computing accuracy with the model's .evaluate() method, your model takes the class with the highest probability as the prediction. np.argmax() can help you do this since it returns the index with the highest value in an array.

# Use the collection of test throws stored in coords_small_test and np.argmax()to check this out!

# Predict on coords_small_test
preds = model.predict(coords_small_test)

# Print preds vs true values
print("{:45} | {}".format('Raw Model Predictions','True labels'))
for i,pred in enumerate(preds):
  print("{} | {}".format(pred,competitors_small_test[i]))

# Extract the position of highest probability from each pred vector
preds_chosen = [np.argmax(pred) for pred in preds]

# Print preds vs true values
print("{:10} | {}".format('Rounded Model Predictions','True labels'))
for i,pred in enumerate(preds_chosen):
  print("{:25} | {}".format(pred,competitors_small_test[i]))

# <script.py> output:
#     Raw Model Predictions                         | True labels
#     [0.34438723 0.00842557 0.63167274 0.01551455] | [0. 0. 1. 0.]
#     [0.0989717  0.00530467 0.07537904 0.8203446 ] | [0. 0. 0. 1.]
#     [0.33512568 0.00785374 0.28132284 0.37569773] | [0. 0. 0. 1.]
#     [0.8547263  0.01328656 0.11279515 0.01919206] | [1. 0. 0. 0.]
#     [0.3540977  0.00867271 0.6223853  0.01484426] | [0. 0. 1. 0.]
#     Rounded Model Predictions | True labels
#                             2 | [0. 0. 1. 0.]
#                             3 | [0. 0. 0. 1.]
#                             3 | [0. 0. 0. 1.]
#                             0 | [1. 0. 0. 0.]
#                             2 | [0. 0. 1. 0.]