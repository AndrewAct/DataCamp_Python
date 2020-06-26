# # 6/25/2020
# Let's take a look at the wine dataset again, which is made up of continuous, numerical features. Run Pearson's correlation coefficient on the dataset to determine which columns are good candidates for eliminating. Then, remove those columns from the DataFrame.

# Print out the column correlations of the wine dataset
print(wine.corr())

# Take a minute to find the column where the correlation value is greater than 0.75 at least twice
to_drop = "Flavanoids"

# Drop that column from the DataFrame
wine = wine.drop(to_drop, axis = 1)

# <script.py> output:
#                                   Flavanoids  Total phenols    ...     OD280/OD315 of diluted wines       Hue
#     Flavanoids                      1.000000       0.864564    ...                         0.787194  0.543479
#     Total phenols                   0.864564       1.000000    ...                         0.699949  0.433681
#     Malic acid                     -0.411007      -0.335167    ...                        -0.368710 -0.561296
#     OD280/OD315 of diluted wines    0.787194       0.699949    ...                         1.000000  0.565468
#     Hue                             0.543479       0.433681    ...                         0.565468  1.000000
    
#     [5 rows x 5 columns]
