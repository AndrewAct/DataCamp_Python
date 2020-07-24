# # 7/24/2020
# You're now going to have some fun with named-entity recognition! A scraped news article has been pre-loaded into your workspace. Your task is to use nltk to find the named entities in this article.

# What might the article be about, given the names you found?

# Along with nltk, sent_tokenize and word_tokenize from nltk.tokenize have been pre-imported.

# Tokenize the article into sentences: sentences
sentences = nltk.sent_tokenize(article)

# Tokenize each sentence into words: token_sentences
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences] 

# Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences,binary =True)

# Test for stems of the tree with 'NE' tags
# hasattr would evaluate if an object has an given attribute
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)


# <script.py> output:
#     (NE Uber/NNP)
#     (NE Beyond/NN)
#     (NE Apple/NNP)
#     (NE Uber/NNP)
#     (NE Uber/NNP)
#     (NE Travis/NNP Kalanick/NNP)
#     (NE Tim/NNP Cook/NNP)
#     (NE Apple/NNP)
#     (NE Silicon/NNP Valley/NNP)
#     (NE CEO/NNP)
#     (NE Yahoo/NNP)
#     (NE Marissa/NNP Mayer/NNP)