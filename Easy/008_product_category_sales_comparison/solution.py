#import library
import matplotlib.pyplot as plt
import numpy as np

#define datasets
categories = [
    "Electronics",
    "Furniture",
    "Clothing",
    "Groceries",
    "Sports"
]

q1_sales = [85, 62, 74, 96, 58]

q2_sales = [92, 68, 79, 101, 64]

#define x positions
x = np.arange(len(categories))
width = 0.35

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define q1 sales bars
ax.bar(
    x - width/2,
    q1_sales,
    width=width,
    color="royalblue",
    label="Q1"
)

#define q2 sales bars
ax.bar(
    x + width/2,
    q2_sales,
    width=width,
    color="orange",
    label="Q2"
)

#define title and label
ax.set_title("Product Category Sales Comparison")
ax.set_xlabel("Product Category")
ax.set_ylabel("Quarterly Sales (Thousand Units)")

#define x ticks
ax.set_xticks(x)
ax.set_xticklabels(categories)

#enable grid
ax.grid(True, axis="y")

#define legend
ax.legend(loc="upper left")

#show
plt.tight_layout()
plt.show()