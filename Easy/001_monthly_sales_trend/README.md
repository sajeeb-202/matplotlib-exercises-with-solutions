# 001. Monthly Sales Trend

**Difficulty:** 🟢 Easy  
**Estimated Time:** 10–15 minutes  
**Topics:** Line Plot, Figure, Axes, Labels, Legend, Grid

---

## Problem

A retail company has recorded its monthly sales for the first half of the year. Your task is to create a visualization that clearly presents the sales trend over time.

Using **Matplotlib**, generate a line chart that satisfies all of the requirements below.

---

## Dataset

```python
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 160, 210, 250]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

### Plot

Create a **line plot** using the dataset above with the following properties:

| Property | Value |
|----------|-------|
| Color | Blue |
| Line Width | 2 |
| Marker | `o` |
| Marker Size | 8 |

### Title

```text
Monthly Sales Trend
```

### X-axis Label

```text
Month
```

### Y-axis Label

```text
Sales
```

### Legend

- Label: `Sales`
- Position: Upper Left

### Grid

Enable the grid.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Do **not** use `plt.plot()` directly.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---

## Expected Output

Your visualization should contain:

- A blue line chart
- Circular markers
- Figure size of **8 × 5**
- Title
- X-axis label
- Y-axis label
- Legend in the upper-left corner
- Grid

The final result should closely match **`output.png`**.