# # 6/18/2020
# You'll let PCA determine the number of components to calculate based on an explained variance threshold that you decide.

# You'll work on the numeric ANSUR female dataset pre-loaded as ansur_df.

# All relevant packages and classes have been pre-loaded too (Pipeline(), StandardScaler(), PCA()).
# Pipe a scaler to PCA selecting 80% of the variance
pipe = Pipeline([('scaler', StandardScaler()),
        		 ('reducer', PCA(n_components=0.8))])

# Fit the pipe to the data
pipe.fit(ansur_df)

print('{} components selected'.format(len(pipe.steps[1][1].components_)))

# <script.py> output:
#     11 components selected

# Let PCA select 90% of the variance
pipe = Pipeline([('scaler', StandardScaler()),
        		 ('reducer', PCA(n_components= 0.9))])

# Fit the pipe to the data
pipe.fit(ansur_df)

print('{} components selected'.format(len(pipe.steps[1][1].components_)))

# <script.py> output:
#     23 components selected