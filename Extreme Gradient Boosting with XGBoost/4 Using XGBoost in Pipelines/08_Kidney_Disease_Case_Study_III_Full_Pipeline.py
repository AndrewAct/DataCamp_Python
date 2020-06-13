# # 6/12/2020
# It's time to piece together all of the transforms along with an XGBClassifier to build the full pipeline!

# Besides the numeric_categorical_union that you created in the previous exercise, there are two other transforms needed: the Dictifier() transform which we created for you, and the DictVectorizer().

# After creating the pipeline, your task is to cross-validate it to see how well it performs.

# Create full pipeline
pipeline = Pipeline([
                     ("featureunion", numeric_categorical_union),
                     ("dictifier", Dictifier()),
                     ("vectorizer", DictVectorizer(sort = False)),
                     ("clf", xgb.XGBClassifier(max_depth= 3))
                    ])

# Perform cross-validation
cross_val_scores = cross_val_score(pipeline, kidney_data, y, scoring ="roc_auc", cv = 3)

# Print avg. AUC
print("3-fold AUC: ", np.mean(cross_val_scores))

# <script.py> output:
#     3-fold AUC:  0.998637406769937
