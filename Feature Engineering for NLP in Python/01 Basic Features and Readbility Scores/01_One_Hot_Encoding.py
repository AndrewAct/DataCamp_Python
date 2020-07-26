# # 7/25/2020
# In the previous exercise, we encountered a dataframe df1 which contained categorical features and therefore, was unsuitable for applying ML algorithms to.

# In this exercise, your task is to convert df1 into a format that is suitable for machine learning.

# Print the features of df1
print(df1.columns)

# Perform one-hot encoding
df1 = pd.get_dummies(df1, columns=['feature 5'])

# Print the new features of df1
print(df1.columns)

# Print first five rows of df1
print(df1.head())

# <script.py> output:
#     Index(['feature 1', 'feature 2', 'feature 3', 'feature 4', 'feature 5', 'label'], dtype='object')
#     Index(['feature 1', 'feature 2', 'feature 3', 'feature 4', 'label', 'feature 5_female', 'feature 5_male'], dtype='object')
#        feature 1  feature 2  feature 3  feature 4  label  feature 5_female  feature 5_male
#     0    29.0000          0          0   211.3375      1                 1               0
#     1     0.9167          1          2   151.5500      1                 0               1
#     2     2.0000          1          2   151.5500      0                 1               0
#     3    30.0000          1          2   151.5500      0                 0               1
#     4    25.0000          1          2   151.5500      0                 1               0
