# 5/3/2020
# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue ="Region")

# Show the results
plt.show()