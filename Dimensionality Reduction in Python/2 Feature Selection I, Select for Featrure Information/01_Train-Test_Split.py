# # 6/14/2020
# In this chapter, you will keep working with the ANSUR dataset. Before you can build a model on your dataset, you should first decide on which feature you want to predict. In this case, you're trying to predict gender.

# You need to extract the column holding this feature from the dataset and then split the data into a training and test set. The training set will be used to train the model and the test set will be used to check its performance on unseen data.

# ansur_df has been pre-loaded for you.

# Import train_test_split()
from sklearn.model_selection import train_test_split

# Select the Gender column as the feature to be predicted (y)
y = ansur_df['Gender']

# Remove the Gender column to create the training data
X = ansur_df.drop('Gender', axis = 1)

# Perform a 70% train and 30% test data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

print("{} rows in test set vs. {} in training set. {} Features.".format(X_test.shape[0], X_train.shape[0], X_test.shape[1]))

# Gender  abdominalextensiondepthsitting  acromialheight  acromionradialelength  anklecircumference  ...  waistdepth  waistfrontlengthsitting  waistheightomphalion  wristcircumference  wristheight
# 0   Male                             266            1467                    337                 222  ...         240                      440                  1054                 175          853
# 1   Male                             233            1395                    326                 220  ...         225                      371                  1054                 167          815
# 2   Male                             287            1430                    341                 230  ...         255                      411                  1041                 180          831
# 3   Male                             234            1347                    310                 230  ...         205                      399                   968                 176          793
# 4   Male                             250            1585                    372                 247  ...         214                      379                  1245                 188          954

# [5 rows x 92 columns]

# <script.py> output:
#     300 rows in test set vs. 700 in training set. 91 Features.
