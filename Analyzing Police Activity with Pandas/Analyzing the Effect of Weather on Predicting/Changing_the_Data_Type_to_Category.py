# 5/11/2020
# Create a list of weather ratings in logical order
cats = ['good', 'bad', 'worse']

# Change the data type of 'rating' to category
weather['rating'] = weather.rating.astype('category', ordered=True, categories = cats)

# Examine the head of 'rating'
print(weather.rating.head())

# <script.py> output:
#     0    bad
#     1    bad
#     2    bad
#     3    bad
#     4    bad
#     Name: rating, dtype: category
#     Categories (3, object): [good < bad < worse]