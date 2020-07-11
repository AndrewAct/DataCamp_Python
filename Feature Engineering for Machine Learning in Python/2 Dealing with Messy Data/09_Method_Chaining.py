# # 7/7/2020
# When applying multiple operations on the same column (like in the previous exercises), you made the changes in several steps, assigning the results back in each step. However, when applying multiple successive operations on the same column, you can "chain" these operations together for clarity and ease of management. This can be achieved by calling multiple methods sequentially:

# # Method chaining
# df['column'] = df['column'].method1().method2().method3()

# # Same as 
# df['column'] = df['column'].method1()
# df['column'] = df['column'].method2()
# df['column'] = df['column'].method3()
# In this exercise you will repeat the steps you performed in the last two exercises, but do so using method chaining.

# Use method chaining
so_survey_df['RawSalary'] = so_survey_df['RawSalary']\
                              .str.replace(',', '')\
                              .str.replace('$', '')\
                              .str.replace('£', '')\
                              .astype('float')
 
# Print the RawSalary column
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
