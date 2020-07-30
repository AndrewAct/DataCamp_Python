# # 7/29/2020
# In most cases, performing a univariate linear regression will not yield a model that is useful for making accurate predictions. In this exercise, you will perform a multiple regression, which uses more than one feature.

# You will use price_log as your target and size_log and bedrooms as your features. Each of these tensors has been defined and is available. You will also switch from using the the mean squared error loss to the mean absolute error loss: keras.losses.mae(). Finally, the predicted values are computed as follows: params[0] + feature1*params[1] + feature2*params[2]. Note that we've defined a vector of parameters, params, as a variable, rather than using three variables. Here, params[0] is the intercept and params[1] and params[2] are the slopes.

# Define the linear regression model
def linear_regression(params, feature1 = size_log, feature2 = bedrooms):
	return params[0] + feature1*params[1] + feature2*params[2]

# Define the loss function
def loss_function(params, targets = price_log, feature1 = size_log, feature2 = bedrooms):
	# Set the predicted values
	predictions = linear_regression(params, feature1, feature2)
  
	# Use the mean absolute error loss
	return keras.losses.mae(targets, predictions)

# Define the optimize operation
opt = keras.optimizers.Adam()

# Perform minimization and print trainable variables
for j in range(10):
	opt.minimize(lambda: loss_function(params), var_list=[params])
	print_results(params)

# <script.py> output:
#     loss: 12.418, intercept: 0.101, slope_1: 0.051, slope_2: 0.021
#     loss: 12.404, intercept: 0.102, slope_1: 0.052, slope_2: 0.022
#     loss: 12.391, intercept: 0.103, slope_1: 0.053, slope_2: 0.023
#     loss: 12.377, intercept: 0.104, slope_1: 0.054, slope_2: 0.024
#     loss: 12.364, intercept: 0.105, slope_1: 0.055, slope_2: 0.025
#     loss: 12.351, intercept: 0.106, slope_1: 0.056, slope_2: 0.026
#     loss: 12.337, intercept: 0.107, slope_1: 0.057, slope_2: 0.027
#     loss: 12.324, intercept: 0.108, slope_1: 0.058, slope_2: 0.028
#     loss: 12.311, intercept: 0.109, slope_1: 0.059, slope_2: 0.029
#     loss: 12.297, intercept: 0.110, slope_1: 0.060, slope_2: 0.030