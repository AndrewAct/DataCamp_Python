# # 8/9/2020
# You're going to build a simple neural network to get a feeling of how quickly it is to accomplish this in Keras.

# You will build a network that takes two numbers as an input, passes them through a hidden layer of 10 neurons, and finally outputs a single non-constrained number.

# A non-constrained output can be obtained by avoiding setting an activation function in the output layer. This is useful for problems like regression, when we want our output to be able to take any non-constrained value.

# Import the Sequential model and Dense layer
from keras.models import Sequential
from keras.layers import Dense

# Create a Sequential model
model = Sequential()

# Add an input layer and a hidden layer with 10 neurons
model.add(Dense(10, input_shape=(2,), activation="relu"))

# Add a 1-neuron output layer
model.add(Dense(1, activation = 'relu'))

# Summarise your model
model.summary()

# <script.py> output:
#     Model: "sequential_1"
#     _________________________________________________________________
#     Layer (type)                 Output Shape              Param #   
#     =================================================================
#     dense_1 (Dense)              (None, 10)                30        
#     _________________________________________________________________
#     dense_2 (Dense)              (None, 1)                 11        
#     =================================================================
#     Total params: 41
#     Trainable params: 41
#     Non-trainable params: 0
#     _________________________________________________________________