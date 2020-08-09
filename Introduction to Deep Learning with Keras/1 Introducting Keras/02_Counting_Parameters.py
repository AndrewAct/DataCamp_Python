# # 8/9/2020
# You've just created a neural network. But you're going to create a new one now, taking some time to think about the weights of each layer. The Keras Dense layer and the Sequential model are already loaded for you to use.

# This is the network you will be creating:

# Instantiate a new Sequential model
model = Sequential()

# Add a Dense layer with five neurons and three inputs
model.add(Dense(5, input_shape=(3,), activation="relu"))

# Add a final Dense layer with one neuron and no activation
model.add(Dense(1, activation= 'relu'))

# Summarize your model
model.summary()

# <script.py> output:
#     Model: "sequential_1"
#     _________________________________________________________________
#     Layer (type)                 Output Shape              Param #   
#     =================================================================
#     dense_1 (Dense)              (None, 5)                 20        
#     _________________________________________________________________
#     dense_2 (Dense)              (None, 1)                 6         
#     =================================================================
#     Total params: 26
#     Trainable params: 26
#     Non-trainable params: 0
#     _________________________________________________________________

