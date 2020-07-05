# # 7/5/2020
# For many continuous values you will care less about the exact value of a numeric column, but instead care about the bucket it falls into. This can be useful when plotting values, or simplifying your machine learning models. It is mostly used on continuous variables where accuracy is not the biggest concern e.g. age, height, wages.

# Bins are created using pd.cut(df['column_name'], bins) where bins can be an integer specifying the number of evenly spaced bins, or a list of bin boundaries.

# Bin the continuous variable ConvertedSalary into 5 bins
so_survey_df['equal_binned'] = pd.cut(so_survey_df['ConvertedSalary'], 5)

# Print the first 5 rows of the equal_binned column
print(so_survey_df[['equal_binned', 'ConvertedSalary']].head())

# <script.py> output:
#               equal_binned  ConvertedSalary
#     0  (-2000.0, 400000.0]              0.0
#     1  (-2000.0, 400000.0]          70841.0
#     2  (-2000.0, 400000.0]              0.0
#     3  (-2000.0, 400000.0]          21426.0
#     4  (-2000.0, 400000.0]          41671.0

# Import numpy
import numpy as np

# Specify the boundaries of the bins
bins = [-np.inf, 10000, 50000, 100000, 150000, np.inf]

# Bin labels
labels = ['Very low', 'Low', 'Medium', 'High', 'Very high']

# Bin the continuous variable ConvertedSalary using these boundaries
so_survey_df['boundary_binned'] = pd.cut(so_survey_df['ConvertedSalary'], 
                                         bins = [-np.inf, 10000, 50000, 100000, 150000, np.inf], 
                                         labels = ['Very low', 'Low', 'Medium', 'High', 'Very high'])

# Print the first 5 rows of the boundary_binned column
print(so_survey_df[['boundary_binned', 'ConvertedSalary']].head())

# <script.py> output:
#       boundary_binned  ConvertedSalary
#     0        Very low              0.0
#     1          Medium          70841.0
#     2        Very low              0.0
#     3             Low          21426.0
#     4             Low          41671.0
