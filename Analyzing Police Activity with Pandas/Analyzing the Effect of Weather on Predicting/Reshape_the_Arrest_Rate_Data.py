# 5/11/2020
# Unstack the 'arrest_rate' Series into a DataFrame
print(arrest_rate.unstack())

# Create the same DataFrame using a pivot table
print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))

# <script.py> output:
#     rating                   good       bad     worse
#     violation                                        
#     Equipment            0.059007  0.066311  0.097357
#     Moving violation     0.056227  0.058050  0.065860
#     Other                0.076966  0.087443  0.062893
#     Registration/plates  0.081574  0.098160  0.115625
#     Seat belt            0.028587  0.022493  0.000000
#     Speeding             0.013405  0.013314  0.016886
#     rating                   good       bad     worse
#     violation                                        
#     Equipment            0.059007  0.066311  0.097357
#     Moving violation     0.056227  0.058050  0.065860
#     Other                0.076966  0.087443  0.062893
#     Registration/plates  0.081574  0.098160  0.115625
#     Seat belt            0.028587  0.022493  0.000000
#     Speeding             0.013405  0.013314  0.016886
