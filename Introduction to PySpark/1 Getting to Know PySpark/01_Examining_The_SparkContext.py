# # 8/18/2020
# In this exercise you'll get familiar with the SparkContext.

# You'll probably notice that code takes longer to run than you might expect. This is because Spark is some serious software. It takes more time to start up than you might be used to. You may also find that running simpler computations might take longer than expected. That's because all the optimizations that Spark has under its hood are designed for complicated operations with big data sets. That means that for simple or small problems Spark may actually perform worse than some other solutions!

# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)

# <script.py> output:
#     <SparkContext master=local[*] appName=pyspark-shell>
#     2.3.1