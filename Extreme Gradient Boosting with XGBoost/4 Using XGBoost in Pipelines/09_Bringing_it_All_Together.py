# # 6/12/2020
# Alright, it's time to bring together everything you've learned so far! In this final exercise of the course, you will combine your work from the previous exercises into one end-to-end XGBoost pipeline to really cement your understanding of preprocessing and pipelines in XGBoost.

# Your work from the previous 3 exercises, where you preprocessed the data and set up your pipeline, has been pre-loaded. Your job is to perform a randomized search and identify the best hyperparameters.

# Create the parameter grid
gbm_param_grid = {
    'clf__learning_rate': np.arange(0.05, 1, 0.05),
    'clf__max_depth': np.arange(3, 10, 1),
    'clf__n_estimators': np.arange(50, 200, 50)
}

# Perform RandomizedSearchCV
randomized_roc_auc = RandomizedSearchCV(estimator= pipeline, param_distributions= gbm_param_grid,
                                        cv = 2, n_iter= 2, scoring = "roc_auc", verbose = 1)

# Fit the estimator
randomized_roc_auc.fit(X, y)

# Compute metrics
print(randomized_roc_auc.best_score_)
print(randomized_roc_auc.best_estimator_)

# <script.py> output:
#     Fitting 3 folds for each of 2 candidates, totalling 6 fits
#     0.9975202094090647
#     Pipeline(memory=None,
#              steps=[('featureunion',
#                      FeatureUnion(n_jobs=None,
#                                   transformer_list=[('num_mapper',
#                                                      DataFrameMapper(default=False,
#                                                                      df_out=True,
#                                                                      features=[(['age'],
#                                                                                 Imputer(axis=0,
#                                                                                         copy=True,
#                                                                                         missing_values='NaN',
#                                                                                         strategy='median',
#                                                                                         verbose=0)),
#                                                                                (['bp'],
#                                                                                 Imputer(axis=0,
#                                                                                         copy=True,
#                                                                                         missing_values='NaN',
#                                                                                         strategy='median',
#                                                                                         verbose=0)),
#                                                                                (['sg'],
#                                                                                 Imputer(axis=0,
#                                                                                         copy=...
#                      XGBClassifier(base_score=0.5, booster='gbtree',
#                                    colsample_bylevel=1, colsample_bynode=1,
#                                    colsample_bytree=1, gamma=0,
#                                    learning_rate=0.9000000000000001,
#                                    max_delta_step=0, max_depth=5,
#                                    min_child_weight=1, missing=None,
#                                    n_estimators=150, n_jobs=1, nthread=None,
#                                    objective='binary:logistic', random_state=0,
#                                    reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
#                                    seed=None, silent=None, subsample=1,
#                                    verbosity=1))],
#              verbose=False)

# <script.py> output:
#     Fitting 2 folds for each of 2 candidates, totalling 4 fits
#     0.9965333333333334
#     Pipeline(memory=None,
#              steps=[('featureunion',
#                      FeatureUnion(n_jobs=None,
#                                   transformer_list=[('num_mapper',
#                                                      DataFrameMapper(default=False,
#                                                                      df_out=True,
#                                                                      features=[(['age'],
#                                                                                 Imputer(axis=0,
#                                                                                         copy=True,
#                                                                                         missing_values='NaN',
#                                                                                         strategy='median',
#                                                                                         verbose=0)),
#                                                                                (['bp'],
#                                                                                 Imputer(axis=0,
#                                                                                         copy=True,
#                                                                                         missing_values='NaN',
#                                                                                         strategy='median',
#                                                                                         verbose=0)),
#                                                                                (['sg'],
#                                                                                 Imputer(axis=0,
#                                                                                         copy=...
#                      XGBClassifier(base_score=0.5, booster='gbtree',
#                                    colsample_bylevel=1, colsample_bynode=1,
#                                    colsample_bytree=1, gamma=0,
#                                    learning_rate=0.9500000000000001,
#                                    max_delta_step=0, max_depth=4,
#                                    min_child_weight=1, missing=None,
#                                    n_estimators=100, n_jobs=1, nthread=None,
#                                    objective='binary:logistic', random_state=0,
#                                    reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
#                                    seed=None, silent=None, subsample=1,
#                                    verbosity=1))],
#              verbose=False)
