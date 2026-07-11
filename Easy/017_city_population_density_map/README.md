# 017. City Population Density Map

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Hexbin Plot, `hexbin()`

---

## Business Scenario

An urban planning department wants to analyze where residents are concentrated within a city.

Each point represents the location of a household. Since thousands of households can overlap in the same area, the department wants a visualization that groups nearby points into hexagonal bins.

As a Data Analyst, create a professional hexbin plot to visualize the population density.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing household locations.

```python
import numpy as np

np.random.seed(42)

x = np.random.normal(50, 12, 600)
y = np.random.normal(50, 10, 600)
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **hexbin plot**.

Use the following properties.

| Property | Value |
|----------|-------|
| Grid Size | 20 |
| Color Map | Blues |

---

### Colorbar

Display a colorbar.

Label:

```text
Number of Households
```

---

### Title

```text
City Population Density Map
```

---

### X-axis Label

```text
East-West Position
```

---

### Y-axis Label

```text
North-South Position
```

---

### Grid

Do **not** display a grid.

---

## Constraints

Your solution must satisfy all of the following:

- Use Matplotlib's **Object-Oriented API**.
- Use `ax.hexbin()`.
- Use `np.random.seed(42)` exactly as provided.
- Do **not** modify the dataset generation.
- Do **not** create multiple figures.
- Do **not** use Seaborn.

---

## Expected Output

Your visualization should contain:

- One hexbin plot
- Blues colormap
- Grid size of 20
- One colorbar
- Professional title
- Axis labels
- No grid
- Figure size **8 × 5**

The final result should closely match **output.png**.