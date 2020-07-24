# # 7/23/2020
# In this exercise, you'll practice advanced tokenization by tokenizing some non-ascii based text. You'll be using German with emoji!

# Here, you have access to a string called german_text, which has been printed for you in the Shell. Notice the emoji and the German characters!

# The following modules have been pre-imported from nltk.tokenize: regexp_tokenize and word_tokenize.

# Unicode ranges for emoji are:

# ('\U0001F300'-'\U0001F5FF'), ('\U0001F600-\U0001F64F'), ('\U0001F680-\U0001F6FF'), and ('\u2600'-\u26FF-\u2700-\u27BF').

# Tokenize and print all words in german_text
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words
# Ü means check the German Ü
capital_words = r"[A-ZÜ]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))

# Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕

# <script.py> output:
#     ['Wann', 'gehen', 'wir', 'Pizza', 'essen', '?', '🍕', 'Und', 'fährst', 'du', 'mit', 'Über', '?', '🚕']
#     ['Wann', 'Pizza', 'Und', 'Über']
#     ['🍕', '🚕']