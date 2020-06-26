# # 6/25/2020
# Now let's identify the redundant columns in the volunteer dataset and perform feature selection on the dataset to return a DataFrame of the relevant features.

# For example, if you explore the volunteer dataset in the console, you'll see three features which are related to location: locality, region, and postalcode. They contain repeated information, so it would make sense to keep only one of the features.

# There are also features that have gone through the feature engineering process: columns like Education and Emergency Preparedness are a product of encoding the categorical variable category_desc, so category_desc itself is redundant now.

# Take a moment to examine the features of volunteer in the console, and try to identify the redundant features.

# Create a list of redundant column names to drop
to_drop = ["locality", "region", "category_desc", "created_date", "vol_requests"]

# Drop those columns from the dataset
volunteer_subset = volunteer.drop(to_drop, axis = 1)

# Print out the head of the new dataset
print(volunteer_subset.head())

# <script.py> output:
#                                                    title            ...              Strengthening Communities
#     1                                       Web designer            ...                                      1
#     2      Urban Adventures - Ice Skating at Lasker Rink            ...                                      1
#     3  Fight global hunger and support women farmers ...            ...                                      1
#     4                                      Stop 'N' Swap            ...                                      0
#     5                               Queens Stop 'N' Swap            ...                                      0
    
#     [5 rows x 11 columns]