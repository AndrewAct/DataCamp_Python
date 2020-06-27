# # 6/26/2020
# Let's remove some of the rows where certain columns have missing values. We're going to look at the length_of_time column, the state column, and the type column. If any of the values in these columns are missing, we're going to drop the rows.

# Check how many values are missing in the length_of_time, state, and type columns
print(ufo[["length_of_time", "state", "type"]].isnull().sum())

# Keep only rows where length_of_time, state, and type are not null
ufo_no_missing = ufo[ufo["length_of_time"].notnull() & 
          ufo["state"].notnull() & 
          ufo["type"].notnull()]

# Print out the shape of the new dataset
print(ufo_no_missing.shape)

# <script.py> output:
#     length_of_time    143
#     state             419
#     type              159
#     dtype: int64
#     (4283, 4)