# # 7/25/2020
# Your job in this exercise is to test a few different alpha levels using the Tfidf vectors to determine if there is a better performing combination.

# The training and test sets have been created, and tfidf_vectorizer, tfidf_train, and tfidf_test have been computed.

# Create the list of alphas: alphas
alphas = np.arange(0, 1, 0.1)

# Define train_and_predict()
def train_and_predict(alpha):
    # Instantiate the classifier: nb_classifier
    nb_classifier = MultinomialNB(alpha = alpha)
    # Fit to the training data
    nb_classifier.fit(tfidf_train, y_train)
    # Predict the labels: pred
    pred = nb_classifier.predict(tfidf_test)
    # Compute accuracy: score
    score = metrics.accuracy_score(y_test, pred)
    return score

# Iterate over the alphas and print the corresponding score
for alpha in alphas:
    print('Alpha: ', alpha)
    print('Score: ', train_and_predict(alpha))
    print()

# <script.py> output:
#     Alpha:  0.0
#     Score:  0.8813964610234337
    
#     Alpha:  0.1
#     Score:  0.8976566236250598
    
#     Alpha:  0.2
#     Score:  0.8938307030129125
    
#     Alpha:  0.30000000000000004
#     Score:  0.8900047824007652
    
#     Alpha:  0.4
#     Score:  0.8857006217120995
    
#     Alpha:  0.5
#     Score:  0.8842659014825442
    
#     Alpha:  0.6000000000000001
#     Score:  0.874701099952176
    
#     Alpha:  0.7000000000000001
#     Score:  0.8703969392635102
    
#     Alpha:  0.8
#     Score:  0.8660927785748446
    
#     Alpha:  0.9
#     Score:  0.8589191774270684