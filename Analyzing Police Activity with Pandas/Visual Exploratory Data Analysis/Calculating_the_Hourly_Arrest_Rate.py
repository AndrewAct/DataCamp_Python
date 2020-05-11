# 5/11/2020
# Calculate the overall arrest rate
print(ri.is_arrested.mean())

# Calculate the hourly arrest rate
print(ri.groupby(ri.index.hour).is_arrested.mean())

# Save the hourly arrest rate
hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()

# <script.py> output:
#     0.0355690117407784
#     stop_datetime
#     0     0.051431
#     1     0.064932
#     2     0.060798
#     3     0.060549
#     4     0.048000
#     5     0.042781
#     6     0.013813
#     7     0.013032
#     8     0.021854
#     9     0.025206
#     10    0.028213
#     11    0.028897
#     12    0.037399
#     13    0.030776
#     14    0.030605
#     15    0.030679
#     16    0.035281
#     17    0.040619
#     18    0.038204
#     19    0.032245
#     20    0.038107
#     21    0.064541
#     22    0.048666
#     23    0.047592
#     Name: is_arrested, dtype: float64
