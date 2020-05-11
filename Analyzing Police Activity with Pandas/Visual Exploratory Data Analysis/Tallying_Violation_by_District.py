# 5/11/2020
# Create a frequency table of districts and violations
print(pd.crosstab(ri.district, ri.violation))

# Save the frequency table as 'all_zones'
all_zones = pd.crosstab(ri.district, ri.violation)

# Select rows 'Zone K1' through 'Zone K3'
print(all_zones.loc['Zone K1': 'Zone K3'])

# Save the smaller table as 'k_zones'
k_zones = all_zones.loc['Zone K1': 'Zone K3']

# <script.py> output:
#     violation  Equipment  Moving violation  Other  Registration/plates  Seat belt  \
#     district                                                                        
#     Zone K1          672              1254    290                  120          0   
#     Zone K2         2061              2962    942                  768        481   
#     Zone K3         2302              2898    705                  695        638   
#     Zone X1          296               671    143                   38         74   
#     Zone X3         2049              3086    769                  671        820   
#     Zone X4         3541              5353   1560                 1411        843   
    
#     violation  Speeding  
#     district             
#     Zone K1        5960  
#     Zone K2       10448  
#     Zone K3       12322  
#     Zone X1        1119  
#     Zone X3        8779  
#     Zone X4        9795  
#     violation  Equipment  Moving violation  Other  Registration/plates  Seat belt  \
#     district                                                                        
#     Zone K1          672              1254    290                  120          0   
#     Zone K2         2061              2962    942                  768        481   
#     Zone K3         2302              2898    705                  695        638   
    
#     violation  Speeding  
#     district             
#     Zone K1        5960  
#     Zone K2       10448  
#     Zone K3       12322