# Magic method / Dunder method

# In Python, magic methods, also known as dunder methods (short for "double underscore" methods), are special methods with names surrounded by double underscores. 
# These methods allow you to define custom behavior for built-in operations, such as arithmetic operations, comparison, string representation, and more. 
# They are called automatically by the Python interpreter in response to specific events or operations.

# Here are a few examples of commonly used magic methods:

# - `__init__`: This method is called when an object is created from a class and is used for initializing the object's attributes.

# - `__str__`: This method returns a string representation of an object and is used when the object is passed to the `str()` function or when it is used in a string context.

#  `__add__`, `__sub__`, `__mul__`, `__div__`, etc.: These methods define behavior for arithmetic operations like addition, subtraction, multiplication, division, and others. They are called when the corresponding operator is used on objects of the class.

#  `__eq__`, `__ne__`, `__lt__`, `__gt__`, etc.: These methods define behavior for comparison operations like equality, inequality, less than, greater than, and others.

#  `__len__`: This method is used to define the behavior of the `len()` function when called on objects of a class. It should return the length or size of the object.

#  `__getitem__`, `__setitem__`, `__delitem__`: These methods are used to define behavior for accessing, assigning, and deleting items using indexing or slicing (`[]` notation) on objects.

# Magic methods allow you to customize the behavior of your objects and make them behave like built-in types. 
# By implementing these methods, you can define how your objects interact with operators, functions, and other language constructs.

# Here's an example to illustrate the usage of a magic method:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

point1 = Point(2, 3)
point2 = Point(5, 7)
sum_point = point1 + point2
print(sum_point)  # Output: (7, 10)

# In this example, the `Point` class defines the `__init__`, `__str__`, and `__add__` magic methods. The `__str__` method provides a string representation of the `Point` object. 
# The `__add__` method allows addition of two `Point` objects by defining the behavior of the `+` operator.

# When the line `point1 + point2` is executed, the `__add__` method of `point1` is called with `point2` as the argument. 
# The method performs the addition of the `x` and `y` coordinates of the two points and returns a new `Point` object representing the sum.

# Magic methods provide a way to make your objects more powerful, expressive, and compatible with the language's built-in features and conventions. 
# They are an important aspect of Python's object-oriented programming capabilities.