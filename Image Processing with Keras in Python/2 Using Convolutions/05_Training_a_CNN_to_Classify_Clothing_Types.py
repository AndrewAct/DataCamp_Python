# # 8/19/2020
# Before training a neural network it needs to be compiled with the right cost function, using the right optimizer. During compilation, you can also define metrics that the network calculates and reports in every epoch. Model fitting requires a training data set, together with the training labels to the network.

# The Conv2D model you built in the previous exercise is available in your workspace.

# Compile the model 
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Fit the model on a training set
model.fit(train_data, train_labels, 
          validation_split=0.2, 
          epochs=3, batch_size=10)


# <script.py> output:
#     Train on 40 samples, validate on 10 samples
#     Epoch 1/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 1.1084 - acc: 0.3000
#     40/40 [==============================] - 0s 5ms/step - loss: 0.9589 - acc: 0.4750 - val_loss: 0.6300 - val_acc: 0.9000
#     Epoch 2/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 0.7656 - acc: 0.9000
#     40/40 [==============================] - 0s 367us/step - loss: 0.6722 - acc: 0.8500 - val_loss: 0.4497 - val_acc: 1.0000
#     Epoch 3/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 0.5367 - acc: 1.0000
#     40/40 [==============================] - 0s 349us/step - loss: 0.4332 - acc: 0.9750 - val_loss: 0.3750 - val_acc: 1.0000
