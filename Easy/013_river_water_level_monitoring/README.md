# 013. River Water Level Monitoring

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Area Plot, `fill_between()`

---

## Business Scenario

A national flood monitoring agency records the average river water level every month to monitor seasonal changes and identify potential flood risks.

The agency wants a visualization that clearly shows how the water level changes throughout the year while emphasizing the area under the curve.

As a Data Analyst, create a professional area plot to visualize the monthly river water levels.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing average monthly river water levels (in meters).

```python
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug"
]

water_level = [
    2.4,
    2.6,
    3.1,
    3.8,
    4.6,
    5.3,
    5.0,
    4.2
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create an **area plot**.

Use the following properties.

| Property | Value |
|----------|-------|
| Fill Color | Sky Blue |
| Alpha | 0.5 |
| Edge Color | Royal Blue |
| Line Width | 2 |

---

### Title

```text
Monthly River Water Level
```

---

### X-axis Label

```text
Month
```

---

### Y-axis Label

```text
Water Level (Meters)
```

---

### Grid

- Enable the grid.
- Display the grid **only on the Y-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Use `ax.fill_between()`.
- Do **not** use Seaborn or any other visualization library.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.

---

## Expected Output

Your visualization should contain:

- One area plot
- Sky blue filled area
- Royal blue outline
- Alpha transparency of **0.5**
- Professional title
- Axis labels
- Grid on the Y-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.