# 5/12/2020
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

# Label the axes
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('ECDF')


# Display the plot
plt.show()
