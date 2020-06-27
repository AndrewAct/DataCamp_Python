# # 6/26/2020
# Another feature engineering task to perform is month and year extraction. Perform this task on the date column of the ufo dataset.

# Look at the first 5 rows of the date column
print(ufo["date"].head())

# Extract the month from the date column
ufo["month"] = ufo["date"].apply(lambda date: date.month)

# Extract the year from the date column
ufo["year"] = ufo["date"].apply(lambda date: date.year)

# Take a look at the head of all three columns
print(ufo[["date", "month", "year"]].head())

# <script.py> output:
#     0   2002-11-21 05:45:00
#     1   2012-06-16 23:00:00
#     2   2013-06-09 00:00:00
#     3   2013-04-26 23:27:00
#     4   2013-09-13 20:30:00
#     Name: date, dtype: datetime64[ns]
#                      date  month  year
#     0 2002-11-21 05:45:00     11  2002
#     1 2012-06-16 23:00:00      6  2012
#     2 2013-06-09 00:00:00      6  2013
#     3 2013-04-26 23:27:00      4  2013
#     4 2013-09-13 20:30:00      9  2013