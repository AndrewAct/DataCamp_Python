# # 6/26/2020
# In this section, you'll investigate the variance of columns in the UFO dataset to determine which features should be standardized. After taking a look at the variances of the seconds and minutes column, you'll see that the variance of the seconds column is extremely high. Because seconds and minutes are related to each other (an issue we'll deal with when we select features for modeling), let's log normlize the seconds column.

# Check the variance of the seconds and minutes columns
print(ufo[["seconds","minutes"]].var())

# Log normalize the seconds column
ufo["seconds_log"] = np.log(ufo["seconds"])

# Print out the variance of just the seconds_log column
print(ufo["seconds_log"].var())

# <script.py> output:
#     seconds    424087.417474
#     minutes       117.546372
#     dtype: float64
#     1.1223923881183004
