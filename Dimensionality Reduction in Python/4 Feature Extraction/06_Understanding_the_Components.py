# # 6/17/2020
# You'll apply PCA to the numeric features of the Pokemon dataset, poke_df, using a pipeline to combine the feature scaling and PCA in one go. You'll then interpret the meanings of the first two components.

# All relevant packages and classes have been pre-loaded for you (Pipeline(), StandardScaler(), PCA()).

# Build the pipeline
pipe = Pipeline([('scaler', StandardScaler()),
        		 ('reducer', PCA(n_components=2))])

# Fit it to the dataset and extract the component vectors
pipe.fit(poke_df)
vectors = pipe.steps[1][1].components_.round(2)

# Print feature effects
print('PC 1 effects = ' + str(dict(zip(poke_df.columns, vectors[0]))))
print('PC 2 effects = ' + str(dict(zip(poke_df.columns, vectors[1]))))

# <script.py> output:
#     PC 1 effects = {'Attack': 0.44, 'HP': 0.39, 'Sp. Atk': 0.46, 'Defense': 0.36, 'Speed': 0.34, 'Sp. Def': 0.45}
#     PC 2 effects = {'Attack': -0.01, 'HP': 0.08, 'Sp. Atk': -0.31, 'Defense': 0.63, 'Speed': -0.67, 'Sp. Def': 0.24}
