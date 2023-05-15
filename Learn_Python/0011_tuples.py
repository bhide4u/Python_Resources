# Tuples

# Tuples: A tuple is similar to a list, but it is immutable, which means you cannot modify its contents once it is created. 
# Tuples are commonly used to store related data that should not be changed.

person = ('John', 25, 'Male')

# In Python, a tuple is a collection of ordered and immutable elements, enclosed in parentheses. 
# Tuples are similar to lists, but they cannot be modified once created. 
# This means that you can't add, remove, or change elements in a tuple.

# Here's an example of creating a tuple:
my_tuple = (1, 2, 3)

# You can also create a tuple using the built-in tuple() function:
my_tuple = tuple([1, 2, 3])

# One important thing to note about creating a tuple with a single element is that you must include a comma after the element, to distinguish it from just a regular value in parentheses. 

# For example:
single_tuple = (1,)

# Now that we've created a tuple, let's look at some of its features:

# Accessing elements: You can access elements in a tuple using indexing, just like with a list. For example:
my_tuple = (1, 2, 3)
print(my_tuple[0]) 		# Output: 1

# Slicing: You can also slice a tuple to extract a subset of its elements, just like with a list. For example:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4]) 		# Output: (2, 3, 4)

# Concatenation: You can concatenate tuples using the + operator, which creates a new tuple containing the elements of both tuples. For example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple) 	# Output: (1, 2, 3, 4, 5, 6)

# Tuple unpacking: You can use tuple unpacking to assign the elements of a tuple to separate variables. For example:
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a) 			# Output: 1
print(b) 			# Output: 2
print(c) 			# Output: 3

# Length: You can find the length of a tuple using the built-in len() function. For example:
my_tuple = (1, 2, 3)
print(len(my_tuple)) 		# Output: 3

# Immutable: Unlike lists, tuples are immutable, which means you cannot add, remove or change elements once a tuple has been created. For example:
my_tuple = (1, 2, 3)
my_tuple[0] = 4 		# Raises TypeError: 'tuple' object does not support item assignment

# Tuples are commonly used for returning multiple values from a function, as they can be unpacked to separate variables. 
# They are also used to create a collection of elements that should not be modified, or to represent an ordered collection of items where the order should not be changed.
