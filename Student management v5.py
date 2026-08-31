students_dict = {}


# Function to calculate student result
def calculate_result(details):
    total = details["Physics"] + details["Chemistry"] + details["Maths"]
    average = total / 3

    if (
        details["Physics"] >= 40
        and details["Chemistry"] >= 40
        and details["Maths"] >= 40
    ):
        result = "Pass"
    else:
        result = "Fail"

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "E"

    return total, average, result, grade


# Add students
number = int(input("Enter number of students: "))

for i in range(number):
    name = input("\nEnter student name: ")

    physics = int(input("Enter Physics Marks: "))
    chemistry = int(input("Enter Chemistry Marks: "))
    maths = int(input("Enter Maths Marks: "))

    students_dict[name] = {
        "Physics": physics,
        "Chemistry": chemistry,
        "Maths": maths
    }


# Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Display students")
    print("2. Search student")
    print("3. Find class topper")
    print("4. Show class average")
    print("5. Exit")

    choice = int(input("Enter choice: "))


    # Display students
    if choice == 1:

        for student, details in students_dict.items():

            total, average, result, grade = calculate_result(details)

            print("\n===== STUDENT RESULT =====")
            print(f"Name = {student}")
            print(f"Physics = {details['Physics']}")
            print(f"Chemistry = {details['Chemistry']}")
            print(f"Maths = {details['Maths']}")
            print(f"Total = {total}")
            print(f"Average = {average:.2f}")
            print(f"Result = {result}")
            print(f"Grade = {grade}")


    # Search student
    elif choice == 2:

        name = input("\nEnter student name to search: ")

        if name in students_dict:

            details = students_dict[name]

            total, average, result, grade = calculate_result(details)

            print("\n===== STUDENT FOUND =====")
            print(f"Name = {name}")
            print(f"Physics = {details['Physics']}")
            print(f"Chemistry = {details['Chemistry']}")
            print(f"Maths = {details['Maths']}")
            print(f"Total = {total}")
            print(f"Average = {average:.2f}")
            print(f"Result = {result}")
            print(f"Grade = {grade}")

        else:
            print("Student not found!")


    # Class topper
    elif choice == 3:

        highest = float("-inf")
        top_student = ""

        for student, details in students_dict.items():

            total, average, result, grade = calculate_result(details)

            if total > highest:
                highest = total
                top_student = student

        print("\n===== CLASS TOPPER =====")
        print(f"Topper = {top_student}")
        print(f"Highest marks = {highest}")


    # Class average
    elif choice == 4:

        total_marks = 0

        for details in students_dict.values():

            total, average, result, grade = calculate_result(details)

            total_marks += total

        class_average = total_marks / number

        print(f"\nClass Average = {class_average:.2f}")


    # Exit
    elif choice == 5:

        print("Exiting Student Management System...")
        break


    else:
        print("Invalid choice!")