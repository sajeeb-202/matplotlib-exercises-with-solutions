#import library
import matplotlib.pyplot as plt

#define datasets
engineering = [
    5200, 5400, 5600, 5900, 6100,
    6300, 6400, 6500, 6800, 9200
]

marketing = [
    3600, 3800, 3900, 4100, 4200,
    4300, 4400, 4600, 4700, 5200
]

sales = [
    3100, 3300, 3400, 3600, 3700,
    3900, 4100, 4300, 4500, 6100
]

#define datasets for box plot
salary_data = [
    engineering,
    marketing,
    sales
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define box plot
ax.boxplot(
    salary_data,
    tick_labels=[
        "Engineering",
        "Marketing",
        "Sales"
    ]
)

#define title and label
ax.set_title("Employee Salary Distribution by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Monthly Salary (USD)")

#enable grid
ax.grid(True, axis="y")

#show
plt.tight_layout()
plt.show()