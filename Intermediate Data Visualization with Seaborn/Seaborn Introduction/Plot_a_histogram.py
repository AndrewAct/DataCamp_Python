# 5/3/2020
# KDE: Kernel Density Estimation
# Create a distplot
sns.distplot(df['Award_Amount'],
             kde= False,
             bins= 20)

# Display the plot
plt.show()