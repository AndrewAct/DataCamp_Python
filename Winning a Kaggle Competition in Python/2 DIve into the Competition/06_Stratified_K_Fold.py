# # 8/18/2020
# As you've just noticed, you have a pretty different target variable distribution among the folds due to the random splits. It's not crucial for this particular competition, but could be an issue for the classification competitions with the highly imbalanced target variable.

# To overcome this, let's implement the stratified K-fold strategy with the stratification on the target variable. train DataFrame is already available in your workspace.


# Import StratifiedKFold
from sklearn.model_selection import StratifiedKFold

# Create a StratifiedKFold object
str_kf = StratifiedKFold(n_splits=3, shuffle=True, random_state=123)

# Loop through each split
fold = 0
for train_index, test_index in str_kf.split(train, train['interest_level']):
    # Obtain training and testing folds
    cv_train, cv_test = train.iloc[train_index], train.iloc[test_index]
    print('Fold: {}'.format(fold))
    print('CV train shape: {}'.format(cv_train.shape))
    print('Medium interest listings in CV train: {}\n'.format(sum(cv_train.interest_level == 'medium')))
    fold += 1

# <script.py> output:
#     Fold: 0
#     CV train shape: (666, 9)
#     Medium interest listings in CV train: 167
    
#     Fold: 1
#     CV train shape: (666, 9)
#     Medium interest listings in CV train: 167
    
#     Fold: 2
#     CV train shape: (668, 9)
#     Medium interest listings in CV train: 168