# # 7/15/2020
# Although some candy attributes, such as chocolate, may be extremely popular, it doesn't mean they will be important to model prediction. After a random forest model has been fit, you can review the model's attribute, .feature_importances_, to see which variables had the biggest impact. You can check how important each variable was in the model by looping over the feature importance array using enumerate().

# If you are unfamiliar with Python's enumerate() function, it can loop over a list while also creating an automatic counter.

# Fit the model using X and y
rfr.fit(X_train, y_train)

# Print how important each column is to the model
for i, item in enumerate(rfr.feature_importances_):
      # Use i and item to print out the feature importance of each column
    print("{0:s}: {1:.2f}".format(X_train.columns[i], item))

# <script.py> output:
#     chocolate: 0.44
#     fruity: 0.03
#     caramel: 0.02
#     peanutyalmondy: 0.05
#     nougat: 0.01
#     crispedricewafer: 0.03
#     hard: 0.01
#     bar: 0.02
#     pluribus: 0.02
#     sugarpercent: 0.17
#     pricepercent: 0.19
