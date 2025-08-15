import random

names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]

# using a list to create a dictionary
students_score = {student:random.randint(20,100) for student in names}
print(students_score)

# using a dictionary to create a dictionary
passed_students = {student:score for (student,score) in students_score.items() if score > 50}
print(passed_students)