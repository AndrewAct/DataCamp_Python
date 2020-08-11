# # 8/11/2020
# Now that you have a model with 2 outputs, compile it with 2 loss functions: mean absolute error (MAE) for 'score_diff' and binary cross-entropy (also known as logloss) for 'won'. Then fit the model with 'seed_diff' and 'pred' as inputs. For outputs, predict 'score_diff' and 'won'.

# This model can use the scores of the games to make sure that close games (small score diff) have lower win probabilities than blowouts (large score diff).

# The regression problem is easier than the classification problem because MAE punishes the model less for a loss due to random chance. For example, if score_diff is -1 and won is 0, that means team_1 had some bad luck and lost by a single free throw. The data for the easy problem helps the model find a solution to the hard problem.

# Import the Adam optimizer
from keras.optimizers import Adam

# Compile the model with 2 losses and the Adam optimzer with a higher learning rate
model.compile(loss=['mean_absolute_error', 'binary_crossentropy'], optimizer=Adam(lr = 0.01))

# Fit the model to the tournament training data, with 2 inputs and 2 outputs
model.fit(games_tourney_train[['seed_diff', 'pred']],
          [games_tourney_train[['score_diff']], games_tourney_train[['won']]],
          epochs=10,
          verbose=True,
          batch_size=16384)



# <script.py> output:
#     Epoch 1/10
    
#     3430/3430 [==============================] - 0s 55us/step - loss: 9.5718 - dense_1_loss: 8.9779 - dense_2_loss: 0.5939
#     Epoch 2/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.5437 - dense_1_loss: 8.9614 - dense_2_loss: 0.5823
#     Epoch 3/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.5200 - dense_1_loss: 8.9480 - dense_2_loss: 0.5720
#     Epoch 4/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.5004 - dense_1_loss: 8.9374 - dense_2_loss: 0.5630
#     Epoch 5/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.4845 - dense_1_loss: 8.9291 - dense_2_loss: 0.5553
#     Epoch 6/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.4731 - dense_1_loss: 8.9240 - dense_2_loss: 0.5491
#     Epoch 7/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.4659 - dense_1_loss: 8.9216 - dense_2_loss: 0.5443
#     Epoch 8/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.4615 - dense_1_loss: 8.9208 - dense_2_loss: 0.5408
#     Epoch 9/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.4585 - dense_1_loss: 8.9200 - dense_2_loss: 0.5385
#     Epoch 10/10
    
#     3430/3430 [==============================] - 0s 2us/step - loss: 9.4561 - dense_1_loss: 8.9189 - dense_2_loss: 0.5372
