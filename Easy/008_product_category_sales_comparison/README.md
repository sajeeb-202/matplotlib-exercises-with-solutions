# 008. Product Category Sales Comparison

**Difficulty:** 🟢 Easy+

**Estimated Time:** 15–20 minutes

**Topics:** Grouped Bar Chart, NumPy Bar Positioning

---

## Business Scenario

A retail company wants to compare sales across different product categories for the first and second quarters of the year. The management team needs a visualization that clearly shows how sales changed between the two quarters for each product category.

As a Data Analyst, create a professional grouped bar chart to compare quarterly sales.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing quarterly sales (in thousand units).

```python
categories = [
    "Electronics",
    "Furniture",
    "Clothing",
    "Groceries",
    "Sports"
]

q1_sales = [85, 62, 74, 96, 58]

q2_sales = [92, 68, 79, 101, 64]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **grouped bar chart**.

#### Q1 Sales

| Property | Value |
|----------|-------|
| Color | Royal Blue |
| Width | 0.35 |
| Label | Q1 |

#### Q2 Sales

| Property | Value |
|----------|-------|
| Color | Orange |
| Width | 0.35 |
| Label | Q2 |

---

### Title

```text
Product Category Sales Comparison
```

---

### X-axis Label

```text
Product Category
```

---

### Y-axis Label

```text
Quarterly Sales (Thousand Units)
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

- Two bars for every product category
- Royal blue bars for Q1
- Orange bars for Q2
- Proper legend
- Grid on the Y-axis only
- Professional title
- Axis labels
- Figure size **8 × 5**

The final result should closely match **output.png**.