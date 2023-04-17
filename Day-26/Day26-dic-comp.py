# Syntax for creating a dictionary from a list
# new_dict = {new_key:new_value for item in list}

# Syntax for creating a dictionary from another dictionary

# new_dict = {new_key:new_value for (key,value) in dict.items()}

# Syntax for creating a dictionary from another dictionary - conditional

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}


import random

# 1. List to dictionary with value as random scores
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# student_scores = {stud_key:stud_value for student in names}
student_scores = {student: random.randint(1, 100) for student in names}

print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
