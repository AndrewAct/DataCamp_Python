# # 7/4/2020
# To use categorical variables in a machine learning model, you first need to represent them in a quantitative way. The two most common approaches are to one-hot encode the variables using or to use dummy variables. In this exercise, you will create both types of encoding, and compare the created column sets. We will continue using the same DataFrame from previous lesson loaded as so_survey_df and focusing on its Country column.

# Convert the Country column to a one hot encoded Data Frame
one_hot_encoded = pd.get_dummies(so_survey_df, columns=['Country'], prefix='OH')

# Print the columns names
print(one_hot_encoded.columns)

# <script.py> output:
#     Index(['SurveyDate', 'FormalEducation', 'ConvertedSalary', 'Hobby', 'StackOverflowJobsRecommend', 'VersionControl', 'Age', 'Years Experience', 'Gender', 'RawSalary', 'OH_France', 'OH_India',
#            'OH_Ireland', 'OH_Russia', 'OH_South Africa', 'OH_Spain', 'OH_Sweeden', 'OH_UK', 'OH_USA', 'OH_Ukraine'],
#           dtype='object')

# Create dummy variables for the Country column
dummy = pd.get_dummies(so_survey_df, columns=['Country'], drop_first=True, prefix='DM')

# Print the columns names
print(dummy.columns)

# <script.py> output:
#     Index(['SurveyDate', 'FormalEducation', 'ConvertedSalary', 'Hobby', 'StackOverflowJobsRecommend', 'VersionControl', 'Age', 'Years Experience', 'Gender', 'RawSalary', 'DM_India', 'DM_Ireland',
#            'DM_Russia', 'DM_South Africa', 'DM_Spain', 'DM_Sweeden', 'DM_UK', 'DM_USA', 'DM_Ukraine'],
#           dtype='object')