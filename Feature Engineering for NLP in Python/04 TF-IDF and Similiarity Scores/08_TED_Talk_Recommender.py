# # 7/27/2020
# In this exercise, we will build a recommendation system that suggests TED Talks based on their transcripts. You have been given a get_recommendations() function that takes in the title of a talk, a similarity matrix and an indices series as its arguments, and outputs a list of most similar talks. indices has already been provided to you.

# You have also been given a transcripts series that contains the transcripts of around 500 TED talks. Your task is to generate a cosine similarity matrix for the tf-idf vectors of the talk transcripts.

# Consequently, we will generate recommendations for a talk titled '5 ways to kill your dreams' by Brazilian entrepreneur Bel Pesce.

# Initialize the TfidfVectorizer 
tfidf = TfidfVectorizer(stop_words= "english")

# Construct the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(transcripts)

# Generate the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
 
# Generate recommendations 
print(get_recommendations("5 ways to kill your dreams", cosine_sim, indices))

# <script.py> output:
#     453             Success is a continuous journey
#     157                        Why we do what we do
#     494                   How to find work you love
#     149          My journey into movies that matter
#     447                        One Laptop per Child
#     230             How to get your ideas to spread
#     497         Plug into your hard-wired happiness
#     495    Why you will fail to have a great career
#     179             Be suspicious of simple stories
#     53                          To upgrade is human
#     Name: title, dtype: object