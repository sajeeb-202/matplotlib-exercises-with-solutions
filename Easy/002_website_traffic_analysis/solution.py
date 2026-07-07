#import library
import matplotlib.pyplot as plt
import numpy as np

#datasets
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [1200, 1450, 1380, 1670, 1820, 2100, 1950]

#figure size
fig, ax = plt.subplots(figsize = (8,5))

#define plot
ax.bar(
    days,
    visitors,
    color = 'skyblue',
    width = 0.6,
    edgecolor = 'black'

)

#define title and label
ax.set_title('Website Visitors Over the Last 7 Days')
ax.set_xlabel('Day')
ax.set_ylabel('Number of Visitors')
ax.grid(True, axis ='y')

#show the graph
plt.tight_layout()
plt.show()