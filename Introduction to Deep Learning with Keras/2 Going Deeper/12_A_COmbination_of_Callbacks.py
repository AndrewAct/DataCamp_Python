# # 8/9/2020
# Deep learning models can take a long time to train, especially when you move to deeper architectures and bigger datasets. Saving your model every time it improves as well as stopping it when it no longer does allows you to worry less about choosing the number of epochs to train for. You can also restore a saved model anytime and resume training where you left it.

# The model training and validation data are available in your workspace as X_train, X_test, y_train, and y_test.

# Use the EarlyStopping() and the ModelCheckpoint() callbacks so that you can go eat a jar of cookies while you leave your computer to work!

# Import the EarlyStopping and ModelCheckpoint callbacks
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Early stop on validation accuracy
monitor_val_acc = EarlyStopping(monitor = 'val_acc', patience = 3)

# Save the best model as best_banknote_model.hdf5
modelCheckpoint = ModelCheckpoint('best_banknote_model.hdf5', save_best_only = True)

# Fit your model for a stupid amount of epochs
h_callback = model.fit(X_train, y_train,
                    epochs = 1000000000000,
                    callbacks = [monitor_val_acc, modelCheckpoint],
                    validation_data = (X_test, y_test))



# <script.py> output:
#     Train on 960 samples, validate on 412 samples
#     Epoch 1/1000000000000
    
#      32/960 [>.............................] - ETA: 1s - loss: 0.3227 - acc: 0.8438
#     960/960 [==============================] - 0s 125us/step - loss: 0.2829 - acc: 0.9250 - val_loss: 0.3030 - val_acc: 0.9126
#     Epoch 2/1000000000000
    
#      32/960 [>.............................] - ETA: 0s - loss: 0.2523 - acc: 0.9688
#     960/960 [==============================] - 0s 53us/step - loss: 0.2776 - acc: 0.9271 - val_loss: 0.2973 - val_acc: 0.9126
#     Epoch 3/1000000000000
    
#      32/960 [>.............................] - ETA: 0s - loss: 0.2336 - acc: 0.9688
#     960/960 [==============================] - 0s 53us/step - loss: 0.2726 - acc: 0.9292 - val_loss: 0.2920 - val_acc: 0.9126
#     Epoch 4/1000000000000
    
#      32/960 [>.............................] - ETA: 0s - loss: 0.2699 - acc: 0.9688
#     960/960 [==============================] - 0s 53us/step - loss: 0.2679 - acc: 0.9312 - val_loss: 0.2870 - val_acc: 0.9126