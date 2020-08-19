# # 8/18/2020
# All of the common aggregation methods, like .min(), .max(), and .count() are GroupedData methods. These are created by calling the .groupBy() DataFrame method. You'll learn exactly what that means in a few exercises. For now, all you have to do to use these functions is call that method on your DataFrame. For example, to find the minimum value of a column, col, in a DataFrame, df, you could do

# df.groupBy().min("col").show()
# This creates a GroupedData object (so you can use the .min() method), then finds the minimum value in col, and returns it as a DataFrame.

# Now you're ready to do some aggregating of your own!

# A SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()

# <script.py> output:
#     +-------------+
#     |min(distance)|
#     +-------------+
#     |          106|
#     +-------------+
    
#     +-------------+
#     |max(air_time)|
#     +-------------+
#     |          409|
#     +-------------+