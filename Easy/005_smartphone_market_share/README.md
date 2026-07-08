# 005. Smartphone Market Share Analysis

**Difficulty:** 🟢 Easy  
**Estimated Time:** 10–15 minutes  
**Topics:** Pie Chart, Labels, Shadow, Start Angle

---

## Business Scenario

A market research company conducted a survey on smartphone brands used by customers in a metropolitan city. The company wants a simple visualization to present each brand's market share during a business meeting.

As a Data Analyst, your task is to create a clear and professional pie chart using Matplotlib.

---

## Dataset

```python
brands = [
    "Samsung",
    "Apple",
    "Xiaomi",
    "Realme",
    "Others"
]

market_share = [35, 28, 18, 10, 9]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

### Plot

Create a **pie chart** using the dataset above.

| Property | Value |
|----------|-------|
| Labels | Brand Names |
| Autopct | Show percentages with one decimal place |
| Start Angle | 90° |
| Shadow | Enabled |

---

### Title

```text
Smartphone Market Share
```

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Do **not** use `plt.pie()` directly.
- Do **not** modify the dataset.
- Do **not** create multiple figures.
- Do **not** use Seaborn or any other visualization library.

---

## Expected Output

Your visualization should contain:

- Five pie slices
- Percentage labels
- Shadow enabled
- Starting angle of **90°**
- Figure size **8 × 5**
- Appropriate title

The final result should closely match **output.png**.