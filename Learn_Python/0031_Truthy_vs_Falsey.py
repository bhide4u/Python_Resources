# Truthy vs Falsey

# In Python, a value is said to be "truthy" if it evaluates to True in a boolean context, and "falsey" if it evaluates to False. 
# When a boolean value is expected in a Python expression, any value can be used, and Python will automatically convert it to a boolean using the following rules:

# Falsey values: False, 0, 0.0, "" (empty string), None, [] (empty list), {} (empty dictionary), and () (empty tuple)

# Truthy values: anything else that is not falsey


# Here are some examples to illustrate truthy vs falsey in Python:

if 0:
    print("This will not be printed, because 0 is falsey.")

if "":
    print("This will not be printed, because an empty string is falsey.")
    
if None:
    print("This will not be printed, because None is falsey.")
    
if []:
	print("This will not be printed, because an empty list is falsey.")
    
if {}:
	print("This will not be printed, because an empty dictionary is falsey.")
    
if ():
	print("This will not be printed, because an empty tuple is falsey.")
    
if "hello":
	print("This will be printed, because a non-empty string is truthy.")
    
if [1, 2, 3]:
	print("This will be printed, because a non-empty list is truthy.")
    
if {"a": 1, "b": 2}:
	print("This will be printed, because a non-empty dictionary is truthy.")
    
if (1, 2, 3):
	print("This will be printed, because a non-empty tuple is truthy.")


# Note that the bool() function can also be used to convert a value to a boolean explicitly. 
# For example:

print(bool(0))   		# False
print(bool(""))  		# False
print(bool(None))	    # False
print(bool([]))  		# False
print(bool({}))  		# False
print(bool(()))  		# False
print(bool("hello")) 	# True
print(bool([1, 2]))  	# True
print(bool({"a": 1}))	# True
print(bool((1,)))	    # True

# To make use of truthy and falsey values in Python, you can use them in conditional statements like if, elif, and while loops. 

# For example:

x = 5
if x > 10:
	print("x is greater than 10")
elif x > 5:
	print("x is greater than 5 but less than or equal to 10")
else:
	print("x is less than or equal to 5")

# In this example, the first condition x > 10 is false, so Python moves on to the next condition x > 5, which is also false, so it finally executes the else block.

# Another example of using truthy and falsey values is checking if a variable is defined:

# Define a variable
my_var = "hello"

# Check if the variable is defined
if my_var:
	print("my_var is defined")
else:
	print("my_var is not defined")

# In this example, the if statement checks if my_var is truthy, which means it's defined and has a value. 
# If my_var was not defined (e.g. my_var = None), then the else block would be executed instead.

# It's important to keep truthy and falsey values in mind when working with conditional logic in Python, as it can help simplify your code and make it more readable.
