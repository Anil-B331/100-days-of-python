# Input
students = []
for _ in range(int(input("Enter the number of students: "))):
    name = input("Enter the student's name: ")
    grade = float(input("Enter the student's grade: "))
    students.append([name, grade])

# Find the second lowest grade
grades = sorted(set([student[1] for student in students]))
second_lowest_grade = grades[1]

# Find and print the names of students with the second lowest grade
second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_grade])
for name in second_lowest_students:
    print(name)
