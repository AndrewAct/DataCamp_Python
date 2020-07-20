# # 7/18/2020
# You just finished running a colleagues code that creates a random forest model and calculates an out-of-sample accuracy. You noticed that your colleague's code did not have a random state, and the errors you found were completely different than the errors your colleague reported.

# To get a better estimate for how accurate this random forest model will be on new data, you have decided to generate some indices to use for KFold cross-validation.

from sklearn.model_selection import KFold

# Use KFold
kf = KFold(n_splits= 5, shuffle= True, random_state= 1111)

# Create splits
splits = kf.split(X)

# Print the number of indices
for train_index, val_index in splits:
    print("Number of training indices: %s" % len(train_index))
    print("Number of validation indices: %s" % len(val_index))

# <script.py> output:
#     Number of training indices: 68
#     Number of validation indices: 17
#     Number of training indices: 68
#     Number of validation indices: 17
#     Number of training indices: 68
#     Number of validation indices: 17
#     Number of training indices: 68
#     Number of validation indices: 17
#     Number of training indices: 68
#     Number of validation indices: 17