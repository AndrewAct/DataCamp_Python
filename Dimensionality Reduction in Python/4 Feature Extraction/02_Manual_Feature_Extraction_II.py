# # 6/17/2020
# You're working on a variant of the ANSUR dataset, height_df, where a person's height was measured 3 times. Add a feature with the mean height to the dataset, then drop the 3 original features.

# Calculate the mean height
height_df['height'] = height_df[['height_1', 'height_2', 'height_3']].mean(axis = 1)

# Drop the 3 original height features
reduced_df = height_df.drop(['height_1', 'height_2', 'height_3'], axis=1)

print(reduced_df.head())

# <script.py> output:
#        weight_kg    height
#     0       81.5  1.793333
#     1       72.6  1.696667
#     2       92.9  1.740000
#     3       79.4  1.670000
#     4       94.6  1.913333