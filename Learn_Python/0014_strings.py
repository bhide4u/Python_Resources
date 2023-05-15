# Strings

# Strings: A string is a sequence of characters. Strings are immutable in Python, which means you cannot modify them once they are created. Strings are used to represent text data.

greeting = 'Hello, World!'

another_greeting = "Hello Again!!!"

# Multi-line strings

multi_line_string = '''
Hi this is a multi line string
'''

another_multi_line_string = """
Hi this is another multi line string
"""

# Strings are arrays 

# To access string, [] can be used, index of first character is 0
random_string = "sdfwgsdgesgg"

# to access 3rd character
print("Third letter of string is: ", random_string[2])

# String Concatenation - 
# 1. Using +
print("This string is concatenated" + " using +")

# Formatted Strings 
name = "Alice"
age = 25
occupation = "Software Engineer"

print(f"My name is {name}, and I am {age} years old. I work as a {occupation}.")

# You can also use formatted strings to specify formatting options for the values that are inserted into the string. For example, you can specify the number of decimal places to display for a floating-point value, or the width of a field to ensure that values are aligned properly. Here 

# is an example:
pi = 3.14159265358979323846

print(f"The value of pi is approximately {pi:.2f}")

# .format() method
name = "Bob"
age = 35
occupation = "Data Scientist"

message = "My name is {}, and I am {} years old. I work as a {}.".format(name, age, occupation)

print(message)

# String Indexes
