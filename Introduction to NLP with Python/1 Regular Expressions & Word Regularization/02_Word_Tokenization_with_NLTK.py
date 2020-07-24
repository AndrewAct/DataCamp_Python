# # 7/22/2020
# Here, you'll be using the first scene of Monty Python's Holy Grail, which has been pre-loaded as scene_one. Feel free to check it out in the IPython Shell!

# Your job in this exercise is to utilize word_tokenize and sent_tokenize from nltk.tokenize to tokenize both words and sentences from Python strings - in this case, the first scene of Monty Python's Holy Grail.

# A tokenizer would divide a string into substrings by splitting on the specified string
# sent_tokenize would return a sentence-tokenized copy of text
# word_tokenize woudld return a word-tokenized copy of text


# Import necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)


# <script.py> output:
#     {'from', 'beat', 'that', 'You', 'carry', 'Ridden', 'through', 'join', 'anyway', 'house', 'line', 'land', 'So', 'go', 'why', 'does', '#', 'yet', 'Found', 'What', 'Pendragon', 'these', 'But', 'length', 'but', '[', 'just', 'maybe', 'dorsal', 'seek', 'must', 'you', 'ounce', 'by', "'m", 'Yes', 'Will', 'Who', 'and', 'bangin', '.', 'defeator', 'a', 'order', 'I', 'Patsy', 'feathers', 'of', 'temperate', "'ve", 'pound', 'European', 'two', 'second', 'with', 'right', 'if', 'Supposing', 'We', 'under', 'speak', 'have', 'weight', 'creeper', 'Saxons', 'knights', 'Arthur', 'bird', 'my', 'husk', '2', 'where', "'", 'non-migratory', '1', 'lord', 'me', 'They', 'be', 'England', 'velocity', 'or', '!', '...', 'ask', 'this', 'five', 'together', 'castle', 'halves', 'martin', 'African', 'it', 'Uther', 'all', 'ARTHUR', 'Whoa', "n't", 'simple', 'maintain', 'using', 'wings', 'strand', 'one', 'then', 'bring', 'Oh', 'guiding', 'son', 'ridden', 'The', 'wants', 'yeah', 'there', 'tropical', 'held', 'swallow', 'SOLDIER', 'In', 'Wait', 'kingdom', 'winter', 'forty-three', 'Well', 'sun', 'trusty', 'horse', 'them', 'search', 'carried', 'every', 'minute', 'Britons', 'course', 'That', 'King', 'clop', 'tell', 'Mercea', 'get', 'times', ',', 'matter', 'Are', 'wind', 'empty', 'could', "'re", 'Am', 'Court', 'interested', 'Camelot', 'found', 'covered', 'goes', 'climes', 'Listen', "'d", 'question', 'will', 'to', 'back', 'Halt', 'breadth', 'am', 'got', 'Please', 'zone', '--', 'at', 'Not', 'use', 'in', 'on', 'No', '?', 'plover', 'agree', 'coconuts', "'em", 'not', 'air-speed', 'your', 'Where', 'migrate', 'suggesting', 'its', 'grips', 'Pull', 'do', 'south', 'KING', 'they', 'is', 'sovereign', 'snows', 'an', "'s", 'may', 'carrying', 'swallows', 'warmer', 'strangers', 'servant', 'our', 'are', 'master', 'fly', 'who', 'ratios', 'point', 'here', 'since', 'needs', 'the', 'grip', 'It', 'coconut', 'mean', ']', 'court', 'he', 'SCENE', ':', 'A', 'other'}