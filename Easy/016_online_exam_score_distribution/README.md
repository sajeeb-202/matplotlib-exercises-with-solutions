# 016. Online Exam Score Distribution

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Violin Plot, `violinplot()`

---

## Business Scenario

An online learning platform wants to analyze the distribution of final exam scores across three different courses.

Unlike a box plot, the platform also wants to understand where scores are more concentrated within each course.

As a Data Analyst, create a professional violin plot to visualize the score distributions.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing final exam scores.

```python
python_scores = [
    62, 68, 71, 74, 76,
    79, 81, 84, 87, 91
]

sql_scores = [
    55, 60, 64, 67, 70,
    73, 75, 78, 82, 86
]

machine_learning_scores = [
    58, 63, 69, 72, 77,
    80, 83, 86, 90, 94
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create a **violin plot**.

Display one violin for each course.

---

### X-axis Categories

Display the following course names on the X-axis.

- Python
- SQL
- Machine Learning

---

### Title

```text
Online Course Exam Score Distribution
```

---

### X-axis Label

```text
Course
```

---

### Y-axis Label

```text
Exam Score
```

---

### Grid

- Enable the grid.
- Display the grid **only on the Y-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API**.
- Use `ax.violinplot()`.
- Do **not** use Seaborn or any other visualization library.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.

---

## Expected Output

Your visualization should contain:

- One violin plot
- Three violins
- Course names on the X-axis
- Professional title
- Axis labels
- Grid on the Y-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.