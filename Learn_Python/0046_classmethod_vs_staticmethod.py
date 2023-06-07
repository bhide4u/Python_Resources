# @classmethod vs @staticmethod

# In Python, both '@classmethod' and '@staticmethod' are decorators used to define methods within a class. They provide different ways to define and use methods that are not bound to the instance of the class. Here's an explanation of each decorator with examples:

# 1. '@classmethod':
#    - The '@classmethod' decorator defines a method that is bound to the class itself rather than an instance of the class.
#    - It takes the class (usually named 'cls') as the first parameter, rather than the instance (usually named 'self').
#    - It can be called on the class directly, without creating an instance of the class.
#    - '@classmethod' is commonly used for alternative constructors, class-specific operations, or methods that need to access class-level attributes.

# Here's an example to illustrate the usage of '@classmethod':


class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def area(self):
        return self.pi * (self.radius ** 2)

# Using the alternative constructor defined with @classmethod
circle = Circle.from_diameter(10)
print(circle.radius)  # Output: 5
print(circle.area())  # Output: 78.53975


# In the example above, the 'from_diameter()' method is decorated with '@classmethod'. It creates a new instance of the 'Circle' class by accepting the diameter as a parameter and calculating the radius. Since it's a class method, it can be called directly on the class itself, without creating an instance of 'Circle'.

# 2. '@staticmethod':
#    - The '@staticmethod' decorator defines a method that belongs to the class, but it doesn't have access to the class or instance attributes.
#    - It behaves like a regular function defined inside a class, but it's logically related to the class.
#    - '@staticmethod' does not require any reference to the class or instance and can be called on the class directly.
#    - It is commonly used for utility functions that don't rely on class-specific data.

# Here's an example to demonstrate the usage of '@staticmethod':


class MathUtils:
    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def add(a, b):
        return a + b

# Calling the static methods directly on mathematicalthe class
result = MathUtils.multiply(5, 3)
print(result)  # Output: 15

result = MathUtils.add(10, 20)
print(result)  # Output: 30


# In the example above, the 'multiply()' and 'add()' methods are decorated with '@staticmethod'. They perform basic mathematical operations and don't require any class-specific data. These static methods can be called directly on the class 'MathUtils' without creating an instance.

# Both '@classmethod' and '@staticmethod' decorators provide ways to define methods that are not tied to specific instances, but they differ in terms of the parameters they accept. '@classmethod' takes the class as the first parameter, while '@staticmethod' does not require any special parameters.