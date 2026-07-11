#import library
import matplotlib.pyplot as plt

#define datasets
hours = [
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15"
]

temperature = [
    62,
    65,
    69,
    74,
    71,
    68,
    66,
    64
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define stem plot
markerline, stemlines, baseline = ax.stem(
    hours,
    temperature
)

#define stem plot style
plt.setp(stemlines, color="royalblue")
plt.setp(markerline, markerfacecolor="orange", markeredgecolor="orange")
plt.setp(baseline, color="gray")

#define title and label
ax.set_title("Hourly Machine Temperature")
ax.set_xlabel("Hour")
ax.set_ylabel("Temperature (°C)")

#enable grid
ax.grid(True, axis="y")

#show
plt.tight_layout()
plt.show()