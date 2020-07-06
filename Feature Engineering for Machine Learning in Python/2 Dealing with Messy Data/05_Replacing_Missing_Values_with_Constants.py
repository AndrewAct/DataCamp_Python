# # 7/5/2020
# While removing missing data entirely maybe a correct approach in many situations, this may result in a lot of information being omitted from your models.

# You may find categorical columns where the missing value is a valid piece of information in itself, such as someone refusing to answer a question in a survey. In these cases, you can fill all missing values with a new category entirely, for example 'No response given'.

# Replace missing values
so_survey_df['Gender'].fillna(value = 'Not Given', inplace = True)

# Print the count of each value
print(so_survey_df['Gender'].value_counts())

# <script.py> output:
#     Male                                                                         632
#     Not Given                                                                    306
#     Female                                                                        53
#     Female;Male                                                                    2
#     Transgender                                                                    2
#     Female;Transgender                                                             1
#     Male;Non-binary. genderqueer. or gender non-conforming                         1
#     Non-binary. genderqueer. or gender non-conforming                              1
#     Female;Male;Transgender;Non-binary. genderqueer. or gender non-conforming      1
#     Name: Gender, dtype: int64
