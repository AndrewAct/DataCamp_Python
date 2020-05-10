# 5/1/2020
# Create a point plot of family relationship vs. absences
sns.catplot(x = "famrel",
            y = "absences",
            data = student_data,
            kind = "point")


            
# Show plot
plt.show()

# Remove lines that join together 
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join = False)
            
# Show plot
plt.show()