# # 7/11/2020
# Once high level information has been recorded you can begin creating features based on the actual content of each text. One way to do this is to approach it in a similar way to how you worked with categorical variables in the earlier lessons.

# For each unique word in the dataset a column is created.
# For each entry, the number of times this word occurs is counted and the count value is entered into the respective column.
# These "count" columns can then be used to train machine learning models.


# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Instantiate CountVectorizer
cv = CountVectorizer()

# Fit the vectorizer
cv.fit(speech_df['text_clean'])

# Print feature names
print(cv.get_feature_names())


