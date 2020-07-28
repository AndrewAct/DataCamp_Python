# # 7/27/2020
# In this exercise, you have been given tfidf_matrix which contains the tf-idf vectors of a thousand documents. Your task is to generate the cosine similarity matrix for these vectors first using cosine_similarity and then, using linear_kernel.

# We will then compare the computation times for both functions.

# Record start time
start = time.time()

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Print cosine similarity matrix
print(cosine_sim)

# Print time taken
print("Time taken: %s seconds" %(time.time() - start))

# <script.py> output:
#     [[1.         0.         0.         ... 0.         0.         0.        ]
#      [0.         1.         0.         ... 0.         0.         0.        ]
#      [0.         0.         1.         ... 0.         0.01418221 0.        ]
#      ...
#      [0.         0.         0.         ... 1.         0.01589009 0.        ]
#      [0.         0.         0.01418221 ... 0.01589009 1.         0.        ]
#      [0.         0.         0.         ... 0.         0.         1.        ]]
#     Time taken: 0.4587216377258301 seconds

# Record start time
start = time.time()

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Print cosine similarity matrix
print(cosine_sim)

# Print time taken
print("Time taken: %s seconds" %(time.time() - start))

# <script.py> output:
#     [[1.         0.         0.         ... 0.         0.         0.        ]
#      [0.         1.         0.         ... 0.         0.         0.        ]
#      [0.         0.         1.         ... 0.         0.01418221 0.        ]
#      ...
#      [0.         0.         0.         ... 1.         0.01589009 0.        ]
#      [0.         0.         0.01418221 ... 0.01589009 1.         0.        ]
#      [0.         0.         0.         ... 0.         0.         1.        ]]
#     Time taken: 0.3770928382873535 seconds
