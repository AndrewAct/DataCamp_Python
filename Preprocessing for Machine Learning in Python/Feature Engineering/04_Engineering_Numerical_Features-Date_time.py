# # 6/24/2020
# There are several columns in the volunteer dataset comprised of datetimes. Let's take a look at the start_date_date column and extract just the month to use as a feature for modeling.

# First, convert string column to date column
volunteer["start_date_converted"] = pd.to_datetime(volunteer["start_date_date"])

# Extract just the month from the converted column
volunteer["start_date_month"] = volunteer["start_date_converted"].apply(lambda row: row.month)

# Take a look at the converted and new month columns
print(volunteer[["start_date_converted", "start_date_month"]].head())

# <script.py> output:
#       start_date_converted  start_date_month
#     0           2011-07-30                 7
#     1           2011-02-01                 2
#     2           2011-01-29                 1
#     3           2011-02-14                 2
#     4           2011-02-05                 2