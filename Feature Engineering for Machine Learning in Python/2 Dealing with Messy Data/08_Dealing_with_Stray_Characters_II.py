# # 7/5/2020
# n the last exercise, you could tell quickly based off of the df.head() call which characters were causing an issue. In many cases this will not be so apparent. There will often be values deep within a column that are preventing you from casting a column as a numeric type so that it can be used in a model or further feature engineering.

# One approach to finding these values is to force the column to the data type desired using pd.to_numeric(), coercing any values causing issues to NaN, Then filtering the DataFrame by just the rows containing the NaN values.

# Try to cast the RawSalary column as a float and it will fail as an additional character can now be found in it. Find the character and remove it so the column can be cast as a float.


# Attempt to convert the column to numeric values
numeric_vals = pd.to_numeric(so_survey_df['RawSalary'], errors='coerce')

# Find the indexes of missing values
idx = numeric_vals.isna()

# Print the relevant rows
print(so_survey_df['RawSalary'][idx])

# <script.py> output:
#     0             NaN
#     2             NaN
#     4       £41671.00
#     6             NaN
#     8             NaN
#     11            NaN
#     13            NaN
#     15      £75000.00
#     16      £10958.00
#     20            NaN
#     22            NaN
#     25            NaN
#     27            NaN
#     28            NaN
#     29            NaN
#     30            NaN
#     34            NaN
#     37            NaN
#     38      £90000.00
#     41            NaN
#     43            NaN
#     44            NaN
#     45            NaN
#     47      £48955.00
#     48            NaN
#     49      £19500.00
#     50            NaN
#     52            NaN
#     53      £36000.00
#     54            NaN
#               ...    
#     925           NaN
#     926           NaN
#     927           NaN
#     929           NaN
#     934           NaN
#     936           NaN
#     937     £63156.00
#     938      £8496.00
#     941           NaN
#     942           NaN
#     944     £75000.00
#     948           NaN
#     949           NaN
#     952           NaN
#     954           NaN
#     955           NaN
#     960           NaN
#     961           NaN
#     962     £80286.00
#     964    £154000.00
#     966           NaN
#     975           NaN
#     976           NaN
#     977           NaN
#     980           NaN
#     989           NaN
#     990           NaN
#     992           NaN
#     994           NaN
#     997           NaN
#     Name: RawSalary, Length: 401, dtype: object

# Replace the offending characters
so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace('£','')

# Convert the column to float
so_survey_df['RawSalary'] = so_survey_df['RawSalary'].astype('float')

# Print the column
print(so_survey_df['RawSalary'])

# <script.py> output:
#     0            NaN
#     1        70841.0
#     2            NaN
#     3        21426.0
#     4        41671.0
#     5       120000.0
#     6            NaN
#     7       250000.0
#     8            NaN
#     9            0.0
#     10       47904.0
#     11           NaN
#     12       95968.0
#     13           NaN
#     14         420.0
#     15       75000.0
#     16       10958.0
#     17       51408.0
#     18       72611.0
#     19      900000.0
#     20           NaN
#     21       30000.0
#     22           NaN
#     23       44000.0
#     24       60000.0
#     25           NaN
#     26       80000.0
#     27           NaN
#     28           NaN
#     29           NaN
#              ...    
#     969      37200.0
#     970      79973.0
#     971      73428.0
#     972      56298.0
#     973      17628.0
#     974     125000.0
#     975          NaN
#     976          NaN
#     977          NaN
#     978      75000.0
#     979       6576.0
#     980          NaN
#     981      60000.0
#     982      80000.0
#     983      90000.0
#     984      70000.0
#     985      39648.0
#     986      99967.0
#     987       2352.0
#     988      50448.0
#     989          NaN
#     990          NaN
#     991      55562.0
#     992          NaN
#     993      30000.0
#     994          NaN
#     995      58746.0
#     996      55000.0
#     997          NaN
#     998    1000000.0
#     Name: RawSalary, Length: 999, dtype: float64