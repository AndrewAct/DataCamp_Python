# # 7/22/2020
# In this exercise, you'll utilize re.search() and re.match() to find specific tokens. Both search and match expect regex patterns, similar to those you defined in an earlier exercise. You'll apply these regex library methods to the same Monty Python text from the nltk corpora.

# You have both scene_one and sentences available from the last exercise; now you can use them with re.search() and re.match() to extract and match more text.

# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

# <script.py> output:
#     580 588

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*\]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1, scene_one))

# <script.py> output:
#     <_sre.SRE_Match object; span=(9, 32), match='[wind] [clop clop clop]'>


# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w\s]+:"
print(re.match(pattern2, sentences[3]))

# <script.py> output:
#     <_sre.SRE_Match object; span=(0, 7), match='ARTHUR:'>
