# # 8/16/2020
# Understanding what hyperparameters are available and the impact of different hyperparameters is a core skill for any data scientist. As models become more complex, there are many different settings you can set, but only some will have a large impact on your model.

# You will now assess an existing random forest model (it has some bad choices for hyperparameters!) and then make better choices for a new random forest model and assess its performance.

# You will have available:

# X_train, X_test, y_train, y_test DataFrames
# An existing pre-trained random forest estimator, rf_clf_old
# The predictions of the existing random forest estimator on the test set, rf_old_predictions

# Print out the old estimator, notice which hyperparameter is badly set
print(rf_clf_old)

# Get confusion matrix & accuracy for the old rf_model
print("Confusion Matrix: \n\n {} \n Accuracy Score: \n\n {}".format(
  	confusion_matrix(y_test, rf_old_predictions),  
  	accuracy_score(y_test, rf_old_predictions)))

# <script.py> output:
#     RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#                 max_depth=None, max_features='auto', max_leaf_nodes=None,
#                 min_impurity_decrease=0.0, min_impurity_split=None,
#                 min_samples_leaf=1, min_samples_split=2,
#                 min_weight_fraction_leaf=0.0, n_estimators=5, n_jobs=None,
#                 oob_score=False, random_state=42, verbose=0, warm_start=False)
#     Confusion Matrix: 
    
#      [[276  37]
#      [ 64  23]] 
#      Accuracy Score: 
    
#      0.7475


# Print out the old estimator, notice which hyperparameter is badly set
print(rf_clf_old)

# Get confusion matrix & accuracy for the old rf_model
print("Confusion Matrix: \n\n {} \n Accuracy Score: \n\n {}".format(
  confusion_matrix(y_test, rf_old_predictions),
  accuracy_score(y_test, rf_old_predictions))) 

# Create a new random forest classifier with better hyperparamaters
rf_clf_new = RandomForestClassifier(n_estimators=500)

# Fit this to the data and obtain predictions
rf_new_predictions = rf_clf_new.fit(X_train, y_train).predict(X_test)

# Assess the new model (using new predictions!)
print("Confusion Matrix: \n\n", confusion_matrix(y_test, rf_new_predictions))
print("Accuracy Score: \n\n", accuracy_score(y_test, rf_new_predictions))

# <script.py> output:
#     RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#                 max_depth=None, max_features='auto', max_leaf_nodes=None,
#                 min_impurity_decrease=0.0, min_impurity_split=None,
#                 min_samples_leaf=1, min_samples_split=2,
#                 min_weight_fraction_leaf=0.0, n_estimators=5, n_jobs=None,
#                 oob_score=False, random_state=42, verbose=0, warm_start=False)
#     Confusion Matrix: 
    
#      [[276  37]
#      [ 64  23]] 
#      Accuracy Score: 
    
#      0.7475
#     Confusion Matrix: 
    
#      [[300  13]
#      [ 63  24]]
#     Accuracy Score: 
    
#      0.81