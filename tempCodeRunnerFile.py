import json
import os

FILE_NAME = "student.json"

# ------------ Class ---------------------
class Student:
    def __init__(self, sid, name, age, course):
        self.sid = sid
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

# ------------ File Handling -----------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ------------ Functions ----------------
def add_student():
    try:
        sid = int(input("Enter student id: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter student course: ")

        student = Student(sid, name, age, course)

        data = load_data()

        # check duplicate ID
        for s in data:
            if s['sid'] == sid:
                print("Student ID already exists!")
                return

        data.append(student.to_dict())
        save_data(data)
        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data.")

def view_student():
    data = load_data()
    if not data:
        print("No student data found.")
        return

    for student in data:
        print("\n--------------------")
        print(f"ID: {student['sid']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")

def search_student():
    try:
        sid = int(input("Enter student id: "))
        data = load_data()

        for student in data:
            if student['sid'] == sid:
                print("\nStudent Found:")
                print(student)
                return

        print("Student not found.")

    except ValueError:
        print("Invalid input!")

def update_student():
    try:
        sid = int(input("Enter student id: "))
        data = load_data()

        for student in data:
            if student['sid'] == sid:
                student['name'] = input("Enter new name: ")
                student['age'] = int(input("Enter new age: "))
                student['course'] = input("Enter new course: ")

                save_data(data)
                print("Student updated successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid input!")

def delete_student():
    try:
        sid = int(input("Enter student id: "))
        data = load_data()

        new_data = [s for s in data if s['sid'] != sid]

        if len(data) == len(new_data):
            print("Student not found!")
        else:
            save_data(new_data)
            print("Student deleted successfully!")

    except ValueError:
        print("Invalid input!")

# ------------ Menu ----------------
def menu():
    while True:
        print("\n============= Student Management System =============")
        print("1. Add student")
        print("2. View student")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                view_student()
            elif choice == 3:
                search_student()
            elif choice == 4:
                update_student()
            elif choice == 5:
                delete_student()
            elif choice == 6:
                print("Thank you for using this program!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")

# ------------ Run Program ----------------
if __name__ == "__main__":
    menu()