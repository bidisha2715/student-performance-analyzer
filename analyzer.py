import csv

students = []

# GRADE FUNCTION
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# LOAD DATA
def load_data():
    global students
    students = []

    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            avg = (int(row["Math"]) + int(row["Science"]) + int(row["English"])) / 3
            students.append({
                "Name": row["Name"],
                "Average": round(avg, 2),
                "Grade": calculate_grade(avg)
            })

# SHOW ALL STUDENTS
def show_all():
    print("\n📊 All Students:")
    for s in students:
        print(f"{s['Name']} → Avg: {s['Average']} | Grade: {s['Grade']}")

# TOPPER
def show_topper():
    topper = max(students, key=lambda x: x["Average"])
    print(f"\n🏆 Topper: {topper['Name']} ({topper['Average']})")

# CLASS AVERAGE
def class_average():
    avg = sum(s["Average"] for s in students) / len(students)
    print(f"\n📈 Class Average: {round(avg, 2)}")

# SEARCH
def search_student():
    name = input("Enter student name: ").strip().lower()
    for s in students:
        if s["Name"].lower() == name:
            print(f"{s['Name']} → Avg: {s['Average']} | Grade: {s['Grade']}")
            return
    print("❌ Student not found")

# SAVE RESULTS
def save_results():
    with open("output.txt", "w") as f:
        for s in students:
            f.write(f"{s['Name']} - {s['Average']} - {s['Grade']}\n")
    print("✅ Results saved to output.txt")

# GRAPH
def show_graph():
    import matplotlib.pyplot as plt

    names = [s["Name"] for s in students]
    averages = [s["Average"] for s in students]

    plt.bar(names, averages)
    plt.title("Student Average Marks")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")

    plt.show()

# MENU
def menu():
    while True:
        print("\n==== Student Analyzer ====")
        print("1. Show all students")
        print("2. Show topper")
        print("3. Class average")
        print("4. Search student")
        print("5. Save results")
        print("6. Show graph")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            show_topper()
        elif choice == "3":
            class_average()
        elif choice == "4":
            search_student()
        elif choice == "5":
            save_results()
        elif choice == "6":
            show_graph()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# RUN PROGRAM
load_data()
menu()