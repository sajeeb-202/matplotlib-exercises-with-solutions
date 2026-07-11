#import library
import matplotlib.pyplot as plt

#define datasets
request_times = [
    3,
    8,
    12,
    18,
    26,
    33,
    41,
    49,
    58
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define event plot
ax.eventplot(
    request_times,
    orientation="horizontal",
    colors="royalblue",
    lineoffsets=1,
    linelengths=0.8
)

#define y ticks
ax.set_yticks([1])
ax.set_yticklabels(["Server"])

#define title and label
ax.set_title("Server Request Timeline")
ax.set_xlabel("Minutes After 9:00 AM")
ax.set_ylabel("Server")

#enable grid
ax.grid(True, axis="x")

#show
plt.tight_layout()
plt.show()