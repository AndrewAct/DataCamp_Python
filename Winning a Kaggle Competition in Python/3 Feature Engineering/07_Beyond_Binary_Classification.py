# # 8/19/2020
# Of course, binary classification is just a single special case. Target encoding could be applied to any target variable type:

# For binary classification usually mean target encoding is used
# For regression mean could be changed to median, quartiles, etc.
# For multi-class classification with N classes we create N features with target mean for each category in one vs. all fashion
# The mean_target_encoding() function you've created could be used for any target type specified above. Let's apply it for the regression problem on the example of House Prices Kaggle competition.

# Your goal is to encode a categorical feature "RoofStyle" using mean target encoding. The train and test DataFrames are already available in your workspace.

# Create mean target encoded feature
train['RoofStyle_enc'], test['RoofStyle_enc'] = mean_target_encoding(train=train,
                                                                     test=test,
                                                                     target='SalePrice',
                                                                     categorical='RoofStyle',
                                                                     alpha=10)

# Look at the encoding
print(test[['RoofStyle', 'RoofStyle_enc']].drop_duplicates())

# <script.py> output:
#          RoofStyle  RoofStyle_enc
#     0        Gable  171565.947836
#     1          Hip  217594.645131
#     98     Gambrel  164152.950424
#     133       Flat  188703.563431
#     362    Mansard  180775.938759
#     1053      Shed  188267.663242
