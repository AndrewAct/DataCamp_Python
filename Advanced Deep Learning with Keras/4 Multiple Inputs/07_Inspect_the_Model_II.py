# # 8/11/2020
# Now you should take a look at the weights for this model. In particular, note the last weight of the model. This weight converts the predicted score difference to a predicted win probability. If you multiply the predicted score difference by the last weight of the model and then apply the sigmoid function, you get the win probability of the game.

# Print the model weights
print(model.get_weights())

# Print the training data means
print(games_tourney_train.mean())

# <script.py> output:
#     [array([[0.9695341 ],
#            [0.22126554]], dtype=float32), array([[0.1428871]], dtype=float32)]
#     season        1.998074e+03
#     team_1        5.556771e+03
#     team_2        5.556771e+03
#     home          0.000000e+00
#     seed_diff     0.000000e+00
#     score_diff    0.000000e+00
#     score_1       7.162128e+01
#     score_2       7.162128e+01
#     won           5.000000e-01
#     pred         -1.625470e-14
#     dtype: float64

# Import the sigmoid function from scipy
from scipy.special import expit as sigmoid

# Weight from the model
weight = 0.14

# Print the approximate win probability predicted close game
print(sigmoid(1 * weight))

# Print the approximate win probability predicted blowout game
print(sigmoid(10 * weight))

# <script.py> output:
#     0.5349429451582145
#     0.8021838885585818