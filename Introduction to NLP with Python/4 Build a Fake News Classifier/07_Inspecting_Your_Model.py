# # 7/25/2020
# Now that you have built a "fake news" classifier, you'll investigate what it has learned. You can map the important vector weights back to actual words using some simple inspection techniques.

# You have your well performing tfidf Naive Bayes classifier available as nb_classifier, and the vectors as tfidf_vectorizer.

# Get the class labels: class_labels
class_labels = nb_classifier.classes_

# Extract the features: feature_names
feature_names = tfidf_vectorizer.get_feature_names()

# Zip the feature names together with the coefficient array and sort by weights: feat_with_weights
feat_with_weights = sorted(zip(nb_classifier.coef_[0], feature_names))

# Print the first class label and the top 20 feat_with_weights entries
print(class_labels[0], feat_with_weights[:20])

# Print the second class label and the bottom 20 feat_with_weights entries
print(class_labels[1], feat_with_weights[-20:])

# <script.py> output:
#     FAKE [(-12.641778440826338, '0000'), (-12.641778440826338, '000035'), (-12.641778440826338, '0001'), (-12.641778440826338, '0001pt'), (-12.641778440826338, '000km'), (-12.641778440826338, '0011'), (-12.641778440826338, '006s'), (-12.641778440826338, '007'), (-12.641778440826338, '007s'), (-12.641778440826338, '008s'), (-12.641778440826338, '0099'), (-12.641778440826338, '00am'), (-12.641778440826338, '00p'), (-12.641778440826338, '00pm'), (-12.641778440826338, '014'), (-12.641778440826338, '015'), (-12.641778440826338, '018'), (-12.641778440826338, '01am'), (-12.641778440826338, '020'), (-12.641778440826338, '023')]
#     REAL [(-6.790929954967984, 'states'), (-6.765360557845786, 'rubio'), (-6.751044290367751, 'voters'), (-6.701050756752027, 'house'), (-6.695547793099875, 'republicans'), (-6.6701912490429685, 'bush'), (-6.661945235816139, 'percent'), (-6.589623788689862, 'people'), (-6.559670340096453, 'new'), (-6.489892292073901, 'party'), (-6.452319082422527, 'cruz'), (-6.452076515575875, 'state'), (-6.397696648238072, 'republican'), (-6.376343060363355, 'campaign'), (-6.324397735392007, 'president'), (-6.2546017970213645, 'sanders'), (-6.144621899738043, 'obama'), (-5.756817248152807, 'clinton'), (-5.596085785733112, 'said'), (-5.357523914504495, 'trump')]
