students = {
    "alice": 8,
    "bob": 7,
    "carlos": 9
}

total = sum(students.values())
total_students = len(students.keys())
average = total / total_students
print("the average grade is ", average)
