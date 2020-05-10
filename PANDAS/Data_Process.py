# Data Process
# With virtual file 

import time 
import re 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
# warnings.filterwarnings("ignore")


df = pd.read_csv('/Users/chenzhuo/Desktop/data_file.csv')

# Evaluate time series 
x = time.strftime('%Y-%m-%d: %M:%S', time.localtime(1347617370))

print(x)

# Print the output of df.head()
print(df.head())