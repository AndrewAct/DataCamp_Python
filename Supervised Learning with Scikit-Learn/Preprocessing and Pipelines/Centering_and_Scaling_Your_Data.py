# 5/19/2020
# Import scale
from sklearn.preprocessing import scale

# Scale the features: X_scaled
X_scaled = scale(X)

# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(np.mean(X))) 
print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(np.mean(X_scaled))) 
print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))

# <script.py> output:
#     Mean of Unscaled Features: 18.432687072460002
#     Standard Deviation of Unscaled Features: 41.54494764094571
#     Mean of Scaled Features: 2.7314972981668206e-15
#     Standard Deviation of Scaled Features: 0.9999999999999999