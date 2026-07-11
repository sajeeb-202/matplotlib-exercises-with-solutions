# 011. Employee Salary Distribution

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Box Plot, Outliers

---

## Business Scenario

A company's Human Resources (HR) department wants to analyze employee salaries across different departments. They need a visualization that highlights the salary distribution and helps identify potential outliers.

As a Data Analyst, create a professional box plot to visualize the salary distribution of each department.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing monthly salaries (in USD).

```python
engineering = [
    5200, 5400, 5600, 5900, 6100,
    6300, 6400, 6500, 6800, 9200
]

marketing = [
    3600, 3800, 3900, 4100, 4200,
    4300, 4400, 4600, 4700, 5200
]

sales = [
    3100, 3300, 3400, 3600, 3700,
    3900, 4100, 4300, 4500, 6100
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **box plot**.

Display salary distributions for:

- Engineering
- Marketing
- Sales

---

### Title

```text
Employee Salary Distribution by Department
```

---

### X-axis Label

```text
Department
```

---

### Y-axis Label

```text
Monthly Salary (USD)
```

---

### Grid

- Enable the grid.
- Display the grid **only on the Y-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Do **not** use `plt.boxplot()` directly.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---

## Expected Output

Your visualization should contain:

- Three box plots
- Department names on the X-axis
- Professional title
- Axis labels
- Grid on the Y-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.