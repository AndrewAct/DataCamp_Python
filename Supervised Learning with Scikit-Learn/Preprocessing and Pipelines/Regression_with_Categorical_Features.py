# 5/19/2020
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha = 0.5, normalize = True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge,X, y, cv= 5)

# Print the cross-validated scores
print(ridge_cv)

# <script.py> output:
#     [0.86808336 0.80623545 0.84004203 0.7754344  0.87503712]
