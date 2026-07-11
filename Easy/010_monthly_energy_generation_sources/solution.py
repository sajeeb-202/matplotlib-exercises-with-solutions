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

solar = [
    12,
    16,
    20,
    24,
    28,
    30
]

wind = [
    18,
    20,
    21,
    23,
    24,
    26
]

hydro = [
    30,
    31,
    30,
    29,
    28,
    27
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define stack plot
ax.stackplot(
    months,
    solar,
    wind,
    hydro,
    labels=["Solar", "Wind", "Hydropower"],
    colors=["gold", "royalblue", "forestgreen"],
    alpha=0.8
)

#define title and label
ax.set_title("Monthly Energy Generation Sources")
ax.set_xlabel("Month")
ax.set_ylabel("Electricity Generation (GWh)")

#enable grid
ax.grid(True, axis="y")

#define legend
ax.legend(loc="upper left")

#show
plt.tight_layout()
plt.show()