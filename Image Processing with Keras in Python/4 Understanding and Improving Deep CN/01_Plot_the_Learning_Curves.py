# # 8/16/2020
# During learning, the model will store the loss function evaluated in each epoch. Looking at the learning curves can tell us quite a bit about the learning process. In this exercise, you will plot the learning and validation loss curves for a model that you will train.

import matplotlib.pyplot as plt

# Train the model and store the training object
training = model.fit(train_data, train_labels, epochs = 3, batch_size= 10, validation_split= 0.2)

# Extract the history from the training object
history = training.history

# Plot the training loss 
plt.plot(history['loss'])
# Plot the validation loss
plt.plot(history['val_loss'])

# Show the figure
plt.show()

# <script.py> output:
#     Train on 40 samples, validate on 10 samples
#     Epoch 1/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 1.0841 - acc: 0.2000
#     40/40 [==============================] - 0s 7ms/step - loss: 1.0812 - acc: 0.2750 - val_loss: 1.0335 - val_acc: 0.6000
#     Epoch 2/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 1.0681 - acc: 0.6000
#     40/40 [==============================] - 0s 402us/step - loss: 1.0382 - acc: 0.5000 - val_loss: 0.9755 - val_acc: 0.8000
#     Epoch 3/3
    
#     10/40 [======>.......................] - ETA: 0s - loss: 1.0370 - acc: 0.3000
#     40/40 [==============================] - 0s 390us/step - loss: 0.9902 - acc: 0.5750 - val_loss: 0.9121 - val_acc: 0.8000
