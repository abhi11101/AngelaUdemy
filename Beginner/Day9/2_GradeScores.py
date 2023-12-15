student_scores= {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

print(student_scores)

student_grades={}

for key in student_scores:
    value = student_scores[key]
    newValue=""
    if(91 <= value <= 100):
        newValue="Outstanding"
    elif(81 <= value <=90):
        newValue="Exceeds Expectations"
    elif(71<= value<=80):
        newValue="Acceptable"
    else:
        newValue="Fail"
    student_grades[key] = newValue

print(student_grades)