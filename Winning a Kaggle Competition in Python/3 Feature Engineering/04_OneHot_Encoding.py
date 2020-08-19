# # 8/19/2020
# The problem with label encoding is that it implicitly assumes that there is a ranking dependency between the categories. So, let's change the encoding method for the features "RoofStyle" and "CentralAir" to one-hot encoding. Again, the train and test DataFrames from House Prices Kaggle competition are already available in your workspace.

# Recall that if you're dealing with binary features (categorical features with only two categories) it is suggested to apply label encoder only.

# Your goal is to determine which of the mentioned features is not binary, and to apply one-hot encoding only to this one.

# Concatenate train and test together
houses = pd.concat([train, test])

# Look at feature distributions
print(houses['RoofStyle'].value_counts(), '\n')
print(houses['CentralAir'].value_counts())

# <script.py> output:
#     Gable      2310
#     Hip         551
#     Gambrel      22
#     Flat         20
#     Mansard      11
#     Shed          5
#     Name: RoofStyle, dtype: int64 
    
#     Y    2723
#     N     196
#     Name: CentralAir, dtype: int64

# Concatenate train and test together
houses = pd.concat([train, test])

# Label encode binary 'CentralAir' feature
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
houses['CentralAir_enc'] = le.fit_transform(houses['CentralAir'])

# Create One-Hot encoded features
ohe = pd.get_dummies(houses['RoofStyle'], prefix='RoofStyle')

# Concatenate OHE features to houses
houses = pd.concat([houses, ohe], axis=1)

# Look at OHE features
print(houses[[col for col in houses.columns if 'RoofStyle' in col]].head(3))

# <script.py> output:
#       RoofStyle  RoofStyle_Flat  RoofStyle_Gable  RoofStyle_Gambrel  RoofStyle_Hip  RoofStyle_Mansard  RoofStyle_Shed
#     0     Gable               0                1                  0              0                  0               0
#     1     Gable               0                1                  0              0                  0               0
#     2     Gable               0                1                  0              0                  0               0