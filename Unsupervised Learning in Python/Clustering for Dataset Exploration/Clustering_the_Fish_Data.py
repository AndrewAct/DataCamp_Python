# 5/21/2020
# Import pandas
import pandas as pd

# Fit the pipeline to samples
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({'labels': labels, 'species': species})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['species'])

# Display ct
print(ct)

# <script.py> output:
#     species  Bream  Pike  Roach  Smelt
#     labels                            
#     0            0     0      0     13
#     1           33     0      1      0
#     2            0    17      0      0
#     3            1     0     19      1
