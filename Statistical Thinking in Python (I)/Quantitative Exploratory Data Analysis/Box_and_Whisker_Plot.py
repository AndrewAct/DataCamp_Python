# 5/12/2020
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x = 'species', y = 'petal length (cm)', data = df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')


# Show the plot
plt.show()
