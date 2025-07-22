def reverse_string(s):
    
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


input_string = input("Enter string to make it reverse")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)