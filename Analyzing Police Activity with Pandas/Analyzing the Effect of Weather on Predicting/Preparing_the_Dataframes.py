# 5/11/2020
# Reset the index of 'ri'
ri.reset_index(inplace= True)

# Examine the head of 'ri'
print(ri.head())

# Create a DataFrame from the 'DATE' and 'rating' columns
weather_rating = weather[['DATE', 'rating']]

# Examine the head of 'weather_rating'
print(weather_rating.head())

# script.py> output:
#             stop_datetime   stop_date stop_time driver_gender driver_race  \
#     0 2005-01-04 12:55:00  2005-01-04     12:55             M       White   
#     1 2005-01-23 23:15:00  2005-01-23     23:15             M       White   
#     2 2005-02-17 04:15:00  2005-02-17     04:15             M       White   
#     3 2005-02-20 17:15:00  2005-02-20     17:15             M       White   
#     4 2005-02-24 01:20:00  2005-02-24     01:20             F       White   
    
#                         violation_raw  violation  search_conducted search_type  \
#     0  Equipment/Inspection Violation  Equipment             False         NaN   
#     1                        Speeding   Speeding             False         NaN   
#     2                        Speeding   Speeding             False         NaN   
#     3                Call for Service      Other             False         NaN   
#     4                        Speeding   Speeding             False         NaN   
    
#         stop_outcome  is_arrested stop_duration  drugs_related_stop district  \
#     0       Citation        False      0-15 Min               False  Zone X4   
#     1       Citation        False      0-15 Min               False  Zone K3   
#     2       Citation        False      0-15 Min               False  Zone X4   
#     3  Arrest Driver         True     16-30 Min               False  Zone X1   
#     4       Citation        False      0-15 Min               False  Zone X3   
    
#        frisk  stop_minutes  
#     0  False             8  
#     1  False             8  
#     2  False             8  
#     3  False            23  
#     4  False             8  
#              DATE rating
#     0  2005-01-01    bad
#     1  2005-01-02    bad
#     2  2005-01-03    bad
#     3  2005-01-04    bad
#     4  2005-01-05    bad