# range()
# A built-in function that returns an immutable sequence of numbers
# It is commonly used to create a sequence of integers to use in a for loop or to generate a list of numbers

# Basic syntax of the range() function is range(start, stop, step)

# Here are a few examples of using range():

# Print the numbers from 0 to 4
for i in range(5):
	print(i)

# Print the even numbers from 0 to 8
for i in range(0, 9, 2):
	print(i)

# Generate a list of squares of numbers from 1 to 5
squares = [i**2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Note that range() returns an object of type range, which is an immutable sequence type. 
# If you need a list of numbers instead, you can convert the range object to a list using the list() function:

# Generate a list of numbers from 1 to 10
numbers = list(range(1, 11))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
