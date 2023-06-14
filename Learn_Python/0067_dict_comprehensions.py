# Dictionary comprehensions

# In Python, dictionary comprehensions provide a concise way to create new dictionaries based on existing sequences or other dictionaries. 
# Similar to list and set comprehensions, dictionary comprehensions allow you to combine loops, conditional statements, and expressions into a single line.

# The basic syntax of a dictionary comprehension is as follows:

# new_dict = {key_expression: value_expression for item in iterable if condition}

# - 'key_expression': An expression that determines the keys of the new dictionary.
# - 'value_expression': An expression that determines the values of the new dictionary.
# - 'item': A variable representing each item in the iterable.
# - 'iterable': The sequence of elements to iterate over.
# - 'condition' (optional): A condition that filters the elements based on a Boolean expression.

# Here's an example that demonstrates the usage of dictionary comprehensions:

# Example 1: Creating a dictionary of squared numbers using dictionary comprehension

numbers = [1, 2, 3, 4, 5]

squared_dict = {x: x**2 for x in numbers}

print(squared_dict)

# Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# In the above example, we create a new dictionary called 'squared_dict' using a dictionary comprehension. The key expression is 'x', which represents each element in the 'numbers' list. The value expression is 'x**2', resulting in a new dictionary with keys as the elements from 'numbers' and values as their squared values.

# Dictionary comprehensions can also include conditional statements to filter elements. 

# Here's an example that filters even numbers from a list and creates a dictionary:

# Example 2: Creating a dictionary of even numbers using dictionary comprehension

numbers = [1, 2, 3, 4, 5]

even_dict = {x: x**2 for x in numbers if x % 2 == 0}

print(even_dict)

# Output:

{2: 4, 4: 16}

# In this case, we use a dictionary comprehension with a conditional statement ('if x % 2 == 0') to filter only the even numbers from the 'numbers' list and create a new dictionary 'even_dict' with keys as the even numbers and values as their squared values.

# Dictionary comprehensions can also be used with strings or other dictionaries. Here's an example that creates a dictionary mapping each character in a string to its ASCII value:

# Example 3: Creating a dictionary mapping characters to ASCII values using dictionary comprehension

string = "Hello"

ascii_dict = {ch: ord(ch) for ch in string}

print(ascii_dict)

# Output:

{'H': 72, 'e': 101, 'l': 108, 'o': 111}

# In this example, we iterate over each character ('ch') in the string and create a new dictionary 'ascii_dict' that maps each character to its ASCII value using the 'ord()' function.

# Dictionary comprehensions provide a concise and expressive way to create new dictionaries based on existing sequences or dictionaries. 
# They are useful for creating dictionaries with custom key-value mappings or performing transformations on existing dictionaries. 
# However, it's important to ensure that dictionary comprehensions do not become overly complex or nested for the sake of readability and maintainability.