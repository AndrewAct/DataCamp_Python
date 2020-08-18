# # 8/17/2020
# To solidify your knowledge of random sampling, let's try a similar exercise but using different hyperparameters and a different algorithm.

# As before, create some lists of hyperparameters that can be zipped up to a list of lists. You will use the hyperparameters criterion, max_depth and max_features of the random forest algorithm. Then you will randomly sample hyperparameter combinations in preparation for running a random search.

# You will use a slightly different package for sampling in this task, random.sample().

# Create lists for criterion and max_features
criterion_list = ['gini', 'entropy']
max_feature_list = ['auto', 'sqrt', 'log2', None]

# Create a list of values for the max_depth hyperparameter
max_depth_list = list(range(3,56))

# Combination list
combinations_list = [list(x) for x in product(criterion_list, max_feature_list, max_depth_list)]

# Sample hyperparameter combinations for a random search
combinations_random_chosen = random.sample(combinations_list, 150)

# Print the result
print(combinations_random_chosen)

# <script.py> output:
#     [['gini', 'auto', 18], ['entropy', 'log2', 23], ['entropy', 'auto', 38], ['entropy', 'log2', 14], ['gini', 'sqrt', 28], ['entropy', 'log2', 13], ['entropy', 'log2', 32], ['entropy', 'log2', 18], ['gini', 'log2', 20], ['gini', 'auto', 42], ['entropy', 'auto', 12], ['gini', None, 8], ['gini', None, 41], ['gini', 'auto', 3], ['gini', 'log2', 5], ['gini', 'sqrt', 52], ['gini', 'log2', 7], ['entropy', 'auto', 43], ['entropy', 'log2', 17], ['gini', 'log2', 55], ['entropy', 'log2', 5], ['entropy', 'log2', 19], ['gini', None, 40], ['gini', None, 35], ['gini', 'auto', 22], ['gini', None, 10], ['entropy', 'auto', 35], ['entropy', None, 27], ['gini', 'sqrt', 12], ['gini', 'auto', 43], ['gini', 'auto', 25], ['gini', None, 39], ['gini', 'log2', 26], ['gini', 'auto', 27], ['gini', 'log2', 8], ['gini', 'sqrt', 10], ['entropy', 'auto', 15], ['gini', 'log2', 41], ['gini', None, 44], ['entropy', 'sqrt', 4], ['entropy', 'auto', 20], ['entropy', 'auto', 5], ['entropy', 'log2', 27], ['gini', 'log2', 32], ['gini', None, 13], ['gini', 'log2', 44], ['gini', 'log2', 36], ['entropy', 'auto', 13], ['gini', 'auto', 24], ['entropy', 'sqrt', 54], ['entropy', 'log2', 29], ['gini', 'log2', 40], ['entropy', 'sqrt', 51], ['entropy', 'auto', 27], ['gini', 'auto', 8], ['entropy', 'sqrt', 33], ['gini', 'sqrt', 39], ['gini', 'log2', 6], ['gini', 'auto', 31], ['gini', 'auto', 12], ['entropy', 'auto', 16], ['entropy', 'sqrt', 35], ['gini', 'sqrt', 53], ['gini', 'auto', 30], ['entropy', None, 29], ['gini', 'auto', 33], ['entropy', 'sqrt', 43], ['entropy', None, 48], ['gini', None, 18], ['gini', None, 48], ['gini', 'auto', 23], ['gini', 'auto', 48], ['gini', 'sqrt', 4], ['gini', 'sqrt', 48], ['gini', 'sqrt', 15], ['entropy', 'auto', 46], ['entropy', 'log2', 53], ['gini', 'sqrt', 45], ['gini', 'auto', 47], ['entropy', 'log2', 39], ['entropy', 'log2', 15], ['entropy', None, 32], ['gini', None, 31], ['gini', 'auto', 10], ['gini', 'log2', 11], ['gini', 'log2', 33], ['gini', 'log2', 21], ['entropy', 'sqrt', 11], ['entropy', None, 10], ['gini', 'log2', 13], ['gini', None, 29], ['entropy', 'auto', 36], ['entropy', 'sqrt', 37], ['gini', 'log2', 30], ['entropy', 'auto', 8], ['entropy', 'log2', 54], ['gini', None, 17], ['entropy', 'log2', 16], ['gini', 'sqrt', 23], ['entropy', 'sqrt', 48], ['gini', 'sqrt', 40], ['entropy', 'sqrt', 18], ['gini', None, 4], ['entropy', None, 16], ['entropy', 'auto', 26], ['gini', 'auto', 55], ['gini', 'log2', 52], ['gini', 'sqrt', 6], ['gini', 'sqrt', 11], ['gini', None, 20], ['entropy', 'log2', 51], ['gini', 'sqrt', 55], ['entropy', 'sqrt', 19], ['entropy', None, 40], ['entropy', 'auto', 29], ['gini', None, 28], ['gini', 'auto', 40], ['entropy', 'log2', 25], ['entropy', 'sqrt', 14], ['entropy', 'sqrt', 20], ['gini', 'log2', 4], ['gini', None, 16], ['gini', 'auto', 35], ['entropy', 'auto', 47], ['entropy', 'sqrt', 3], ['entropy', 'log2', 31], ['entropy', None, 37], ['entropy', 'sqrt', 34], ['entropy', None, 11], ['gini', 'sqrt', 49], ['gini', 'sqrt', 42], ['entropy', None, 19], ['entropy', 'sqrt', 16], ['entropy', 'auto', 7], ['entropy', 'auto', 44], ['entropy', 'sqrt', 9], ['gini', None, 55], ['entropy', 'auto', 30], ['gini', None, 6], ['gini', 'sqrt', 54], ['gini', 'auto', 9], ['gini', 'auto', 19], ['entropy', 'sqrt', 46], ['gini', 'log2', 43], ['entropy', 'log2', 42], ['entropy', 'auto', 22], ['entropy', 'log2', 35], ['gini', None, 14], ['entropy', 'auto', 11], ['gini', None, 15]]
