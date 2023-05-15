# Sets

# Sets: A set is an unordered collection of unique elements.
# Sets are useful when you need to perform operations such as intersection, union, and difference on collections of data.

fruits = {'apple', 'banana', 'cherry'}

# In Python, a set is an unordered collection of unique elements enclosed in curly braces {} or created using the built-in set() function. Sets are similar to lists and tuples, but they cannot contain duplicate values.

# Here's an example of creating a set:
my_set = {1, 2, 3}

# You can also create a set using the set() function:
my_set = set([1, 2, 3])

# One of the key features of a set is that it only contains unique elements. If you try to add a duplicate value to a set, it will be ignored. For example:
my_set = {1, 2, 3}
my_set.add(3) 	    # Ignored, since 3 is already in the set
print(my_set) 		# Output: {1, 2, 3}

# Here are some other important features of sets:

# Membership testing: You can test whether an element is in a set using the in operator. For example:
my_set = {1, 2, 3}
print(2 in my_set) 	# Output: True
print(4 in my_set) 	# Output: False

# Set operations: You can perform operations on sets, such as union, intersection, and difference, using various methods or operators. 
# For example:
set1 = {1, 2, 3}
set2 = {2, 3, 4}

union_set = set1.union(set2)
print(union_set) 	        # Output: {1, 2, 3, 4}

intersection_set = set1.intersection(set2)
print(intersection_set) 	# Output: {2, 3}

difference_set = set1.difference(set2)
print(difference_set) 		# Output: {1}