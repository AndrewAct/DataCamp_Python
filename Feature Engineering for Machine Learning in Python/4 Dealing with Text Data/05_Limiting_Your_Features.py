# # 7/11/2020
# As you have seen, using the CountVectorizer with its default settings creates a feature for every single word in your corpus. This can create far too many features, often including ones that will provide very little analytical value.

# For this purpose CountVectorizer has parameters that you can set to reduce the number of features:

# min_df : Use only words that occur in more than this percentage of documents. This can be used to remove outlier words that will not generalize across texts.
# max_df : Use only words that occur in less than this percentage of documents. This is useful to eliminate very common words that occur in every corpus without adding value such as "and" or "the".

# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Specify arguements to limit the number of features generated
cv = CountVectorizer(min_df = 0.2, max_df = 0.8)

# Fit, transform, and convert into array
cv_transformed = cv.fit_transform(speech_df['text_clean'])
cv_array = cv_transformed.toarray()

# Print the array shape
print(cv_array.shape)

# <script.py> output:
#     (58, 818)