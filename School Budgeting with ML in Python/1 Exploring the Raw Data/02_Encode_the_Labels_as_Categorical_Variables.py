# # 5/24/2020
# Remember, your ultimate goal is to predict the probability that a certain label is attached to a budget line item. 
# You just saw that many columns in your data are the inefficient object type. 
# Does this include the labels you're trying to predict? Let's find out!

# There are 9 columns of labels in the dataset. 
# Each of these columns is a category that has many possible values it can take. The 9 labels have been loaded into a list called LABELS. In the Shell, check out the type for these labels using df[LABELS].dtypes.

# You will notice that every label is encoded as an object datatype. 
# Because category datatypes are much more efficient your task is to convert the labels to category types using the .astype() method.

# Note: .astype() only works on a pandas Series. 
# Since you are working with a pandas DataFrame, you'll need to use the .apply() method and provide a lambda function called categorize_label that applies .astype() to each column, x.
# Define the lambda function: categorize_label
categorize_label = lambda x: x.astype('category')

# Convert df[LABELS] to a categorical type
df[LABELS] = df[LABELS].apply(categorize_label, axis = 0)

# Print the converted dtypes
print(df[LABELS].dtypes)

# <script.py> output:
#     Function            category
#     Use                 category
#     Sharing             category
#     Reporting           category
#     Student_Type        category
#     Position_Type       category
#     Object_Type         category
#     Pre_K               category
#     Operating_Status    category
#     dtype: object

