# # 8/9/2020
# You've already prepared your sequences of text. It's time to build your LSTM model!

# Remember your sequences had 4 words each, your model will be trained on the first three words of each sequence, predicting the 4th one. You are going to use an Embedding layer that will essentially learn to turn words into vectors. These vectors will then be passed to a simple LSTM layer. Our output is a Dense layer with as many neurons as words in the vocabulary and softmax activation. This is because we want to obtain the highest probable next word out of all possible words.

# The size of the vocabulary of words (the unique number of words) is stored in vocab_size.

# Import the Embedding, LSTM and Dense layer
from keras.layers import Embedding, LSTM, Dense

model = Sequential()

# Add an Embedding layer with the right parameters
# Embedding will turn positive integers into dense vectors of fixed size
# It can only be used as the first layer of the model
model.add(Embedding(input_dim = vocab_size, input_length = 3, output_dim = 8 ))

# Add a 32 unit LSTM layer
model.add(LSTM(32))

# Add a hidden Dense layer of 32 units and an output layer of vocab_size with softmax
model.add(Dense(32, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
model.summary()

# <script.py> output:
#     Model: "sequential_1"
#     _________________________________________________________________
#     Layer (type)                 Output Shape              Param #   
#     =================================================================
#     embedding_1 (Embedding)      (None, 3, 8)              352       
#     _________________________________________________________________
#     lstm_1 (LSTM)                (None, 32)                5248      
#     _________________________________________________________________
#     dense_1 (Dense)              (None, 32)                1056      
#     _________________________________________________________________
#     dense_2 (Dense)              (None, 44)                1452      
#     =================================================================
#     Total params: 8,108
#     Trainable params: 8,108
#     Non-trainable params: 0
#     _________________________________________________________________
