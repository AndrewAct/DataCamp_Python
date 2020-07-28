# # 7/27/2020
# In this exercise, we will build a recommender function get_recommendations(), as discussed in the lesson and the previous exercise. As we know, it takes in a title, a cosine similarity matrix, and a movie title and index mapping as arguments and outputs a list of 10 titles most similar to the original title (excluding the title itself).

# You have been given a dataset metadata that consists of the movie titles and overviews. The head of this dataset has been printed to console.

#                title                                            tagline
# 938  Cinema Paradiso  A celebration of youth, friendship, and the ev...
# 630         Spy Hard  All the action. All the women. Half the intell...
# 682        Stonewall                    The fight for the right to love
# 514           Killer                    You only hurt the one you love.
# 365    Jason's Lyric                                   Love is courage.

# Generate mapping between titles and index
indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

def get_recommendations(title, cosine_sim, indices):
    # Get index of movie that matches title
    idx = indices[title]
    # Sort the movies based on the similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores for 10 most similar movies
    sim_scores = sim_scores[1:11]
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    # Return the top 10 most similar movies
    return metadata['title'].iloc[movie_indices]

