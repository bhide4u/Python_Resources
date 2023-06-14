# map() 

# In Python, 'map()' is a built-in function that applies a given function to each item of an iterable (e.g., a list, tuple, or string) and returns an iterator of the results. It provides a concise and efficient way to perform transformations on sequences of data.

# The syntax of the 'map()' function is as follows:


# map(function, iterable)


# - 'function': The function to apply to each element of the iterable.
# - 'iterable': The sequence of elements to apply the function to.

# Here's an example that demonstrates the usage of 'map()':

# Example 1: Convert a list of integers to their squares

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x: x**2, numbers)

# Convert the map object to a list
squared_numbers = list(squared_numbers)

print(squared_numbers)


# Output:

[1, 4, 9, 16, 25]


# In the above example, we have a list of numbers. We use 'map()' to apply a lambda function that calculates the square of each number in the list. The 'map()' function returns an iterator that produces the squared values. By converting the iterator to a list using 'list()', we obtain the final result.

# You can also use named functions instead of lambda functions. Here's an example that converts a list of strings to their lengths:


# Example 2: Convert a list of strings to their lengths

names = ["Alice", "Bob", "Charlie"]

name_lengths = map(len, names)

# Convert the map object to a list
name_lengths = list(name_lengths)

print(name_lengths)


# Output:

[5, 3, 7]


# In this case, we apply the built-in 'len()' function to each name in the list, resulting in a map object that contains the lengths of the strings. Converting the map object to a list gives us the final result.

# The 'map()' function allows you to apply a function to every element in an iterable, without the need for explicit loops. It is a powerful tool for performing transformations and calculations on collections of data efficiently.