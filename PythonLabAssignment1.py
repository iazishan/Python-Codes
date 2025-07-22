# ********************** Program 1 ***********************
marks = float(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Error: Marks should be between 0 and 100.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")


# ************************** Program 2 **************************
num = int(input("Enter a postive number: "))

if num < 0:
    print("Enter a positive number!")

else:
    result = 1
    for i in range(1,num+1):
        result *=i
        print(f"Factorial of {num} is {result}")



#  ***************************** Program 3 ****************************
even_list = []
odd_list = []

for i in range(10):
    num = int(input("Enter number: "))
    if num % 2 ==0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even List: ",even_list)
print("Odd List: ",odd_list)

#  ********************** Program 4 ************************
persons = { 
    "keys": "Emotions",
    "Zain": "happy", 
    "Ali": "sad", 
    "Ahmed": "happy", 
    "Kashif": "sad", 
    "Ahmer": "happy"
      }

for name,emotion in persons.items():
    if emotion == "happy":
        print(name)


# ******************** Program 5 *************************
number = int(input("Enter a positive number: "))
if number < 0:
    print("Enter a positive number!")
else:
    result = 1  # Initialize result variable to 1
    for i in range(1, number + 1):
        result *= i
    print(f"Factorial of {number} is {result}")