# # 6/5/2020
# You'll now practice using XGBoost's learning API through its baked in cross-validation capabilities. As Sergey discussed in the previous video, XGBoost gets its lauded performance and efficiency gains by utilizing its own optimized data structure for datasets called a DMatrix.

# In the previous exercise, the input datasets were converted into DMatrix data on the fly, but when you use the xgboost cv object, you have to first explicitly convert your data into a DMatrix. So, that's what you will do here before running cross-validation on churn_data.

# Create arrays for the features and the target: X, y
X, y = churn_data.iloc[:,:-1], churn_data.iloc[:,-1]

# Create the DMatrix from X and y: churn_dmatrix
churn_dmatrix = xgb.DMatrix(data= churn_data.iloc[:,:-1], label= churn_data.month_5_still_here)

# Create the parameter dictionary: params
params = {"objective":"reg:logistic", "max_depth":3}

# Perform cross-validation: cv_results
cv_results = xgb.cv(dtrain= churn_dmatrix, params= params, 
                  nfold= 3, num_boost_round= 5, 
                  metrics="error", as_pandas= True, seed=123)

# Print cv_results
print(cv_results)

# Print the accuracy
print(((1-cv_results["test-error-mean"]).iloc[-1]))

# <script.py> output:
#        train-error-mean  train-error-std  test-error-mean  test-error-std
#     0           0.28232         0.002366          0.28378        0.001932
#     1           0.26951         0.001855          0.27190        0.001932
#     2           0.25605         0.003213          0.25798        0.003963
#     3           0.25090         0.001845          0.25434        0.003827
#     4           0.24654         0.001981          0.24852        0.000934
#     0.75148