#import library
import matplotlib.pyplot as plt

#define datasets
python_scores = [
    62, 68, 71, 74, 76,
    79, 81, 84, 87, 91
]

sql_scores = [
    55, 60, 64, 67, 70,
    73, 75, 78, 82, 86
]

machine_learning_scores = [
    58, 63, 69, 72, 77,
    80, 83, 86, 90, 94
]

#define datasets for violin plot
score_data = [
    python_scores,
    sql_scores,
    machine_learning_scores
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define violin plot
ax.violinplot(score_data)

#define x ticks
ax.set_xticks([1, 2, 3])
ax.set_xticklabels([
    "Python",
    "SQL",
    "Machine Learning"
])

#define title and label
ax.set_title("Online Course Exam Score Distribution")
ax.set_xlabel("Course")
ax.set_ylabel("Exam Score")

#enable grid
ax.grid(True, axis="y")

#show
plt.tight_layout()
plt.show()