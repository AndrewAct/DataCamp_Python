# # 8/19/2020
# In this exercise, you will fit the fully connected neural network that you constructed in the previous exercise to image data. The training data is provided as two variables: train_data that contains the pixel data for 50 images of the three clothing classes and train_labels, which contains one-hot encoded representations of the labels for each one of these 50 images. Transform the data into the network's expected input and then fit the model on training data and training labels.

# The model you compiled in the previous exercise, and train_data and train_labels are available in your workspace.

# Reshape the data to two-dimensional array
train_data = train_data.reshape(50, 784)

# Fit the model
model.fit(train_data, train_labels, validation_split=0.2, epochs=3)

# <script.py> output:
#     Train on 40 samples, validate on 10 samples
#     Epoch 1/3
    
#     32/40 [=======================>......] - ETA: 0s - loss: 1.0043 - acc: 0.5000
#     40/40 [==============================] - 0s 6ms/step - loss: 1.0061 - acc: 0.5000 - val_loss: 0.9917 - val_acc: 0.4000
#     Epoch 2/3
    
#     32/40 [=======================>......] - ETA: 0s - loss: 0.9580 - acc: 0.5625
#     40/40 [==============================] - 0s 132us/step - loss: 0.9442 - acc: 0.6000 - val_loss: 0.9595 - val_acc: 0.4000
#     Epoch 3/3
    
#     32/40 [=======================>......] - ETA: 0s - loss: 0.8757 - acc: 0.5625
#     40/40 [==============================] - 0s 127us/step - loss: 0.8938 - acc: 0.5500 - val_loss: 0.9222 - val_acc: 0.4000
