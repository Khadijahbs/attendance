import os
import student as ST

class Attendance:
    @staticmethod
    def take_attendance():
        reg_no = input("Enter Student Registration Number: ")
        if not ST.Student.check_student_exists(reg_no):
            print("Student not found!")
            return
        status = input("Enter Attendance (1 for Present, 0 for Absent): ")
        if status not in ["1", "0"]:
            print("Invalid attendance status. Use 1 for Present and 0 for Absent.")
            return

        with open(ST.Student.ATTENDANCE_FILE, "a") as file:
            file.write(f"{reg_no},{status}\n")
        print("Attendance recorded successfully.")

    @staticmethod
    def generate_report():
        reg_no = input("Enter Student Registration Number: ")
        if not ST.Student.check_student_exists(reg_no):
            print("Student not found!")
            return

        total_classes = 0
        present_count = 0

        if not os.path.exists(ST.Student.ATTENDANCE_FILE):
            print("No attendance records found.")
            return

        with open(ST.Student.ATTENDANCE_FILE, "r") as file:
            records = file.readlines()

        print("\nAttendance Report:")
        for record in records:
            student_id, status = record.strip().split(",")
            if student_id == reg_no:
                total_classes += 1
                if status == "1":
                    present_count += 1

        if total_classes == 0:
            print("No attendance records found for this student.")
            return

        percentage = (present_count / total_classes) * 100
        print(f"Total Classes: {total_classes}")
        print(f"Present: {present_count}")
        print(f"Absent: {total_classes - present_count}")
        print(f"Attendance Percentage: {percentage:.2f}%\n")

