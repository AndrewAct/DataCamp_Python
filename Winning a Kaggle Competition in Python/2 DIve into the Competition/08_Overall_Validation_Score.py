# # 8/18/2020
# Now it's time to get the actual model performance using cross-validation! How does our store item demand prediction model perform?

# Your task is to take the Mean Squared Error (MSE) for each fold separately, and then combine these results into a single number.

# For simplicity, you're given get_fold_mse() function that for each cross-validation split fits a Random Forest model and returns a list of MSE scores by fold. get_fold_mse() accepts two arguments: train and TimeSeriesSplit object.

from sklearn.model_selection import TimeSeriesSplit
import numpy as np

# Sort train data by date
train = train.sort_values('date')

# Initialize 3-fold time cross-validation
kf = TimeSeriesSplit(n_splits=3)

# Get MSE scores for each cross-validation split
mse_scores = get_fold_mse(train, kf)

print('Mean validation MSE: {:.5f}'.format(np.mean(mse_scores)))
print('MSE by fold: {}'.format(mse_scores))
print('Overall validation MSE: {:.5f}'.format(np.mean(mse_scores) + np.std(mse_scores)))

# <script.py> output:
#     Mean validation MSE: 955.49186
#     MSE by fold: [890.30336, 961.65797, 1014.51424]
#     Overall validation MSE: 1006.38784
