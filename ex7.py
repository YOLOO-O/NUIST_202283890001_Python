def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    for name in studentNames:
        print(name + " Evans")
    return studentNames

def addToList(studentNames):
    new_name = input("Enter a new first name to add: ")
    studentNames.append(new_name)
    print("\nUpdated student list:")
    for name in studentNames:
        print(name + " Evans")

students = studList()
addToList(students)
