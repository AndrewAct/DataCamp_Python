# 5/11/2020
# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())

# <script.py> output:
#     driver_gender  violation          
#     F              Equipment              0.039984
#                    Moving violation       0.039257
#                    Other                  0.041018
#                    Registration/plates    0.054924
#                    Seat belt              0.017301
#                    Speeding               0.008309
#     M              Equipment              0.071496
#                    Moving violation       0.061524
#                    Other                  0.046191
#                    Registration/plates    0.108802
#                    Seat belt              0.035119
#                    Speeding               0.027885
#     Name: search_conducted, dtype: float64

# Reverse the ordering to group by violation before gender
print(ri.groupby(['violation', 'driver_gender']).search_conducted.mean())

# <script.py> output:
#     violation            driver_gender
#     Equipment            F                0.039984
#                          M                0.071496
#     Moving violation     F                0.039257
#                          M                0.061524
#     Other                F                0.041018
#                          M                0.046191
#     Registration/plates  F                0.054924
#                          M                0.108802
#     Seat belt            F                0.017301
#                          M                0.035119
#     Speeding             F                0.008309
#                          M                0.027885
#     Name: search_conducted, dtype: float64
