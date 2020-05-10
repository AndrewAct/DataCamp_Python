# 4/16/2020 
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type", aggfunc = [np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
import numpy as np
mean_sales_by_type_holiday = sales.pivot_table(values = "weekly_sales", index = "type", columns= "is_holiday", aggfunc = np.mean)

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Exercise 
# "margins" would add all values in one row/column
# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value= 0, margins = True))