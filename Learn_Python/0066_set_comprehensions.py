# Set Comprehensions

# In Python, set comprehensions provide a concise way to create new sets based on existing sequences, such as lists, tuples, or strings. 
# Similar to list comprehensions, set comprehensions allow you to combine loops, conditional statements, and expressions into a single line.

# The basic syntax of a set comprehension is as follows:

# new_set = {expression for item in iterable if condition}

# - 'expression': An expression that determines the elements of the new set.
# - 'item': A variable representing each item in the iterable.
# - 'iterable': The sequence of elements to iterate over.
# - 'condition' (optional): A condition that filters the elements based on a Boolean expression.

# Here's an example that demonstrates the usage of set comprehensions:

# Example 1: Creating a set of squared numbers using set comprehension

numbers = [1, 2, 3, 4, 5]

squared_set = {x**2 for x in numbers}

print(squared_set)

# Output:

{1, 4, 9, 16, 25}


# In the above example, we create a new set called 'squared_set' using a set comprehension. 
# The expression 'x**2' is evaluated for each element 'x' in the 'numbers' list, resulting in a new set with the squared values.

# Set comprehensions can also include conditional statements to filter elements. 

# Here's an example that filters even numbers from a list and creates a set:


# Example 2: Creating a set of even numbers using set comprehension

numbers = [1, 2, 3, 4, 5]

even_set = {x for x in numbers if x % 2 == 0}

print(even_set)


# Output:

{2, 4}


# In this case, we use a set comprehension with a conditional statement ('if x % 2 == 0') to filter only the even numbers from the 'numbers' list and create a new set 'even_set'.

# Set comprehensions can also be used with strings. Here's an example that creates a set of unique characters from a string:


# Example 3: Creating a set of unique characters using set comprehension

string = "Hello, World!"

unique_characters = {ch for ch in string}

print(unique_characters)


# Output:

{'W', 'r', ',', '!', 'd', 'e', 'H', 'o', 'l', ' '}


# In this example, we iterate over each character ('ch') in the string and create a new set 'unique_characters' that contains unique characters from the string.

# Set comprehensions provide a concise and expressive way to create new sets based on existing sequences. 
# They are useful for creating sets with unique elements or performing set operations. 
# Similar to list comprehensions, it's important to ensure that set comprehensions do not become overly complex or nested for the sake of readability and maintainability.