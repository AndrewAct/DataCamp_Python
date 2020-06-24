# # 6/22/2020
# If you take a look at the volunteer dataset types, you'll see that the column hits is type object. But, if you actually look at the column, you'll see that it consists of integers. Let's convert that column to type int.
# Print the head of the hits column
print(volunteer["hits"].head())

# Convert the hits column to type int
volunteer["hits"] = volunteer["hits"].astype(int)

# Look at the dtypes of the dataset
print(volunteer.dtypes)

# <script.py> output:
#     0    737
#     1     22
#     2     62
#     3     14
#     4     31
#     Name: hits, dtype: object
#     opportunity_id          int64
#     content_id              int64
#     vol_requests            int64
#     event_time              int64
#     title                  object
#     hits                    int64
#     summary                object
#     is_priority            object
#     category_id           float64
#     category_desc          object
#     amsl                  float64
#     amsl_unit             float64
#     org_title              object
#     org_content_id          int64
#     addresses_count         int64
#     locality               object
#     region                 object
#     postalcode            float64
#     primary_loc           float64
#     display_url            object
#     recurrence_type        object
#     hours                   int64
#     created_date           object
#     last_modified_date     object
#     start_date_date        object
#     end_date_date          object
#     status                 object
#     Latitude              float64
#     Longitude             float64
#     Community Board       float64
#     Community Council     float64
#     Census Tract          float64
#     BIN                   float64
#     BBL                   float64
#     NTA                   float64
#     dtype: object
