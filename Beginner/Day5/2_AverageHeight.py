
total_students = int(input("How many students you want to enter?\n"))
students_heights = []
average = 0
for i in range(0,total_students):
    height = int(input("Enter the height of the student: "))
    average += height
    students_heights.append(height)
print(students_heights)

average /= total_students
print(round(average))

