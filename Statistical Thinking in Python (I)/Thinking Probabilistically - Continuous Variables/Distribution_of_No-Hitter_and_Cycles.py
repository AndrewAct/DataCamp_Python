# 5/14/2020
# Draw samples of waiting times: waiting_times
waiting_times = np.array(successive_poisson(764, 715, 100000))

# Make the histogram
_ = plt.hist(waiting_times, bins = 100, normed = True, histtype= 'step')


# Label axes
_ = plt.xlabel('x');
_ = plt.ylabel('Waiting Time');


# Show the plot
plt.show()
