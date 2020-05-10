# 4/13/2020
# Concatenate dataframes
import pandas as pd

s1 = pd.Series(['red', 'blue', 'yellow'], index = [1, 2, 3])
s2 = pd.Series(['purple', 'green', 'orange'], index = [4, 5, 6])

pd.concat([s1, s2])

