# 5/11/2020
# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na= False)

# Check the data type of 'frisk'
print(ri.frisk.dtype)

# Take the sum of 'frisk'
print(ri.frisk.sum())

# <script.py> output:
#     Incident to Arrest                                          1290
#     Probable Cause                                               924
#     Inventory                                                    219
#     Reasonable Suspicion                                         214
#     Protective Frisk                                             164
#     Incident to Arrest,Inventory                                 123
#     Incident to Arrest,Probable Cause                            100
#     Probable Cause,Reasonable Suspicion                           54
#     Incident to Arrest,Inventory,Probable Cause                   35
#     Probable Cause,Protective Frisk                               35
#     Incident to Arrest,Protective Frisk                           33
#     Inventory,Probable Cause                                      25
#     Protective Frisk,Reasonable Suspicion                         19
#     Incident to Arrest,Inventory,Protective Frisk                 18
#     Incident to Arrest,Probable Cause,Protective Frisk            13
#     Inventory,Protective Frisk                                    12
#     Incident to Arrest,Reasonable Suspicion                        8
#     Probable Cause,Protective Frisk,Reasonable Suspicion           5
#     Incident to Arrest,Probable Cause,Reasonable Suspicion         5
#     Incident to Arrest,Inventory,Reasonable Suspicion              4
#     Inventory,Reasonable Suspicion                                 2
#     Incident to Arrest,Protective Frisk,Reasonable Suspicion       2
#     Inventory,Protective Frisk,Reasonable Suspicion                1
#     Inventory,Probable Cause,Protective Frisk                      1
#     Inventory,Probable Cause,Reasonable Suspicion                  1
#     Name: search_type, dtype: int64
#     bool
#     303
