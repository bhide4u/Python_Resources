# Abstraction

# Abstraction is a concept in object-oriented programming (OOP) that allows you to create abstract classes or interfaces that define a common behavior without providing the implementation details. It focuses on hiding the complexity and exposing only the essential features or functionalities to the outside world. In Python, abstraction can be achieved using abstract base classes (ABC) from the 'abc' module. Here's an example to illustrate abstraction step by step:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

# 1. In the code above, we define an abstract base class called 'Shape' by inheriting from 'ABC', which stands for Abstract Base Class.

# 2. Inside the 'Shape' class, we define two abstract methods: 'calculate_area()' and 'calculate_perimeter()'. These methods don't have any implementation details and are marked with the '@abstractmethod' decorator.

# 3. The 'Rectangle' class and 'Circle' class inherit from the 'Shape' class. Since 'Shape' is an abstract base class, any concrete class inheriting from it must provide implementations for all the abstract methods.

# 4. The 'Rectangle' class overrides the abstract methods 'calculate_area()' and 'calculate_perimeter()' with its own implementations based on the width and height.

# 5. Similarly, the 'Circle' class provides its own implementations for the abstract methods, using the radius.

# By using abstraction, we define a common interface (the abstract methods) that all shapes must have, but we don't provide the specific implementation details. Now, let's see how we can use the 'Rectangle' and 'Circle' classes:

rectangle = Rectangle(5, 3)
print(rectangle.calculate_area())  # Output: 15
print(rectangle.calculate_perimeter())  # Output: 16

circle = Circle(4)
print(circle.calculate_area())  # Output: 50.26544
print(circle.calculate_perimeter())  # Output: 25.13272

# 1. We create an instance of the 'Rectangle' class called 'rectangle', passing the width (5) and height (3) as arguments to the constructor.

# 2. We call the 'calculate_area()' method on 'rectangle' and print the result, which outputs 15.

# 3. We call the 'calculate_perimeter()' method on 'rectangle' and print the result, which outputs 16.

# 4. Similarly, we create an instance of the 'Circle' class called 'circle', passing the radius (4) as an argument to the constructor.

# 5. We call the 'calculate_area()' method on 'circle' and print the result, which outputs 50.26544.

# 6. We call the 'calculate_perimeter()' method on 'circle' and print the result, which outputs 25.13272.

# By utilizing abstraction, we can define common behaviors through abstract methods in the abstract base class, and each concrete subclass can provide its own implementation. This allows us to work with shapes without worrying about their specific implementation details, promoting