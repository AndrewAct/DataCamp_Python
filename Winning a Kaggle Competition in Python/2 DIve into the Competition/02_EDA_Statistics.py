# # 8/18/2020
# As mentioned in the slides, you'll work with New York City taxi fare prediction data. You'll start with finding some basic statistics about the data. Then you'll move forward to plot some dependencies and generate hypotheses on them.

# The train and test DataFrames are already available in your workspace.

# Shapes of train and test data
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Train head()
print(train.head())

# <script.py> output:
#     Train shape: (20000, 8)
#     Test shape: (9914, 7)
#        id  fare_amount          pickup_datetime  pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  passenger_count
#     0   0          4.5  2009-06-15 17:26:21 UTC        -73.844311        40.721319         -73.841610         40.712278                1
#     1   1         16.9  2010-01-05 16:52:16 UTC        -74.016048        40.711303         -73.979268         40.782004                1
#     2   2          5.7  2011-08-18 00:35:00 UTC        -73.982738        40.761270         -73.991242         40.750562                2
#     3   3          7.7  2012-04-21 04:30:42 UTC        -73.987130        40.733143         -73.991567         40.758092                1
#     4   4          5.3  2010-03-09 07:51:00 UTC        -73.968095        40.768008         -73.956655         40.783762                1

# Shapes of train and test data
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Train head()
print(train.head())

# Describe the target variable
print(train.fare_amount.describe())

# Train distribution of passengers within rides
print(train.passenger_count.value_counts())

# <script.py> output:
#     Train shape: (20000, 8)
#     Test shape: (9914, 7)
#        id  fare_amount          pickup_datetime  pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  passenger_count
#     0   0          4.5  2009-06-15 17:26:21 UTC        -73.844311        40.721319         -73.841610         40.712278                1
#     1   1         16.9  2010-01-05 16:52:16 UTC        -74.016048        40.711303         -73.979268         40.782004                1
#     2   2          5.7  2011-08-18 00:35:00 UTC        -73.982738        40.761270         -73.991242         40.750562                2
#     3   3          7.7  2012-04-21 04:30:42 UTC        -73.987130        40.733143         -73.991567         40.758092                1
#     4   4          5.3  2010-03-09 07:51:00 UTC        -73.968095        40.768008         -73.956655         40.783762                1
#     count    20000.000000
#     mean        11.303321
#     std          9.541637
#     min         -3.000000
#     25%          6.000000
#     50%          8.500000
#     75%         12.500000
#     max        180.000000
#     Name: fare_amount, dtype: float64
#     count    20000.000000
#     mean         1.658000
#     std          1.283674
#     min          0.000000
#     25%          1.000000
#     50%          1.000000
#     75%          2.000000
#     max          6.000000
#     Name: passenger_count, dtype: float64

# <script.py> output:
#     Train shape: (20000, 8)
#     Test shape: (9914, 7)
#        id  fare_amount          pickup_datetime  pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  passenger_count
#     0   0          4.5  2009-06-15 17:26:21 UTC        -73.844311        40.721319         -73.841610         40.712278                1
#     1   1         16.9  2010-01-05 16:52:16 UTC        -74.016048        40.711303         -73.979268         40.782004                1
#     2   2          5.7  2011-08-18 00:35:00 UTC        -73.982738        40.761270         -73.991242         40.750562                2
#     3   3          7.7  2012-04-21 04:30:42 UTC        -73.987130        40.733143         -73.991567         40.758092                1
#     4   4          5.3  2010-03-09 07:51:00 UTC        -73.968095        40.768008         -73.956655         40.783762                1
#     count    20000.000000
#     mean        11.303321
#     std          9.541637
#     min         -3.000000
#     25%          6.000000
#     50%          8.500000
#     75%         12.500000
#     max        180.000000
#     Name: fare_amount, dtype: float64
#     1    13999
#     2     2912
#     5     1327
#     3      860
#     4      420
#     6      407
#     0       75
#     Name: passenger_count, dtype: int64

# In [1]: 