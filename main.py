import os
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

students_data = [
    ('Amit', 78), ('Priya', 92), ('Rahul', 65),
    ('Sneha', 88), ('Vikas', 55), ('Neha', 74),
    ('Arjun', 96), ('Kiran', 82), ('Riya', 69),
    ('Ankit', 90)
]


class Student:
    def __init__(self, name, marks):
        self.__name = name      # private variable
        self.__marks = marks    # private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")

    def get_grade(self):
        m = self.__marks
        if m >= 90:
            return "O (Outstanding)"
        elif m >= 80:
            return "A+ (Excellent)"
        elif m >= 70:
            return "A (Very Good)"
        elif m >= 60:
            return "B (Good)"
        elif m >= 50:
            return "C (Average)"
        else:
            return "F (Fail)"

    def display(self):
        status = "PASS" if self.__marks >= 50 else "FAIL"
        print(f"  Name: {self.__name}  |  Marks: {self.__marks}  |  Grade: {self.get_grade()}  |  {status}")


# Inheritance
class TopStudent(Student):
    def __init__(self, name, marks, achievement):
        super().__init__(name, marks)
        self.achievement = achievement

    # Polymorphism - overriding display()
    def display(self):
        super().display()
        print(f"  Achievement: {self.achievement}")


student_list = []
student_dict = {}


def load_default_data():
    student_list.clear()
    student_dict.clear()
    for name, marks in students_data:
        s = Student(name, marks)
        student_list.append(s)
        student_dict[name] = marks
    print(f"\n  {len(student_list)} students loaded successfully.")


def display_all_students():
    if len(student_list) == 0:
        print("  No students found.")
        return
    print("\n" + "=" * 55)
    print("  ALL STUDENTS")
    print("=" * 55)
    print(f"  {'No':<4} {'Name':<12} {'Marks':>5}  {'Grade':<20} Status")
    print("-" * 55)
    for i, s in enumerate(student_list, 1):
        status = "PASS" if s.get_marks() >= 50 else "FAIL"
        print(f"  {i:<4} {s.get_name():<12} {s.get_marks():>5}  {s.get_grade():<20} {status}")
    print("=" * 55)
    total = sum(s.get_marks() for s in student_list)
    print(f"  Class Average: {total / len(student_list):.2f}")


def add_student():
    print("\n--- ADD STUDENT ---")
    name = input("  Enter Name  : ").strip().title()
    if name in student_dict:
        print("  Student already exists!")
        return
    try:
        marks = int(input("  Enter Marks (0-100): "))
        if marks < 0 or marks > 100:
            print("  Invalid marks. Must be 0-100.")
            return
        s = Student(name, marks)
        student_list.append(s)
        student_dict[name] = marks
        print(f"  '{name}' added. Grade: {s.get_grade()}")
    except ValueError:
        print("  Please enter a valid number.")


def update_student():
    print("\n--- UPDATE MARKS ---")
    name = input("  Enter student name: ").strip().title()
    if name not in student_dict:
        print("  Student not found.")
        return
    try:
        new_marks = int(input("  Enter new marks: "))
        if new_marks < 0 or new_marks > 100:
            print("  Invalid marks.")
            return
        for s in student_list:
            if s.get_name() == name:
                s.set_marks(new_marks)
                student_dict[name] = new_marks
                print(f"  Updated! New grade: {s.get_grade()}")
                break
    except ValueError:
        print("  Please enter a valid number.")


def delete_student():
    print("\n--- DELETE STUDENT ---")
    name = input("  Enter student name to delete: ").strip().title()
    if name not in student_dict:
        print("  Student not found.")
        return
    for s in student_list:
        if s.get_name() == name:
            student_list.remove(s)
            del student_dict[name]
            print(f"  '{name}' deleted successfully.")
            break


def search_student():
    print("\n--- SEARCH STUDENT ---")
    name = input("  Enter student name: ").strip().title()
    found = False
    for s in student_list:
        if s.get_name() == name:
            print(f"\n  Found:")
            s.display()
            found = True
            break
    if not found:
        print("  Student not found.")


