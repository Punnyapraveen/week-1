class Student:
    def __init__(self, student_id, name):
        # Initialize a student with ID and name
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}"

class StudentManagementSystem:
    def __init__(self):
        # Store students in a dictionary (ID -> Student)
        self.students = {}

    def add_student(self, student_id, name):
        # Add a new student
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = Student(student_id, name)
            print("Student added successfully.")

    def remove_student(self, student_id):
        # Remove a student by ID
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed successfully.")
        else:
            print("Student ID not found.")

    def search_student(self, student_id):
        # Search and display student by ID
        if student_id in self.students:
            print("Student found:", self.students[student_id])
        else:
            print("Student not found.")

    def list_students(self):
        # List all students
        if self.students:
            print("All students:")
            for student in self.students.values():
                print(student)
        else:
            print("No students in the system.")

# Interactive menu
def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. List All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            system.add_student(student_id, name)
        elif choice == "2":
            student_id = input("Enter student ID to remove: ")
            system.remove_student(student_id)
        elif choice == "3":
            student_id = input("Enter student ID to search: ")
            system.search_student(student_id)
        elif choice == "4":
            system.list_students()
        elif choice == "5":
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
