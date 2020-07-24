# # 7/23/2020
# It's time to apply the methods you learned in the previous video to create your first gensim dictionary and corpus!

# You'll use these data structures to investigate word trends and potential interesting topics in your document set. To get started, we have imported a few additional messy articles from Wikipedia, which were preprocessed by lowercasing all words, tokenizing them, and removing stop words and punctuation. These were then stored in a list of document tokens called articles. You'll need to do some light preprocessing and then generate the gensim dictionary and corpus.

# Corpora will encapusulate the mapping between normalized words and integer ids

# Import Dictionary
from gensim.corpora.dictionary import Dictionary

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])

# <script.py> output:
#     computer
#     [(0, 88), (23, 11), (24, 2), (39, 1), (41, 2), (55, 22), (56, 1), (57, 1), (58, 1), (59, 3)]
