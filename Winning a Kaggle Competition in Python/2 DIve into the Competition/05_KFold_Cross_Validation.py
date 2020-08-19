# # 8/18/2020
# You will start by getting hands-on experience in the most commonly used K-fold cross-validation.

# The data you'll be working with is from the "Two sigma connect: rental listing inquiries" Kaggle competition. The competition problem is a multi-class classification of the rental listings into 3 classes: low interest, medium interest and high interest. For faster performance, you will work with a subsample consisting of 1,000 observations.

# You need to implement a K-fold validation strategy and look at the sizes of each fold obtained. train DataFrame is already available in your workspace.

# Import KFold
from sklearn.model_selection import KFold

# Create a KFold object
kf = KFold(n_splits=3, shuffle=True, random_state=123)

# Loop through each split
fold = 0
for train_index, test_index in kf.split(train):
    # Obtain training and testing folds
    cv_train, cv_test = train.iloc[train_index], train.iloc[test_index]
    print('Fold: {}'.format(fold))
    print('CV train shape: {}'.format(cv_train.shape))
    print('Medium interest listings in CV train: {}\n'.format(sum(cv_train.interest_level == 'medium')))
    fold += 1

# <script.py> output:
#     Fold: 0
#     CV train shape: (666, 9)
#     Medium interest listings in CV train: 175
    
#     Fold: 1
#     CV train shape: (667, 9)
#     Medium interest listings in CV train: 165
    
#     Fold: 2
#     CV train shape: (667, 9)
#     Medium interest listings in CV train: 162
