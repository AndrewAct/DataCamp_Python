# # 6/24/2020
# Let's transform the volunteer dataset's title column into a text vector, to use in a prediction task in the next exercise.
# Take the title text
title_text = volunteer["title"]

# Create the vectorizer method
tfidf_vec = TfidfVectorizer()

# Transform the text into tf-idf vectors
text_tfidf = tfidf_vec.fit_transform(title_text)
