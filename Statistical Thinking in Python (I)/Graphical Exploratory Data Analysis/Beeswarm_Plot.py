# 5/11/2020
# Create bee swarm plot with Seaborn's default settings
print(df.head())
sns.swarmplot(x = 'species', y = 'petal length (cm)', data = df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()

# sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
# 0                5.1               3.5                1.4               0.2  setosa
# 1                4.9               3.0                1.4               0.2  setosa
# 2                4.7               3.2                1.3               0.2  setosa
# 3                4.6               3.1                1.5               0.2  setosa
# 4                5.0               3.6                1.4               0.2  setosa

# <script.py> output:
#        sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
#     0                5.1               3.5                1.4               0.2  setosa
#     1                4.9               3.0                1.4               0.2  setosa
#     2                4.7               3.2                1.3               0.2  setosa
#     3                4.6               3.1                1.5               0.2  setosa
#     4                5.0               3.6                1.4               0.2  setosa