# # 5/24/2020
# In this exercise, you'll study the effects of tokenizing in different ways by comparing the bag-of-words representations resulting from different token patterns.

# You will focus on one feature only, the Position_Extra column, which describes any additional information not captured by the Position_Type label.

# For example, in the Shell you can check out the budget item in row 8960 of the data using df.loc[8960]. 
# Looking at the output reveals that this Object_Description is overtime pay. For who? 
# The Position Type is merely "other", but the Position Extra elaborates: "BUS DRIVER". 
# Explore the column further to see more instances. It has a lot of NaN values.

# Your task is to turn the raw text in this column into a bag-of-words representation by creating tokens that contain only alphanumeric characters.

# For comparison purposes, the first 15 tokens of vec_basic, which splits df.Position_Extra into tokens when it encounters only whitespace characters, have been printed along with the length of the representation.
# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create the token pattern: TOKENS_ALPHANUMERIC
TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

# Fill missing values in df.Position_Extra
df.Position_Extra.fillna('', inplace = True)

# Instantiate the CountVectorizer: vec_alphanumeric
vec_alphanumeric = CountVectorizer(token_pattern = TOKENS_ALPHANUMERIC)

# Fit to the data
vec_alphanumeric.fit(df.Position_Extra)

# Print the number of tokens and first 15 tokens
msg = "There are {} tokens in Position_Extra if we split on non-alpha numeric"
print(msg.format(len(vec_alphanumeric.get_feature_names())))
print(vec_alphanumeric.get_feature_names()[:15])


# <script.py> output:
#     There are 123 tokens in Position_Extra if we split on non-alpha numeric
#     ['1st', '2nd', '3rd', 'a', 'ab', 'additional', 'adm', 'administrative', 'and', 'any', 'art', 'assessment', 'assistant', 'asst', 'athletic']
