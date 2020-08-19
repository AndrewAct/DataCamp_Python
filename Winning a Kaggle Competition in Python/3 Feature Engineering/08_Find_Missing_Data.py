# # 8/19/2020
# Let's impute missing data on a real Kaggle dataset. For this purpose, you will be using a data subsample from the Kaggle "Two sigma connect: rental listing inquiries" competition.

# Before proceeding with any imputing you need to know the number of missing values for each of the features. Moreover, if the feature has missing values, you should explore the type of this feature.

# Read DataFrame
twosigma = pd.read_csv('twosigma_train.csv')

# Find the number of missing values in each column
print(twosigma.isnull().sum())

# Look at the columns with the missing values
print(twosigma[["building_id", "price"]].head())

# <script.py> output:
#     id                 0
#     bathrooms          0
#     bedrooms           0
#     building_id       13
#     latitude           0
#     longitude          0
#     manager_id         0
#     price             32
#     interest_level     0
#     dtype: int64
#                             building_id   price
#     0  53a5b119ba8f7b61d4e010512e0dfc85  3000.0
#     1  c5c8a357cba207596b04d1afd1e4f130  5465.0
#     2  c3ba40552e2120b0acfc3cb5730bb2aa  2850.0
#     3  28d9ad350afeaab8027513a3e52ac8d5  3275.0
#     4                               NaN  3350.0