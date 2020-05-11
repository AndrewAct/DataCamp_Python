# 5/10/2020
# Select the first 1000 respondents
brfss = brfss[:1000]

# Add jittering to age
age = brfss['AGE'] + np.random.normal(0, 2.5, size = len(brfss))
# Extract weight
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', alpha = 0.2, markersize = 5)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')
plt.show()