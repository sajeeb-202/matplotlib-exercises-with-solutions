# 018. Earthquake Seismic Analysis

**Difficulty:** 🟡 Medium

**Estimated Time:** 35–45 minutes

**Topics:** Annotations, Highlighting Important Data Points

---

## Business Scenario

A geological research center monitors earthquake activity throughout the day.

Most earthquakes are minor, but strong earthquakes require immediate attention.

As a Data Analyst, create a visualization that displays earthquake magnitudes and automatically highlights the strongest earthquake on the chart.

---

## Dataset

```python
hours = [
    "00","03","06","09",
    "12","15","18","21"
]

magnitude = [
    2.1,
    2.8,
    3.2,
    2.9,
    4.7,
    3.8,
    5.4,
    3.1
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**

---

### Plot

Create a **line chart**.

Properties

| Property | Value |
|----------|-------|
| Color | Firebrick |
| Line Width | 2 |
| Marker | Circle |

---

### Annotation

Highlight the **largest earthquake**.

Requirements

- Add an arrow.
- Display the text

```text
Strongest Earthquake
```

pointing to the largest magnitude.

---

### Title

```text
Daily Earthquake Magnitude Monitoring
```

---

### X-axis Label

```text
Hour
```

---

### Y-axis Label

```text
Magnitude
```

---

### Grid

- Enable the grid.
- Display the grid only on the Y-axis.

---

## Constraints

Your solution must satisfy all of the following.

- Use Matplotlib Object-Oriented API.
- Use `ax.annotate()`.
- Do not modify the dataset.
- Do not create multiple figures.
- Do not use Seaborn.

---

## Expected Output

The visualization should contain

- One line chart
- One annotation with an arrow
- The strongest earthquake highlighted
- Professional title
- Axis labels
- Grid
- Figure size **8 × 5**

The final result should closely match **output.png**.