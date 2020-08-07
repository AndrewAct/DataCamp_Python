# # 8/7/2020
# You'll now create a classification model using the titanic dataset, which has been pre-loaded into a DataFrame called df. You'll take information about the passengers and predict which ones survived.

# The predictive variables are stored in a NumPy array predictors. The target to predict is in df.survived, though you'll have to manipulate it for keras. The number of predictive features is stored in n_cols.

# Here, you'll use the 'sgd' optimizer, which stands for Stochastic Gradient Descent. You'll learn more about this in the next chapter!

# Convert df.survived to a categorical variable using the to_categorical() function.
# Specify a Sequential model called model.
# Add a Dense layer with 32 nodes. Use 'relu' as the activation and (n_cols,) as the input_shape.
# Add the Dense output layer. Because there are two outcomes, it should have 2 units, and because it is a classification model, the activation should be 'softmax'.
# Compile the model, using 'sgd' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] to see the accuracy (what fraction of predictions were correct) at the end of each epoch.
# Fit the model using the predictors and the target.

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))

# Add the output layer
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='sgd', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Fit the model
model.fit(predictors, target)

# <script.py> output:
#     Epoch 1/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 7.6250 - acc: 0.2188
# 768/891 [========================>.....] - ETA: 0s - loss: 2.3826 - acc: 0.6042
# 891/891 [==============================] - 0s - loss: 2.5170 - acc: 0.5948     
#     Epoch 2/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 1.1922 - acc: 0.3125
# 768/891 [========================>.....] - ETA: 0s - loss: 1.1910 - acc: 0.6029
# 891/891 [==============================] - 0s - loss: 1.1834 - acc: 0.6083     
#     Epoch 3/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 2.1141 - acc: 0.5000
# 768/891 [========================>.....] - ETA: 0s - loss: 0.8163 - acc: 0.6549
# 891/891 [==============================] - 0s - loss: 0.7783 - acc: 0.6700     
#     Epoch 4/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 0.7271 - acc: 0.5625
# 768/891 [========================>.....] - ETA: 0s - loss: 0.7222 - acc: 0.6641
# 891/891 [==============================] - 0s - loss: 0.7257 - acc: 0.6689     
#     Epoch 5/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 0.6173 - acc: 0.5938
# 768/891 [========================>.....] - ETA: 0s - loss: 0.6361 - acc: 0.6628
# 891/891 [==============================] - 0s - loss: 0.6529 - acc: 0.6588     
#     Epoch 6/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 0.4729 - acc: 0.7500
# 768/891 [========================>.....] - ETA: 0s - loss: 0.6196 - acc: 0.6888
# 891/891 [==============================] - 0s - loss: 0.6164 - acc: 0.6936     
#     Epoch 7/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 0.6732 - acc: 0.5938
# 768/891 [========================>.....] - ETA: 0s - loss: 0.6391 - acc: 0.6797
# 891/891 [==============================] - 0s - loss: 0.6302 - acc: 0.6880     
#     Epoch 8/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 0.5363 - acc: 0.7188
# 768/891 [========================>.....] - ETA: 0s - loss: 0.6208 - acc: 0.6849
# 891/891 [==============================] - 0s - loss: 0.6199 - acc: 0.6891     
#     Epoch 9/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 0.6629 - acc: 0.6250
# 768/891 [========================>.....] - ETA: 0s - loss: 0.6055 - acc: 0.6901
# 891/891 [==============================] - 0s - loss: 0.5959 - acc: 0.6970     
#     Epoch 10/10
    
#  32/891 [>.............................] - ETA: 0s - loss: 0.4738 - acc: 0.7500
# 768/891 [========================>.....] - ETA: 0s - loss: 0.6319 - acc: 0.6810
# 891/891 [==============================] - 0s - loss: 0.6375 - acc: 0.6813

