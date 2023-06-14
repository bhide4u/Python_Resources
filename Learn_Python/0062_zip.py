# zip()

# In Python, 'zip()' is a built-in function that takes multiple iterables as input and returns an iterator of tuples. 
# Each tuple contains the corresponding elements from the input iterables, aligned based on their indices.

# The syntax of the 'zip()' function is as follows:

# zip(*iterables)


# - 'iterables': Multiple iterables (e.g., lists, tuples) that you want to zip together.

# Here's an example that demonstrates the usage of 'zip()':

# Example 1: Zip two lists together

names = ["Alice", "Bob", "Charlie"]
ages = [25, 32, 42]

zipped_data = zip(names, ages)

# Convert the zip object to a list of tuples
zipped_data = list(zipped_data)

print(zipped_data)


# Output:

[('Alice', 25), ('Bob', 32), ('Charlie', 42)]


# In the above example, we have two lists: 'names' and 'ages'. We use 'zip()' to combine the elements from both lists into tuples. 
# Each tuple contains the corresponding name and age based on their indices. 
# By converting the zip object to a list of tuples, we obtain the final zipped data.

# If the input iterables have different lengths, 'zip()' stops when it reaches the end of the shortest iterable. 
# This ensures that the resulting iterator has tuples aligned only up to the shortest length.

# You can also use more than two iterables with 'zip()'. Here's an example that zips three lists together:

# Example 2: Zip three lists together

names = ["Alice", "Bob", "Charlie"]
ages = [25, 32, 42]
countries = ["USA", "Canada", "UK"]

zipped_data = zip(names, ages, countries)

# Convert the zip object to a list of tuples
zipped_data = list(zipped_data)

print(zipped_data)

# Output:

[('Alice', 25, 'USA'), ('Bob', 32, 'Canada'), ('Charlie', 42, 'UK')]


# In this case, we zip three lists ('names', 'ages', 'countries') together, resulting in tuples that contain the corresponding elements from each list.

# The 'zip()' function is useful when you need to combine multiple iterables and process their elements together. 
# It provides an elegant way to iterate over multiple sequences simultaneously, aligning the elements based on their indices.