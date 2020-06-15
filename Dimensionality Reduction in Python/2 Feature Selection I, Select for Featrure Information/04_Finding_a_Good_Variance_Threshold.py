# # 6/14/2020
# You'll be working on a slightly modified subsample of the ANSUR dataset with just head measurements pre-loaded as head_df.

# Create the boxplot
head_df.boxplot()

plt.show()

# Normalize the data
normalized_df = head_df / head_df.mean()

# Print the variances of the normalized data
print(normalized_df.var())

# script.py> output:
#     headbreadth          1.678952e-03
#     headcircumference    1.029623e-03
#     headlength           1.867872e-03
#     tragiontopofhead     2.639840e-03
#     n_hairs              1.002552e-08
#     measurement_error    3.231707e-27