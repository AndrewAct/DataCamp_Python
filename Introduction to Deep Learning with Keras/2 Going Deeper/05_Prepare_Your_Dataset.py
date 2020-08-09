# # 8/9/2020
# In the console you can check that your labels, darts.competitor are not yet in a format to be understood by your network. They contain the names of the competitors as strings. You will first turn these competitors into unique numbers,then use the to_categorical() function from keras.utils to turn these numbers into their one-hot encoded representation.

# This is useful for multi-class classification problems, since there are as many output neurons as classes and for every observation in our dataset we just want one of the neurons to be activated.

# The dart's dataset is loaded as darts. Pandas is imported as pd. Let's prepare this dataset!

# Transform into a categorical variable
darts.competitor = pd.Categorical(darts.competitor)

# Assign a number to each category (label encoding)
darts.competitor = darts.competitor.cat.codes 

# Print the label encoded competitors
print('Label encoded competitors: \n',darts.competitor.head())

# <script.py> output:
#     Label encoded competitors: 
#      0    2
#     1    3
#     2    1
#     3    0
#     4    2
#     Name: competitor, dtype: int8

# Transform into a categorical variable
darts.competitor = pd.Categorical(darts.competitor)

# Assign a number to each category (label encoding)
darts.competitor = darts.competitor.cat.codes 

# Import to_categorical from keras utils module
from keras.utils import to_categorical

coordinates = darts.drop(['competitor'], axis=1)
# Use to_categorical on your labels
competitors = to_categorical(darts.competitor)

# Now print the one-hot encoded labels
print('One-hot encoded competitors: \n',competitors)

# <script.py> output:
#     One-hot encoded competitors: 
#      [[0. 0. 1. 0.]
#      [0. 0. 0. 1.]
#      [0. 1. 0. 0.]
#      ...
#      [0. 1. 0. 0.]
#      [0. 1. 0. 0.]
#      [0. 0. 0. 1.]]