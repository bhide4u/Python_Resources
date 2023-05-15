# Variables

# Variable declaration in python

# 1. Use descriptive variable names that are easy to read and understand.
# For example, use ‘num_of_students’ instead of ‘n’, ‘students’ or ‘s’.

# 2. Avoid using reserved keywords as variable names.
# For example, don't use ‘print’ or ‘list’ as variable names.

# 3. Use lower case letters for variable names, with words separated by underscores.
# This is known as snake_case. For example, ‘my_variable_name’ is better than ‘MyVariableName’ or ‘myvariablename’.

# 4. Use meaningful variable names that reflect the purpose of the variable.
# For example, ‘user_age’ is better than ‘age’ or ‘variable1’.

# 5. Declare variables close to where they are first used.
# This helps to reduce confusion and makes it easier to understand the purpose of the variable.

# 6. Use constants for values that don't change.
# Constants are usually defined in all capital letters.
# For example, ‘PI = 3.14159’.

# 7. Don't reuse variable names for different purposes in the same block of code.
# This can lead to confusion and errors.

# 8. Avoid using global variables unless absolutely necessary.
# Global variables can make code difficult to understand and debug.

# 9. Use variable type annotations to indicate the type of a variable.
# For example, ‘num_students: int = 20’.
# This can help with code clarity and error checking.


# Descriptive and meaningful variable names
number_of_students = 100

# Do not use reserved keywords
list = 'List of Students'   # list is a reserved keyword

# Use snake_case for variable naming
my_variable_name = 'This is my variable'

# Declare variables near to their first usage

# Constants are defined by all capital values
PI = 3.14159

#  Don't reuse variable names in same block of code to avoid confusion

# Avoid using global variables unless absolutely necessary

# Use variable type annotations to indicate the type of a variable
num_students: int = 20


# Variables that start with a single underscore (_) or double underscore (__) have a special meaning
# These variables are known as "special variables" or "magic variables"

def add(num1, num2):
    return num1 + num2


_ = add(10, 20)  # Used as a placeholder for variables that are not used in the code


# The double underscore is used for name mangling in Python classes.
# Name mangling is a technique that makes a variable or method private to a class

class MyClass:
    def __init__(self):
        self.__my_private_variable = 42

    def get_my_private_variable(self):
        return self.__my_private_variable

# In this example, the double underscore before the variable name makes it "private" to the class.
# It can still be accessed by calling the ‘get_my_private_variable’ method.


# __init__ --> Double underscore on both sides
# Used for special methods or attributes in Python

class MyClass:
    def __init__(self):
    	self.my_variable = 42

# In this example, ‘__init__’ is a special method that is called when an object of the ‘MyClass class’ is created.

# Keep in mind that while these special variables have specific meanings in Python, they are not enforced by the language. For example, you can still access a "private" variable in Python by using its name, even if it starts with a double underscore. However, it is considered best practice to follow the conventions of the language and use these special variables as intended.


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"

# One Value to Multiple Variables
x = y = z = "Orange"

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# You can also use the ‘+’ operator to output multiple variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Following will give error as string and int are combined
x = 5
y = "John"
print(x + y)
