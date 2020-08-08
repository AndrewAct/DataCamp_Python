# # 8/7/2020
# Now that you know how to monitor your model performance throughout optimization, you can use early stopping to stop optimization when it isn't helping any more. Since the optimization stops automatically when it isn't helping, you can also set a high value for epochs in your call to .fit(), as Dan showed in the video.

# The model you'll optimize has been specified as model. As before, the data is pre-loaded as predictors and target.

# Import EarlyStopping from keras.callbacks.
# Compile the model, once again using 'adam' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] to see the accuracy at each epoch.
# Create an EarlyStopping object called early_stopping_monitor. Stop optimization when the validation loss hasn't improved for 2 epochs by specifying the patience parameter of EarlyStopping() to be 2.
# Fit the model using the predictors and target. Specify the number of epochs to be 30 and use a validation split of 0.3. In addition, pass [early_stopping_monitor] to the callbacks parameter.


# Import EarlyStopping
from keras.callbacks import EarlyStopping

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience = 2)

# Fit the model
model.fit(predictors, target, validation_split = 0.3, epochs = 30, callbacks= [early_stopping_monitor])


# <script.py> output:
#     Train on 623 samples, validate on 268 samples
#     Epoch 1/30
    
#  32/623 [>.............................] - ETA: 1s - loss: 5.6563 - acc: 0.4688
# 623/623 [==============================] - 0s - loss: 1.6477 - acc: 0.5650 - val_loss: 1.0903 - val_acc: 0.6604
#     Epoch 2/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 1.8477 - acc: 0.4688
# 623/623 [==============================] - 0s - loss: 0.8318 - acc: 0.6083 - val_loss: 0.5606 - val_acc: 0.7351
#     Epoch 3/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.8343 - acc: 0.6250
# 623/623 [==============================] - 0s - loss: 0.7657 - acc: 0.6244 - val_loss: 0.6429 - val_acc: 0.7201
#     Epoch 4/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 1.4017 - acc: 0.5312
# 623/623 [==============================] - 0s - loss: 0.7340 - acc: 0.6260 - val_loss: 0.5441 - val_acc: 0.7351
#     Epoch 5/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.5749 - acc: 0.7500
# 623/623 [==============================] - 0s - loss: 0.6598 - acc: 0.6581 - val_loss: 0.6068 - val_acc: 0.6903
#     Epoch 6/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.4400 - acc: 0.8438
# 623/623 [==============================] - 0s - loss: 0.6076 - acc: 0.7063 - val_loss: 0.5896 - val_acc: 0.6940
#     Epoch 7/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.6495 - acc: 0.6562
# 623/623 [==============================] - 0s - loss: 0.6363 - acc: 0.7014 - val_loss: 0.7011 - val_acc: 0.6493
