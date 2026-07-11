#import library
import matplotlib.pyplot as plt
import numpy as np

#define datasets
np.random.seed(42)

x = np.random.normal(50, 12, 600)
y = np.random.normal(50, 10, 600)

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define hexbin plot
hb = ax.hexbin(
    x,
    y,
    gridsize=20,
    cmap="Blues"
)

#define colorbar
cbar = fig.colorbar(hb)
cbar.set_label("Number of Households")

#define title and label
ax.set_title("City Population Density Map")
ax.set_xlabel("East-West Position")
ax.set_ylabel("North-South Position")

#disable grid
ax.grid(False)

#show
plt.tight_layout()
plt.show()