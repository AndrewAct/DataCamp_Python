# 5/4/2020
# Create a boxplot
sns.boxplot(data=df,
         x='Award_Amount',
         y='Model Selected')

plt.show()
plt.clf()

# Create a violinplot with the husl palette
sns.violinplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette ='husl')

plt.show()
plt.clf()

# Create a lvplot with the Paired palette and the Region column as the hue
# lvplot: Letter Value Plot
sns.lvplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='Paired',
         hue ='Region')

plt.show()
plt.clf()