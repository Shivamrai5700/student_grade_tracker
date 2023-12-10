import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def add_student(students):
    name = input("Enter student name: ")
    grades = []
    while True:
        grade = input("Enter a grade (type 'done' to finish): ")
        if grade.lower() == 'done':
            break
        try:
            grade = float(grade)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    students[name] = grades
    print(f"{name}'s grades have been added.")
    
def update_grades(students):
    name = input("Enter student name to update grades: ")
    if name in students:
        grades = students[name]
        print(f"Current grades for {name}: {grades}")
        new_grades = []
        while True:
            grade = input("Enter a new grade (type 'done' to finish): ")
            if grade.lower() == 'done':
                break
            try:
                grade = float(grade)
                new_grades.append(grade)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        students[name] = new_grades
        print(f"{name}'s grades have been updated.")
    else:
        print(f"Student {name} not found.")

def display_students(students):
    for name, grades in students.items():
        average_grade = sum(grades) / len(grades) if grades else 0
        print(f"{name}: Grades - {grades}, Average Grade - {average_grade:.2f}")

def main():
    students = {}
    while True:
        clear_screen()
        print("Student Grade Tracker")
        print("1. Add a new student")
        print("2. Update grades for a student")
        print("3. Display all students")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_grades(students)
        elif choice == '3':
            display_students(students)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
