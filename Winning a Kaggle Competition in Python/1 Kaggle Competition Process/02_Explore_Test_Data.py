# # 8/18/2020
# Having looked at the train data, let's explore the test data in the "Store Item Demand Forecasting Challenge". Remember, that the test dataset generally contains one column less than the train one.

# This column, together with the output format, is presented in the sample submission file. Before making any progress in the competition, you should get familiar with the expected output.

# That is why, let's look at the columns of the test dataset and compare it to the train columns. Additionally, let's explore the format of the sample submission. The train DataFrame is available in your workspace.

import pandas as pd

# Read the test data
test = pd.read_csv('test.csv')
# Print train and test columns
print('Train columns:', train.columns.tolist())
print('Test columns:', test.columns.tolist())

# Read the sample submission file
sample_submission = pd.read_csv('sample_submission.csv')

# Look at the head() of the sample submission
print(sample_submission.head())

# <script.py> output:
#     Train columns: ['id', 'date', 'store', 'item', 'sales']
#     Test columns: ['id', 'date', 'store', 'item']
#        id  sales
#     0   0     52
#     1   1     52
#     2   2     52
#     3   3     52
#     4   4     52