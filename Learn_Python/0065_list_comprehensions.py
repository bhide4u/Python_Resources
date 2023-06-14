# list comprehensions

# In Python, list comprehensions provide a concise way to create new lists based on existing sequences, such as lists, tuples, or strings. They allow you to combine loops, conditional statements, and expressions into a single line, making the code more readable and expressive.

# The basic syntax of a list comprehension is as follows:

# new_list = [expression for item in iterable if condition]


# - 'expression': An expression that determines the elements of the new list.
# - 'item': A variable representing each item in the iterable.
# - 'iterable': The sequence of elements to iterate over.
# - 'condition' (optional): A condition that filters the elements based on a Boolean expression.

# Here's an example that demonstrates the usage of list comprehensions:

# Example 1: Squaring numbers using list comprehension

numbers = [1, 2, 3, 4, 5]

squared_numbers = [x**2 for x in numbers]

print(squared_numbers)


# Output:

[1, 4, 9, 16, 25]


# In the above example, we create a new list called 'squared_numbers' using a list comprehension. 
# The expression 'x**2' is evaluated for each element 'x' in the 'numbers' list, resulting in a new list with the squared values.

# List comprehensions can also include conditional statements to filter elements. 
# Here's an example that filters even numbers from a list:


# Example 2: Filtering even numbers using list comprehension

numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

# Output:

[2, 4]


# In this case, we use a list comprehension with a conditional statement ('if x % 2 == 0') to filter only the even numbers from the 'numbers' list.

# List comprehensions can also be used with strings. 
# Here's an example that converts a string to a list of its characters:

# Example 3: Converting a string to a list of characters using list comprehension

string = "Hello, World!"

characters = [ch for ch in string]

print(characters)


# Output:

['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']


# In this example, we iterate over each character ('ch') in the string and create a new list 'characters' that contains each character as an element.

# List comprehensions offer a concise and expressive way to create new lists based on existing sequences. 
# They are widely used in Python to simplify code and make it more readable. 
# However, it's important to ensure that list comprehensions do not become overly complex or nested, as it may negatively impact readability and maintainability.