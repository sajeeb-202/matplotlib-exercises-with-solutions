#import library
import matplotlib.pyplot as plt

#datasets
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [48, 55, 60, 66, 72, 80, 88, 94]

#define fig, plot
fig, ax = plt.subplots(figsize = (8,5))

ax.scatter(
    study_hours,
    exam_scores,
    color = 'green',
    s = 80,
    marker="o"

)

#define label
ax.set_title('Student Study Time vs Exam Score')
ax.set_xlabel('Study Hours')          #x label
ax.set_ylabel('Exam Score')           #y label

#enable grid
ax.grid(True)

#show graph
plt.show()
