#import library
import matplotlib.pyplot as plt
import numpy as np

#define datasets
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

Z = np.exp(-(X**2 + Y**2))

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define contour plot
ax.contour(
    X,
    Y,
    Z,
    levels=10,
    colors="royalblue"
)

#define title and label
ax.set_title("Astronomical Star Density")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")

#disable grid
ax.grid(False)

#show
plt.tight_layout()
plt.show()