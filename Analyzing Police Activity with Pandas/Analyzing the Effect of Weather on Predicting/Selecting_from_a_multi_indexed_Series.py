# 5/11/2020
# Save the output of the groupby operation from the last exercise
arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

# Print the 'arrest_rate' Series
print(arrest_rate)

# Print the arrest rate for moving violations in bad weather
print(arrest_rate.loc['Moving violation', 'bad'])

# Print the arrest rates for speeding violations in all three weather conditions
print(arrest_rate.loc['Speeding'])

# <script.py> output:
#     violation            rating
#     Equipment            good      0.059007
#                          bad       0.066311
#                          worse     0.097357
#     Moving violation     good      0.056227
#                          bad       0.058050
#                          worse     0.065860
#     Other                good      0.076966
#                          bad       0.087443
#                          worse     0.062893
#     Registration/plates  good      0.081574
#                          bad       0.098160
#                          worse     0.115625
#     Seat belt            good      0.028587
#                          bad       0.022493
#                          worse     0.000000
#     Speeding             good      0.013405
#                          bad       0.013314
#                          worse     0.016886
#     Name: is_arrested, dtype: float64
#     0.05804964058049641
#     rating
#     good     0.013405
#     bad      0.013314
#     worse    0.016886
#     Name: is_arrested, dtype: float64
