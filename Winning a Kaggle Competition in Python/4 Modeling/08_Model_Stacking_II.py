# # 8/19/2020
# OK, what you've done so far in the stacking implementation:

# Split train data into two parts
# Train multiple models on Part 1
# Make predictions on Part 2
# Make predictions on the test data
# Now, your goal is to create a second level model using predictions from steps 3 and 4 as features. So, this model is trained on Part 2 data and then you can make stacking predictions on the test data.

# part_2 and test DataFrames are already available in your workspace. Gradient Boosting and Random Forest predictions are stored in these DataFrames under the names "gb_pred" and "rf_pred", respectively.

from sklearn.linear_model import LinearRegression

# Create linear regression model without the intercept
lr = LinearRegression(fit_intercept=False)

# Train 2nd level model on the Part 2 data
lr.fit(part_2[['gb_pred', 'rf_pred']], part_2.fare_amount)

# Make stacking predictions on the test data
test['stacking'] = lr.predict(test[['gb_pred', 'rf_pred']])

# Look at the model coefficients
print(lr.coef_)

# <script.py> output:
#     [0.72504358 0.27647395]