# # 5/23/2020
# In this exercise, you'll train a regression tree to predict the mpg (miles per gallon) consumption of cars in the auto-mpg dataset using all the six available features.

# The dataset is processed for you and is split to 80% train and 20% test. 
# The features matrix X_train and the array y_train are available in your workspace.

# Import DecisionTreeRegressor from sklearn.tree
from sklearn.tree import DecisionTreeRegressor

# Instantiate dt
dt = DecisionTreeRegressor(max_depth= 8,
             min_samples_leaf = 0.13,
            random_state=3)

# Fit dt to the training set
dt.fit(X_train, y_train)