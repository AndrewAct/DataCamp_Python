# # 8/10/2020
# Now that you've looked up how "strong" each team is, subtract the team strengths to determine which team is expected to win the game.

# This is a bit like the seeds that the tournament committee uses, which are also a measure of team strength. But rather than using seed differences to predict score differences, you'll use the difference of your own team strength model to predict score differences.

# The subtract layer will combine the weights from the two layers by subtracting them.
# Import the Subtract layer from keras
# Subtract would return a single tensore, (inouts[0] - inputs[1])
from keras.layers import Subtract

# Create a subtract layer using the inputs from the previous exercise
score_diff = Subtract()([team_1_strength, team_2_strength])