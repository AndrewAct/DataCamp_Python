# # 8/10/2020
# Now that the model is compiled, you are ready to fit it to some data!

# In this exercise, you'll use a dataset of scores from US College Basketball tournament games. Each row of the dataset has the team ids: team_1 and team_2, as integers. It also has the seed difference between the teams (seeds are assigned by the tournament committee and represent a ranking of how strong the teams are) and the score difference of the game (e.g. if team_1 wins by 5 points, the score difference is 5).

# To fit the model, you provide a matrix of X variables (in this case one column: the seed difference) and a matrix of Y variables (in this case one column: the score difference).

# The games_tourney DataFrame along with the compiled model object is available in your workspace.

# Now fit the model
model.fit(games_tourney_train['seed_diff'], games_tourney_train['score_diff'],
          epochs=1,
          batch_size=128,
          validation_split= 0.1,
          verbose=True)

# <script.py> output:
#     Train on 3087 samples, validate on 343 samples
#     Epoch 1/10
    
#      128/3087 [>.............................] - ETA: 2s - loss: 12.6147
#     3087/3087 [==============================] - 0s 56us/step - loss: 12.6617 - val_loss: 11.8746
#     Epoch 2/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 12.8586
#     3087/3087 [==============================] - 0s 17us/step - loss: 12.5666 - val_loss: 11.7909
#     Epoch 3/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 12.3928
#     3087/3087 [==============================] - 0s 16us/step - loss: 12.4813 - val_loss: 11.7138
#     Epoch 4/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 12.8825
#     3087/3087 [==============================] - 0s 16us/step - loss: 12.4011 - val_loss: 11.6445
#     Epoch 5/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 11.7432
#     3087/3087 [==============================] - 0s 17us/step - loss: 12.3305 - val_loss: 11.5810
#     Epoch 6/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 12.6989
#     3087/3087 [==============================] - 0s 16us/step - loss: 12.2648 - val_loss: 11.5260
#     Epoch 7/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 12.1438
#     3087/3087 [==============================] - 0s 17us/step - loss: 12.2069 - val_loss: 11.4764
#     Epoch 8/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 11.7714
#     3087/3087 [==============================] - 0s 17us/step - loss: 12.1540 - val_loss: 11.4312
#     Epoch 9/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 11.3491
#     3087/3087 [==============================] - 0s 18us/step - loss: 12.1061 - val_loss: 11.3889
#     Epoch 10/10
    
#      128/3087 [>.............................] - ETA: 0s - loss: 11.5629
#     3087/3087 [==============================] - 0s 17us/step - loss: 12.0616 - val_loss: 11.3503

# <script.py> output:
#     Train on 3087 samples, validate on 343 samples
#     Epoch 1/1
    
#      128/3087 [>.............................] - ETA: 3s - loss: 12.6147
#     3087/3087 [==============================] - 0s 64us/step - loss: 12.6617 - val_loss: 11.8746
