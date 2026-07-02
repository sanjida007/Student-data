class Student:
    def __init__(self, name, age, address, student_id):
        self.name = name
        self.age = age
        self.address = address
        self.student_id = student_id
        self.grades = {}  # Course: Grade
        self.courses = []  # List of course codes


class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student information
        self.courses = {}  # Dictionary to store course information

    def add_new_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("Error: Student ID already exists. Please enter a different ID.")
            return  # Stop adding the student
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        address = input("Enter Student Address: ")
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_new_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor: ")
        course = {"name": course_name, "code": course_code, "instructor": instructor}
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        if student_id not in self.students:
            print("Error: Student ID not found.")
            return
        course_code = input("Enter Course Code: ")
        if course_code not in self.courses:
            print("Error: Course Code not found.")
            return
        student = self.students[student_id]
        student.courses.append(course_code)
        print(f"Student {student_id} enrolled in course {course_code}.")

    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        if student_id not in self.students:
            print("Error: Student ID not found.")
            return
        course_code = input("Enter Course Code: ")
        if course_code not in self.courses:
            print("Error: Course Code not found.")
            return
        grade = input("Enter Grade: ")
        student = self.students[student_id]
        student.grades[course_code] = grade
        print(f"Grade {grade} added for student {student_id} in course {course_code}.")

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        if student_id not in self.students:
            print("Error: Student ID not found.")
            return
        student = self.students[student_id]
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Age: {student.age}")
        print(f"Address: {student.address}")
        print("Courses:", student.courses)
        print("Grades:", student.grades)

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        if course_code not in self.courses:
            print("Error: Course Code not found.")
            return
        course = self.courses[course_code]
        print(f"Course Code: {course['code']}")
        print(f"Name: {course['name']}")
        print(f"Instructor: {course['instructor']}")

    def run(self):
        while True:
            print("\n=== Student Management System ===")
            print("1. Add New Student")
            print("2. Add New Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade for Student")
            print("5. Display Student Details")
            print("6. Display Course Details")
            print("0. Exit")

            choice = input("Select Option: ")

            if choice == '1':
                self.add_new_student()
            elif choice == '2':
                self.add_new_course()
            elif choice == '3':
                self.enroll_student_in_course()
            elif choice == '4':
                self.add_grade_for_student()
            elif choice == '5':
                self.display_student_details()
            elif choice == '6':
                self.display_course_details()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")


# Create an instance of the StudentManagementSystem class
sms = StudentManagementSystem()

# Run the system
sms.run()
 
 
