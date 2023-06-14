# filter()

# In Python, 'filter()' is a built-in function that filters elements from an iterable (e.g., a list, tuple, or string) based on a given function's condition. 
# It returns an iterator that contains only the elements for which the function's condition evaluates to 'True'.

# The syntax of the 'filter()' function is as follows:

# filter(function, iterable)


# - 'function': The function that specifies the condition for filtering.
# - 'iterable': The sequence of elements to be filtered.

# Here's an example that demonstrates the usage of 'filter()':

# Example 1: Filter even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object to a list
even_numbers = list(even_numbers)

print(even_numbers)


# Output:

[2, 4, 6, 8, 10]


# In the above example, we have a list of numbers. We use 'filter()' along with a lambda function that checks if each number is even ('x % 2 == 0'). 
# The 'filter()' function returns an iterator that yields only the elements that satisfy the condition. By converting the iterator to a list, we obtain the final result.

# You can also use named functions instead of lambda functions. Here's an example that filters names starting with the letter 'A':

# Example 2: Filter names starting with 'A'

names = ["Alice", "Bob", "Charlie", "Amy", "Andrew"]

filtered_names = filter(lambda name: name.startswith('A'), names)

# Convert the filter object to a list
filtered_names = list(filtered_names)

print(filtered_names)


# Output:

['Alice', 'Amy', 'Andrew']


# In this case, we apply a lambda function to each name in the list to check if it starts with the letter 'A'. 
# The 'filter()' function returns an iterator that contains only the names that satisfy the condition.

# The 'filter()' function is a convenient way to extract elements from a sequence based on a specific condition. 
# It allows you to selectively filter out elements without the need for explicit loops. By converting the filter object to a list or iterating over it, you can obtain the final filtered result.