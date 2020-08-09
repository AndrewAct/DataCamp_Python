# # 8/9/2020
# You're going to automate the watering of farm parcels by making an intelligent irrigation machine. Multi-label classification problems differ from multi-class problems in that each observation can be labeled with zero or more classes. So classes/labels are not mutually exclusive, you could water all, none or any combination of farm parcels based on the inputs.

# To account for this behavior what we do is have an output layer with as many neurons as classes but this time, unlike in multi-class problems, each output neuron has a sigmoid activation function. This makes each neuron in the output layer able to output a number between 0 and 1 independently.

# Keras Sequential() model and Dense() layers are preloaded. It's time to build an intelligent irrigation machine!
# Binary crossentropy is for multil-label classfications, whereas categorical cross entropy is for multiclass classification
# Instantiate a Sequential model
model = Sequential()

# Add a hidden layer of 64 neurons and a 20 neuron's input
model.add(Dense(64, activation= 'relu', input_shape = (20,)))

# Add an output layer of 3 neurons with sigmoid activation
model.add(Dense(3, activation= 'sigmoid', input_shape = (64, )))

# Compile your model with binary crossentropy loss
model.compile(optimizer='adam',
           loss = 'binary_crossentropy',
           metrics=['accuracy'])

model.summary()

# <script.py> output:
#     Model: "sequential_1"
#     _________________________________________________________________
#     Layer (type)                 Output Shape              Param #   
#     =================================================================
#     dense_1 (Dense)              (None, 64)                1344      
#     _________________________________________________________________
#     dense_2 (Dense)              (None, 3)                 195       
#     =================================================================
#     Total params: 1,539
#     Trainable params: 1,539
#     Non-trainable params: 0
#     _________________________________________________________________