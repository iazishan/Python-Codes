    # ------------------------------
# Python Lab: Introduction to Dictionaries
# ------------------------------

# 1. Creating a Simple Dictionary
print("\n1. Creating a Simple Dictionary")


student = {
    "name": "Ali",
    "age": 22,
    "course": "Computer Science",
    "grades": [85, 90, 78],
    
}




print(student)

# 2. Accessing Values
print("\n2. Accessing Values")
print("Name:", student["name"])
print("Age:", student["age"])

# 3. Adding a New Key-Value Pair
print("\n3. Adding a New Key-Value Pair")
student["grade"] = "A"
print(student)

# 4. Modifying a Value
print("\n4. Modifying a Value")
student["course"] = "Software Engineering"
print("Updated Course:", student["course"])

# 5. Removing a Key
print("\n5. Removing a Key")
del student["age"]
print("Updated Dictionary:", student)
print('After item() call', student.items())
# 6. Iterating Over a Dictionary
print("\n6. Iterating Over a Dictionary")
for key, value in student.items():
    print(f"{key}: {value}")

# 7. Using the .get() Method (to avoid errors)
print("\n7. Using the .get() Method")
print("Grade:", student.get("grade", "Not Found"))

# 8. Checking if a Key Exists
print("\n8. Checking if a Key Exists")
if "name" in student:
    print("Name exists in the dictionary!")

# ------------------------------
# Moving to Nested Dictionaries
# ------------------------------

# 9. Creating a Nested Dictionary
print("\n9. Creating a Nested Dictionary")
students = {
    "Ali": {"age": 22, "course": "CS", "grades": [85, 90, 88]},
    "Asad": {"age": 21, "course": "Mechanical Eng", "grades": [78, 80, 75]},
    "Fatima": {"age": 23, "course": "Data Science", "grades": [92, 95, 98]},
}
print(students)

# 10. Accessing Data from Nested Dictionary
print("\n10. Accessing Data from Nested Dictionary")
print("Ali's Course:", students["Ali"]["course"])
print("Fatima's Grades:", students["Fatima"]["grades"])

# 11. Adding a New Student
print("\n11. Adding a New Student")
students["Hassan"] = {"age": 20, "course": "AI & Robotics", "grades": [88, 84, 89]}
print(students)

# 12. Function to Calculate Average Grades
def average_grade(student_dict, student_name):
    if student_name in student_dict:
        return sum(student_dict[student_name]["grades"]) / len(student_dict[student_name]["grades"])
    return f"Student {student_name} not found"

print("\n12. Calculating Average Grades")
print("Ali's Average Grade:", average_grade(students, "Ali"))
print("Hassan's Average Grade:", average_grade(students, "Hassan"))