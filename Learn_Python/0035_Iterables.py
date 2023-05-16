# Iterables

# In Python, an iterable is any object that can be looped over using a for loop. 
# An iterable object is an object that has an __iter__() method that returns an iterator object. 
# An iterator object is an object that has a __next__() method that returns the next item in the sequence, and raises a StopIteration exception when there are no more items to return.

# Some examples of iterable objects in Python include:

# Lists: A list is an ordered collection of elements, and it can be iterated over using a for loop. 
# For example:
	
numbers = [1, 2, 3, 4, 5]
for num in numbers:
	print(num)

# Tuples: A tuple is similar to a list, but it is immutable. Tuples can also be iterated over using a for loop. 
# For example:

person = ("Alice", 25, "New York")
for item in person:
	print(item)

# Strings: A string is a sequence of characters, and it can be iterated over using a for loop. 
# For example:

message = "Hello, World!"
for char in message:
	print(char)

# Sets: A set is an unordered collection of unique elements, and it can be iterated over using a for loop. 
# For example:

names = {"Alice", "Bob", "Charlie"}
for name in names:
	print(name)

# Dictionaries: A dictionary is a collection of key-value pairs, and it can be iterated over using a for loop. 
# For example:

person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
	print(key, ":", value)

# In addition to these built-in iterable objects, you can also create your own iterable objects by defining a class with an __iter__() method that returns an iterator object. This is a powerful feature of Python that allows you to create custom iterable objects tailored to your specific needs.

# range()-
# The range() function in Python is used to generate a sequence of numbers that can be used in a for loop or other iteration constructs. 

# The basic syntax of the range() function is:
# range(stop)
# range(start, stop, step)

# The range() function takes one to three arguments:
# start (optional): The starting value of the sequence (inclusive). If not specified, the default value is 0.
# stop (required): The stopping value of the sequence (exclusive). This argument must be specified.
# step (optional): The step size between each number in the sequence. If not specified, the default value is 1.
# Here are a few examples of how the range() function can be used:

# Print the numbers from 0 to 4
for i in range(5):
	print(i)

# Print the even numbers from 0 to 8
for i in range(0, 9, 2):
	print(i)

# Print the odd numbers from 1 to 9
for i in range(1, 10, 2):
	print(i)

# In the first example, the range() function generates a sequence of numbers from 0 to 4 (inclusive) because we specified 5 as the stop argument.

# In the second example, the range() function generates a sequence of even numbers from 0 to 8 (inclusive) because we specified 0 as the start argument, 9 as the stop argument, and 2 as the step argument.

# In the third example, the range() function generates a sequence of odd numbers from 1 to 9 (inclusive) because we specified 1 as the start argument, 10 as the stop argument, and 2 as the step argument.

# It's worth noting that the range() function returns a sequence object that is not actually a list. 
# This means that you cannot access the individual elements of a range() object directly like you can with a list. 
# Instead, you must iterate over the range() object using a for loop or convert it to a list using the list() function.

for _ in range(0,10):
    print('i')

# Enumerate - 
# The enumerate() function in Python is a built-in function that adds a counter to an iterable object (like a list or a string) and returns an enumerate object. 
# The enumerate object contains pairs of the form (index, value) for each item in the iterable.

# The basic syntax of the enumerate() function is:
# enumerate(iterable, start=0)

# The enumerate() function takes two arguments:

# iterable (required): The iterable object that you want to enumerate.
# start (optional): The starting value of the index. If not specified, the default value is 0.

# Here is an example of how to use the enumerate() function:
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
	print(index, fruit)

# In this example, the enumerate() function is used to add a counter to the fruits list. 
# The resulting enumerate object contains pairs of the form (index, value) for each fruit in the list. 
# The for loop then iterates over the enumerate object and prints out the index and value of each fruit.

# The output of this code will be:

# 0 apple
# 1 banana
# 2 orange

# The enumerate() function can be useful when you want to keep track of the index of each item in an iterable object. 
# It is a handy shortcut that can save you from writing a separate counter variable and incrementing it manually.
