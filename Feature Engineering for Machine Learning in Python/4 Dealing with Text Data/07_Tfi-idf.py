# # 7/12/2020
# While counts of occurrences of words can be useful to build models, words that occur many times may skew the results undesirably. To limit these common words from overpowering your model a form of normalization can be used. In this lesson you will be using Term frequency-inverse document frequency (Tf-idf) as was discussed in the video. Tf-idf has the effect of reducing the value of common words, while increasing the weight of words that do not occur in many documents.

# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Instantiate TfidfVectorizer
tv = TfidfVectorizer(max_features = 100, stop_words = 'english')

# Fit the vectroizer and transform the data
tv_transformed = tv.fit_transform(speech_df['text_clean'])

# Create a DataFrame with these features
tv_df = pd.DataFrame(tv_transformed.toarray(), 
                     columns=tv.get_feature_names()).add_prefix('TFIDF_')
print(tv_df.head())

# <script.py> output:
#        TFIDF_action  TFIDF_administration  TFIDF_america  TFIDF_american  TFIDF_americans  ...  TFIDF_war  TFIDF_way  TFIDF_work  TFIDF_world  TFIDF_years
#     0      0.000000              0.133415       0.000000        0.105388              0.0  ...   0.000000   0.060755    0.000000     0.045929     0.052694
#     1      0.000000              0.261016       0.266097        0.000000              0.0  ...   0.000000   0.000000    0.000000     0.000000     0.000000
#     2      0.000000              0.092436       0.157058        0.073018              0.0  ...   0.024339   0.000000    0.000000     0.063643     0.073018
#     3      0.000000              0.092693       0.000000        0.000000              0.0  ...   0.036610   0.000000    0.039277     0.095729     0.000000
#     4      0.041334              0.039761       0.000000        0.031408              0.0  ...   0.094225   0.000000    0.000000     0.054752     0.062817
    
#     [5 rows x 100 columns]
