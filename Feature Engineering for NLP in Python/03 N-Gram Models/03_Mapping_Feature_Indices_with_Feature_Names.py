# # 7/26/2020
# In the lesson video, we had seen that CountVectorizer doesn't necessarily index the vocabulary in alphabetical order. In this exercise, we will learn to map each feature index to its corresponding feature name from the vocabulary.

# We will use the same three sentences on lions from the video. The sentences are available in a list named corpus and has already been printed to the console.

# Create CountVectorizer object
vectorizer = CountVectorizer()

# Generate matrix of word vectors
bow_matrix = vectorizer.fit_transform(corpus)

# Convert bow_matrix into a DataFrame
bow_df = pd.DataFrame(bow_matrix.toarray())

# Map the column names to vocabulary 
bow_df.columns = vectorizer.get_feature_names()

# Print bow_df
print(bow_df)

# <script.py> output:
#        an  decade  endangered  have  is  ...  lion  lions  of  species  the
#     0   0       0           0     0   1  ...     1      0   1        0    3
#     1   0       1           0     1   0  ...     0      1   1        0    0
#     2   1       0           1     0   1  ...     1      0   0        1    1
    
#     [3 rows x 13 columns]