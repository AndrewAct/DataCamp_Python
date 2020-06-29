# # 6/27/2020
# The next dataset contains information about company market value over several years of time. This is one of the most popular kind of time series data used for regression. If you can model the value of a company as it changes over time, you can make predictions about where that company will be in the future. This dataset was also originally provided as part of a public Kaggle competition.

# In this exercise, you'll plot the time series for a number of companies to get an understanding of how they are (or aren't) related to one another.
# Read in the data
data = pd.read_csv('prices.csv', index_col=0)

# Convert the index of the DataFrame to datetime
data.index = pd.to_datetime(data.index)
print(data.head())

# Loop through each column, plot its values over time
fig, ax = plt.subplots()
for column in data:
    data[column].plot(ax=ax, label=column)
ax.legend()
plt.show()

# <script.py> output:
#                       AAPL  FB       NFLX          V        XOM
#     time                                                       
#     2010-01-04  214.009998 NaN  53.479999  88.139999  69.150002
#     2010-01-05  214.379993 NaN  51.510001  87.129997  69.419998
#     2010-01-06  210.969995 NaN  53.319999  85.959999  70.019997
#     2010-01-07  210.580000 NaN  52.400001  86.760002  69.800003
#     2010-01-08  211.980005 NaN  53.300002  87.000000  69.519997