# # 7/13/2020
# After creating Tf-idf features you will often want to understand what are the most highest scored words for each corpus. This can be achieved by isolating the row you want to examine and then sorting the the scores from high to low.

# The DataFrame from the last exercise (tv_df) is available in your workspace.

# Isolate the row to be examined
sample_row = tv_df.iloc[0]

# Print the top 5 words of the sorted output
print(sample_row.sort_values(ascending=False).head())


# <script.py> output:
#     TFIDF_government    0.367430
#     TFIDF_public        0.333237
#     TFIDF_present       0.315182
#     TFIDF_duty          0.238637
#     TFIDF_citizens      0.229644
#     Name: 0, dtype: float64
