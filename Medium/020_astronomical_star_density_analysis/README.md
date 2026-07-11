# 020. Astronomical Star Density Analysis

**Difficulty:** 🟡 Medium

**Estimated Time:** 35–45 minutes

**Topics:** Contour Plot, `contour()`

---

## Business Scenario

An astronomical observatory studies the density of stars in a region of the night sky.

The researchers have converted telescope observations into a two-dimensional density field.

Instead of displaying individual stars, they want contour lines that connect regions with the same density.

As a Data Analyst, create a professional contour plot to visualize the star density.

---

## Dataset

```python
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

Z = np.exp(-(X**2 + Y**2))
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **contour plot**.

Use the following properties.

| Property | Value |
|----------|-------|
| Levels | 10 |
| Color | Royal Blue |

---

### Title

```text
Astronomical Star Density
```

---

### X-axis Label

```text
X Coordinate
```

---

### Y-axis Label

```text
Y Coordinate
```

---

### Grid

Do **not** display a grid.

---

## Constraints

Your solution must satisfy all of the following.

- Use Matplotlib Object-Oriented API.
- Use `ax.contour()`.
- Do not modify the dataset.
- Do not create multiple figures.
- Do not use Seaborn.

---

## Expected Output

The visualization should contain

- One contour plot
- Ten contour levels
- Royal blue contour lines
- Professional title
- Axis labels
- No grid
- Figure size **8 × 5**

The final result should closely match **output.png**.