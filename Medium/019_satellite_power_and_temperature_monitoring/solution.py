#import library
import matplotlib.pyplot as plt

#define datasets
time = [
    "00",
    "03",
    "06",
    "09",
    "12",
    "15",
    "18",
    "21"
]

battery = [
    100,
    97,
    94,
    90,
    86,
    82,
    79,
    75
]

temperature = [
    18,
    22,
    27,
    31,
    35,
    33,
    28,
    23
]

#define fig and plot size
fig, ax1 = plt.subplots(figsize=(8, 5))

#define battery plot
ax1.plot(
    time,
    battery,
    color="royalblue",
    marker="o",
    linewidth=2
)

#define primary axis label
ax1.set_xlabel("Time (Hours)")
ax1.set_ylabel("Battery Level (%)")

#enable grid
ax1.grid(True, axis="y")

#define secondary axis
ax2 = ax1.twinx()

#define temperature plot
ax2.plot(
    time,
    temperature,
    color="firebrick",
    marker="s",
    linewidth=2
)

#define secondary axis label
ax2.set_ylabel("Temperature (°C)")

#define title
ax1.set_title("Satellite Battery and Temperature Monitoring")

#show
plt.tight_layout()
plt.show()