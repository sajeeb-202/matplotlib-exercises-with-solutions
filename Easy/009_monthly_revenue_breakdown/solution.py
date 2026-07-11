#import library
import matplotlib.pyplot as plt

#define datasets
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

physical_sales = [
    45,
    52,
    48,
    60,
    58,
    65
]

digital_sales = [
    18,
    22,
    25,
    24,
    28,
    30
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define physical product bars
ax.bar(
    months,
    physical_sales,
    color="steelblue",
    label="Physical Products"
)

#define digital product bars
ax.bar(
    months,
    digital_sales,
    bottom=physical_sales,
    color="orange",
    label="Digital Products"
)

#define title and label
ax.set_title("Monthly Revenue Breakdown")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (Thousand USD)")

#enable grid
ax.grid(True, axis="y")

#define legend
ax.legend(loc="upper left")

#show
plt.tight_layout()
plt.show()