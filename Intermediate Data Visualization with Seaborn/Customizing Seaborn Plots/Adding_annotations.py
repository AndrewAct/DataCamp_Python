# 5/3/2020
# axvline: add vertical line to x axis
# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.distplot(df['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel ="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")

# Add vertical lines for the median and mean
ax.axvline(x= df['fmr_1'].median(), color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x= df['fmr_1'].mean(), color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
ax.plot()
plt.show()