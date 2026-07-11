# 009. Monthly Revenue Breakdown

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Stacked Bar Chart, Bottom Parameter

---

## Business Scenario

An e-commerce company tracks revenue from two major product categories: **Physical Products** and **Digital Products**.

The finance team wants to visualize the **total monthly revenue** while also understanding how much each product category contributes to the total.

As a Data Analyst, create a professional stacked bar chart that displays the monthly revenue breakdown.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing monthly revenue (in thousand USD).

```python
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

physical_sales = [
    45,
    52,
    48,
    60,
    58,
    65
]

digital_sales = [
    18,
    22,
    25,
    24,
    28,
    30
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **stacked bar chart**.

#### Physical Products

| Property | Value |
|----------|-------|
| Color | Steel Blue |
| Label | Physical Products |

#### Digital Products

| Property | Value |
|----------|-------|
| Color | Orange |
| Label | Digital Products |
| Bottom | Physical Products |

---

### Title

```text
Monthly Revenue Breakdown
```

---

### X-axis Label

```text
Month
```

---

### Y-axis Label

```text
Revenue (Thousand USD)
```

---

### Legend

Display the legend in the **upper left** corner.

---

### Grid

- Enable the grid.
- Display the grid **only on the Y-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Do **not** use `plt.bar()` directly.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---

## Expected Output

Your visualization should contain:

- One stacked bar for each month
- Steel blue section representing Physical Products
- Orange section stacked on top representing Digital Products
- Professional title
- Axis labels
- Legend
- Grid on the Y-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.