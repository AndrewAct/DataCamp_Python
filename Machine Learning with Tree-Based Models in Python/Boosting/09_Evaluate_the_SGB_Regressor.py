# # 5/26/2020
# You have prepared the ground to determine the test set RMSE of sgbr which you shall evaluate in this exercise.

# y_pred and y_test are available in your workspace.

# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Compute test set MSE
mse_test = MSE(y_test, y_pred)

# Compute test set RMSE
rmse_test = mse_test ** (1/2)

# Print rmse_test
print('Test set RMSE of sgbr: {:.3f}'.format(rmse_test))

# <script.py> output:
#     Test set RMSE of sgbr: 49.979