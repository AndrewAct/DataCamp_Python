# # 5/28/2020
# FIFA 18 is a football video game that was released in 2017 for PC and consoles. The dataset that you are about to work on contains data on the 1000 top individual players in the game. You will explore various features of the data as we move ahead in the course. In this exercise, you will work with two columns, eur_wage, the wage of a player in Euros and eur_value, their current transfer market value.

# The data for this exercise is stored in a Pandas dataframe, fifa. whiten from scipy.cluster.vq and matplotlib.pyplot as plt have been pre-loaded.

# Scale wage and value
fifa['scaled_wage'] = whiten(fifa['eur_wage'])
fifa['scaled_value'] = whiten(fifa['eur_value'])


# Plot the two columns in a scatter plot
# Hope you have a better understanding of dataframe now
# do not make dumb mistakes 
fifa.plot(x='scaled_wage', y='scaled_value', kind = 'scatter')
plt.show()

# Check mean and standard deviation of scaled values
print(fifa[['scaled_wage', 'scaled_value']].describe())

# <script.py> output:
#            scaled_wage  scaled_value
#     count      1000.00       1000.00
#     mean          1.12          1.31
#     std           1.00          1.00
#     min           0.00          0.00
#     25%           0.47          0.73
#     50%           0.85          1.02
#     75%           1.41          1.54
#     max           9.11          8.98
