# # 7/26/2020
# In this exercise, we will perform lemmatization on the same gettysburg address from before.

# However, this time, we will also take a look at the speech, before and after lemmatization, and try to adjudge the kind of changes that take place to make the piece more machine friendly.

import spacy

# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(gettysburg)

# Generate lemmas
lemmas = [token.lemma_ for token in doc]

# Convert lemmas into a string
print(' '.join(lemmas))

# <script.py> output:
#     four score and seven year ago -PRON- father bring forth on this continent , a new nation , conceive in liberty , and dedicate to the proposition that all man be create equal . now -PRON- be engage in a great civil war , test whether that nation , or any nation so conceive and so dedicated , can long endure . -PRON- be meet on a great battlefield of that war . -PRON- have come to dedicate a portion of that field , as a final resting place for those who here give -PRON- life that that nation may live . -PRON- be altogether fitting and proper that -PRON- should do this . but , in a large sense , -PRON- can not dedicate - -PRON- can not consecrate - -PRON- can not hallow - this ground . the brave man , living and dead , who struggle here , have consecrate -PRON- , far above -PRON- poor power to add or detract . the world will little note , nor long remember what -PRON- say here , but -PRON- can never forget what -PRON- do here . -PRON- be for -PRON- the living , rather , to be dedicate here to the unfinished work which -PRON- who fight here have thus far so nobly advanced . -PRON- be rather for -PRON- to be here dedicate to the great task remain before -PRON- - that from these honor dead -PRON- take increase devotion to that because for which -PRON- give the last full measure of devotion - that -PRON- here highly resolve that these dead shall not have die in vain - that this nation , under god , shall have a new birth of freedom - and that government of the people , by the people , for the people , shall not perish from the earth .

