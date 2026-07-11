#import library
import matplotlib.pyplot as plt

#define datasets
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug"
]

water_level = [
    2.4,
    2.6,
    3.1,
    3.8,
    4.6,
    5.3,
    5.0,
    4.2
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define area plot
ax.fill_between(
    months,
    water_level,
    color="skyblue",
    alpha=0.5
)

#define outline
ax.plot(
    months,
    water_level,
    color="royalblue",
    linewidth=2
)

#define title and label
ax.set_title("Monthly River Water Level")
ax.set_xlabel("Month")
ax.set_ylabel("Water Level (Meters)")

#enable grid
ax.grid(True, axis="y")

#show
plt.tight_layout()
plt.show()