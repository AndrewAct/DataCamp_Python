# # 8/10/2020
# The team strength lookup has three components: an input, an embedding layer, and a flatten layer that creates the output.

# If you wrap these three layers in a model with an input and output, you can re-use that stack of three layers at multiple places.

# Note again that the weights for all three layers will be shared everywhere we use them.

# Imports
from keras.layers import Input, Embedding, Flatten
from keras.models import Model

# Create an input layer for the team ID
teamid_in = Input(shape=(1,))

# Lookup the input in the team strength embedding layer
strength_lookup = team_lookup(teamid_in)

# Flatten the output
# Flatten would reshape the tensor to have the shape that is equal to the number of elements contained in tensor 
# non including the batch dimension
strength_lookup_flat = Flatten()(strength_lookup)

# Combine the operations into a single, re-usable model
team_strength_model = Model(teamid_in, strength_lookup_flat, name='Team-Strength-Model')