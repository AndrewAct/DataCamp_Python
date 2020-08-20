# # 8/19/2020
# Now it's time for stacking. To implement the stacking approach, you will follow the 6 steps we've discussed in the previous video:

# Split train data into two parts
# Train multiple models on Part 1
# Make predictions on Part 2
# Make predictions on the test data
# Train a new model on Part 2 using predictions as features
# Make predictions on the test data using the 2nd level model
# train and test DataFrames are already available in your workspace. features is a list of columns to be used for training on the Part 1 data and it is also available in your workspace. Target variable name is "fare_amount".

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor

# Split train data into two parts
part_1, part_2 = train_test_split(train, test_size=0.5, random_state=123)

# Train a Gradient Boosting model on Part 1
gb = GradientBoostingRegressor().fit(part_1[features], part_1.fare_amount)

# Train a Random Forest model on Part 1
rf = RandomForestRegressor().fit(part_1[features], part_1.fare_amount)

# Make predictions on the Part 2 data
part_2['gb_pred'] = gb.predict(part_2[features])
part_2['rf_pred'] = rf.predict(part_2[features])

# Make predictions on the test data
test['gb_pred'] = gb.predict(test[features])
test['rf_pred'] = rf.predict(test[features])