# 5/10/2020
# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ < 16) & (educ >= 14) 

# High school (12 or fewer years of education)
high = (educ <= 12) 
print(high.mean())