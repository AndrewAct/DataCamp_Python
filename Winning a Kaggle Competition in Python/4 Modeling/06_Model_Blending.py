# # 8/19/2020
# You will start creating model ensembles with a blending technique.

# Your goal is to train 2 different models on the New York City Taxi competition data. Make predictions on the test data and then blend them using a simple arithmetic mean.

# The train and test DataFrames are already available in your workspace. features is a list of columns to be used for training and it is also available in your workspace. The target variable name is "fare_amount".

from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor

# Train a Gradient Boosting model
gb = GradientBoostingRegressor().fit(train[features], train.fare_amount)

# Train a Random Forest model
rf = RandomForestRegressor().fit(train[features], train.fare_amount)

# Make predictions on the test data
test['gb_pred'] = gb.predict(test[features])
test['rf_pred'] = rf.predict(test[features])

# Find mean of model predictions
test['blend'] = (test['gb_pred'] + test['rf_pred']) / 2
print(test[['gb_pred', 'rf_pred', 'blend']].head(3))

# <script.py> output:
#         gb_pred  rf_pred     blend
#     0  9.661374     9.00  9.330687
#     1  9.304288     8.45  8.877144
#     2  5.795140     5.11  5.452570
