# 5/12/2020
# Compute ECDF: x, y
x, y = ecdf(n_defaults)

# Plot the ECDF with labeled axes
_ = plt.plot(x, y, marker ='.', linestyle = 'none')
_ = plt.xlabel('x')
_ = plt.ylabel('y')

# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))

# <script.py> output:
#     Probability of losing money = 0.022

# <script.py> output:
#     Probability of losing money = 0.022