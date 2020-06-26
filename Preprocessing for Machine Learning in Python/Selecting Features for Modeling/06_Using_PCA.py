# # 6/25/2020
# Let's apply PCA to the wine dataset, to see if we can get an increase in our model's accuracy

from sklearn.decomposition import PCA

# Set up PCA and the X vector for diminsionality reduction
pca = PCA()
wine_X = wine.drop("Type", axis=1)

# Apply PCA to the wine dataset X vector
transformed_X = pca.fit_transform(wine_X)

# Look at the percentage of variance explained by the different components
print(pca.explained_variance_ratio_)

# <script.py> output:
#     [9.98091230e-01 1.73591562e-03 9.49589576e-05 5.02173562e-05
#      1.23636847e-05 8.46213034e-06 2.80681456e-06 1.52308053e-06
#      1.12783044e-06 7.21415811e-07 3.78060267e-07 2.12013755e-07
#      8.25392788e-08]
