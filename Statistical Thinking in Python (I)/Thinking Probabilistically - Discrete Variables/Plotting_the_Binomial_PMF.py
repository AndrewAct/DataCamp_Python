# 5/12/2020
# Compute bin edges: bins
bins = np.arange(min(n_defaults), max(n_defaults) + 1.5) - 0.5

# Generate histogram
_ = plt.hist(n_defaults, normed = True, bins = bins)

# Label axes
_ = plt.xlabel('x')
_ = plt.ylabel('y')

# Show the plot
plt.show()