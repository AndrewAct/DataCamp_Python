# # 7/26/2020
# In this exercise, you have been given an excerpt from a blog post. Your task is to clean this text into a more machine friendly format. This will involve converting to lowercase, lemmatization and removing stopwords, punctuations and non-alphabetic characters.

# The excerpt is available as a string blog and has been printed to the console. The list of stopwords are available as stopwords.

# Load model and create Doc object
nlp = spacy.load('en_core_web_sm')
doc = nlp(blog)

# Generate lemmatized tokens
lemmas = [token.lemma_ for token in doc]

# Remove stopwords and non-alphabetic tokens
a_lemmas = [lemma for lemma in lemmas 
            if lemma.isalpha() and lemma not in stopwords]

# Print string after text cleaning
print(' '.join(a_lemmas))

# <script.py> output:
#     century politic witness alarming rise populism europe warning sign come uk brexit referendum vote swinging way leave follow stupendous victory billionaire donald trump president united states november europe steady rise populist far right party capitalize europe immigration crisis raise nationalist anti europe sentiment instance include alternative germany afd win seat enter bundestag upset germany political order time second world war success star movement italy surge popularity neo nazism neo fascism country hungary czech republic poland austria