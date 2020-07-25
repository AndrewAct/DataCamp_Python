# # 7/24/2020
# In this exercise and the next, you'll use the polyglot library to identify French entities. The library functions slightly differently than spacy, so you'll use a few of the new things you learned in the last video to display the named entity text and category.

# You have access to the full article string in article. Additionally, the Text class of polyglot has been imported from polyglot.text.

# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
# Print the type of ent
print(type(ent))

# <script.py> output:
#     ['Charles', 'Cuvelliez']
#     ['Charles', 'Cuvelliez']
#     ['Bruxelles']
#     ['l’IA']
#     ['Julien', 'Maldonato']
#     ['Deloitte']
#     ['Ethiquement']
#     ['l’IA']
#     ['.']
#     <class 'polyglot.text.Chunk'>