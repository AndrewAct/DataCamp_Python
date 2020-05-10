# 5/1/2020
# Why use Relplot?
# It allows to make subplots in one diagram 
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time", 
            )

# Show plot
plt.show()

sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            col = "study_time")
            
plt.show()