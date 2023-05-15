# Lists

# Lists: A list is a collection of items that can be of any data type. Lists are mutable, which means you can add, remove, or modify elements in the list.

fruits = ['apple', 'banana', 'cherry']

# In Python, a list is a collection of values that are ordered and changeable. 
# Lists are one of the most versatile and commonly used data structures in Python
# They can be used to store any combination of data types, including other lists.

# Lists are created using square brackets [ ] and commas (,) are used to separate values. 
# For example, 
my_list = [1, 2, 3] # creates a list with three values.

# Lists are ordered, which means that the position of each value in the list is important. 
# You can access individual values in a list using their index, which starts at 0 for the first value in the list. 
# For example, 
my_list[0] # would return the first value in the list.

# Lists are mutable, which means that you can add, remove, or modify values in a list after it has been created. 
# For example, 
my_list.append(4) # would add the value 4 to the end of the list.

# Lists can contain any combination of data types, including other lists. 
# This means that you can create nested lists, where one or more values in the list are also lists.

# Here are some examples of using lists in Python:

# Creating a list
my_list = [1, 2, 3, "hello", True]

# Accessing values in a list
print(my_list[0])  # 1
print(my_list[3])  # "hello"

# Modifying a list
my_list[1] = "world"
print(my_list)  # [1, "world", 3, "hello", True]

# Adding values to a list
my_list.append(4)
print(my_list)  # [1, "world", 3, "hello", True, 4]

# Removing values from a list
my_list.remove("hello")
print(my_list)  # [1, "world", 3, True, 4]

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # 6

# List slicing
# list slicing is a way to extract a portion of a list by specifying a range of indices. The syntax for list slicing is as follows:

# my_list[start:stop:step]

# start is the index of the first element to include in the slice (inclusive).
# stop is the index of the last element to include in the slice (exclusive).
# step is the increment between elements in the slice (default is 1).

# Here are some examples of using list slicing in Python:

# Creating a list
my_list = [0, 1, 2, 3, 4, 5]

# Slicing a list
print(my_list[1:4])  	# [1, 2, 3]
print(my_list[:3])  	# [0, 1, 2]
print(my_list[3:])  	# [3, 4, 5]
print(my_list[::2])  	# [0, 2, 4]
print(my_list[1::2])  	# [1, 3, 5]

# Matrix - 
# In Python, a multi-dimensional list is a list of lists. Each element of the outer list is itself a list, which can contain other lists, and so on. Multi-dimensional lists are useful for representing matrices, tables, or any other data structure that has multiple dimensions.

# Here's an example of a two-dimensional list in Python:

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

# In this example, the matrix is a 3x3 matrix, with three rows and three columns. 
# The first row is [1, 2, 3], the second row is [4, 5, 6], and the third row is [7, 8, 9].

# You can access individual elements of a multi-dimensional list using two indices, one for the row and one for the column. 
# For example, to access the element in the second row and third column of the matrix above, you can use the following code:

print(matrix[1][2])  # Output: 6

# You can also use list slicing with multi-dimensional lists to extract submatrices. 
# For example, to extract the first two rows and the first two columns of the matrix, you can use the following code:

submatrix = [row[:2] for row in matrix[:2]]
print(submatrix)  # Output: [[1, 2], [4, 5]]

# In this code, we used list slicing with two indices to extract the first two rows (matrix[:2]) and then used a list comprehension to extract the first two elements of each row (row[:2]).

# Multi-dimensional lists can have any number of dimensions, not just two. For example, a three-dimensional list might represent a cube, and a four-dimensional list might represent a hypercube. 
# The principles of indexing and slicing are the same regardless of the number of dimensions.


# List unpacking
# unpacking is a way to assign each element of a list to a separate variable, in a single line of code

# Here is an example that demonstrates the use of list unpacking:
	
my_list = [1, 2, 3, 4, 5]
a, b, *c = my_list

print(a) # Output: 1
print(b) # Output: 2
print(c) # Output: [3, 4, 5]

# In this example, we have a list my_list that contains five elements. 
# We use list unpacking to assign the first two elements to the variables a and b, and the remaining elements to the list variable c, using the special * syntax. 
# The * syntax indicates that any remaining elements in the list should be packed into a list.

# List unpacking can also be used to swap the values of two variables without using a temporary variable:

a = 1
b = 2

a, b = b, a

print(a) 	# Output: 2
print(b) 	# Output: 1
