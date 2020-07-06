# # 7/5/2020
# While having a summary of how much of your data is missing can be useful, often you will need to find the exact locations of these missing values. Using the same subset of the StackOverflow data from the last exercise (sub_df), you will show how a value can be flagged as missing.

# Print the top 10 entries of the DataFrame
print(sub_df.head(10))

# <script.py> output:
#        Age  Gender
#     0   21    Male
#     1   38    Male
#     2   45     NaN
#     3   46    Male
#     4   39    Male
#     5   39    Male
#     6   34    Male
#     7   24  Female
#     8   23    Male
#     9   36     NaN

# Print the locations of the missing values
print(sub_df.head(10).isnull())

# <script.py> output:
#          Age  Gender
#     0  False   False
#     1  False   False
#     2  False    True
#     3  False   False
#     4  False   False
#     5  False   False
#     6  False   False
#     7  False   False
#     8  False   False
#     9  False    True

# Print the locations of the non-missing values
print(sub_df.head(10).notnull())

# <script.py> output:
#         Age  Gender
#     0  True    True
#     1  True    True
#     2  True   False
#     3  True    True
#     4  True    True
#     5  True    True
#     6  True    True
#     7  True    True
#     8  True    True
#     9  True   False


