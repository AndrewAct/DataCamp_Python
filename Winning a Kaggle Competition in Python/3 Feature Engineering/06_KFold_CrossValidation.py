# # 8/19/2020
# You will work with a binary classification problem on a subsample from Kaggle playground competition. The objective of this competition is to predict whether a famous basketball player Kobe Bryant scored a basket or missed a particular shot.

# Train data is available in your workspace as bryant_shots DataFrame. It contains data on 10,000 shots with its properties and a target variable "shot\_made\_flag" -- whether shot was scored or not.

# One of the features in the data is "game_id" -- a particular game where the shot was made. There are 541 distinct games. So, you deal with a high-cardinality categorical feature. Let's encode it using a target mean!

# Suppose you're using 5-fold cross-validation and want to evaluate a mean target encoded feature on the local validation.

# Create 5-fold cross-validation
kf = KFold(n_splits=5, random_state=123, shuffle=True)

# For each folds split
for train_index, test_index in kf.split(bryant_shots):
    cv_train, cv_test = bryant_shots.iloc[train_index], bryant_shots.iloc[test_index]

    # Create mean target encoded feature
    cv_train['game_id_enc'], cv_test['game_id_enc'] = mean_target_encoding(train=cv_train,
                                                                           test=cv_test,
                                                                           target='shot_made_flag',
                                                                           categorical='game_id',
                                                                           alpha=5)
    # Look at the encoding
    print(cv_train[['game_id', 'shot_made_flag', 'game_id_enc']].sample(n=1))

# <script.py> output:
#            game_id  shot_made_flag  game_id_enc
#     7106  20500532             0.0     0.361914
#            game_id  shot_made_flag  game_id_enc
#     5084  20301100             0.0     0.568395
#            game_id  shot_made_flag  game_id_enc
#     6687  20500228             0.0      0.48131
#            game_id  shot_made_flag  game_id_enc
#     5046  20301075             0.0     0.252103
#            game_id  shot_made_flag  game_id_enc
#     4662  20300515             1.0     0.452637
