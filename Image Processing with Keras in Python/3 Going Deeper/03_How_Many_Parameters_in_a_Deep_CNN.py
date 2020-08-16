# # 8/16/2020
# In this exercise, you will use Keras to calculate the total number of parameters along with the number of parameters in each layer of the network.

# We have already provided code that builds a deep CNN for you.

# CNN model
model = Sequential()
model.add(Conv2D(10, kernel_size=2, activation='relu', 
                 input_shape=(28, 28, 1)))
model.add(Conv2D(10, kernel_size=2, activation='relu'))
model.add(Flatten())
model.add(Dense(3, activation='softmax'))

# Summarize the model 
model.summary()

# <script.py> output:
#     Model: "sequential_1"
#     _________________________________________________________________
#     Layer (type)                 Output Shape              Param #   
#     =================================================================
#     conv2d_1 (Conv2D)            (None, 27, 27, 10)        50        
#     _________________________________________________________________
#     conv2d_2 (Conv2D)            (None, 26, 26, 10)        410       
#     _________________________________________________________________
#     flatten_1 (Flatten)          (None, 6760)              0         
#     _________________________________________________________________
#     dense_1 (Dense)              (None, 3)                 20283     
#     =================================================================
#     Total params: 20,743
#     Trainable params: 20,743
#     Non-trainable params: 0
#     _________________________________________________________________