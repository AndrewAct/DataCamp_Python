# # 6/6/2020
# It's now time to begin evaluating model quality.

# Here, you will compare the RMSE and MAE of a cross-validated XGBoost model on the Ames housing data. As in previous exercises, all necessary modules have been pre-loaded and the data is available in the DataFrame df.
# Create the DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary: params
params = {"objective":"reg:linear", "max_depth":4}

# Perform cross-validation: cv_results
cv_results = xgb.cv(dtrain= housing_dmatrix, params= params, nfold= 4, num_boost_round= 5, metrics= "rmse", as_pandas=True, seed=123)

# Print cv_results
print(cv_results)

# Extract and print final boosting round metric
print((cv_results["test-rmse-mean"]).tail(1))


# <script.py> output:
#     [03:20:00] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:20:00] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:20:00] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:20:00] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#        train-rmse-mean  train-rmse-std  test-rmse-mean  test-rmse-std
#     0    141767.527344      429.450237   142980.429688    1193.794436
#     1    102832.542969      322.473304   104891.392578    1223.157623
#     2     75872.617187      266.469946    79478.939453    1601.341376
#     3     57245.650390      273.626583    62411.921875    2220.149857
#     4     44401.297851      316.422372    51348.280274    2963.379319
#     4    51348.280274
#     Name: test-rmse-mean, dtype: float64

# Create the DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary: params
params = {"objective":"reg:linear", "max_depth":4}

# Perform cross-validation: cv_results
# "mae" should refer to mean absolute error
cv_results = xgb.cv(dtrain= housing_dmatrix, params= params, nfold= 4, num_boost_round= 5, metrics= "mae", as_pandas=True, seed=123)

# Print cv_results
print(cv_results)

# Extract and print final boosting round metric
print((cv_results["test-mae-mean"]).tail(1))

# <script.py> output:
#     [03:22:34] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:22:35] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:22:36] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#     [03:22:36] WARNING: /workspace/src/objective/regression_obj.cu:152: reg:linear is now deprecated in favor of reg:squarederror.
#        train-mae-mean  train-mae-std  test-mae-mean  test-mae-std
#     0   127343.480468     668.337982  127633.980469   2404.008070
#     1    89770.052735     456.957620   90122.500000   2107.913315
#     2    63580.791992     263.408277   64278.561523   1887.564925
#     3    45633.153320     151.884919   46819.167968   1459.819967
#     4    33587.093750      86.999137   35670.645508   1140.606558
#     4    35670.645508
#     Name: test-mae-mean, dtype: float64
