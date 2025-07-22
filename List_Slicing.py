my_list = [1, 2, 3, 4, 5]
my_string = "Hello, World!"

print(my_list[-1:-3]) # [5, 4]
print(my_list[1:3]) # [2, 3]
print(my_list[:3]) # [1, 2, 3]
print(my_list[0:]) # [1, 2, 3, 4, 5]
print(my_list[0:4:2]) # [1, 3]
print(my_list[::-2]) # [5, 3, 1]


# Negative Start Index
# "Hello, World!"
sliced_list1 = my_list[-2:] # [4, 5]
sliced_list2 = my_string[:-6] # Hello,
print("Negative Start Index:")
print(sliced_list1)  # Output: [4, 5]
print(sliced_list2)  # Output: "Hello, "

# Negative Stop Index
my_list = [1, 2, 3, 4, 5]
my_string = "Hello, World!"
sliced_list3 = my_list[-4:]
sliced_list4 = my_string[:-6]
print("\nNegative Stop Index:")
print(sliced_list3)  # Output: [2, 3, 4, 5]
print(sliced_list4)  # Output: "Hello, "

# Negative Start and Stop Indices
my_string = "Hello, World!"
sliced_list5 = my_list[-3:-1] #[1,2,3,4,5]
sliced_list6 = my_string[-5:-2]
print("\nNegative Start and Stop Indices:")
print(sliced_list5)  # Output: [3, 4]
print(sliced_list6)  # Output: "orl"

# Negative Start, Stop, and Step
#my_list = [1, 2, 3, 4, 5]
my_string = "Hello, World!"
sliced_list7 = my_list[-5:-1:2] # [1, 3]
sliced_list8 = my_string[-6::-2]

print("\nNegative Start, Stop, and Step:")
print(sliced_list7)  # Output: [1, 3]
print(sliced_list8)  # Output: "W,le"

# Negative Start and Step
sliced_list9 = my_list[::-2]
sliced_list10 = my_string[-1::-1]
print("\nNegative Start and Step:")
print(sliced_list9)   # Output: [5, 3, 1]
print(sliced_list10)  # Output: "!dlroW ,olleH"

# Negative Stop and Step
sliced_list11 = my_list[-4::2] # [1, 2, 3, 4, 5]
sliced_list12 = my_string[:-1:2]
print("\nNegative Stop and Step :")
print(sliced_list11)  # Output: [2, 4]
print(sliced_list12)  # Output: "Hlo ol"

# Negative Start, Stop, and Full Reverse
reversed_list1 = my_list[::-1]
reversed_list2 = my_string[::-1]
print("\nNegative Start, Stop, and Full Reverse:")
print(reversed_list1)  # Output: [5, 4, 3, 2, 1]
print(reversed_list2)  # Output: "!dlroW ,olleH"
