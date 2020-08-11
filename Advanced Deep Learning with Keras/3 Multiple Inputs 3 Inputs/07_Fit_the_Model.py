# # 8/11/2020
# Now that you've enriched the tournament dataset and built a model to make use of the new data, fit that model to the tournament data.

# Note that this model has only one input layer that is capable of handling all 3 inputs, so it's inputs and outputs do not need to be a list.

# Tournament games are split into a training set and a test set. The tournament games before 2010 are in the training set, and the ones after 2010 are in the test set.

# Fit the model
model.fit(games_tourney_train[['home', 'seed_diff', 'pred']],
          games_tourney_train['score_diff'],
          epochs=1,
          verbose=True)

# <script.py> output:
#     Epoch 1/1
    
#       32/3168 [..............................] - ETA: 13s - loss: 21.2439
#      832/3168 [======>.......................] - ETA: 0s - loss: 18.4599 
#     1664/3168 [==============>...............] - ETA: 0s - loss: 18.2767
#     2496/3168 [======================>.......] - ETA: 0s - loss: 17.9993
#     3168/3168 [==============================] - 0s 105us/step - loss: 17.8147