# # 7/26/2020
# In this exercise, you will be tokenizing one of the most famous speeches of all time: the Gettysburg Address delivered by American President Abraham Lincoln during the American Civil War.

# The entire speech is available as a string named gettysburg.\

import spacy

#'en'Glish, 'core'Vocabulary, 'web'Written text, Size
# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(gettysburg)

# Generate the tokens
tokens = [token.text for token in doc]
print(tokens)

# <script.py> output:
#     ['Four', 'score', 'and', 'seven', 'years', 'ago', 'our', 'fathers', 'brought', 'forth', 'on', 'this', 'continent', ',', 'a', 'new', 'nation', ',', 'conceived', 'in', 'Liberty', ',', 'and', 'dedicated', 'to', 'the', 'proposition', 'that', 'all', 'men', 'are', 'created', 'equal', '.', 'Now', 'we', "'re", 'engaged', 'in', 'a', 'great', 'civil', 'war', ',', 'testing', 'whether', 'that', 'nation', ',', 'or', 'any', 'nation', 'so', 'conceived', 'and', 'so', 'dedicated', ',', 'can', 'long', 'endure', '.', 'We', "'re", 'met', 'on', 'a', 'great', 'battlefield', 'of', 'that', 'war', '.', 'We', "'ve", 'come', 'to', 'dedicate', 'a', 'portion', 'of', 'that', 'field', ',', 'as', 'a', 'final', 'resting', 'place', 'for', 'those', 'who', 'here', 'gave', 'their', 'lives', 'that', 'that', 'nation', 'might', 'live', '.', 'It', "'s", 'altogether', 'fitting', 'and', 'proper', 'that', 'we', 'should', 'do', 'this', '.', 'But', ',', 'in', 'a', 'larger', 'sense', ',', 'we', 'ca', "n't", 'dedicate', '-', 'we', 'can', 'not', 'consecrate', '-', 'we', 'can', 'not', 'hallow', '-', 'this', 'ground', '.', 'The', 'brave', 'men', ',', 'living', 'and', 'dead', ',', 'who', 'struggled', 'here', ',', 'have', 'consecrated', 'it', ',', 'far', 'above', 'our', 'poor', 'power', 'to', 'add', 'or', 'detract', '.', 'The', 'world', 'will', 'little', 'note', ',', 'nor', 'long', 'remember', 'what', 'we', 'say', 'here', ',', 'but', 'it', 'can', 'never', 'forget', 'what', 'they', 'did', 'here', '.', 'It', 'is', 'for', 'us', 'the', 'living', ',', 'rather', ',', 'to', 'be', 'dedicated', 'here', 'to', 'the', 'unfinished', 'work', 'which', 'they', 'who', 'fought', 'here', 'have', 'thus', 'far', 'so', 'nobly', 'advanced', '.', 'It', "'s", 'rather', 'for', 'us', 'to', 'be', 'here', 'dedicated', 'to', 'the', 'great', 'task', 'remaining', 'before', 'us', '-', 'that', 'from', 'these', 'honored', 'dead', 'we', 'take', 'increased', 'devotion', 'to', 'that', 'cause', 'for', 'which', 'they', 'gave', 'the', 'last', 'full', 'measure', 'of', 'devotion', '-', 'that', 'we', 'here', 'highly', 'resolve', 'that', 'these', 'dead', 'shall', 'not', 'have', 'died', 'in', 'vain', '-', 'that', 'this', 'nation', ',', 'under', 'God', ',', 'shall', 'have', 'a', 'new', 'birth', 'of', 'freedom', '-', 'and', 'that', 'government', 'of', 'the', 'people', ',', 'by', 'the', 'people', ',', 'for', 'the', 'people', ',', 'shall', 'not', 'perish', 'from', 'the', 'earth', '.']

