# # 6/28/2020
# Now that you've removed some of the noisier fluctuations in the audio, let's see if this improves your ability to classify.

# audio_rectified_smooth from the previous exercise is available in your workspace.


# Calculate stats
means = np.mean(audio_rectified_smooth, axis=0)
stds = np.std(audio_rectified_smooth, axis=0)
maxs = np.max(audio_rectified_smooth, axis=0)

# Create the X and y arrays
X = np.column_stack([means, stds, maxs])
y = labels.reshape([-1, 1])

# Fit the model and score on testing data
from sklearn.model_selection import cross_val_score
percent_score = cross_val_score(model, X, y, cv=5)
print(np.mean(percent_score))

# <script.py> output:
#     0.716666666667