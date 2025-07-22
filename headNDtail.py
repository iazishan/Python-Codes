import random

# The following code simulates a "head or tail" game.
# It asks the user to choose "head" or "tail" and then generates a random number between 1 and 200.

# The next two lines are incorrect and unnecessary, so they can be removed:
# head="head".random()
# tail="tail".random()

##choice = input("Enter your choice head or tail:")  # Prompt user for input

##if choice == "head":
   ## head = random.randint(1, 200)  # Generate random number for "head"
   ## print(head)  # Output the random number
##elif choice == "tail":
    ##tail = random.randint(1, 200)  # Generate random number for "tail"
    ##print(tail)  # Output the random number









head_tail=random.randint(0,1)  #    Generate a random number between 1 and 200
if head_tail==0:
    print("Head")
else:
    print("Tail")