def calculate_statistics():
    if len(student_list) == 0:
        print("  No data available.")
        return

    marks = [s.get_marks() for s in student_list]
    marks_sorted = sorted(marks)
    n = len(marks)

    mean = sum(marks) / n

    mid = n // 2
    if n % 2 == 0:
        median = (marks_sorted[mid - 1] + marks_sorted[mid]) / 2
    else:
        median = marks_sorted[mid]

    freq = Counter(marks)
    max_freq = max(freq.values())
    mode = [k for k, v in freq.items() if v == max_freq]

    data_range = max(marks) - min(marks)

    variance = sum((x - mean) ** 2 for x in marks) / n
    std_dev = math.sqrt(variance)

    def get_quartile(data, q):
        pos = (len(data) + 1) * q / 4
        lower = max(0, int(pos) - 1)
        upper = min(len(data) - 1, lower + 1)
        frac = pos - int(pos)
        return data[lower] + frac * (data[upper] - data[lower])

    q1 = get_quartile(marks_sorted, 1)
    q2 = get_quartile(marks_sorted, 2)
    q3 = get_quartile(marks_sorted, 3)
    iqr = q3 - q1

    print("\n" + "=" * 45)
    print("  DESCRIPTIVE STATISTICS")
    print("=" * 45)
    print(f"  Count      : {n}")
    print(f"  Mean       : {mean:.2f}")
    print(f"  Median     : {median:.2f}")
    print(f"  Mode       : {mode}")
    print(f"  Range      : {data_range}")
    print(f"  Variance   : {variance:.2f}")
    print(f"  Std Dev    : {std_dev:.2f}")
    print(f"  Q1         : {q1:.2f}")
    print(f"  Q2         : {q2:.2f}")
    print(f"  Q3         : {q3:.2f}")
    print(f"  IQR        : {iqr:.2f}")
    print(f"  Min        : {min(marks)}")
    print(f"  Max        : {max(marks)}")
    print("=" * 45)


def calculate_probability():
    if len(student_list) == 0:
        print("  No data available.")
        return

    total = len(student_list)
    marks = [s.get_marks() for s in student_list]

    print("\n" + "=" * 45)
    print("  PROBABILITY ANALYSIS")
    print("=" * 45)

    pass_count = sum(1 for m in marks if m >= 50)
    p_pass = pass_count / total
    print(f"\n  P(Student passes) = {pass_count}/{total} = {p_pass:.2f} ({p_pass*100:.1f}%)")

    above75 = sum(1 for m in marks if m > 75)
    p_above75 = above75 / total
    print(f"  P(Marks > 75)     = {above75}/{total} = {p_above75:.2f} ({p_above75*100:.1f}%)")

    below60 = sum(1 for m in marks if m < 60)
    p_below60 = below60 / total
    print(f"  P(Marks < 60)     = {below60}/{total} = {p_below60:.2f} ({p_below60*100:.1f}%)")

    grade_o = sum(1 for m in marks if m >= 90)
    p_grade_o = grade_o / total
    print(f"  P(Grade O >=90)   = {grade_o}/{total} = {p_grade_o:.2f} ({p_grade_o*100:.1f}%)")

    print(f"\n  Conditional Probability: P(marks > 80 | marks > 60)")
    count_b = sum(1 for m in marks if m > 60)
    count_ab = sum(1 for m in marks if m > 80 and m > 60)
    p_b = count_b / total
    p_ab = count_ab / total
    cond = p_ab / p_b if p_b > 0 else 0
    print(f"  P(marks > 60)        = {count_b}/{total} = {p_b:.2f}")
    print(f"  P(marks > 80 & > 60) = {count_ab}/{total} = {p_ab:.2f}")
    print(f"  P(A|B)               = {p_ab:.2f} / {p_b:.2f} = {cond:.4f} ({cond*100:.1f}%)")
    print("=" * 45)


