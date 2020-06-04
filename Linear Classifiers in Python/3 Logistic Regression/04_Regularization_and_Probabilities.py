# # 6/3/2020
# In this exercise, you will observe the effects of changing the regularization strength on the predicted probabilities.

# A 2D binary classification dataset is already loaded into the environment as X and y

# Set the regularization strength
model = LogisticRegression(C=0.1)

# Fit and plot
model.fit(X,y)
plot_classifier(X,y,model,proba=True)

# Predict probabilities on training points
prob = model.predict_proba(X)
print("Maximum predicted probability", np.max(prob))

# <script.py> output:
#     Maximum predicted probability 0.8990965659596716
