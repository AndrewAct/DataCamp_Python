# # 5/24/2020
# Alright, you've been patient and awesome. 
# It's finally time to start training models!

# The first step is to split the data into a training set and a test set. 
# Some labels don't occur very often, but we want to make sure that they appear in both the training and the test sets. 
# We provide a function that will make sure at least min_count examples of each label appear in each split: multilabel_train_test_split.

# Feel free to check out the full code for multilabel_train_test_split here.

# You'll start with a simple model that uses just the numeric columns of your DataFrame when calling multilabel_train_test_split. 
# The data has been read into a DataFrame df and a list consisting of just the numeric columns is available as NUMERIC_COLUMNS.

## Note: get_dummies would covert categorical variable into dummy/indicator variaables
# Create the new DataFrame: numeric_data_only
numeric_data_only = df[NUMERIC_COLUMNS].fillna(-1000)

# Get labels and convert to dummy variables: label_dummies
label_dummies = pd.get_dummies(df[LABELS])

# Create training and test sets
X_train, X_test, y_train, y_test = multilabel_train_test_split(numeric_data_only,
                                                               label_dummies,
                                                               size=0.2, 
                                                               seed=123)

# Print the info
print("X_train info:")
print(X_train.info())
print("\nX_test info:")  
print(X_test.info())
print("\ny_train info:")  
print(y_train.info())
print("\ny_test info:")  
print(y_test.info()) 

# <script.py> output:
#     X_train info:
#     <class 'pandas.core.frame.DataFrame'>
#     Int64Index: 1040 entries, 198 to 101861
#     Data columns (total 2 columns):
#     FTE      1040 non-null float64
#     Total    1040 non-null float64
#     dtypes: float64(2)
#     memory usage: 24.4 KB
#     None
    
#     X_test info:
#     <class 'pandas.core.frame.DataFrame'>
#     Int64Index: 520 entries, 209 to 448628
#     Data columns (total 2 columns):
#     FTE      520 non-null float64
#     Total    520 non-null float64
#     dtypes: float64(2)
#     memory usage: 12.2 KB
#     None
    
#     y_train info:
#     <class 'pandas.core.frame.DataFrame'>
#     Int64Index: 1040 entries, 198 to 101861
#     Columns: 104 entries, Function_Aides Compensation to Operating_Status_PreK-12 Operating
#     dtypes: uint8(104)
#     memory usage: 113.8 KB
#     None
    
#     y_test info:
#     <class 'pandas.core.frame.DataFrame'>
#     Int64Index: 520 entries, 209 to 448628
#     Columns: 104 entries, Function_Aides Compensation to Operating_Status_PreK-12 Operating
#     dtypes: uint8(104)
#     memory usage: 56.9 KB
#     None