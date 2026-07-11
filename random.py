students = {}
def addStudent():
        name = input("Enter name of student: ")
        if name not in students:
            grade = int(input("Enter grade: "))
            if 0 <= grade <= 100:
                students[name] = grade
            else:
                print("Grade insufficient")
        else:
            print("Cannot add same name")
            return students
        
def deleteStudent():
        name = input("Remove a student: ")
        if name in students:
            del students[name]
            print("Deleted student")
        else:
            print("No student with that name to delete")
            return students

def searchStudent():
        name = input("Search for a student: ")
        if name in students:
            grade = students[name]
            print(f"Found {name}, grade: {grade}")
        else:
            print("Student not found")
            return students

def displayStudents():
        print("Students:\n")
        if len(students) == 0:
            print("No students available to display")
        else:
            for information in students:
                grade = students[information]
                print(f"{information}: {grade}")

def editStudents():
    name = input("Enter a students name to edit: ")
    if name not in students:
        print("Name not found to edit")
    else:
        while True:
            try:
                grade = int(input("Grade to edit: "))
                if 0 <= grade <= 100:
                    students[name] = grade
                    print(f"{name}'s grade was edited to {grade}")
                    break
                else:
                    print("Grade outside of boundaries, try again")
            except ValueError:
                print("Enter an integer")

def saveStudents():
    file = open("students.txt", "w")
    file.write("Students:\n")
    for information in students:
        grade = students[information]
        file.write(f"{information}: {grade}\n")
    file.close()
    return file

def loadFile():
    file = open("students.txt", "r")
    read = file.read()
    separate = read.split("\n")
    print(separate)


while True:
        try:
            print("---------Student Management--------\n")
            print("1. Add student\n 2. Delete Student\n 3. Search Student\n 4. Display all students\n 5. Edit student\n 6. Save\n 7. Load\n 8. Exit\n")
            number = int(input("Choose an option: "))

            if number == 1:
                addStudent()

            elif number == 2:
                deleteStudent()

            elif number == 3:
                searchStudent()

            elif number == 4:
                displayStudents()

            elif number == 5:
                editStudents()

            elif number == 6:
                saveStudents()

            elif number == 7:
                loadFile()
            elif number == 8:
                print("Exiting..")
                break
            else:
                print("Only numbers between 1 to 8, nothing else!")
        except ValueError:
            print("Enter an integer")








