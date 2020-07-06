# # 7/5/2020
# The simplest way to deal with missing values in your dataset when they are occurring entirely at random is to remove those rows, also called 'listwise deletion'.

# Depending on the use case, you will sometimes want to remove all missing values in your data while other times you may want to only remove a particular column if too many values are missing in that column.

# Print the number of rows and columns
print(so_survey_df.shape)

# <script.py> output:
#     (999, 11)

# Create a new DataFrame dropping all incomplete rows
no_missing_values_rows = so_survey_df.dropna()

# Print the shape of the new DataFrame
print(no_missing_values_rows.shape)

# <script.py> output:
#     (264, 11)

# Create a new DataFrame dropping all columns with incomplete rows
no_missing_values_cols = so_survey_df.dropna(how = 'any', axis=1)

# Print the shape of the new DataFrame
print(no_missing_values_cols.shape)

# <script.py> output:
#     (999, 7)

# Drop all rows where Gender is missing
no_gender = so_survey_df.dropna(subset= ['Gender'])

# Print the shape of the new DataFrame
print(no_gender.shape)

# <script.py> output:
#     (693, 11)