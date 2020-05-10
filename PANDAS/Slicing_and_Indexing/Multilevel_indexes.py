# 4/17/2020 
# Index temperatures by country & city
print(temperatures)
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
# Specify the "Country", "City" format
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

## Erercise
# Sort index
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level = "city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level = ["country", "city"], ascending= [True, False]))

