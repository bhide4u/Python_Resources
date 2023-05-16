# Functions

# A Python function is a block of reusable code that performs a specific task. 
# Functions allow you to break your program down into smaller, more manageable pieces, making your code easier to read, write, and maintain. 
# In Python, functions are defined using the "def" keyword, followed by the function name, arguments in parentheses, and a colon. 
# The function body is indented below the header, and it contains the code that performs the task.

# Here is an example of a Python function that calculates the area of a circle, given its radius:
def calculate_area(radius):
	pi = 3.14159
	area = pi * radius**2
	return area

# In this function, "calculate_area" is the function name, and "radius" is the argument that the function takes. 
# The function calculates the area of the circle using the formula pi times the radius squared, and then returns the result using the "return" keyword.

# You can call the function by passing a value for the radius, like this:

# calculate_area(5)
# 78.53975

# This will return the area of a circle with a radius of 5.

# Functions can also have multiple arguments, like this:
def add_numbers(x, y):
	sum = x + y
	return sum

# This function takes two arguments, "x" and "y", adds them together, and then returns the result.

# You can call this function by passing two values for "x" and "y":

# add_numbers(2, 3)
# 5

# This will return the sum of 2 and 3, which is 5.

# Functions can also have optional arguments, like this:
def greet(name, greeting='Hello'):
    print(greeting, name)

# In this function, "name" is a required argument, while "greeting" is an optional argument that defaults to "Hello" if no value is provided.

# You can call this function with or without a value for "greeting":

greet('Bob')
# Hello Bob

greet('Alice', 'Hi')
# Hi Alice

# In the first example, "greeting" defaults to "Hello", while in the second example, it is set to "Hi".

# Functions can also return multiple values, like this:
def rectangle_dimensions(length, width):
	area = length * width
	perimeter = 2 * (length + width)
	return area, perimeter

# In this function, "rectangle_dimensions", the area and perimeter of a rectangle are calculated using the length and width passed as arguments, and then returned as a tuple.

# You can call this function and assign its output to two variables like this:

area, perimeter = rectangle_dimensions(3, 4)
print('Area:', area)
# Area: 12

print('Perimeter:', perimeter)
# Perimeter: 14

# This will print the area and perimeter of a rectangle with a length of 3 and a width of 4.

# Conventions - 
# - Should do one thing really well
# - And function should return something 

# Arguments vs Parameters - 

# Parameter - define a function 
# Parameters are placeholders or variables defined in the function declaration or definition. 
# They represent the values that a function expects to receive when it is called. Parameters are defined within the parentheses following the function name.

# Argument - call , invoke a function 
# Actual values passed to a function when it is called. 
# They correspond to the parameters defined in the function declaration. 
# When a function is called, the arguments are provided within the parentheses.

# Positional arguments
# positional arguments are the arguments that are passed to a function based on their position or order. When calling a function, the positional arguments are assigned to the parameters in the function declaration based on their position.

# Here's an example to illustrate positional arguments:
def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet("Alice", 25)

# In this example, the function greet takes two parameters: name and age. 
# When calling the function with greet("Alice", 25), the value "Alice" is assigned to the name parameter, and the value 25 is assigned to the age parameter. 
# The order of the arguments matters, as they are assigned to the parameters in the same order.

# Positional arguments are useful when the order of the arguments is meaningful and consistent with the function's definition. 
# However, it's important to ensure that the number and order of the arguments match the function's parameter list; otherwise, you may encounter errors or unexpected behavior.

# Default parameters 
# In Python, default parameters allow you to specify a default value for a function's parameter. 
# When a default value is assigned to a parameter, it means that the argument for that parameter becomes optional when calling the function. 
# If no argument is provided for a parameter with a default value, the default value will be used.

# Here's an example that demonstrates the use of default parameters:
def greet(name, message="Hello"):
    print(message + ", " + name + "!")

greet("Alice")
greet("Bob", "Hi")

