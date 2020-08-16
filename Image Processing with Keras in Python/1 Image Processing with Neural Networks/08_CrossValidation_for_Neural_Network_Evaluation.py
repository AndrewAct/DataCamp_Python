# # 8/19/2020
# To evaluate the model, we use a separate test data-set. As in the train data, the images in the test data also need to be reshaped before they can be provided to the fully-connected network because the network expects one column per pixel in the input.

# The model you fit in the previous exercise, and test_data and test_labels are available in your workspace.

# Reshape test data
test_data = test_data.reshape(10,  784)

# Evaluate the model
model.evaluate(test_data, test_labels)

# <script.py> output:
    
#     10/10 [==============================] - 0s 121us/step