# 4/18/2020
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
print(avocados.head())
# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind = "bar")

# Show the plot
plt.show()