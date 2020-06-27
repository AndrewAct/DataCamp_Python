# # 6/26/2020
# In this exercise, we're going to build a k-nearest neighbor model to predict which country the UFO sighting took place in. Our X dataset has the log-normalized seconds column, the one-hot encoded type columns, as well as the month and year when the sighting took place. The y labels are the encoded country column, where 1 is us and 0 is ca.

# Take a look at the features in the X set of data
print(X.columns)

# Split the X and y sets using train_test_split, setting stratify=y
train_X, test_X, train_y, test_y = train_test_split(X, y, stratify = y)

# Fit knn to the training sets
knn.fit(train_X, train_y)

# Print the score of knn on the test sets
print(knn.score(test_X, test_y))

# <script.py> output:
#     Index(['seconds_log', 'changing', 'chevron', 'cigar', 'circle', 'cone',
#            'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash',
#            'formation', 'light', 'other', 'oval', 'rectangle', 'sphere',
#            'teardrop', 'triangle', 'unknown', 'month', 'year'],
#           dtype='object')
#     0.8693790149892934