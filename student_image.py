from PIL import Image, ImageDraw, ImageFont

class Student:
    def __init__(self, name, age, address, student_id):
        self.name = name
        self.age = age
        self.address = address
        self.student_id = student_id
        self.grades = {}
        self.courses = []

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_new_student(self):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")

        student = Student(name, age, address, student_id)
        self.students[student_id] = student

        # Create image
        self.create_student_image(student)

        print(f"Student {name} (ID: {student_id}) added successfully.")

    def create_student_image(self, student):
        image_width = 600
        image_height = 400
        image = Image.new('RGB', (image_width, image_height), color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 20) # Replace "arial.ttf" with a valid font file

        text_color = 'black'
        text_x = 50
        text_y = 50
        line_spacing = 30

        lines = [
            f"Name: {student.name}",
            f"Age: {student.age}",
            f"Address: {student.address}",
            f"Student ID: {student.student_id}"
        ]

        for line in lines:
            draw.text((text_x, text_y), line, fill=text_color, font=font)
            text_y += line_spacing

        image.save(f"{student.student_id}.jpg")
        print(f"Image saved as {student.student_id}.jpg")


    def run(self):
        while True:
            print("\n=== Student Management System ===")
            print("1. Add New Student")
            print("0. Exit")

            choice = input("Select Option: ")

            if choice == '1':
                self.add_new_student()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")


# Main execution
sms = StudentManagementSystem()
sms.run()
