# # 8/16/2020
# You are now going to practice extracting an important parameter of the logistic regression model. The logistic regression has a few other parameters you will not explore here but you can review them in the scikit-learn.org documentation for the LogisticRegression() module under 'Attributes'.

# This parameter is important for understanding the direction and magnitude of the effect the variables have on the target.

# In this exercise we will extract the coefficient parameter (found in the coef_ attribute), zip it up with the original column names, and see which variables had the largest positive effect on the target variable.

# You will have available:

# A logistic regression model object named log_reg_clf
# The X_train DataFrame
# sklearn and pandas have been imported for you.

# Create a list of original variable names from the training DataFrame
original_variables = X_train.columns

# Extract the coefficients of the logistic regression estimator
model_coefficients = log_reg_clf.coef_[0]

# Create a dataframe of the variables and coefficients & print it out
coefficient_df = pd.DataFrame({"Variable" : original_variables, "Coefficient": model_coefficients})
print(coefficient_df)

# Print out the top 3 positive variables
top_three_df = coefficient_df.sort_values(by="Coefficient", axis=0, ascending=False)[0:3]
print(top_three_df)

# <script.py> output:
#            Variable   Coefficient
#     0     LIMIT_BAL -2.886513e-06
#     1           AGE -8.231685e-03
#     2         PAY_0  7.508570e-04
#     3         PAY_2  3.943751e-04
#     4         PAY_3  3.794236e-04
#     5         PAY_4  4.346120e-04
#     6         PAY_5  4.375615e-04
#     7         PAY_6  4.121071e-04
#     8     BILL_AMT1 -6.410891e-06
#     9     BILL_AMT2 -4.393645e-06
#     10    BILL_AMT3  5.147052e-06
#     11    BILL_AMT4  1.476978e-05
#     12    BILL_AMT5  2.644462e-06
#     13    BILL_AMT6 -2.446051e-06
#     14     PAY_AMT1 -5.448954e-05
#     15     PAY_AMT2 -8.516338e-05
#     16     PAY_AMT3 -4.732779e-05
#     17     PAY_AMT4 -3.238528e-05
#     18     PAY_AMT5 -3.141833e-05
#     19     PAY_AMT6  2.447717e-06
#     20        SEX_2 -2.240863e-04
#     21  EDUCATION_1 -1.642599e-05
#     22  EDUCATION_2 -1.777295e-04
#     23  EDUCATION_3 -5.875596e-05
#     24  EDUCATION_4 -3.681278e-06
#     25  EDUCATION_5 -7.865964e-06
#     26  EDUCATION_6 -9.450362e-07
#     27   MARRIAGE_1 -5.036826e-05
#     28   MARRIAGE_2 -2.254362e-04
#     29   MARRIAGE_3  1.070545e-05
#       Variable  Coefficient
#     2    PAY_0     0.000751
#     6    PAY_5     0.000438
#     5    PAY_4     0.000435