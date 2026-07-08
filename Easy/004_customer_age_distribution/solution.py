#import library
import matplotlib.pyplot as plt

#define datasets
customer_ages = [
    18, 19, 20, 21, 22, 22, 23, 24, 24, 25,
    25, 26, 27, 28, 28, 29, 30, 31, 32, 33,
    34, 35, 36, 37, 38, 40, 42, 45, 48, 50
]

#define fig and plot size
fig, ax = plt.subplots(figsize = (8,5))

#define histogram
ax.hist(
    customer_ages,
    bins = 8,
    color = 'orange',
    edgecolor = 'black'
)

#define title and label
ax.set_title('Customer Age Distribution')
ax.set_xlabel('Age')
ax.set_ylabel('Number of Customers')

#enable grid
ax.grid(True, axis = 'y')

#show
plt.tight_layout()
plt.show()