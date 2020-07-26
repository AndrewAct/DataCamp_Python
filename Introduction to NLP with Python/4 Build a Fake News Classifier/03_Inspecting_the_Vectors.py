# # 7/24/2020
# To get a better idea of how the vectors work, you'll investigate them by converting them into pandas DataFrames.

# Here, you'll use the same data structures you created in the previous two exercises (count_train, count_vectorizer, tfidf_train, tfidf_vectorizer) as well as pandas, which is imported as pd.

# Create the CountVectorizer DataFrame: count_df
count_df = pd.DataFrame(count_train.A, columns=count_vectorizer.get_feature_names())

# Create the TfidfVectorizer DataFrame: tfidf_df
tfidf_df = pd.DataFrame(tfidf_train.A, columns= tfidf_vectorizer.get_feature_names())

# Print the head of count_df
print(count_df.head())

# Print the head of tfidf_df
print(tfidf_df.head())

# Calculate the difference in columns: difference
difference = set(count_df.columns) - set(tfidf_df.columns)
print(difference)

# Check whether the DataFrames are equal
print(count_df.equals(tfidf_df))


# <script.py> output:
#        000  00am  0600  10  100  107  11  110  1100  12    ...      younger  \
#     0    0     0     0   0    0    0   0    0     0   0    ...            0   
#     1    0     0     0   3    0    0   0    0     0   0    ...            0   
#     2    0     0     0   0    0    0   0    0     0   0    ...            0   
#     3    0     0     0   0    0    0   0    0     0   0    ...            1   
#     4    0     0     0   0    0    0   0    0     0   0    ...            0   
    
#        youth  youths  youtube  ypg  yuan  zawahiri  zeitung  zero  zerohedge  
#     0      0       0        0    0     0         0        0     1          0  
#     1      0       0        0    0     0         0        0     0          0  
#     2      0       0        0    0     0         0        0     0          0  
#     3      0       0        0    0     0         0        0     0          0  
#     4      0       0        0    0     0         0        0     0          0  
    
#     [5 rows x 5111 columns]
#        000  00am  0600        10  100  107   11  110  1100   12    ...      \
#     0  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
#     1  0.0   0.0   0.0  0.105636  0.0  0.0  0.0  0.0   0.0  0.0    ...       
#     2  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
#     3  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
#     4  0.0   0.0   0.0  0.000000  0.0  0.0  0.0  0.0   0.0  0.0    ...       
    
#         younger  youth  youths  youtube  ypg  yuan  zawahiri  zeitung      zero  \
#     0  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.033579   
#     1  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
#     2  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
#     3  0.015175    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
#     4  0.000000    0.0     0.0      0.0  0.0   0.0       0.0      0.0  0.000000   
    
#        zerohedge  
#     0        0.0  
#     1        0.0  
#     2        0.0  
#     3        0.0  
#     4        0.0  
    
#     [5 rows x 5111 columns]
#     set()
#     False