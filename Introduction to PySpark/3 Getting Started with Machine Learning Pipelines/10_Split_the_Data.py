# # 8/18/2020
# Now that you've done all your manipulations, the last step before modeling is to split the data!

# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])