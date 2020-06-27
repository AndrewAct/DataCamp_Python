# # 6/26/2020
# Take a look at the UFO dataset's column types using the dtypes attribute. Two columns jump out for transformation: the seconds column, which is a numeric column but is being read in as object, and the date column, which can be transformed into the datetime type. That will make our feature engineering efforts easier later on.

# Check the column types
print(ufo.dtypes)

# Change the type of seconds to float
ufo["seconds"] = ufo["seconds"].astype(float)

# Change the date column to type datetime
ufo["date"] = pd.to_datetime(ufo["date"])

# Check the column types
print(ufo[["seconds", "date"]].dtypes)

# <script.py> output:
#     date               object
#     city               object
#     state              object
#     country            object
#     type               object
#     seconds            object
#     length_of_time     object
#     desc               object
#     recorded           object
#     lat                object
#     long              float64
#     dtype: object
#     seconds           float64
#     date       datetime64[ns]
#     dtype: object
