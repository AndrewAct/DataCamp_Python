# 4/17/2020 
# loc is label-based, iloc is integer based 
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
print(temperatures[(temperatures["date"] >= "2010") & (temperatures["date"] < "2012")])

# Set date as an index
temperatures_ind = temperatures.set_index("date")

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])


# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[23,2])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5, :])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
# Don't forget the basic sytax of python 
print(temperatures.iloc[:5, 2:4])


# Add a year column to temperatures
temperatures["year"]= temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country","city"], columns= "year")

# See the result
print(temp_by_country_city_vs_year)


# Exercises 
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt": "India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"): ("India", "Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"): ("India", "Delhi"), 2005: 2010]

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Find the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Find the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])