# # 8/9/2020
# What you coded in the previous exercise has been executed to obtain theactivation_results variable, this time 100 epochs were used instead of 20. This way you will have more epochs to further compare how the training evolves per activation function.

# For every h_callback of each activation function in activation_results:

# The h_callback.history['val_loss'] has been extracted.
# The h_callback.history['val_acc'] has been extracted.
# Both are saved into two dictionaries: val_loss_per_function and val_acc_per_function.

# Pandas is also loaded as pd for you to use. Let's plot some quick validation loss and accuracy charts!

# Create a dataframe from val_loss_per_function
val_loss= pd.DataFrame(val_loss_per_function)

# Call plot on the dataframe
val_loss.plot()
plt.show()

# Create a dataframe from val_acc_per_function
val_acc = pd.DataFrame(val_acc_per_function)

# Call plot on the dataframe
val_acc.plot()
plt.show()

