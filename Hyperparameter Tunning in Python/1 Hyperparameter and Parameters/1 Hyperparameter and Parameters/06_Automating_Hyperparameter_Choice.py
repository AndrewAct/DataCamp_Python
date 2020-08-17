# # 8/14/2020
# Finding the best hyperparameter of interest without writing hundreds of lines of code for hundreds of models is an important efficiency gain that will greatly assist your future machine learning model building.

# An important hyperparameter for the GBM algorithm is the learning rate. But which learning rate is best for this problem? By writing a loop to search through a number of possibilities, collating these and viewing them you can find the best one.

# Possible learning rates to try include 0.001, 0.01, 0.05, 0.1, 0.2 and 0.5

# You will have available X_train, X_test, y_train & y_test datasets, and GradientBoostingClassifier has been imported for you.

# Set the learning rates & results storage
learning_rates = [0.001, 0.01, 0.05, 0.1, 0.2,0.5]
results_list = []

# Create the for loop to evaluate model predictions for each learning rate
for rate in learning_rates:
    model = GradientBoostingClassifier(learning_rate=rate)
    predictions = model.fit(X_train, y_train).predict(X_test)
    # Save the learning rate and accuracy score
    results_list.append([rate, accuracy_score(y_test, predictions)])

# Gather everything into a DataFrame
results_df = pd.DataFrame(results_list, columns=['learning_rate', 'accuracy'])
print(results_df)


# <script.py> output:
#        learning_rate  accuracy
#     0          0.001    0.7825
#     1          0.010    0.8025
#     2          0.050    0.8100
#     3          0.100    0.7975
#     4          0.200    0.7900
#     5          0.500    0.7775