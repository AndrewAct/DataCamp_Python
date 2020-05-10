# Scatter plot of nb_sold vs avg_price with titlr
avocados.plot(x = "nb_sold", y = "avg_price", kind = "scatter", title = "Number of avocados sold vs. average price")

# Show the plot
plt.show()

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins = 20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins = 20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()