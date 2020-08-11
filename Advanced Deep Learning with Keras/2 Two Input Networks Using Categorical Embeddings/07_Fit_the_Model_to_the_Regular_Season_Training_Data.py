# # 8/10/2020
# Now that you've defined a complete team strength model, you can fit it to the basketball data! Since your model has two inputs now, you need to pass the input data as a list.

# Get the team_1 column from the regular season data
input_1 = games_season['team_1']

# Get the team_2 column from the regular season data
input_2 = games_season['team_2']

# Fit the model to input 1 and 2, using score diff as a target
model.fit([input_1, input_2],
          games_season['score_diff'],
          epochs=1,
          batch_size=2048,
          validation_split=0.1,
          verbose=True)


# <script.py> output:
#     Train on 280960 samples, validate on 31218 samples
#     Epoch 1/1
    
#       2048/280960 [..............................] - ETA: 21s - loss: 12.0254
#      20480/280960 [=>............................] - ETA: 2s - loss: 12.2582 
#      45056/280960 [===>..........................] - ETA: 1s - loss: 12.2006
#      69632/280960 [======>.......................] - ETA: 0s - loss: 12.1566
#      92160/280960 [========>.....................] - ETA: 0s - loss: 12.1353
#     118784/280960 [===========>..................] - ETA: 0s - loss: 12.1133
#     143360/280960 [==============>...............] - ETA: 0s - loss: 12.1285
#     165888/280960 [================>.............] - ETA: 0s - loss: 12.1347
#     186368/280960 [==================>...........] - ETA: 0s - loss: 12.1323
#     208896/280960 [=====================>........] - ETA: 0s - loss: 12.1267
#     233472/280960 [=======================>......] - ETA: 0s - loss: 12.1248
#     258048/280960 [==========================>...] - ETA: 0s - loss: 12.1243
#     280960/280960 [==============================] - 1s 3us/step - loss: 12.1203 - val_loss: 11.8384