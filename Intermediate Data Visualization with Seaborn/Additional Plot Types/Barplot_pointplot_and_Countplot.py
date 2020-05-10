# 5/4/2020
# Show a countplot with the number of models used with each region a different color
sns.countplot(data=df,
         y="Model Selected",
         hue="Region")

plt.show()
plt.clf()

# Create a pointplot and include the capsize in order to show bars on the confidence interval
sns.pointplot(data= df,
         y='Award_Amount',
         x='Model Selected',
         capsize=.1)

plt.show()
plt.clf()

# Create a barplot with each Region shown as a different color
sns.barplot(data= df,
         y='Award_Amount',
         x='Model Selected',
         hue = 'Region')

plt.show()
plt.clf()