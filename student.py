import os
import attendance as AT

class Student:
    STUDENT_FILE = "students.txt"
    ATTENDANCE_FILE = "attendance.txt"

    @staticmethod
    def register_student():
        reg_no = input("Enter Student Registration Number (unique): ")
        if Student.check_student_exists(reg_no):
            print("Student with this registration number already exists!")
            return
        name = input("Enter Student Name: ")
        dept = input("Enter Department: ")
        level = input("Enter Level: ")

        with open(Student.STUDENT_FILE, "a") as file:
            file.write(f"{reg_no},{name},{dept},{level}\n")
        print("Student registered successfully.")

    @staticmethod
    def check_student_exists(reg_no):
        if not os.path.exists(Student.STUDENT_FILE):
            return False
        with open(Student.STUDENT_FILE, "r") as file:
            students = file.readlines()
        for student in students:
            if student.startswith(reg_no + ","):
                return True
        return False
    
    @staticmethod
    def delete_student():
        reg_no = input("Enter the Registration Number of the Student to Delete: ")
        if not Student.check_student_exists(reg_no):
            print("Student not found!")
            return

        # Remove the student from the students.txt file
        with open(Student.STUDENT_FILE, "r") as file:
            students = file.readlines()
        with open(Student.STUDENT_FILE, "w") as file:
            for student in students:
                if not student.startswith(reg_no + ","):
                    file.write(student)

        # Remove the student's attendance from the attendance.txt file
        if os.path.exists(Student.ATTENDANCE_FILE):
            with open(Student.ATTENDANCE_FILE, "r") as file:
                records = file.readlines()
            with open(Student.ATTENDANCE_FILE, "w") as file:
                for record in records:
                    if not record.startswith(reg_no + ","):
                        file.write(record)

        print(f"Student with Registration Number {reg_no} and their attendance records have been deleted successfully.")


    @staticmethod
    def get_student_details(reg_no):
        if not os.path.exists(Student.STUDENT_FILE):
            return None
        with open(Student.STUDENT_FILE, "r") as file:
            students = file.readlines()
        for student in students:
            if student.startswith(reg_no + ","):
                return student.strip().split(",")
        return None
