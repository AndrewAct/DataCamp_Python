# # 6/24/2020
# Now that we know that the Proline column in our wine dataset has a large amount of variance, let's log normalize it.

# Numpy has been imported as np in your workspace.
# Log normalization will rescale the data so it will match its neighbors according to some logical relationship 

# Print out the variance of the Proline column
# print(wine.head)
print(wine["Proline"].var())

# Apply the log normalization function to the Proline column
wine['Proline_log'] = np.log(wine["Proline"])

# Check the variance of the normalized Proline column
print(wine['Proline_log'].var)

# <script.py> output:
#     99166.71735542436
#     <bound method Series.var of 0      6.970730
#     1      6.956545
#     2      7.077498
#     3      7.299797
#     4      6.599870
#     5      7.279319
#     6      7.162397
#     7      7.166266
#     8      6.951772
#     9      6.951772
#     10     7.319865
#     11     7.154615
#     12     7.185387
#     13     7.047517
#     14     7.344073
#     15     7.177782
#     16     7.154615
#     17     7.029973
#     18     7.426549
#     19     6.739337
#     20     6.659294
#     21     6.646391
#     22     6.942157
#     23     6.922644
#     24     6.739337
#     25     6.721426
#     26     7.085901
#     27     7.158514
#     28     6.818924
#     29     6.942157
#              ...   
#     148    6.476972
#     149    6.309918
#     150    6.214608
#     151    6.173786
#     152    6.052089
#     153    6.514713
#     154    6.461468
#     155    6.586172
#     156    6.173786
#     157    6.779922
#     158    6.492240
#     159    6.429719
#     160    6.253829
#     161    6.522093
#     162    6.345636
#     163    6.514713
#     164    6.421622
#     165    6.253829
#     166    6.543912
#     167    6.529419
#     168    6.620073
#     169    6.445720
#     170    6.234411
#     171    6.152733
#     172    6.492240
#     173    6.606650
#     174    6.620073
#     175    6.727432
#     176    6.733402
#     177    6.327937
#     Name: Proline_log, Length: 178, dtype: float64>
