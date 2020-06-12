# # 6/11/2020
# Alright, one final trick before you dive into pipelines. The two step process you just went through - LabelEncoder followed by OneHotEncoder - can be simplified by using a DictVectorizer.

# Using a DictVectorizer on a DataFrame that has been converted to a dictionary allows you to get label encoding as well as one-hot encoding in one go.

# Your task is to work through this strategy in this exercise!

# Import DictVectorizer
from sklearn.feature_extraction import DictVectorizer

# Convert df into a dictionary: df_dict
df_dict = df.to_dict(orient = "records")

# Create the DictVectorizer object: dv
dv = DictVectorizer(sparse = False)

# Apply dv on df: df_encoded
df_encoded = dv.fit_transform(df_dict)

# Print the resulting first five rows
print(df_encoded[:5,:])

# Print the vocabulary
print(dv.vocabulary_)

# <script.py> output:
#     [[3.000e+00 1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 2.000e+00 5.480e+02 1.710e+03 1.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00 0.000e+00 0.000e+00
#       8.450e+03 6.500e+01 6.000e+01 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 5.000e+00 7.000e+00
#       0.000e+00 0.000e+00 1.000e+00 0.000e+00 2.085e+05 2.003e+03]
#      [3.000e+00 1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       1.000e+00 1.000e+00 2.000e+00 4.600e+02 1.262e+03 0.000e+00 0.000e+00
#       0.000e+00 1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       9.600e+03 8.000e+01 2.000e+01 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00 8.000e+00 6.000e+00
#       0.000e+00 0.000e+00 1.000e+00 0.000e+00 1.815e+05 1.976e+03]
#      [3.000e+00 1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 1.000e+00 2.000e+00 6.080e+02 1.786e+03 1.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00 0.000e+00 0.000e+00
#       1.125e+04 6.800e+01 6.000e+01 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 5.000e+00 7.000e+00
#       0.000e+00 0.000e+00 1.000e+00 1.000e+00 2.235e+05 2.001e+03]
#      [3.000e+00 1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 1.000e+00 1.000e+00 6.420e+02 1.717e+03 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00 0.000e+00 0.000e+00
#       9.550e+03 6.000e+01 7.000e+01 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 5.000e+00 7.000e+00
#       0.000e+00 0.000e+00 1.000e+00 1.000e+00 1.400e+05 1.915e+03]
#      [4.000e+00 1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 1.000e+00 2.000e+00 8.360e+02 2.198e+03 1.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 1.000e+00 0.000e+00 0.000e+00
#       1.426e+04 8.400e+01 6.000e+01 0.000e+00 0.000e+00 0.000e+00 1.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 1.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00
#       0.000e+00 0.000e+00 0.000e+00 0.000e+00 0.000e+00 5.000e+00 8.000e+00
#       0.000e+00 0.000e+00 1.000e+00 0.000e+00 2.500e+05 2.000e+03]]
#     {'MSSubClass': 23, 'LotFrontage': 22, 'LotArea': 21, 'OverallQual': 55, 'OverallCond': 54, 'YearBuilt': 61, 'Remodeled': 59, 'GrLivArea': 11, 'BsmtFullBath': 6, 'BsmtHalfBath': 7, 'FullBath': 9, 'HalfBath': 12, 'BedroomAbvGr': 0, 'Fireplaces': 8, 'GarageArea': 10, 'MSZoning=RL': 27, 'PavedDrive=Y': 58, 'Neighborhood=CollgCr': 34, 'BldgType=1Fam': 1, 'HouseStyle=2Story': 18, 'SalePrice': 60, 'Neighborhood=Veenker': 53, 'HouseStyle=1Story': 15, 'Neighborhood=Crawfor': 35, 'Neighborhood=NoRidge': 44, 'Neighborhood=Mitchel': 40, 'HouseStyle=1.5Fin': 13, 'Neighborhood=Somerst': 50, 'Neighborhood=NWAmes': 43, 'MSZoning=RM': 28, 'Neighborhood=OldTown': 46, 'Neighborhood=BrkSide': 32, 'BldgType=2fmCon': 2, 'HouseStyle=1.5Unf': 14, 'Neighborhood=Sawyer': 48, 'Neighborhood=NridgHt': 45, 'Neighborhood=NAmes': 41, 'BldgType=Duplex': 3, 'Neighborhood=SawyerW': 49, 'PavedDrive=N': 56, 'Neighborhood=IDOTRR': 38, 'Neighborhood=MeadowV': 39, 'BldgType=TwnhsE': 5, 'MSZoning=C (all)': 24, 'Neighborhood=Edwards': 36, 'PavedDrive=P': 57, 'Neighborhood=Timber': 52, 'HouseStyle=SFoyer': 19, 'MSZoning=FV': 25, 'Neighborhood=Gilbert': 37, 'HouseStyle=SLvl': 20, 'BldgType=Twnhs': 4, 'Neighborhood=StoneBr': 51, 'HouseStyle=2.5Unf': 17, 'Neighborhood=ClearCr': 33, 'Neighborhood=NPkVill': 42, 'HouseStyle=2.5Fin': 16, 'Neighborhood=Blmngtn': 29, 'Neighborhood=BrDale': 31, 'Neighborhood=SWISU': 47, 'MSZoning=RH': 26, 'Neighborhood=Blueste': 30}
