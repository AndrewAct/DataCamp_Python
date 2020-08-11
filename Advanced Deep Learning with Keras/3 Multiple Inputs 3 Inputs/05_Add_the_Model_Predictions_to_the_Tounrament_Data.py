# # 8/11/2020
# In lesson 1 of this chapter, you used the regular season model to make predictions on the tournament dataset, and got pretty good results! Try to improve your predictions for the tournament by modeling it specifically.

# You'll use the prediction from the regular season model as an input to the tournament model. This is a form of "model stacking."

# To start, take the regular season model from the previous lesson, and predict on the tournament data. Add this prediction to the tournament data as a new column.

# Predict
games_tourney['pred'] = model.predict([games_tourney['team_1'],
                                             games_tourney['team_2'],
                                             games_tourney['home']])