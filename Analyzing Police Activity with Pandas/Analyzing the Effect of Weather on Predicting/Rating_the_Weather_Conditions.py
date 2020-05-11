# 5/11/2020
 Count the unique values in 'bad_conditions' and sort the index
print(weather.bad_conditions.value_counts().sort_index())

# Create a dictionary that maps integers to strings
mapping = {0:'good', 1:'bad', 2:'bad', 3: 'bad', 4: 'bad', 
           5: 'worse', 6: 'worse', 7: 'worse', 8: 'worse', 9: 'worse'}

# Convert the 'bad_conditions' integers to strings using the 'mapping'
weather['rating'] = weather.bad_conditions.map(mapping)

# Count the unique values in 'rating'
print(weather.rating.value_counts())

# <script.py> output:
#     0    1749
#     1     613
#     2     367
#     3     380
#     4     476
#     5     282
#     6     101
#     7      41
#     8       4
#     9       4
#     Name: bad_conditions, dtype: int64
#     bad      1836
#     good     1749
#     worse     432
#     Name: rating, dtype: int64
