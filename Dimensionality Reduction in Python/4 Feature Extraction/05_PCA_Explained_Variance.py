# # 6/17/2020
# You'll be inspecting the variance explained by the different principal components of the pca instance you created in the previous exercise.

# Inspect the explained variance ratio per component
print(pca.explained_variance_ratio_)

# <script.py> output:
#     [0.61449404 0.19893965 0.06803095 0.03770499 0.03031502 0.0171759
#      0.01072762 0.00656681 0.00634743 0.00436015 0.0026586  0.00202617
#      0.00065268]

# Print the cumulative sum of the explained variance ratio
print(pca.explained_variance_ratio_.cumsum())

# <script.py> output:
#     [0.61449404 0.81343368 0.88146463 0.91916962 0.94948464 0.96666054
#      0.97738816 0.98395496 0.99030239 0.99466254 0.99732115 0.99934732
#      1.        ]