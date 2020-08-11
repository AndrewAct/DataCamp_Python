# # 8/10/2020
# Now that you've defined a new model, fit it to the regular season basketball data.

# Use the model you fit in the previous exercise (which was trained on the regular season data) and evaluate the model on data for tournament games (games_tourney).

# Fit the model to the games_season dataset
model.fit([games_season['team_1'], games_season['team_2'], games_season['home']],
          games_season['score_diff'],
          epochs=1,
          verbose=True,
          validation_split=.10,
          batch_size=2048)

# Evaluate the model on the games_tourney dataset
print(model.evaluate([games_tourney['team_1'], games_tourney['team_2'], games_tourney['home']],
               games_tourney['score_diff'], verbose=False))

# <script.py> output:
#     Train on 280960 samples, validate on 31218 samples
#     Epoch 1/1
    
#       2048/280960 [..............................] - ETA: 15s - loss: 12.0596
#      34816/280960 [==>...........................] - ETA: 1s - loss: 11.9955 
#      67584/280960 [======>.......................] - ETA: 0s - loss: 12.0207
#      98304/280960 [=========>....................] - ETA: 0s - loss: 11.9921
#     133120/280960 [=============>................] - ETA: 0s - loss: 12.0237
#     167936/280960 [================>.............] - ETA: 0s - loss: 12.0119
#     200704/280960 [====================>.........] - ETA: 0s - loss: 12.0228
#     231424/280960 [=======================>......] - ETA: 0s - loss: 12.0196
#     264192/280960 [===========================>..] - ETA: 0s - loss: 12.0036
#     280960/280960 [==============================] - 1s 2us/step - loss: 12.0003 - val_loss: 12.3391
#     11.683796237086034
