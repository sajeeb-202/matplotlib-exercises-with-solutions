# 019. Satellite Power and Temperature Monitoring

**Difficulty:** 🟡 Medium

**Estimated Time:** 35–45 minutes

**Topics:** Dual Y-Axis, `twinx()`

---

## Business Scenario

An aerospace company monitors the health of a satellite during one orbital cycle.

Engineers want to observe how the satellite's battery level changes alongside its internal temperature.

Since battery percentage (%) and temperature (°C) use different units, both measurements should be displayed on the same timeline using separate Y-axes.

As a Data Analyst, create a professional visualization to monitor both measurements.

---

## Dataset

```python
time = [
    "00",
    "03",
    "06",
    "09",
    "12",
    "15",
    "18",
    "21"
]

battery = [
    100,
    97,
    94,
    90,
    86,
    82,
    79,
    75
]

temperature = [
    18,
    22,
    27,
    31,
    35,
    33,
    28,
    23
]
```

---

## Requirements

Create exactly **one figure**.

### Figure

- Figure size must be **8 × 5 inches**.

---

## Primary Axis

Create a line chart for battery level.

Properties

| Property | Value |
|----------|-------|
| Color | Royal Blue |
| Marker | Circle (`o`) |
| Line Width | 2 |

Y-axis Label

```text
Battery Level (%)
```

---

## Secondary Axis

Create another line chart for temperature.

Properties

| Property | Value |
|----------|-------|
| Color | Firebrick |
| Marker | Square (`s`) |
| Line Width | 2 |

Y-axis Label

```text
Temperature (°C)
```

---

## Shared X-axis

Label

```text
Time (Hours)
```

---

## Title

```text
Satellite Battery and Temperature Monitoring
```

---

## Grid

Enable the grid **only for the primary axis on the Y-axis**.

---

## Constraints

Your solution must satisfy all of the following.

- Use Matplotlib Object-Oriented API.
- Use `ax.twinx()`.
- Do not modify the dataset.
- Do not create multiple figures.
- Do not use Seaborn.

---

## Expected Output

The visualization should contain

- One figure
- Two Y-axes
- Two line charts
- Professional title
- Axis labels
- Grid on the primary Y-axis
- Figure size **8 × 5**

The final result should closely match **output.png**.