

marks = {
    'Ayesha': {'Math': 80, 'physics': 90},
    'Ahmad': {'Math': 70, 'physics': 60},
    'sara': {'Math': 90, 'physics': 80},
    'Omar': {'Math': 85, 'physics': 95},
    'Zain': {'Math': 75, 'physics': 70},
}


highest_math = 0
highest_physics = 0

top_math_students = []
top_physics_students = []

for student, subjects in marks.items():
    if subjects['Math'] > highest_math:
        highest_math = subjects['Math']
        top_math_students = [student]

    elif subjects['Math'] == highest_math:
        top_math_students.append(student)

    if subjects['physics'] > highest_physics:
        highest_physics = subjects['physics']
        top_physics_students = [student]
         
    elif subjects['physics'] == highest_physics:
        top_physics_students.append(student)

print("Math student:", top_math_students, "with marks:", highest_math)
print("Physics student:", top_physics_students, "with marks:", highest_physics)



