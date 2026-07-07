import matplotlib.pyplot as plt

# Dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 160, 210, 250]

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the data
ax.plot(
    months,
    sales,
    color="blue",
    linewidth=2,
    marker="o",
    markersize=8,
    label="Sales"
)

# Add chart elements
ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.legend(loc="upper left")
ax.grid(True)

# Improve spacing and display the chart
plt.tight_layout()
plt.show()