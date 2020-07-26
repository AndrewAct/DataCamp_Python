# # # 7/24/2020
# # It's time to begin building your text classifier! The data has been loaded into a DataFrame called df. Explore it in the IPython Shell to investigate what columns you can use. The .head() method is particularly informative.

# # In this exercise, you'll use pandas alongside scikit-learn to create a sparse text vectorizer you can use to train and test a simple supervised model. To begin, you'll set up a CountVectorizer and investigate some of its features.
# It's time to begin building your text classifier! The data has been loaded into a DataFrame called df. Explore it in the IPython Shell to investigate what columns you can use. The .head() method is particularly informative.

# In this exercise, you'll use pandas alongside scikit-learn to create a sparse text vectorizer you can use to train and test a simple supervised model. To begin, you'll set up a CountVectorizer and investigate some of its features.

# Import the necessary modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Print the head of df
print(df.head())

# Create a series to store the labels: y
y = df.label

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df["text"], y, test_size = 0.33, random_state = 53)

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words = "english")

# Transform the training data using only the 'text' column values: count_train 
count_train = count_vectorizer.fit_transform(X_train)

# Transform the test data using only the 'text' column values: count_test 
count_test = count_vectorizer.transform(X_test)

# Print the first 10 features of the count_vectorizer
print(count_vectorizer.get_feature_names()[:10])


# <script.py> output:
#        Unnamed: 0                                              title  \
#     0        8476                       You Can Smell Hillary’s Fear   
#     1       10294  Watch The Exact Moment Paul Ryan Committed Pol...   
#     2        3608        Kerry to go to Paris in gesture of sympathy   
#     3       10142  Bernie supporters on Twitter erupt in anger ag...   
#     4         875   The Battle of New York: Why This Primary Matters   
    
#                                                     text label  
#     0  Daniel Greenfield, a Shillman Journalism Fello...  FAKE  
#     1  Google Pinterest Digg Linkedin Reddit Stumbleu...  FAKE  
#     2  U.S. Secretary of State John F. Kerry said Mon...  REAL  
#     3  — Kaydee King (@KaydeeKing) November 9, 2016 T...  FAKE  
#     4  It's primary day in New York and front-runners...  REAL  
#     ['00', '000', '0000', '00000031', '000035', '00006', '0001', '0001pt', '000ft', '000km']
