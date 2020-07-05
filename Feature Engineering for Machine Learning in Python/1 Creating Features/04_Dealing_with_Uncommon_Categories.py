# 7/4/2020
# Some features can have many different categories but a very uneven distribution of their occurrences. Take for example Data Science's favorite languages to code in, some common choices are Python, R, and Julia, but there can be individuals with bespoke choices, like FORTRAN, C etc. In these cases, you may not want to create a feature for each value, but only the more common occurrences.
# Create a series out of the Country column
countries = so_survey_df['Country']

# Get the counts of each category
country_counts = countries.value_counts()

# Print the count values for each category
print(country_counts)

# <script.py> output:
#     South Africa    166
#     USA             164
#     Spain           134
#     Sweeden         119
#     France          115
#     Russia           97
#     India            95
#     UK               95
#     Ukraine           9
#     Ireland           5
#     Name: Country, dtype: int64

# Create a series out of the Country column
countries = so_survey_df['Country']

# Get the counts of each category
country_counts = countries.value_counts()

# Create a mask for only categories that occur less than 10 times
mask = countries.isin(country_counts[country_counts < 10].index)

# Print the top 5 rows in the mask series
print(mask.head())

# <script.py> output:
#     0    False
#     1    False
#     2    False
#     3    False
#     4    False
#     Name: Country, dtype: bool

# Create a series out of the Country column
countries = so_survey_df['Country']

# Get the counts of each category
country_counts = countries.value_counts()

# Create a mask for only categories that occur less than 10 times
mask = countries.isin(country_counts[country_counts < 10].index)

# Label all other categories as Other
countries[mask] = 'Other'

# Print the updated category counts
print(countries.value_counts())

# <script.py> output:
#     South Africa    166
#     USA             164
#     Spain           134
#     Sweeden         119
#     France          115
#     Russia           97
#     India            95
#     UK               95
#     Other            14
#     Name: Country, dtype: int64