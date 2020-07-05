# # 6/27/2020
# In this exercise, you'll use the iris dataset (representing petal characteristics of a number of flowers) to practice using the scikit-learn API to fit a classification model. You can see a sample plot of the data to the right.

# Print the first 5 rows for inspection
print(data.head())

# <script.py> output:
#         sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \
#     50                7.0               3.2                4.7               1.4   
#     51                6.4               3.2                4.5               1.5   
#     52                6.9               3.1                4.9               1.5   
#     53                5.5               2.3                4.0               1.3   
#     54                6.5               2.8                4.6               1.5   
    
#         target  
#     50       1  
#     51       1  
#     52       1  
#     53       1  
#     54       1

from sklearn.svm import LinearSVC

# Construct data for the model
X = data[["petal length (cm)", "petal width (cm)"]]
y = data[['target']]

# Fit the model
model = LinearSVC()
model.fit(X, y)