# # 5/22/2020
# In the video, you learned when NMF is applied to documents, the components correspond to topics of documents, and the NMF features reconstruct the documents from the topics. 
# Verify this for yourself for the NMF model that you built earlier using the Wikipedia articles. Previously, you saw that the 3rd NMF feature value was high for the articles about actors Anne Hathaway and Denzel Washington. In this exercise, identify the topic of the corresponding NMF component.

# The NMF model you built earlier is available as model, while words is a list of the words that label the columns of the word-frequency array.

# After you are done, take a moment to recognise the topic that the articles about Anne Hathaway and Denzel Washington have in common!
# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns = words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())

# <script.py> output:
#     (6, 13125)
#     film       0.627877
#     award      0.253131
#     starred    0.245284
#     role       0.211451
#     actress    0.186398
#     Name: 3, dtype: float64
