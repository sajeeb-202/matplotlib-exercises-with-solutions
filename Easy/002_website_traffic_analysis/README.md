# 002. Website Traffic Analysis

**Difficulty:** 🟢 Easy  
**Estimated Time:** 10–15 minutes  
**Topics:** Bar Chart, Figure, Axes, Labels, Title, Grid

---

## Problem

A website administrator wants to analyze the number of visitors during the last seven days.

Using **Matplotlib**, create a visualization that clearly compares the daily website traffic.

---

## Dataset

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

visitors = [1200, 1450, 1380, 1670, 1820, 2100, 1950]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

### Plot

Create a **bar chart** using the dataset above with the following properties:

| Property | Value |
|----------|-------|
| Bar Color | Sky Blue |
| Bar Width | 0.6 |
| Edge Color | Black |

### Title

```text
Website Visitors Over the Last 7 Days
```

### X-axis Label

```text
Day
```

### Y-axis Label

```text
Number of Visitors
```

### Grid

- Enable the grid.
- Display the grid only on the **Y-axis**.

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

- Seven sky-blue bars with black borders
- Figure size of **8 × 5**
- Title
- X-axis label
- Y-axis label
- Grid displayed only on the Y-axis

The final result should closely match **`output.png`**.