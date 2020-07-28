# # 7/27/2020
# In this exercise, we will generate the pairwise similarity scores of all the words in a sentence. The sentence is available as sent and has been printed to the console for your convenience.

# Create the doc object
doc = nlp(sent)

# Compute pairwise similarity scores
for token1 in doc:
  for token2 in doc:
    print(token1.text, token2.text, token1.similarity(token2))

# <script.py> output:
#     I I 1.0
#     I like 0.023032807
#     I apples 0.10175116
#     I and 0.047492094
#     I oranges 0.10894456
#     like I 0.023032807
#     like like 1.0
#     like apples 0.015370452
#     like and 0.189293
#     like oranges 0.021943133
#     apples I 0.10175116
#     apples like 0.015370452
#     apples apples 1.0
#     apples and -0.17736834
#     apples oranges 0.6315578
#     and I 0.047492094
#     and like 0.189293
#     and apples -0.17736834
#     and and 1.0
#     and oranges 0.018627528
#     oranges I 0.10894456
#     oranges like 0.021943133
#     oranges apples 0.6315578
#     oranges and 0.018627528
#     oranges oranges 1.0