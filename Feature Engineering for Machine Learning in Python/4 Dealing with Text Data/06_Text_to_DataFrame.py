# # 7/12/2020
# Now that you have generated these count based features in an array you will need to reformat them so that they can be combined with the rest of the dataset. This can be achieved by converting the array into a pandas DataFrame, with the feature names you found earlier as the column names, and then concatenate it with the original DataFrame.

# The numpy array (cv_array) and the vectorizer (cv) you fit in the last exercise are available in your workspace.

# Create a DataFrame with these features
cv_df = pd.DataFrame(cv_transformed.toarray(), 
                     columns=cv.get_feature_names()).add_prefix('Counts_')

# Add the new columns to the original DataFrame
speech_df_new = pd.concat([speech_df, cv_df], axis=1, sort=False)
print(speech_df_new.head())

# <script.py> output:
#                     Name         Inaugural Address                      Date                                               text                                         text_clean  ...  Counts_years  \
#     0  George Washington   First Inaugural Address  Thursday, April 30, 1789  Fellow-Citizens of the Senate and of the House...  fellow citizens of the senate and of the house...  ...             1   
#     1  George Washington  Second Inaugural Address     Monday, March 4, 1793  Fellow Citizens:  I AM again called upon by th...  fellow citizens   i am again called upon by th...  ...             0   
#     2         John Adams         Inaugural Address   Saturday, March 4, 1797  WHEN it was first perceived, in early times, t...  when it was first perceived  in early times  t...  ...             3   
#     3   Thomas Jefferson   First Inaugural Address  Wednesday, March 4, 1801  Friends and Fellow-Citizens:  CALLED upon to u...  friends and fellow citizens   called upon to u...  ...             0   
#     4   Thomas Jefferson  Second Inaugural Address     Monday, March 4, 1805  PROCEEDING, fellow-citizens, to that qualifica...  proceeding  fellow citizens  to that qualifica...  ...             2   
    
#        Counts_yet  Counts_you  Counts_young  Counts_your  
#     0           0           5             0            9  
#     1           0           0             0            1  
#     2           0           0             0            1  
#     3           2           7             0            7  
#     4           2           4             0            4  
    
#     [5 rows x 826 columns]
