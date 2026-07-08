# 007. Weekly Patient Admissions by Department

**Difficulty:** 🟢 Easy+

**Estimated Time:** 15–20 minutes

**Topics:** Horizontal Bar Chart, Value Labels

---

## Business Scenario

A regional hospital reviews weekly patient admissions across its major departments to optimize staff allocation, bed availability, and medical resource planning.

The hospital's operations team requested a visualization that allows management to quickly compare patient volume between departments.

As a Data Analyst, create a professional horizontal bar chart that summarizes weekly admissions.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing one week's patient admissions.

```python
departments = [
    "Emergency",
    "Internal Medicine",
    "Cardiology",
    "Orthopedics",
    "Pediatrics",
    "Neurology"
]

patients = [
    245,
    198,
    132,
    118,
    176,
    94
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **horizontal bar chart**.

| Property | Value |
|----------|-------|
| Color | Steel Blue |
| Edge Color | Black |
| Bar Height | Default |

---

### Value Labels

Display the patient count at the **end of every bar**.

Example

```
Emergency ━━━━━━━━━━━━━━━━━━━━━━━ 245
```

---

### Title

```text
Weekly Patient Admissions by Department
```

---

### X-axis Label

```text
Number of Patients
```

---

### Y-axis Label

```text
Hospital Department
```

---

### Grid

- Enable the grid.
- Display the grid **only on the X-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Do **not** use `plt.barh()` directly.
- Do **not** modify the dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---


## Expected Output

Your visualization should contain:

- Horizontal bars
- Steel blue bars
- Black borders
- Value labels
- Professional title
- Axis labels
- Grid on the X-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.