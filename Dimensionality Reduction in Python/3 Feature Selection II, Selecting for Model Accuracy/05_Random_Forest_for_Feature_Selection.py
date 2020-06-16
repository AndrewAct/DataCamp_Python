# # 6/15/2020
# Now lets use the fitted random model to select the most important features from our input dataset X.

# The trained model from the previous exercise has been pre-loaded for you as rf

# Create a mask for features importances above the threshold
mask = rf.feature_importances_ > 0.15

# Apply the mask to the feature dataset X
reduced_X = X.loc[:, mask]

# prints out the selected column names
print(reduced_X.columns)

# <script.py> output:
#     [False  True False False False False False  True]

# <script.py> output:
#     Index(['glucose', 'age'], dtype='object')
