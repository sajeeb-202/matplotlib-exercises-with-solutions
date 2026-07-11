# 010. Monthly Energy Generation Sources

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Stack Plot, Alpha Transparency

---

## Business Scenario

A renewable energy company monitors electricity generation from three major renewable sources: **Solar**, **Wind**, and **Hydropower**.

The operations team wants to understand how each energy source contributes to the company's total monthly electricity generation.

As a Data Analyst, create a professional stack plot to visualize the monthly energy generation.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing monthly electricity generation (in gigawatt-hours).

```python
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun"
]

solar = [
    12,
    16,
    20,
    24,
    28,
    30
]

wind = [
    18,
    20,
    21,
    23,
    24,
    26
]

hydro = [
    30,
    31,
    30,
    29,
    28,
    27
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **stack plot**.

| Energy Source | Color |
|--------------|-------|
| Solar | Gold |
| Wind | Royal Blue |
| Hydropower | Forest Green |

Use **alpha = 0.8** for all three layers.

---

### Title

```text
Monthly Energy Generation Sources
```

---

### X-axis Label

```text
Month
```

---

### Y-axis Label

```text
Electricity Generation (GWh)
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
- Do **not** use `plt.stackplot()` directly.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---

## Expected Output

Your visualization should contain:

- One stack plot
- Three energy sources
- Gold, royal blue, and forest green colors
- Alpha transparency of **0.8**
- Professional title
- Axis labels
- Legend
- Grid on the Y-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.