# Create a list
my_list = [1, 2, 3, 4, 5]
# Accessing elements
print("Accessing elements:")
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Slicing
print("\nSlicing:")
sliced_list = my_list[1:4]
print(sliced_list)  # Output: [2, 3, 4]

# Appending and extending
print("\nAppending and extending:")
my_list.append(6) # [1, 2, 3, 4, 5, 6]
my_list.extend([7, 8])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Inserting
print("\nInserting:")
my_list.insert(2, 9)
print(my_list)  # Output: [1, 2, 9, 3, 4, 5, 6, 7, 8]

# Removing and popping
print("\nRemoving and popping:")
my_list.remove(9) # [1, 2, 3, 4, 5, 6, 7, 8]
popped_item = my_list.pop(4)
print(my_list)  # Output: [1, 2, 3, 4, 6, 7, 8]
print("Popped item:", popped_item)  # Output: 5

# Index and count
print("\nIndex and count:")
index = my_list.index(3)
count = my_list.count(4)
print("Index of 3:", index)  # Output: 2
print("Count of 4:", count)  # Output: 1

# Sorting and reversing
print("\nSorting and reversing:")
my_list.sort()
my_list.reverse()
print(my_list)  # Output: [8, 7, 6, 4, 3, 2, 1]

# Length
print("\nLength:")
length = len(my_list)
print("Length of the list:", length)  # Output: 7

# Max and min
print("\nMax and min:")
max_value = max(my_list)
min_value = min(my_list)
print("Max value:", max_value)  # Output: 8
print("Min value:", min_value)  # Output: 1

# Sum
print("\nSum:")
sum_of_elements = sum(my_list)
print("Sum of elements:", sum_of_elements)  # Output: 31

# Clear
print("\nClear:")
my_list.clear()
print("Cleared list:", my_list)  # Output: []

# List comprehension
print("\nList comprehension:")
squared_numbers = [x ** 2 for x in range(1, 6)]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Function 1: Sum of Elements
def sum_list(nums):
    sum = 0
    for value in nums:
        sum = sum + value
    return sum

# Function 2: Product of Elements
def product_list(nums):
    product = 1
    for num in nums:
        product *= num
    return product

# Function 3: Find Max and Min
def max_min(nums): # [10, 20, 5, 2, 90]
    min = nums[0] # 10,
    max = nums[0] # 10, 20
    for val in nums: # val = 10, 20
        if val < min:
            min = val
        if val > max:
            max = val
    return max, min



    #return max(nums), min(nums)

# Function 4: Count Even and Odd
def count_even_odd(nums):
    evens = sum_list(1 for num in nums if num % 2 == 0)
    odds = len(nums) - evens
    return evens, odds
    #return {"even": evens, "odd": odds}

# Function 5: Extract Slices
def extract_slices(nums):
    return {
        "first_4": nums[:4],
        "last_3": nums[-3:],
        "every_2nd": nums[::2],
        "reversed": nums[::-1]
    }

# Function : Remove element
def remove_ele(ele, nums): # nums = [1, 2, 3] , ele = 2
    newList = [] # [1, 3]
    for val in nums: # val = 1, 2, 3
        if ele != val:
            newList.append(ele)
    return newList


# Function 6: Remove Duplicates
def remove_duplicates(nums):
    newList = []


    #return list(dict.fromkeys(nums))  # Preserves order

# Function 7: Find Common Elements
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Function 8: Rotate List
def rotate_list(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k]

# Function 9: Flatten a Nested List
def flatten_list(nested):
    return [item for sublist in nested for item in sublist]

# Function 10: Second Largest Number
def second_largest(nums):
    unique_nums = sorted(set(nums), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None

# Function 11: Group Even and Odd Numbers
def group_even_odd(nums):
    return {
        "even": [num for num in nums if num % 2 == 0],
        "odd": [num for num in nums if num % 2 != 0]
    }

# Sample Inputs
nums = [10, 20, 30, 40, 50, 60, 70]
nested = [[1, 2], [3, 4], [5, 6]]
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Function Calls & Outputs
print("Sum:", sum_list(nums))  # Output: 280
print("Product:", product_list([1, 2, 3, 4]))  # Output: 24
print("Max & Min:", max_min(nums))  # Output: (70, 10)
print("Even & Odd Count:", count_even_odd(nums))  # Output: {'even': 7, 'odd': 0}
print("List Slices:", extract_slices(nums))
print("Without Duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print("Common Elements:", common_elements(list1, list2))  # Output: [4, 5]
print("Rotated List:", rotate_list(nums, 2))  # Output: [60, 70, 10, 20, 30, 40, 50]
print("Flattened List:", flatten_list(nested))  # Output: [1, 2, 3, 4, 5, 6]
print("Second Largest:", second_largest([1, 3, 4, 4, 5, 6]))  # Output: 5
print("Grouped Even & Odd:", group_even_odd(nums))