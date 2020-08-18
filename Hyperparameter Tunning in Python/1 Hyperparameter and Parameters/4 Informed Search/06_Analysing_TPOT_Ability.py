# # 8/17/2020
# You will now see the random nature of TPOT by constructing the classifier with different random states and seeing what model is found to be best by the algorithm. This assists to see that TPOT is quite unstable when not run for a reasonable amount of time.

# Create the tpot classifier 
tpot_clf = TPOTClassifier(generations=2, population_size=4, offspring_size=3, scoring='accuracy', cv=2,
                          verbosity=2, random_state=42)

# Fit the classifier to the training data
tpot_clf.fit(X_train, y_train)

# Score on the test set
print(tpot_clf.score(X_test, y_test))

# <script.py> output:
#     Warning: xgboost.XGBClassifier is not available and will not be used by TPOT.
#     Generation 1 - Current best internal CV score: 0.7549688742218555
#     Generation 2 - Current best internal CV score: 0.7549688742218555
    
#     Best pipeline: DecisionTreeClassifier(input_matrix, criterion=gini, max_depth=7, min_samples_leaf=11, min_samples_split=12)
#     0.75

# Create the tpot classifier 
tpot_clf = TPOTClassifier(generations=2, population_size=4, offspring_size=3, scoring='accuracy', cv=2,
                          verbosity=2, random_state=122)

# Fit the classifier to the training data
tpot_clf.fit(X_train, y_train)

# Score on the test set
print(tpot_clf.score(X_test, y_test))


# <script.py> output:
#     Warning: xgboost.XGBClassifier is not available and will not be used by TPOT.
#     Generation 1 - Current best internal CV score: 0.7675066876671917
#     Generation 2 - Current best internal CV score: 0.7675066876671917
    
#     Best pipeline: KNeighborsClassifier(MaxAbsScaler(input_matrix), n_neighbors=57, p=1, weights=distance)
#     0.75


# Create the tpot classifier 
tpot_clf = TPOTClassifier(generations=2, population_size=4, offspring_size=3, scoring='accuracy', cv=2,
                          verbosity=2, random_state=99)

# Fit the classifier to the training data
tpot_clf.fit(X_train, y_train)

# Score on the test set
print(tpot_clf.score(X_test, y_test))

# <script.py> output:
#     Warning: xgboost.XGBClassifier is not available and will not be used by TPOT.
#     Generation 1 - Current best internal CV score: 0.8075326883172079
#     Generation 2 - Current best internal CV score: 0.8075326883172079
    
#     Best pipeline: RandomForestClassifier(SelectFwe(input_matrix, alpha=0.033), bootstrap=False, criterion=gini, max_features=1.0, min_samples_leaf=19, min_samples_split=10, n_estimators=100)
#     0.78