# 5/22/2020
# Suppose you were a big fan of Bruce Springsteen - which other musicial artists might you like? 
# Use your NMF features from the previous exercise and the cosine similarity to find similar musical artists. 
# A solution to the previous exercise has been run, so norm_features is an array containing the normalized NMF features as rows. 
# The names of the musical artists are available as the list artist_names.

# Import pandas
import pandas as pd

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index = artist_names)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
# nlargest will return the n rows of largest 
# Ordered by columns, descening order
print(similarities.nlargest())

# <script.py> output:
#     Bruce Springsteen    1.000000
#     Neil Young           0.955896
#     Van Morrison         0.872452
#     Leonard Cohen        0.864763
#     Bob Dylan            0.859047
#     dtype: float64