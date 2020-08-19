# # 8/18/2020
# You will work with another Kaggle competition called "Store Item Demand Forecasting Challenge". In this competition, you are given 5 years of store-item sales data, and asked to predict 3 months of sales for 50 different items in 10 different stores.

# To begin, let's explore the train data for this competition. For the faster performance, you will work with a subset of the train data containing only a single month history.

# Your initial goal is to read the input data and take the first look at it.

# Import pandas
import pandas as pd

# Read train data
train = pd.read_csv('train.csv')

# Look at the shape of the data
print('Train shape:', train.shape)

# Look at the head() of the data
print(train.head())

# <script.py> output:
#     Train shape: (15500, 5)
#            id        date  store  item  sales
#     0  100000  2017-12-01      1     1     19
#     1  100001  2017-12-02      1     1     16
#     2  100002  2017-12-03      1     1     31
#     3  100003  2017-12-04      1     1      7
#     4  100004  2017-12-05      1     1     20