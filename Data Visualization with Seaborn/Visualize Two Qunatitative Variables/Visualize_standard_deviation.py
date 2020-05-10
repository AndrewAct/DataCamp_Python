# 5/1/2020
In# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, 
            ci = "sd",
            kind="line")

# Show plot
plt.show()