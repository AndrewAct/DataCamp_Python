# # 8/9/2020
# You will practice building classification models in Keras with the Banknote Authentication dataset.

# Your goal is to distinguish between real and fake dollar bills. In order to do this, the dataset comes with 4 features: variance,skewness,kurtosis and entropy. These features are calculated by applying mathematical operations over the dollar bill images. The labels are found in the dataframe's class column.

# Import seaborn
import seaborn as sns

# Use pairplot and set the hue to be our class column
sns.pairplot(banknotes, hue = "class") 

# Show the plot
plt.show()

# Describe the data
print('Dataset stats: \n', banknotes.describe())

# Count the number of observations per class
print('Observations per class: \n', banknotes["class"].value_counts())

# <script.py> output:
#     Dataset stats: 
#              variance   skewness   curtosis    entropy
#     count  96.000000  96.000000  96.000000  96.000000
#     mean   -0.057791  -0.102829   0.230412   0.081497
#     std     1.044960   1.059236   1.128972   0.975565
#     min    -2.084590  -2.621646  -1.482300  -3.034187
#     25%    -0.839124  -0.916152  -0.415294  -0.262668
#     50%    -0.026748  -0.037559  -0.033603   0.394888
#     75%     0.871034   0.813601   0.978766   0.745212
#     max     1.869239   1.634072   3.759017   1.343345
#     Observations per class: 
#      real    53
#     fake    43
#     Name: class, dtype: int64
