# 5/4/2020
# Import pickle package
import pickle

# Open pickle file and load data: d
# Maybe rb means Read Binary
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))