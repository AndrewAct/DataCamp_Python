# # 6/27/2020
# In these final exercises of this chapter, you'll explore the two datasets you'll use in this course.

# The first is a collection of heartbeat sounds. Hearts normally have a predictable sound pattern as they beat, but some disorders can cause the heart to beat abnormally. This dataset contains a training set with labels for each type of heartbeat, and a testing set with no labels. You'll use the testing set to validate your models.

# The data is downloaded from Kaggle: https://www.kaggle.com/kinguistics/heartbeat-sounds?select=set_b.csv

# librosa is a python package for audio and sound 
# Python's glob package would retrieve the list of files matching the specified pattern

import librosa as lr
from glob import glob

# List all the wav files in the folder
audio_files = glob(data_dir + '/*.wav')

# Read in the first audio file, create the time array
audio, sfreq = lr.load(audio_files[0])
time = np.arange(0, len(audio)) / sfreq

# sfreq: sampling frequency (?)
# Plot audio over time
fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
plt.show()