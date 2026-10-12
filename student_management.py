
students = []


def add_student():
    name = input("Enter student name: ")#taking input from the user for the student's name
    roll_no = input("Enter roll number: ")#taking input from the user for the student's roll number
    marks = float(input("Enter marks out of 100: "))#taking input from the user for the student's marks and converting it to a float

    student = { "name": name,"roll_no": roll_no,"marks": marks}#taking the input values and storing them in a dictionary with keys "name", "roll_no", and "marks"

    students.append(student)#for adding the student dictionary to the students list, which stores all the student records.
    print("Student added successfully!")


def display_students():
    #if executes the indented code when the condition is true.
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
#It takes each student dictionary from the students list, one at a time, and temporarily refers to it using the variable
    for student in students:
        print("Name:", student["name"])#printing the value associated with the "name" key in the student dictionary.
        print("Roll Number:", student["roll_no"])#printing the value associated with the "roll_no" key in the student dictionary.
        print("Marks:", student["marks"])#printing the value associated with the "marks" key in the student dictionary.
        print("Percentage:", student["marks"], "%")#printing the value associated with the "marks" key in the student dictionary followed by a percentage sign.

        if student["marks"] >= 40:#checking if the value associated with the "marks" key in the student dictionary is greater than or equal to 40.
            print("Result: Pass")
        else:
            print("Result: Fail")

        print("---------")


def search_student():
    roll_no = input("Enter roll number to search: ")#taking input from the user for the roll number of the student they want to search for.

    for student in students:#iterating through each student dictionary in the students list.
        if student["roll_no"] == roll_no:
            print("Student Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


while True:#creating an infinite loop that will continue until the user chooses to exit the program.
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")
