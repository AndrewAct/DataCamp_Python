# # 5/28/2020
# Now that you are aware of normalization, let us try to normalize some data. goals_for is a list of goals scored by a football team in their last ten matches. Let us standardize the data using the whiten() function.

# Import the whiten function
# whiten funciton is used for normalization 
# Generally devided by the standard deviation (?)
from scipy.cluster.vq import whiten

goals_for = [4,3,2,3,1,1,2,0,1,4]

# Use the whiten() function to standardize the data
scaled_data = whiten(goals_for)
print(scaled_data)

# <script.py> output:
#     [3.07692308 2.30769231 1.53846154 2.30769231 0.76923077 0.76923077
#      1.53846154 0.         0.76923077 3.07692308]