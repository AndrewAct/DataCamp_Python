# # 6/16/2020
# You want to compare prices for specific products between stores. The features in the pre-loaded dataset sales_df are: storeID, product, quantity and revenue. The quantity and revenue features tell you how many items of a particular product were sold in a store and what the total revenue was. For the purpose of your analysis it's more interesting to know the average price per product.

# Calculate the price from the quantity sold and revenue
sales_df['price'] = sales_df['revenue'] / sales_df['quantity']

# Drop the quantity and revenue features
reduced_df = sales_df.drop(['quantity', 'revenue'], axis=1)

print(reduced_df.head())

# <script.py> output:
#       storeID  product     price
#     0       A   Apples  5.135616
#     1       A  Bananas  3.365105
#     2       A  Oranges  5.317020
#     3       B   Apples  5.143417
#     4       B  Bananas  3.898517