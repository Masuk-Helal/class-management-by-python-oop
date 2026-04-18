class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def get_student_by_id(cls, student_id):
        for student in cls.student_list:
            if student.get_student_id() == student_id:
                return student
        return None

    @classmethod
    def view_all_students(cls):
        if not cls.student_list:
            print("No students found.")
        for student in cls.student_list:
            student.view_student_info()


class Student:
    def __init__(self, student_id, name, department, is_enrolled = False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__name} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__name} enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__name} is not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__name} has been dropped.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"

        print(f"ID: {self.__student_id} Name: {self.__name} Department: {self.__department} Status: {status}")


s1 = Student(101, "Rahim Uddin", "CSE")
s2 = Student(102, "Karim Hasan", "EEE", True)
s3 = Student(103, "Ayesha Akter", "BBA")


while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        StudentDatabase.view_all_students()

    elif choice == "2":
        try:
            student_id = int(input("Enter Student ID to enroll: "))
            student = StudentDatabase.get_student_by_id(student_id)

            if student is None:
                print("Invalid student ID.")
            else:
                student.enroll_student()

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        try:
            student_id = int(input("Enter Student ID to drop: "))
            student = StudentDatabase.get_student_by_id(student_id)

            if student is None:
                print("Invalid student ID.")
            else:
                student.drop_student()

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")