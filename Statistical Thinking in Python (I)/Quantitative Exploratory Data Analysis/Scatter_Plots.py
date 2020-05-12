# 5/12/2020
# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, 
             marker = '.', linestyle = 'none')


# Label the axes
_ = plt.xlabel('versicolor petal length')
_ = plt.ylabel('versicolor petal width')

# Show the result
plt.show()