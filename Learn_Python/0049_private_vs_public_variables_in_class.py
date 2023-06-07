# Private vs Public variables in class 

# In Python, the concepts of private and public variables are achieved through naming conventions rather than strict access modifiers like in some other programming languages. The convention is to use underscores to indicate the intended visibility of variables. Here's an explanation of private and public variables in Python:

# 1. Public Variables:
#    - By convention, variables without any leading underscores are considered public.
#    - Public variables can be accessed and modified from both inside and outside the class.
#    - They are accessible to other classes and code that imports the class.

# Here's an example of a class with a public variable:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

circle = Circle(5)
print(circle.radius)  # Output: 5
circle.radius = 10
print(circle.radius)  # Output: 10

# In the example above, the 'radius' variable is a public variable. It can be accessed and modified directly from outside the class by using the dot notation ('circle.radius').

# 2. Private Variables:
#    - By convention, variables with a single leading underscore (e.g., '_variable') are considered private.
#    - Private variables are intended to be internal to the class and not accessed directly from outside.
#    - Python doesn't enforce strict access control, and private variables can still be accessed and modified from outside the class, but it's a convention to treat them as private and avoid direct access.

# Here's an example of a class with a private variable:

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return 3.14159 * (self._radius ** 2)

circle = Circle(5)
print(circle._radius)  # Output: 5
circle._radius = 10
print(circle._radius)  # Output: 10

# In the example above, the '_radius' variable is a private variable. Although it can be accessed and modified directly from outside the class, it's a convention to treat it as private and access it through public methods or properties.

# It's important to note that private variables are not enforced by the language itself, and the leading underscore is simply a naming convention to indicate their intended visibility. It's up to developers to follow the convention and respect the intended usage of public and private variables.