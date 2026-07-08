# 003. Student Study Time vs Exam Score

**Difficulty:** 🟢 Easy  
**Estimated Time:** 10–15 minutes  
**Topics:** Scatter Plot, Figure, Axes, Labels, Title, Grid

---

## Problem

A school wants to analyze whether students who study for more hours tend to achieve higher exam scores.

Using **Matplotlib**, create a visualization that shows the relationship between study hours and exam scores.

---

## Dataset

```python
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]

exam_scores = [48, 55, 60, 66, 72, 80, 88, 94]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

### Plot

Create a **scatter plot** using the dataset above with the following properties:

| Property | Value |
|----------|-------|
| Marker Color | Green |
| Marker Size | 80 |
| Marker Style | Circle (`o`) |

### Title

```text
Student Study Time vs Exam Score
```

### X-axis Label

```text
Study Hours
```

### Y-axis Label

```text
Exam Score
```

### Grid

- Enable the grid.
- Display the grid on **both axes**.

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

- Eight green circular markers
- Marker size of **80**
- Figure size of **8 × 5**
- Title
- X-axis label
- Y-axis label
- Grid enabled on both axes

The final result should closely match **`output.png`**.