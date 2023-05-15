# Variable Scoping

# 1. Global
# Defined outside of any function or class definition, and they can be accessed from anywhere in your code

x = 10

def print_x():
	print(x)

print_x()  # Output: 10

# x is global variable


# It's important to note that if you try to modify a global variable from within a function, you need to use the global keyword to indicate that you're referring to the global variable and not creating a new local variable with the same name. Here's an example:

x = 10

def modify_x():
	global x
	x = 20

modify_x()
print(x)  # Output: 20



# 2. Local
# Defined within a function or class definition, and they can only be accessed from within that function or class

def add_numbers(a, b):
	c = a + b
	print(c)

add_numbers(2, 3)  # Output: 5

# a, b, c are local variables
 