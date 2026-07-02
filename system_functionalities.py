import json

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_new_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        self.students[student_id] = student_id
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_new_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor: ")
        course = course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            course.add_student(student)
            student.enroll_course(course_code)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid Student ID or Course Code.")

    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            if course_code in student.courses:
                student.add_grade(course_code, grade)
                print(f"Grade {grade} added for {student.name} in {course_code}.")
            else:
                print("Student not enrolled in this course.")
        else:
            print("Invalid Student ID or Course Code.")

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            print("Student Information:")
            student.display_student_info()
        else:
            print("Invalid Student ID.")

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        if course_code in self.courses:
            course = self.courses[course_code]
            print("Course Information:")
            course.display_course_info()
        else:
            print("Invalid Course Code.")

    def save_data(self):
        student_data = {student_id: student.__dict__ for student_id, student in self.students.items()}
        course_data = {course_code: course.__dict__ for course_code, course in self.courses.items()}
        data = {"students": student_data, "courses": course_data}
        with open("sms_data.json", "w") as file:
            json.dump(data, file)
        print("All student and course data saved successfully.")

        def load_data(self):
            try:
                with open("sms_data.json", "r") as file:
                    # Load data from the file
                    pass  # Replace with loading logic
            except FileNotFoundError:
                print("Data file not found. starting with an empty system.")
                # Initialize data structures as empty
                self.students = {}
                self.courses = {} 

    def load_data(self):
        try:
            with open("sms_data.json", "r") as file:
                data = json.load(file)
                # Load students
                for student_id, student_data in data["students"].items():
                    student = student(student_data['name'], student_data['age'], student_data['address'], student_data['student_id'])
                    student.grades = student_data['grades']
                    student.courses = student_data['courses']
                    self.students[student_id] = student
                # Load courses
                for course_code, course_data in data["courses"].items():
                    course = course(course_data['course_name'], course_data['course_code'], course_data['instructor'])
                    # Manually add students to the course (linking from student objects)
                    for student_id in course_data.get('students', []):
                        if student_id in self.students:
                            course.add_student(self.students[student_id])
                    self.courses[course_code] = course
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No data file found. Starting with an empty system.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def run(self):
        self.load_data()
        while True:
            print("\n==== Student Management System ====")
            print("1. Add New Student")
            print("2. Add New Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade for Student")
            print("5. Display Student Details")
            print("6. Display Course Details")
            print("7. Save Data to File")
            print("8. Load Data from File")
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
            elif choice == '7':
                self.save_data()
            elif choice == '8':
                self.load_data()
            elif choice == '0':
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()