# 5/9/2020
# Display the number of rows and columns
import pandas as pd
nsfg = pd.read_hdf('nsfg.hdf5', 'nsfg')
nsfg.shape

# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

# Print the first 5 elements of ounces
print(ounces.head())