# # 8/17/2020
# You're going to undertake a simple example of genetic hyperparameter tuning. TPOT is a very powerful library that has a lot of features. You're just scratching the surface in this lesson, but you are highly encouraged to explore in your own time.

# This is a very small example. In real life, TPOT is designed to be run for many hours to find the best model. You would have a much larger population and offspring size as well as hundreds more generations to find a good model.

# You will create the estimator, fit the estimator to the training data and then score this on the test data.

# For this example we wish to use:

# 3 generations
# 4 in the population size
# 3 offspring in each generation
# accuracy for scoring
# A random_state of 2 has been set for consistency of results.

# Assign the values outlined to the inputs
number_generations = 3
population_size = 4
offspring_size = 3
scoring_function = 'accuracy'

# Create the tpot classifier
tpot_clf = TPOTClassifier(generations=number_generations, population_size=population_size,
                          offspring_size=3, scoring='accuracy',
                          verbosity=2, random_state=2, cv=2)

# Fit the classifier to the training data
tpot_clf.fit(X_train, y_train)

# Score on the test set
print(tpot_clf.score(X_test, y_test))

# <script.py> output:
#     Warning: xgboost.XGBClassifier is not available and will not be used by TPOT.
#     Generation 1 - Current best internal CV score: 0.7575064376609415
#     Generation 2 - Current best internal CV score: 0.7750693767344183
#     Generation 3 - Current best internal CV score: 0.7750693767344183
    
#     Best pipeline: BernoulliNB(input_matrix, alpha=0.1, fit_prior=True)
#     0.76