# # 7/5/2020
# Most data sets contain missing values, often represented as NaN (Not a Number). If you are working with Pandas you can easily check how many missing values exist in each column.

# Let's find out how many of the developers taking the survey chose to enter their age (found in the Age column of so_survey_df) and their gender (Gender column of so_survey_df).
# Subset the DataFrame
sub_df = so_survey_df[['Age', 'Gender']]

# Print the number of non-missing values
print(sub_df.notnull().sum())

# <script.py> output:
#     Age       999
#     Gender    693
#     dtype: int64