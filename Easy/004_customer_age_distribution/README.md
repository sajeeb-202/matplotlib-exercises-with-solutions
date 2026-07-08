# 004. Customer Age Distribution

**Difficulty:** 🟢 Easy  
**Estimated Time:** 10–15 minutes  
**Topics:** Histogram, Figure, Axes, Labels, Title, Grid

---

## Problem

A retail company wants to understand the age distribution of its customers to support future marketing campaigns.

Using **Matplotlib**, create a histogram that visualizes the distribution of customer ages.

---

## Dataset

```python
customer_ages = [
    18, 19, 20, 21, 22, 22, 23, 24, 24, 25,
    25, 26, 27, 28, 28, 29, 30, 31, 32, 33,
    34, 35, 36, 37, 38, 40, 42, 45, 48, 50
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

### Plot

Create a **histogram** using the dataset above.

| Property | Value |
|----------|-------|
| Number of Bins | 8 |
| Bar Color | Orange |
| Edge Color | Black |

### Title

```text
Customer Age Distribution
```

### X-axis Label

```text
Age
```

### Y-axis Label

```text
Number of Customers
```

### Grid

- Enable the grid.
- Display the grid **only on the Y-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Do **not** use `plt.hist()` directly.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---

## Expected Output

Your visualization should contain:

- Orange histogram bars
- Black bar borders
- 8 bins
- Figure size of **8 × 5**
- Title
- X-axis label
- Y-axis label
- Grid displayed only on the Y-axis

The final result should closely match **output.png**.