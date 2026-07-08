#import library
import matplotlib.pyplot as plt

#define datasets
departments = [
    "Emergency",
    "Internal Medicine",
    "Cardiology",
    "Orthopedics",
    "Pediatrics",
    "Neurology"
]

patients = [
    245,
    198,
    132,
    118,
    176,
    94
]

#define fig and plot size
fig, ax = plt.subplots(figsize=(8, 5))

#define horizontal bar chart
bars = ax.barh(
    departments,
    patients,
    color="steelblue",
    edgecolor="black"
)

#define value labels
ax.bar_label(bars)

#define title and label
ax.set_title("Weekly Patient Admissions by Department")
ax.set_xlabel("Number of Patients")
ax.set_ylabel("Hospital Department")

#enable grid
ax.grid(True, axis="x")

#show
plt.tight_layout()
plt.show()