# In this example, the `greet` function has two parameters: `name` and `message`. 
# The `message` parameter has a default value of `"Hello"`. 
# When calling the function with `greet("Alice")`, the default value `"Hello"` is used for the `message` parameter, and the output will be `"Hello, Alice!"`. 
# In the second function call, `greet("Bob", "Hi")`, the provided argument `"Hi"` is used for the `message` parameter, and the output will be `"Hi, Bob!"`.

# Default parameters are helpful when you want to provide a default behavior or value for a parameter but still allow flexibility for the caller to override that value if desired. 
# They make functions more versatile and allow you to provide a reasonable default behavior without requiring the caller to always specify all arguments.

# Keyword arguments 
# In Python functions, keyword arguments allow you to specify arguments explicitly by using the parameter name followed by the corresponding value when calling a function. 
# This provides more flexibility in function calls because you can specify arguments in any order, and even skip some if desired.

# Here's an example to illustrate keyword arguments:
def greet(name, message):
    print(message + ", " + name + "!")

greet(name="Alice", message="Hello")
greet(message="Hi", name="Bob")

# In this example, the `greet` function has two parameters: `name` and `message`. When calling the function, we use keyword arguments to explicitly associate the values with the corresponding parameters. The order in which the arguments are specified doesn't matter.

# In the first function call, `greet(name="Alice", message="Hello")`, the keyword arguments are provided in the order `name="Alice"` and `message="Hello"`. The function will print `"Hello, Alice!"`.

# In the second function call, `greet(message="Hi", name="Bob")`, the keyword arguments are provided in the opposite order. However, since we explicitly associate each argument with the respective parameter, the function will print `"Hi, Bob!"`.

# Keyword arguments are particularly useful when a function has multiple parameters, and you want to make it clear which argument corresponds to which parameter. They enhance the readability and maintainability of code, especially when there are default values and optional parameters involved.

# Return keyword  - if not gives none, automatically exits the function 
# In Python, the `return` keyword is used in functions to specify the value or values that the function should return when it is called. 
# When a `return` statement is encountered in a function, it immediately exits the function and returns the specified value(s) to the caller.

# Here's an example to illustrate the usage of the `return` keyword:
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(3, 5)
print(sum_result)

# In this example, the `add_numbers` function takes two arguments `a` and `b` and calculates their sum. The `return` statement is used to specify that the calculated result should be returned as the function's output. When calling `add_numbers(3, 5)`, the function calculates the sum of 3 and 5, assigns it to the `result` variable, and then returns that value.

# The returned value can be stored in a variable, as shown in the example with `sum_result`, and used later in the code.

# It's important to note that a function can have multiple `return` statements, but only one will be executed when the function is called. 
# The execution of a `return` statement terminates the function, so any code after a `return` statement will not be executed.

# Additionally, if no `return` statement is encountered in a function, or if a `return` statement without any value is used, the function will implicitly return `None`, which represents the absence of a value.

# The `return` keyword is essential for functions as it allows them to produce results and pass information back to the caller, enabling code reusability and modular design.


# Nested functions 

# Different approaches- 
# The two approaches you provided both involve nested functions, but they differ in how they are called and the values they return.

# Approach 1:
def function_one(num1, num2):
    def another_function(num1, num2):
        return num1 + num2
    return another_function

total = function_one(10, 20)
print(total(10, 20))

# In this approach, `function_one` returns the inner function `another_function` itself. 
# When `function_one(10, 20)` is called, it returns the `another_function`. 
# This means that `total` now refers to `another_function`. 
# Subsequently, `total(10, 20)` is called, executing the `another_function` with the arguments `10` and `20`. 
# The result, which is the sum of the arguments, is printed.

# Approach 2:
def function_one(num1, num2):
    def another_function(num1, num2):
        return num1 + num2
    return another_function(num1, num2)

total = function_one(10, 20)
print(total)

