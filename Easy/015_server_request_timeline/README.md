# 015. Server Request Timeline

**Difficulty:** 🟢 Easy+

**Estimated Time:** 20–25 minutes

**Topics:** Event Plot, `eventplot()`

---

## Business Scenario

A cloud service provider monitors the exact times when user requests arrive at a web server.

Instead of counting requests, the operations team wants to visualize **when** each request occurred during the day.

As a Data Analyst, create a professional event plot to display the request timeline.

---

## Dataset

The dataset below is a **synthetic but realistic** sample representing request arrival times (in minutes after 9:00 AM).

```python
request_times = [
    3,
    8,
    12,
    18,
    26,
    33,
    41,
    49,
    58
]
```

---

## Requirements

Create **exactly one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

### Plot

Create an **event plot**.

Use the following properties.

| Property | Value |
|----------|-------|
| Orientation | Horizontal |
| Color | Royal Blue |
| Line Offset | 1 |
| Line Length | 0.8 |

---

### Title

```text
Server Request Timeline
```

---

### X-axis Label

```text
Minutes After 9:00 AM
```

---

### Y-axis Label

```text
Server
```

---

### Grid

- Enable the grid.
- Display the grid **only on the X-axis**.

---

## Constraints

Your solution **must** satisfy all of the following:

- Use Matplotlib's **Object-Oriented API** (`Figure` and `Axes`).
- Use `ax.eventplot()`.
- Do **not** use Seaborn or any other visualization library.
- Do **not** modify the provided dataset.
- Do **not** create multiple figures.

---

## Expected Output

Your visualization should contain:

- One horizontal event plot
- Royal blue event lines
- Professional title
- Axis labels
- Grid on the X-axis only
- Figure size **8 × 5**

The final result should closely match **output.png**.