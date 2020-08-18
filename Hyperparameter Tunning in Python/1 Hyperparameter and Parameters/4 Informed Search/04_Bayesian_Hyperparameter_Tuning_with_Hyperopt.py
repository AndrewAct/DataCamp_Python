# # 8/17/2020
# In this example you will set up and run a bayesian hyperparameter optimization process using the package Hyperopt (already imported as hp for you). You will set up the domain (which is similar to setting up the grid for a grid search), then set up the objective function. Finally, you will run the optimizer over 20 iterations.

# You will need to set up the domain using values:

# max_depth using quniform distribution (between 2 and 10, increasing by 2)
# learning_rate using uniform distribution (0.001 to 0.9)
# Note that for the purpose of this exercise, this process was reduced in data sample size and hyperopt & GBM iterations. If you are trying out this method by yourself on your own machine, try a larger search space, more trials, more cvs and a larger dataset size to really see this in action!

# Set up space dictionary with specified hyperparameters
space = {'max_depth': hp.quniform('max_depth', 2, 10, 2),'learning_rate': hp.uniform('learning_rate', 0.001,0.9)}

# Set up objective function
def objective(params):
    params = {'max_depth': int(params['max_depth']),'learning_rate': params['learning_rate']}
    gbm_clf = GradientBoostingClassifier(n_estimators=100, **params) 
    best_score = cross_val_score(gbm_clf, X_train, y_train, scoring='accuracy', cv=2, n_jobs=4).mean()
    loss = 1 - best_score
    return loss

# Run the algorithm
best = fmin(fn=objective,space=space, max_evals=20, rstate=np.random.RandomState(42), algo=tpe.suggest)
print(best)

# <script.py> output:
    
#   0%|          | 0/20 [00:00<?, ?it/s, best loss: ?]
#   5%|5         | 1/20 [00:00<00:03,  5.47it/s, best loss: 0.26759418985474637]
#  10%|#         | 2/20 [00:00<00:03,  5.37it/s, best loss: 0.2549063726593165] 
#  15%|#5        | 3/20 [00:00<00:03,  5.50it/s, best loss: 0.2549063726593165]
#  20%|##        | 4/20 [00:00<00:02,  5.60it/s, best loss: 0.2549063726593165]
#  25%|##5       | 5/20 [00:01<00:03,  4.07it/s, best loss: 0.2549063726593165]
#  30%|###       | 6/20 [00:01<00:03,  4.15it/s, best loss: 0.2549063726593165]
#  35%|###5      | 7/20 [00:01<00:02,  4.56it/s, best loss: 0.2549063726593165]
#  40%|####      | 8/20 [00:01<00:02,  4.77it/s, best loss: 0.2549063726593165]
#  45%|####5     | 9/20 [00:01<00:02,  4.99it/s, best loss: 0.2549063726593165]
#  50%|#####     | 10/20 [00:02<00:01,  5.37it/s, best loss: 0.2549063726593165]
#  55%|#####5    | 11/20 [00:02<00:01,  5.58it/s, best loss: 0.2549063726593165]
#  60%|######    | 12/20 [00:02<00:01,  5.18it/s, best loss: 0.2549063726593165]
#  65%|######5   | 13/20 [00:02<00:01,  4.78it/s, best loss: 0.2549063726593165]
#  70%|#######   | 14/20 [00:03<00:01,  3.20it/s, best loss: 0.2525688142203555]
#  75%|#######5  | 15/20 [00:03<00:01,  3.70it/s, best loss: 0.2525688142203555]
#  80%|########  | 16/20 [00:03<00:01,  3.98it/s, best loss: 0.2525688142203555]
#  85%|########5 | 17/20 [00:04<00:01,  2.91it/s, best loss: 0.24246856171404285]
#  90%|######### | 18/20 [00:04<00:00,  3.37it/s, best loss: 0.24246856171404285]
#  95%|#########5| 19/20 [00:04<00:00,  3.76it/s, best loss: 0.24246856171404285]
# 100%|##########| 20/20 [00:04<00:00,  4.20it/s, best loss: 0.24246856171404285]
# 100%|##########| 20/20 [00:04<00:00,  4.24it/s, best loss: 0.24246856171404285]
#     {'learning_rate': 0.11310589268581149, 'max_depth': 6.0}
