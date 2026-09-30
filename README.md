# Student Performance Analytics System

A Python application that manages student marks, performs statistical analysis,
and visualizes data using matplotlib.

---

## How to Run

```bash
pip install matplotlib
python main.py
```

---

## Folder Structure

```
StudentPerformanceAnalytics/
├── main.py           -> Main application
├── screenshots/      -> Chart images saved here
│   ├── 01_histogram.png
│   ├── 02_bar_chart.png
│   ├── 03_box_plot.png
│   ├── 04_scatter_plot.png
│   └── 05_line_chart.png
├── README.md
└── video/
    └── explanation_video.mp4
```

---

## Dataset

10 students pre-loaded in the system:

| Name  | Marks |
|-------|-------|
| Amit  | 78    |
| Priya | 92    |
| Rahul | 65    |
| Sneha | 88    |
| Vikas | 55    |
| Neha  | 74    |
| Arjun | 96    |
| Kiran | 82    |
| Riya  | 69    |
| Ankit | 90    |

---

## Menu Options

```
  1. Display All Students
  2. Add Student
  3. Update Student Marks
  4. Delete Student
  5. Search Student
  6. Descriptive Statistics
  7. Probability Analysis
  8. Generate All Charts
  9. OOP Demo
 10. Collections Snapshot
  0. Exit
```

---

## OOP Concepts

**Student class** - stores name and marks as private variables (Encapsulation).
Uses getter/setter methods to access them.

**TopStudent class** - inherits from Student (Inheritance).
Overrides the display() method (Polymorphism).

---

## Statistics Calculated

- Mean, Median, Mode
- Range, Variance, Standard Deviation
- Q1, Q2, Q3, IQR

---

## Probability

- P(Student passes)
- P(Marks > 75)
- P(Marks < 60)
- P(Grade O)
- Conditional Probability: P(marks > 80 | marks > 60)

---

## Charts Generated

| Chart | File |
|-------|------|
| Histogram | 01_histogram.png |
| Bar Chart | 02_bar_chart.png |
| Box Plot | 03_box_plot.png |
| Scatter Plot | 04_scatter_plot.png |
| Line Chart | 05_line_chart.png |

---

## Collections Used

- **List** - stores Student objects
- **Dictionary** - stores name to marks mapping
- **Tuple** - used for the default dataset and snapshots
