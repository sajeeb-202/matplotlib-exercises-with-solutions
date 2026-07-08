#import library
import matplotlib.pyplot as plt

#define datasets
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

web_revenue = [18, 22, 25, 28, 31, 35]

mobile_revenue = [15, 18, 21, 24, 28, 33]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define web platform plot
ax.plot(
    months,
    web_revenue,
    color="blue",
    linewidth=2,
    marker="o",
    label="Web Platform"
)

#define mobile app plot
ax.plot(
    months,
    mobile_revenue,
    color="green",
    linewidth=2,
    marker="s",
    linestyle="--",
    label="Mobile App"
)

#define title and label
ax.set_title("Monthly Revenue Comparison")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (Thousand USD)")

#enable grid
ax.grid(True)

#define legend
ax.legend(loc="upper left")

#show
plt.tight_layout()
plt.show()