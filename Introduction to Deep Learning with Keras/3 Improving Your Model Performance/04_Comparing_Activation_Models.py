# # 8/9/2020
# Comparing activation functions involves a bit of coding, but nothing you can't do!

# You will try out different activation functions on the multi-label model you built for your farm irrigation machine in chapter 2. The function get_model('relu') returns a copy of this model and applies the 'relu' activation function to its hidden layer.

# You will loop through several activation functions, generate a new model for each and train it. By storing the history callback in a dictionary you will be able to visualize which activation function performed best in the next exercise!

# X_train, y_train, X_test, y_test are ready for you to use when training your models.

# Activation functions to try
activations = ['relu', 'leaky_relu', 'sigmoid', 'tanh']

# Loop over the activation functions
activation_results = {}

for act in activations:
  # Get a new model with the current activation
  model = get_model(act)
  # Fit the model and store the history results
  h_callback = model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 20, verbose = 0)
  activation_results[act] = h_callback

# <script.py> output:
#     Finishing with relu ...
#     Finishing with leaky_relu ...
#     Finishing with sigmoid ...
#     Finishing with tanh ...