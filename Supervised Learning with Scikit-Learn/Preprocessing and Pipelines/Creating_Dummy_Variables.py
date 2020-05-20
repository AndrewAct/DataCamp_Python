# 5/19/2020
# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df, drop_first= True)

# Print the new columns of df_region
print(df_region.columns)

# <script.py> output:
#     Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
#            'BMI_female', 'life', 'child_mortality', 'Region_America',
#            'Region_East Asia & Pacific', 'Region_Europe & Central Asia',
#            'Region_Middle East & North Africa', 'Region_South Asia',
#            'Region_Sub-Saharan Africa'],
#           dtype='object')
#     Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
#            'BMI_female', 'life', 'child_mortality', 'Region_East Asia & Pacific',
#            'Region_Europe & Central Asia', 'Region_Middle East & North Africa',
#            'Region_South Asia', 'Region_Sub-Saharan Africa'],
#           dtype='object')

