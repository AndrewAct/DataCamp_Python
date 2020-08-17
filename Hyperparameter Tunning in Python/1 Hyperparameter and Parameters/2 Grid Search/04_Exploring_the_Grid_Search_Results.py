# # 8/17/2020
# You will now explore the cv_results_ property of the GridSearchCV object defined in the video. This is a dictionary that we can read into a pandas DataFrame and contains a lot of useful information about the grid search we just undertook.

# A reminder of the different column types in this property:

# time_ columns
# param_ columns (one for each hyperparameter) and the singular params column (with all hyperparameter settings)
# a train_score column for each cv fold including the mean_train_score and std_train_score columns
# a test_score column for each cv fold including the mean_test_score and std_test_score columns
# a rank_test_score column with a number from 1 to n (number of iterations) ranking the rows based on their mean_test_score

# Read the cv_results_ property of the grid_rf_class GridSearchCV object into a data frame & print the whole thing out to inspect.
# Extract & print the singular column containing a dictionary of all hyperparameters used in each iteration of the grid search.
# Extract & print the row that had the best mean test score by indexing using the rank_test_score column.

# Read the cv_results property into a dataframe & print it out
cv_results_df = pd.DataFrame(grid_rf_class.cv_results_)
print(cv_results_df)

# Extract and print the column with a dictionary of hyperparameters used
column = cv_results_df.loc[:, ["params"]]
print(column)

# Extract and print the row that had the best mean test score
best_row = cv_results_df[cv_results_df["rank_test_score"] == 1 ]
print(best_row)

# <script.py> output:
#         mean_fit_time  std_fit_time       ...         mean_train_score  std_train_score
#     0        0.324582      0.004639       ...                 0.996098     1.248173e-03
#     1        0.671539      0.018667       ...                 0.996983     1.319340e-03
#     2        0.977654      0.011564       ...                 0.997168     1.311001e-03
#     3        0.313844      0.008520       ...                 0.989866     3.382634e-03
#     4        0.645001      0.003995       ...                 0.992082     2.134008e-03
#     5        0.967691      0.010192       ...                 0.991969     2.131063e-03
#     6        0.342355      0.002576       ...                 1.000000     4.965068e-17
#     7        0.724901      0.003929       ...                 1.000000     4.965068e-17
#     8        1.078176      0.013817       ...                 1.000000     0.000000e+00
#     9        0.351497      0.010176       ...                 0.998668     7.821910e-04
#     10       0.695131      0.018459       ...                 0.999002     3.932301e-04
#     11       0.792999      0.021011       ...                 0.998844     7.443455e-04
    
#     [12 rows x 23 columns]
#                                                    params
#     0   {'max_depth': 10, 'min_samples_leaf': 1, 'n_es...
#     1   {'max_depth': 10, 'min_samples_leaf': 1, 'n_es...
#     2   {'max_depth': 10, 'min_samples_leaf': 1, 'n_es...
#     3   {'max_depth': 10, 'min_samples_leaf': 2, 'n_es...
#     4   {'max_depth': 10, 'min_samples_leaf': 2, 'n_es...
#     5   {'max_depth': 10, 'min_samples_leaf': 2, 'n_es...
#     6   {'max_depth': 20, 'min_samples_leaf': 1, 'n_es...
#     7   {'max_depth': 20, 'min_samples_leaf': 1, 'n_es...
#     8   {'max_depth': 20, 'min_samples_leaf': 1, 'n_es...
#     9   {'max_depth': 20, 'min_samples_leaf': 2, 'n_es...
#     10  {'max_depth': 20, 'min_samples_leaf': 2, 'n_es...
#     11  {'max_depth': 20, 'min_samples_leaf': 2, 'n_es...
#        mean_fit_time  std_fit_time       ...         mean_train_score  std_train_score
#     2       0.977654      0.011564       ...                 0.997168         0.001311
    
#     [1 rows x 23 columns]
