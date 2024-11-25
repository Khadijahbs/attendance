import os

# File paths
STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"

# Function to register a student
def register_student():
    reg_no = input("Enter Student Registration Number (unique): ")
    if check_student_exists(reg_no):
        print("Student with this registration number already exists!")
        return
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    level = input("Enter Level: ")

    with open(STUDENT_FILE, "a") as file:
        file.write(f"{reg_no},{name},{dept},{level}\n")
    print("Student registered successfully.")

# Function to check if a student exists
def check_student_exists(reg_no):
    if not os.path.exists(STUDENT_FILE):
        return False
    with open(STUDENT_FILE, "r") as file:
        students = file.readlines()
    for student in students:
        if student.startswith(reg_no + ","):
            return True
    return False

# Function to take attendance
def take_attendance():
    reg_no = input("Enter Student Registration Number: ")
    if not check_student_exists(reg_no):
        print("Student not found!")
        return
    status = input("Enter Attendance (1 for Present, 0 for Absent): ")
    if status not in ["1", "0"]:
        print("Invalid attendance status. Use 1 for Present and 0 for Absent.")
        return

    with open(ATTENDANCE_FILE, "a") as file:
        file.write(f"{reg_no},{status}\n")
    print("Attendance recorded successfully.")

# Function to generate a student report
def generate_report():
    reg_no = input("Enter Student Registration Number: ")
    if not check_student_exists(reg_no):
        print("Student not found!")
        return

    total_classes = 0
    present_count = 0

    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records found.")
        return

    with open(ATTENDANCE_FILE, "r") as file:
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
    print(f"Attendance Percentage: {percentage:.2f}%")

# Main menu
def main():
    while True:
        print("\nStudent Attendance System")
        print("1. Register Student")
        print("2. Take Attendance")
        print("3. Generate Attendance Report")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            register_student()
        elif choice == "2":
            take_attendance()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
