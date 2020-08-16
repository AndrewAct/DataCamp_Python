# # 8/16/2020
# Training a deep learning model is very similar to training a single layer network. Once the model is constructed (as you have done in the previous exercise), the model needs to be compiled with the right set of parameters. Then, the model is fit by providing it with training data, as well as training labels. After training is done, the model can be evaluated on test data.

# The model you built in the previous exercise is available in your workspace.

# Compile model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Fit the model to training data 
model.fit(train_data, train_labels, 
          validation_split=0.2, 
          epochs=3, batch_size=10)

# Evaluate the model on test data
model.evaluate(test_data, test_labels, batch_size=10)

# <script.py> output:
#     Train on 40 samples, validate on 10 samples
#     Epoch 1/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 1.0957 - acc: 0.4000
#     40/40 [==============================] - 0s 8ms/step - loss: 1.0861 - acc: 0.5750 - val_loss: 1.0630 - val_acc: 0.7000
#     Epoch 2/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 1.0665 - acc: 0.7000
#     40/40 [==============================] - 0s 697us/step - loss: 1.0378 - acc: 0.8750 - val_loss: 0.9901 - val_acc: 1.0000
#     Epoch 3/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 1.0023 - acc: 1.0000
#     40/40 [==============================] - 0s 676us/step - loss: 0.9554 - acc: 0.9750 - val_loss: 0.8828 - val_acc: 1.0000
    
#     10/10 [==============================] - 0s 319us/step
