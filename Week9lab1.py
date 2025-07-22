
marks = {
    'Ayesha': {'Math': 80, 'physics': 90},
    'Ahmad': {'Math': 70, 'physics': 60},
    'sara': {'Math': 90, 'physics': 80},
    'Omar': {'Math': 85, 'physics': 95},
    'Zain': {'Math': 75, 'physics': 70},
}

highest_math = max(student['Math'] for student in marks.values())
highest_physics = max(student['physics'] for student in marks.values())

top_math_students = [name for name, subjects in marks.items() if subjects['Math'] == highest_math]
top_physics_students = [name for name, subjects in marks.items() if subjects['physics'] == highest_physics]

print("Math student:", top_math_students, "with marks:", highest_math)
print("Physics student:", top_physics_students, "with marks:", highest_physics)
