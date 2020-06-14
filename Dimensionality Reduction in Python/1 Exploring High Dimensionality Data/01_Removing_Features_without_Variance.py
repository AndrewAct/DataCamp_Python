# # 6/13/2020
# A sample of the Pokemon dataset has been loaded as pokemon_df. To get an idea of which features have little variance you should use the IPython Shell to calculate summary statistics on this sample. Then adjust the code to create a smaller, easier to understand, dataset.

# Leave this list as is
number_cols = ['HP', 'Attack', 'Defense']

# Remove the feature without variance from this list
non_number_cols = ['Name', 'Type']

# Create a new dataframe by subselecting the chosen features
df_selected = pokemon_df[number_cols + non_number_cols]

# Prints the first 5 lines of the new dataframe
print(df_selected.head())


# <script.py> output:
#        HP  Attack  Defense                   Name   Type
#     0  45      49       49              Bulbasaur  Grass
#     1  60      62       63                Ivysaur  Grass
#     2  80      82       83               Venusaur  Grass
#     3  80     100      123  VenusaurMega Venusaur  Grass
#     4  39      52       43             Charmander   Fire