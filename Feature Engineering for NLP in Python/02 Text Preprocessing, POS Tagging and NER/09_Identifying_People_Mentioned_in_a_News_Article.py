# # 7/26/2020
# In this exercise, you have been given an excerpt from a news article published in TechCrunch. Your task is to write a function find_people that identifies the names of people that have been mentioned in a particular piece of text. You will then use find_people to identify the people of interest in the article.

# The article is available as the string tc and has been printed to the console. The required spacy model has also been already loaded as nlp.

def find_persons(text):
      # Create Doc object
  doc = nlp(text)
  
  # Identify the persons
  persons = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
  
  # Return persons
  return persons

print(find_persons(tc))

# <script.py> output:
#     ['Sheryl Sandberg', 'Mark Zuckerberg']