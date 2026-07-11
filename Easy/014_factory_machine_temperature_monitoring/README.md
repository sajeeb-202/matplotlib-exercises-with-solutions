# 014. Factory Machine Temperature Monitoring

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Stem Plot, `stem()`

---

## Business Scenario

A manufacturing company continuously monitors the operating temperature of a production machine every hour.

The maintenance team wants a visualization that emphasizes each recorded measurement individually while still showing its magnitude from the baseline.

As a Data Analyst, create a professional stem plot to visualize the hourly machine temperatures.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing hourly machine temperatures (°C).

```python
hours = [
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15"
]

temperature = [
    62,
    65,
    69,
    74,
    71,
    68,
    66,
    64
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **stem plot**.

Use the following properties:

| Property | Value |
|----------|-------|
| Line Color | Royal Blue |
| Marker | Circle |
| Marker Face Color | Orange |
| Base Line Color | Gray |

---

### Title

```text
Hourly Machine Temperature
```

---

### X-axis Label

```text
Hour
```

---

### Y-axis Label

```text
Temperature (°C)
```

---

### Grid

- Enable the grid.
- Display the grid **only on the Y-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Use `ax.stem()`.
- Do **not** use Seaborn or any other visualization library.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.

---

## Expected Output

Your visualization should contain:

- One stem plot
- Royal blue stems
- Orange circular markers
- Gray baseline
- Professional title
- Axis labels
- Grid on the Y-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.