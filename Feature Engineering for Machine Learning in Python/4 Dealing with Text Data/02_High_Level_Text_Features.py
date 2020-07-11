# # 7/11/2020
# Once the text has been cleaned and standardized you can begin creating features from the data. The most fundamental information you can calculate about free form text is its size, such as its length and number of words. In this exercise (and the rest of this chapter), you will focus on the cleaned/transformed text column (text_clean) you created in the last exercise.

# Find the length of each text
speech_df['char_cnt'] = speech_df['text_clean'].str.len()

# Count the number of words in each text
speech_df['word_cnt'] = speech_df['text_clean'].str.split().str.len()

# Find the average length of word
speech_df['avg_word_length'] = speech_df['char_cnt'] / speech_df['word_cnt']

# Print the first 5 rows of these columns
print(speech_df[['text_clean', 'char_cnt', 'word_cnt', 'avg_word_length']])

# <script.py> output:
#                                                text_clean  char_cnt  word_cnt  avg_word_length
#     0   fellow citizens of the senate and of the house...      8616      1432         6.016760
#     1   fellow citizens   i am again called upon by th...       787       135         5.829630
#     2   when it was first perceived  in early times  t...     13871      2323         5.971158
#     3   friends and fellow citizens   called upon to u...     10144      1736         5.843318
#     4   proceeding  fellow citizens  to that qualifica...     12902      2169         5.948363
#     5   unwilling to depart from examples of the most ...      7003      1179         5.939779
#     6   about to add the solemnity of an oath to the o...      7148      1211         5.902560
#     7   i should be destitute of feeling if i was not ...     19894      3382         5.882318
#     8   fellow citizens   i shall not attempt to descr...     26322      4466         5.893865
#     9   in compliance with an usage coeval with the ex...     17753      2922         6.075633
#     10  fellow citizens   about to undertake the arduo...      6818      1130         6.033628
#     11  fellow citizens   the will of the american peo...      7061      1179         5.988974
#     12  fellow citizens  the practice of all my predec...     23527      3912         6.014059
#     13  called from a retirement which i had supposed ...     32706      5585         5.856043
#     14  fellow citizens   without solicitation on my p...     28739      4821         5.961211
#     15  elected by the american people to the highest ...      6599      1092         6.043040
#     16  my countrymen   it a relief to feel that no he...     20089      3348         6.000299
#     17  fellow citizens   i appear before you this day...     16820      2839         5.924621
#     18  fellow citizens of the united states   in comp...     21032      3642         5.774849
#     19  fellow countrymen     at this second appearing...      3934       706         5.572238
#     20  citizens of the united states   your suffrages...      6521      1138         5.730228
#     21  fellow citizens   under providence i have been...      7736      1342         5.764531
#     22  fellow citizens   we have assembled to repeat ...     14969      2498         5.992394
#     23  fellow citizens   we stand to day upon an emin...     17774      2990         5.944482
#     24  fellow citizens   in the presence of this vast...     10155      1695         5.991150
#     25  fellow citizens   there is no constitutional o...     26175      4399         5.950216
#     26  my fellow citizens   in obedience of the manda...     12340      2028         6.084813
#     27  fellow citizens   in obedience to the will of ...     23691      3980         5.952513
#     28  my fellow citizens   when we assembled here on...     13426      2216         6.058664
#     29  my fellow citizens  no people on earth have mo...      5565       991         5.615540
#     30  my fellow citizens   anyone who has taken the ...     32160      5439         5.912852
#     31  there has been a change of government  it bega...      9554      1712         5.580607
#     32  my fellow citizens   the four years which have...      8402      1535         5.473616
#     33  my countrymen   when one surveys the world abo...     20294      3348         6.061529
#     34  my countrymen   no one can contemplate current...     23937      4055         5.903083
#     35  my countrymen   this occasion is not alone the...     22961      3771         6.088836
#     36  i am certain that my fellow americans expect t...     10910      1888         5.778602
#     37  when four years ago we met to inaugurate a pre...     10629      1831         5.805025
#     38  on each national day of inauguration since    ...      7674      1371         5.597374
#     39  mr  chief justice  mr  vice president  my frie...      3086       573         5.385689
#     40  mr  vice president  mr  chief justice  and fel...     13707      2292         5.980366
#     41  my friends  before i begin the expression of t...     14003      2475         5.657778
#     42  the price of peace mr  chairman  mr  vice pres...      9277      1688         5.495853
#     43  vice president johnson  mr  speaker  mr  chief...      7706      1390         5.543885
#     44  my fellow countrymen  on this occasion  the oa...      8242      1502         5.487350
#     45  senator dirksen  mr  chief justice  mr  vice p...     11701      2152         5.437268
#     46  mr  vice president  mr  speaker  mr  chief jus...     10048      1835         5.475749
#     47  for myself and for our nation  i want to thank...      6934      1238         5.600969
#     48  senator hatfield  mr  chief justice  mr  presi...     13787      2457         5.611315
#     49  senator mathias  chief justice burger  vice pr...     14601      2586         5.646172
#     50  mr  chief justice  mr  president  vice preside...     12536      2342         5.352690
#     51  my fellow citizens today we celebrate the myst...      9119      1608         5.671020
#     52  my fellow citizens at this last presidential i...     12374      2201         5.621990
#     53  president clinton  distinguished guests and my...      9084      1606         5.656289
#     54  vice president cheney  mr  chief justice  pres...     12199      2122         5.748822
#     55  my fellow citizens     i stand here today humb...     13637      2452         5.561582
#     56  vice president biden  mr  chief justice  membe...     12174      2151         5.659693
#     57  chief justice roberts  president carter  presi...      8555      1488         5.749328