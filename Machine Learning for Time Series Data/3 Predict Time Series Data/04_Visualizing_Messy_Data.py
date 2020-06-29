# # 6/27/2020
# Let's take a look at a new dataset - this one is a bit less-clean than what you've seen before.

# As always, you'll first start by visualizing the raw data. Take a close look and try to find datapoints that could be problematic for fitting models.

# The data has been loaded into a DataFrame called prices.

# Visualize the dataset
prices.plot(legend=False)
plt.tight_layout()
plt.show()

# Count the missing values of each time series
missing_values = prices.isna().sum()
print(missing_values)

# <script.py> output:
#     symbol
#     EBAY    273
#     NVDA    502
#     YHOO    232
#     dtype: int64