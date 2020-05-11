# 5/11/2020
# Create a DataFrame of stops in which a search was conducted
searched = ri[ri.search_conducted == True]

# Calculate the overall frisk rate by taking the mean of 'frisk'
print(searched.frisk.mean())

# Calculate the frisk rate for each gender
print(searched.groupby('driver_gender').frisk.mean())

# <script.py> output:
#     0.09162382824312065
#     driver_gender
#     F    0.074561
#     M    0.094353
#     Name: frisk, dtype: float64
