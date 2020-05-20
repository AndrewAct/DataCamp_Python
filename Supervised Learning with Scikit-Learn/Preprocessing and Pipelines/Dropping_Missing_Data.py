# 5/19/2020
# Convert '?' to NaN
df[df == '?'] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape of new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))

# <script.py> output:
#     party                  0
#     infants               12
#     water                 48
#     budget                11
#     physician             11
#     salvador              15
#     religious             11
#     satellite             14
#     aid                   15
#     missile               22
#     immigration            7
#     synfuels              21
#     education             31
#     superfund             25
#     crime                 17
#     duty_free_exports     28
#     eaa_rsa              104
#     dtype: int64
#     Shape of Original DataFrame: (435, 17)
#     Shape of DataFrame After Dropping All Rows with Missing Values: (232, 17)