def generate_charts():
    if len(student_list) < 2:
        print("  Need at least 2 students to generate charts.")
        return

    names = [s.get_name() for s in student_list]
    marks = [s.get_marks() for s in student_list]
    mean_val = sum(marks) / len(marks)

    print("\n  Generating charts...")

    # Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(marks, bins=5, color='steelblue', edgecolor='black')
    plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean = {mean_val:.1f}')
    plt.title('Marks Distribution - Histogram')
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.legend()
    plt.tight_layout()
    plt.savefig('screenshots/01_histogram.png')
    plt.close()
    print("  Saved: 01_histogram.png")

    # Bar Chart
    plt.figure(figsize=(10, 5))
    colors = ['green' if m >= 70 else 'orange' if m >= 50 else 'red' for m in marks]
    plt.bar(names, marks, color=colors, edgecolor='black')
    for i, m in enumerate(marks):
        plt.text(i, m + 0.5, str(m), ha='center', fontsize=9)
    plt.title('Student Marks - Bar Chart')
    plt.xlabel('Student')
    plt.ylabel('Marks')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('screenshots/02_bar_chart.png')
    plt.close()
    print("  Saved: 02_bar_chart.png")

    # Box Plot
    plt.figure(figsize=(6, 6))
    plt.boxplot(marks, patch_artist=True,
                boxprops=dict(facecolor='lightblue'),
                medianprops=dict(color='red', linewidth=2))
    plt.title('Marks Distribution - Box Plot')
    plt.ylabel('Marks')
    plt.xticks([1], ['All Students'])
    plt.tight_layout()
    plt.savefig('screenshots/03_box_plot.png')
    plt.close()
    print("  Saved: 03_box_plot.png")

    # Scatter Plot
    x = list(range(1, len(names) + 1))
    plt.figure(figsize=(9, 5))
    plt.scatter(x, marks, color='purple', s=100, zorder=3)
    for i, (name, mark) in enumerate(zip(names, marks)):
        plt.annotate(name, (i + 1, mark), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=8)
    plt.axhline(mean_val, color='green', linestyle='--', label=f'Mean = {mean_val:.1f}')
    plt.title('Marks per Student - Scatter Plot')
    plt.xlabel('Student Index')
    plt.ylabel('Marks')
    plt.xticks(x, names, rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.savefig('screenshots/04_scatter_plot.png')
    plt.close()
    print("  Saved: 04_scatter_plot.png")

    # Line Chart
    sorted_data = sorted(zip(names, marks), key=lambda x: x[1], reverse=True)
    s_names = [d[0] for d in sorted_data]
    s_marks = [d[1] for d in sorted_data]
    plt.figure(figsize=(10, 5))
    plt.plot(s_names, s_marks, color='blue', marker='o', linewidth=2, markersize=8)
    for name, mark in zip(s_names, s_marks):
        plt.annotate(str(mark), (name, mark), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9)
    plt.title('Student Performance - Line Chart (Sorted)')
    plt.xlabel('Student')
    plt.ylabel('Marks')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('screenshots/05_line_chart.png')
    plt.close()
    print("  Saved: 05_line_chart.png")

    print("\n  All 5 charts saved in 'screenshots/' folder.")


def oop_demo():
    print("\n" + "=" * 45)
    print("  OOP DEMONSTRATION")
    print("=" * 45)

    print("\n  Encapsulation:")
    s = Student("Demo Student", 85)
    print(f"  Name (via getter): {s.get_name()}")
    print(f"  Marks (via getter): {s.get_marks()}")
    s.set_marks(90)
    print(f"  Updated marks: {s.get_marks()}")

    print("\n  Inheritance & Polymorphism:")
    ts = TopStudent("Arjun", 96, "State Rank Holder")
    print("\n  Student.display():")
    s.display()
    print("\n  TopStudent.display():")
    ts.display()
    print("=" * 45)


def show_data_snapshot():
    print("\n" + "=" * 45)
    print("  COLLECTIONS SNAPSHOT")
    print("=" * 45)

    print("\n  List - Student objects:")
    for i, s in enumerate(student_list):
        print(f"    [{i}] {s.get_name()} - {s.get_marks()}")

    print("\n  Tuple - (name, marks):")
    tuples = [(s.get_name(), s.get_marks()) for s in student_list]
    for t in tuples:
        print(f"    {t}")

    print("\n  Dict - name -> marks:")
    for key, val in student_dict.items():
        print(f"    '{key}': {val}")

    print("=" * 45)


def show_menu():
    print("\n" + "=" * 45)
    print("   STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 45)
    print("  1. Display All Students")
    print("  2. Add Student")
    print("  3. Update Student Marks")
    print("  4. Delete Student")
    print("  5. Search Student")
    print("  6. Descriptive Statistics")
    print("  7. Probability Analysis")
    print("  8. Generate All Charts")
    print("  9. OOP Demo")
    print(" 10. Collections Snapshot")
    print("  0. Exit")
    print("=" * 45)


def main():
    load_default_data()

    while True:
        show_menu()
        choice = input("\n  Enter choice: ").strip()

        if choice == '1':
            display_all_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            calculate_statistics()
        elif choice == '7':
            calculate_probability()
        elif choice == '8':
            generate_charts()
        elif choice == '9':
            oop_demo()
        elif choice == '10':
            show_data_snapshot()
        elif choice == '0':
            print("\n  Goodbye!\n")
            break
        else:
            print("  Invalid choice. Enter 0-10.")

        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()
