# 5/12/2020
# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson = np.random.poisson(10, size = 10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
                       np.std(samples_poisson))

# Specify values of n and p to consider for Binomial: n, p
n = [20, 100, 1000];
p = [0.5, 0.1, 0.01];


# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i], p[i], 10000)

    # Print results
    print('n =', n[i], 'Binom:', np.mean(samples_binomial),
                                 np.std(samples_binomial))

# <script.py> output:
#     Poisson:      10.0186 3.144813832327758
#     n = 20 Binom: 9.9637 2.2163443572694206
#     n = 100 Binom: 9.9947 3.0135812433050484
#     n = 1000 Binom: 9.9985 3.139378561116833