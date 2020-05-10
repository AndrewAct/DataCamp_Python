# 5/6/2020
# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)

## Q: Now that you've generated your pairs, you've achieved the first step of record linkage. 
# What are the steps remaining to link both restaurants DataFrames, and in what order?
# A; Compare between columns, score the comparison, then link the DataFrames.
