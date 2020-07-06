# # 7/5/2020
# In the last lesson, you dealt with different methods of removing data missing values and filling in missing values with a fixed string. These approaches are valid in many cases, particularly when dealing with categorical columns but have limited use when working with continuous values. In these cases, it may be most valid to fill the missing values in the column with a value calculated from the entries present in the column.

# Print the first five rows of StackOverflowJobsRecommend column
print(so_survey_df['StackOverflowJobsRecommend'].head())

# <script.py> output:
#     0    NaN
#     1    7.0
#     2    8.0
#     3    NaN
#     4    8.0
#     Name: StackOverflowJobsRecommend, dtype: float64

# Fill missing values with the mean
so_survey_df['StackOverflowJobsRecommend'].fillna(so_survey_df['StackOverflowJobsRecommend'].mean(), inplace=True)

# Print the first five rows of StackOverflowJobsRecommend column
print(so_survey_df['StackOverflowJobsRecommend'].head())

# <script.py> output:
#     0    7.061602
#     1    7.000000
#     2    8.000000
#     3    7.061602
#     4    8.000000
#     Name: StackOverflowJobsRecommend, dtype: float64

# Fill missing values with the mean
so_survey_df['StackOverflowJobsRecommend'].fillna(so_survey_df['StackOverflowJobsRecommend'].mean(), inplace=True)

# Round the StackOverflowJobsRecommend values
so_survey_df['StackOverflowJobsRecommend'] = round(so_survey_df['StackOverflowJobsRecommend'])

# Print the top 5 rows
print(so_survey_df['StackOverflowJobsRecommend'].head())

# <script.py> output:
#     0    7.0
#     1    7.0
#     2    8.0
#     3    7.0
#     4    8.0
#     Name: StackOverflowJobsRecommend, dtype: float64