# In this approach, `function_one` returns the result of calling `another_function` with the arguments `num1` and `num2`. When `function_one(10, 20)` is called, it invokes `another_function(10, 20)` and returns the sum of the arguments. 
# Consequently, `total` holds the return value of `another_function`, which is the sum of `10` and `20`. 
# This value is then printed.

# To summarize:
# - In Approach 1, the function returns the inner function itself, allowing it to be called separately.
# - In Approach 2, the function calls the inner function with specific arguments and returns the result directly.

# Both approaches are valid and serve different purposes. Approach 1 provides a way to store and use the inner function for later use, while Approach 2 immediately executes the inner function and returns the result.

# Methods vs functions 
# In Python, both methods and functions are used to encapsulate a set of instructions that can be executed repeatedly. 
# However, there are some differences between the two.

# A function is a block of code that is designed to perform a specific task. 
# It takes some input (known as arguments or parameters), performs a computation on them, and returns a value (or values). 
# Functions in Python are defined using the `def` keyword, and can be called from anywhere in the code.

# Here's an example of a function in Python:
def square(num):
    return num**2

# In this example, the `square` function takes an argument `num` and returns its square.

# On the other hand, a method is a function that is associated with an object. 
# In Python, objects are instances of classes, and methods are functions that are defined within a class. They can be used to manipulate the object's data or perform specific actions associated with the object.

# Here's an example of a method in Python:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# In this example, the `Person` class has a method called `greet`. This method takes no arguments (apart from `self`, which is a reference to the object itself), and prints a message that introduces the person's name and age.

# The main differences between functions and methods in Python are:

# 1. Methods are defined within classes and are associated with objects, while functions are standalone blocks of code.
# 2. Methods are called on an object using the dot notation, while functions are called by their name.
# 3. Methods can access and manipulate the object's data, while functions can only access their own arguments and local variables.

# In summary, methods are functions that are associated with objects, while functions are standalone blocks of code. 
# Methods can access and manipulate the object's data, while functions can only access their own arguments and local variables.

# Functions - 
# print()
# list()
# input()

# Method needs to be owned by something (right side of the dot) object or datatype
# .capitalize()
# .count()


# docstrings 
# In Python, a docstring (documentation string) is a string literal used to provide documentation and descriptions for modules, classes, functions, and methods. 
# It serves as a way to document the purpose, behavior, parameters, and return values of a piece of code.

# Docstrings are enclosed in triple quotes (either single or double) and are typically placed immediately after the definition of a module, class, function, or method. 
# They can span multiple lines and are often formatted using indentation and appropriate section headers.

# Here's an example of a docstring for a function:
def calculate_square(num):
    """
    Calculates the square of a given number.
    
    Parameters:
    num (int): The number for which to calculate the square.
    
    Returns:
    int: The square of the input number.
    """
    return num ** 2

# In this example, the docstring provides a clear and concise description of the `calculate_square` function, including the purpose, parameters, and return value. 
# It follows a standardized format, with a brief summary, a "Parameters" section that describes the input arguments, and a "Returns" section that explains the output value.

# Docstrings are beneficial for several reasons:

# 1. Documentation: Docstrings serve as self-contained documentation, helping users understand how to use the code without having to examine the implementation details.
# 2. Readability: Well-written docstrings improve code readability and maintainability, making it easier for other developers (including yourself) to understand and use the code.
# 3. Documentation generation: Docstrings can be automatically extracted to generate documentation in various formats, such as HTML or PDF, using tools like Sphinx.

# To access a docstring, you can use the `help()` function or access the `__doc__` attribute of an object. 

# For example:
print(help(calculate_square))
print(calculate_square.__doc__)

# Both of these approaches will display the docstring of the `calculate_square` function.

# In summary, docstrings are used to provide documentation and descriptions for modules, classes, functions, and methods in Python. 
# They improve code understanding, maintainability, and can be used for automatic documentation generation.
