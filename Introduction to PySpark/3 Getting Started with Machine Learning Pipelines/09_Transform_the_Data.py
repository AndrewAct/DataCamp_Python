# # 8/18/2020
# Hooray, now you're finally ready to pass your data through the Pipeline you created!
# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)