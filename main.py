import attendance as AT
import student as ST
class AttendanceSystem:
    @staticmethod
    def main():
        while True:
            print("\nStudent Attendance System")
            print("1. Register Student")
            print("2. Take Attendance")
            print("3. Generate Attendance Report")
            print("4. Delete Attendance")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                ST.Student.register_student()
            elif choice == "2":
                AT.Attendance.take_attendance()
            elif choice == "3":
                AT.Attendance.generate_report()
            elif choice == "4":
                ST.Student.delete_student()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    AttendanceSystem.main()