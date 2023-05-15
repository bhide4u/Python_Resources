# in keyword
# a membership operator in Python that allows you to check if a value is present in a sequence or collection, such as a string, list, tuple, or dictionary
# syntax - value in sequence
# Returns True or False

# Here are some examples:

# Check if a value is in a string
text = "hello world"

if "hello" in text:
	print("Found!")
else:
	print("Not found.")

# Check if a value is in a list
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
	print("Found!")
else:
	print("Not found.")

# Check if a key is in a dictionary
person = {"name": "John", "age": 30}
if "name" in person:
	print("Found!")
else:
	print("Not found.")

# The in keyword can also be used with the not keyword to check if a value is not present in a sequence or collection:

# Check if a value is not in a string
text = "hello world"
if "foo" not in text:
	print("Not found.")
else:
	print("Found.")

# Check if a value is not in a list
numbers = [1, 2, 3, 4, 5]
if 6 not in numbers:
	print("Not found.")
else:
	print("Found.")

# Check if a key is not in a dictionary
person = {"name": "John", "age": 30}
if "email" not in person:
	print("Not found.")
else:
	print("Found.")
