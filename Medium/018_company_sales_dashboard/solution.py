#import library
import matplotlib.pyplot as plt

#define datasets
hours = [
    "00", "03", "06", "09",
    "12", "15", "18", "21"
]

magnitude = [
    2.1,
    2.8,
    3.2,
    2.9,
    4.7,
    3.8,
    5.4,
    3.1
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define line plot
ax.plot(
    hours,
    magnitude,
    color="firebrick",
    linewidth=2,
    marker="o"
)

#define annotation
max_index = magnitude.index(max(magnitude))

ax.annotate(
    "Strongest Earthquake",
    xy=(hours[max_index], magnitude[max_index]),
    xytext=("12", 5.8),
    arrowprops=dict(
        arrowstyle="->",
        color="black"
    )
)

#define title and label
ax.set_title("Daily Earthquake Magnitude Monitoring")
ax.set_xlabel("Hour")
ax.set_ylabel("Magnitude")

#enable grid
ax.grid(True, axis="y")

#show
plt.tight_layout()
plt.show()