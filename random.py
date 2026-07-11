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
            print("No students avaliable to display")
        else:
            for information in students:
                grade = students[information]
                print(f"{information}: {grade}")

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
            
            number = int(input("Enter 1 to add a student, enter 2 to delete a student,
                        enter 3 to search for a student, enter 4 to display all students, 
                        enter 5 to save the information for all students, enter 6 to load the saved info and to end: "))

            if number == 1:
                addStudent()

            elif number == 2:
                deleteStudent()

            elif number == 3:
                searchStudent()

            elif number == 4:
                displayStudents()

            elif number == 5:
                saveStudents()

            elif number == 6:
                loadFile()
                break
            
            else:
                print("Only numbers between 1 to 6, nothing else!")
        except ValueError:
            print("Enter an integer")








