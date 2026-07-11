# 012. Product Price vs Customer Rating

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Bubble Chart, Marker Size

---

## Business Scenario

An e-commerce company wants to analyze whether product price is related to customer ratings. In addition to price and rating, the company also wants to visualize the popularity of each product based on the number of units sold.

As a Data Analyst, create a professional bubble chart to compare product prices, customer ratings, and units sold.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing six products.

```python
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
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **bubble chart**.

Use the following properties:

| Property | Value |
|----------|-------|
| Color | Royal Blue |
| Alpha | 0.6 |
| Bubble Size | Units Sold |

---

### Title

```text
Product Price vs Customer Rating
```

---

### X-axis Label

```text
Price (USD)
```

---

### Y-axis Label

```text
Customer Rating
```

---

### Grid

- Enable the grid.
- Display the grid **only on both axes**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Do **not** use `plt.scatter()` directly.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---

## Expected Output

Your visualization should contain:

- One bubble chart
- Bubble size proportional to units sold
- Royal blue bubbles
- Alpha transparency of **0.6**
- Professional title
- Axis labels
- Grid
- Figure size **8 × 5**

The final result should closely match **output.png**.