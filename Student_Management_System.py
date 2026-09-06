students = []
print(28 * "=")
print("     STUDENT MANAGEMENT")
print(28 * "=")
print("""
What you would like to do today:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Statistics
7. Exit

Type the serial number for using the feature like - 
1 to "Add Student", 
2 to "View Students" etc..
    """)

while True:
    feature = input("""
Type help to see the instructions again
Feature:  """).lower()

    if feature == "1":
        name = input("Name: ")
        if name.strip() == "":
            print("Please put a valid name")

        else:
            roll_number = int(input("Roll Number: "))
            if roll_number < 0:
                print("Roll number can't be negative!")

            else:
                for i in students:
                    if roll_number == i[0] and name == i[1]:
                        print(
                            "This student already exist in the records please add a different student"
                        )
                        break
                    elif roll_number == i[0]:
                        print(
                            f"{i[1]} already has this Roll Number please select some other roll number"
                        )
                        break
                else:
                    age = int(input("Age: "))
                    if 15 <= age <= 30:
                        marks = int(input("Marks: "))
                        if 0 <= marks <= 100:
                            students.append([roll_number, name, age, marks])
                            print(f"✓ Student {name} added successfully.")
                        else:
                            print("Marks can only be between 0 to 100")

                    else:
                        print("Age can be between 15 to 30")

    elif feature == "2":
        if len(students) > 0:
            print(f"""
{"Roll No.":<10}{"Name":<20}{"Age":<10}{"Marks":<10}{"Grade":<10}
{"=" * 60}""")
            for student in students:
                if student[3] >= 90:
                    grade = "A"
                elif student[3] >= 80:
                    grade = "B"
                elif student[3] >= 70:
                    grade = "C"
                elif student[3] >= 40:
                    grade = "D"
                elif student[3] < 40:
                    grade = "F"
                print(
                    f"{student[0]:<10}{student[1]:<20}{student[2]:<10}{student[3]:<10}{grade:<10}"
                )
        else:
            print("""
Please add students to see the records""")

    elif feature == "3":
        roll = int(input("Enter Roll No: "))
        for i1 in students:
            if i1[0] == roll:
                print(f"""Name: {i1[1]}
Age: {i1[2]}
Marks: {i1[3]}""")
                break
        else:
            print("Student Not Found...")

    elif feature == "4":
        roll = int(input("Enter Roll No: "))
        for i1 in students:
            if i1[0] == roll:
                selection = input("""What would you like to update -
A - Name
B - Age
C - Marks
> """).upper()

                if selection == "A":
                    new_name = input("Enter the new name: ")
                    if new_name.strip() == "":
                        print("Please add a valid name")
                        break
                    else:
                        i1[1] = new_name
                        print("Name Changed Successfully!")
                        break
                elif selection == "B":
                    new_age = int(input("Enter the new age: "))
                    if 15 <= new_age <= 30:
                        i1[2] = new_age
                        print("Age Changed Successfully!")
                        break
                    else:
                        print("Age can be between 15 to 30")
                        break
                elif selection == "C":
                    new_marks = int(input("Enter the new marks: "))
                    if 0 <= new_marks <= 100:
                        i1[3] = new_marks
                        print("Marks Changed Successfully!")
                        break
                    else:
                        print("Marks can only be between 0 to 100")
                else:
                    print("""I don't understand that...
        Please type a command as shown below:
        A - Name
        B - Age
        C - Marks""")
                    break
        else:
            print("Student Not Found...")
    elif feature == "5":
        roll = int(input("Enter Roll No: "))
        for i1 in students:
            if i1[0] == roll:
                print(f"""Name: {i1[1]}
Age: {i1[2]}
Marks: {i1[3]}""")
                verify = input(
                    "Are you sure you want to delete this student from records (Y/N): "
                ).upper()
                if verify == "Y":
                    students.remove(i1)
                    print("Student Deleted Successfully!")
                    break
                else:
                    print("Student was not deleted")
                    break

        else:
            print("Student Not Found...")
    elif feature == "6":
        topper_marks = 0
        lowest_marks = 100
        passing_marks = 40
        passed_student = 0
        failed_student = 0
        count = 0
        total_marks = 0
        for i2 in students:
            if i2[3] > topper_marks:
                topper_marks = i2[3]
                topper_name = i2[1]
                topper_roll_number = i2[0]
            if i2[3] < lowest_marks:
                lowest_marks = i2[3]
                lowest_name = i2[1]
                lowest_roll_number = i2[0]
            if i2[3] >= passing_marks:
                passed_student += 1
            if i2[3] < passing_marks:
                failed_student += 1
            count += 1
            total_marks += i2[3]
        if count == 0:
            print("Please add srudents before seeing the stats")
        else:
            average_marks = total_marks / count
            print(f"""
Highest Marks: {topper_marks}
Topper Name: {topper_name}
Topper Roll Number: {topper_roll_number}

Lowest Marks: {lowest_marks}
Name of Student: {lowest_name}
Roll Number: {lowest_roll_number}

Average Marks: {average_marks}
Total Students: {count}

Passing marks: {passing_marks}
Number of Passed Students: {passed_student}
Number of Failed Students: {failed_student}
""")
    elif feature == "7":
        print("Thankyou for using Student Management System!")
        break
    elif feature == "help":
        print(28 * "=")
        print("     STUDENT MANAGEMENT")
        print(28 * "=")
        print("""
        What you would like to do today:

        1. Add Student
        2. View Students
        3. Search Student
        4. Update Student
        5. Delete Student
        6. Statistics
        7. Exit

        Type the serial number for using the feature like - 
        1 to "Add Student", 
        2 to "View Students" etc..
            """)
    else:
        print("""I dont understand that please write from below
        """)
        print(28 * "=")
        print("     STUDENT MANAGEMENT")
        print(28 * "=")
        print("""
What you would like to do today

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Statistics
7. Exit

Type the serial number for using the feature like - 
1 to "Add Student", 
2 to "View Students" etc..
""")
