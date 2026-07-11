#import library
import matplotlib.pyplot as plt

#define datasets
products = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Headphones",
    "Smartwatch",
    "Camera"
]

price = [
    1200,
    850,
    500,
    180,
    320,
    950
]

rating = [
    4.8,
    4.6,
    4.4,
    4.5,
    4.3,
    4.7
]

units_sold = [
    180,
    420,
    250,
    680,
    340,
    140
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define bubble chart
ax.scatter(
    price,
    rating,
    s=units_sold,
    color="royalblue",
    alpha=0.6
)

#define title and label
ax.set_title("Product Price vs Customer Rating")
ax.set_xlabel("Price (USD)")
ax.set_ylabel("Customer Rating")

#enable grid
ax.grid(True)

#show
plt.tight_layout()
plt.show()