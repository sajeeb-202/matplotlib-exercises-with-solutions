#import library
import matplotlib.pyplot as plt

#define datasets
brands = [
    "Samsung",
    "Apple",
    "Xiaomi",
    "Realme",
    "Others"
]

market_share = [35, 28, 18, 10, 9]

#define fig and pie chart size
fig, ax = plt.subplots(figsize = (8,5))

ax.pie(
    market_share,
    labels = brands,
    autopct = "%.1f%%",
    startangle = 90.0,
    shadow = True
)

#define title and label
ax.set_title('Smartphone Market Share')

#show
plt.tight_layout()
plt.show()