# OOPs
# 1. Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. 
# It focuses on representing real-world entities as objects that have 
# 1. attributes (data) and 
# 2. behaviors (methods). 

# OOP promotes modularity, reusability, and encapsulation, allowing developers to create complex systems by building and interacting with objects.

# In Python, like many other programming languages, OOP is supported. 
# It provides features such as classes, objects, inheritance, polymorphism, and encapsulation. 
# Classes define the blueprint for creating objects, while objects are instances of a class that can store data and perform actions through methods. 
# OOP allows for the organization and management of code in a structured and efficient manner.

# 2. In Python, the concept of "everything is an object" is closely related to its support for OOP. 
# It means that every entity in Python, including numbers, strings, functions, modules, and even classes themselves, is an object. 
# An object is an instance of a class, and Python treats them uniformly. This is in contrast to some other languages where primitive types (like integers or booleans) are treated differently from objects.

# Being an object means that these entities in Python have attributes (properties) and methods associated with them. 
# For example, a string object can have attributes like its length, and it can have methods like `upper()` or `split()`. 
# Functions can be assigned to variables, passed as arguments, and even have attributes. 
# This object-oriented nature of Python allows for greater flexibility and enables powerful programming techniques.

# 1. Class: In Python, a class is a blueprint or template that defines the structure and behavior of objects. It serves as a blueprint for creating objects, which are instances of the class. A class encapsulates data (attributes) and functions (methods) that operate on that data. It defines the characteristics and behavior that objects of that class will have.

# To create a class in Python, you use the `class` keyword followed by the class name. Inside a class, you can define attributes and methods that describe the properties and actions of objects created from that class. 

# Here's an example of a simple class definition:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating objects (instances) of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Calling a method on an object
person1.greet()

# In the example above, the `Person` class has two attributes (`name` and `age`) and a method (`greet()`). 
# Objects `person1` and `person2` are created from the `Person` class, and each object has its own set of attributes. The `greet()` method can be called on an instance of the class to perform a specific action.

# 2. Methods: In Python, methods are functions defined inside a class that operate on objects created from that class. 
# They are used to define the behavior of objects and perform actions related to the class. 
# Methods can access and modify the attributes of an object, and they can also take parameters like regular functions.

# In the previous example, the `greet()` function defined inside the `Person` class is a method. It takes `self` as the first parameter, which represents the instance of the class on which the method is called. By convention, the first parameter of a method is always `self`, but you can choose any valid name.

# Methods can be called on objects of the class using the dot notation. For example, `person1.greet()` calls the `greet()` method on the `person1` object. The method can access the attributes of the object using `self.attribute_name` syntax.

# 3. Attributes: Attributes are variables that hold data associated with an object. They represent the state or characteristics of an object. In Python, attributes are defined inside a class and can be accessed and modified through objects created from that class.

# Attributes can be classified into two types: instance attributes and class attributes. 

# - Instance attributes: These attributes are specific to each instance/object of a class. They are defined inside the class methods using the `self` keyword. Each instance of the class can have different values for its instance attributes.

# - Class attributes: These attributes are shared among all instances of a class. They are defined directly inside the class, outside of any methods. Class attributes have the same value for all instances of the class.

# Here's an example that demonstrates both types of attributes:

class Circle:
    # Class attribute
    pi = 3.14

    def __init__(self, radius):
        # Instance attribute
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius * self.radius

# Creating objects of the Circle class
circle1 = Circle(5)
circle2 = Circle(3)

print(circle1.radius)  # Output: 5
print(circle2.radius)  # Output: 3

print(circle1.calculate_area())  # Output: 78.5
print(circle2.calculate_area())  # Output: 28.26

# In the example above, `pi` is a class attribute of the `Circle` class. Each instance of the class can access this attribute using the dot notation (`self.pi` or `Circle.pi`). The `radius` attribute is an instance attribute specific to each object. It is assigned during object creation using the `__init__()` method. Each object can have a different value for the `radius` attribute.

# Methods of the class, such as `calculate_area()`, can access both class attributes (`self.pi`) and instance attributes (`self.radius`). They can perform operations using the attribute values to provide useful functionality.


# Procedural code and Object-Oriented Programming (OOP)

# Procedural code and Object-Oriented Programming (OOP) are two different programming paradigms that structure and organize code in different ways. Here's a comparison between procedural code and OOP:

# Procedural Code:
# 1. Structure: Procedural code is organized around procedures or functions that perform specific tasks. The code consists of a series of functions that manipulate data.
# 2. Data and Functions: In procedural code, data and functions are separate entities. Functions operate on data by passing it as arguments and returning results.
# 3. Global Data: Data can be accessed and modified by any function, leading to potential data integrity and security issues.
# 4. Code Reusability: Code reuse is achieved through functions that can be called multiple times from different parts of the code.
# 5. Emphasis on Procedure Flow: Procedural code is designed to be executed sequentially, with a clear flow of control from one function to another.

# Object-Oriented Programming (OOP):
# 1. Structure: OOP organizes code around objects that represent real-world entities or concepts. Objects encapsulate data (attributes) and behaviors (methods).
# 2. Objects and Classes: In OOP, objects are instances of classes. A class defines the blueprint or template for creating objects with shared attributes and behaviors.
# 3. Encapsulation and Data Abstraction: OOP promotes encapsulation, where data and methods that operate on that data are bundled together. This ensures data privacy and abstraction, allowing objects to expose only necessary information to the outside world.
# 4. Inheritance and Polymorphism: OOP supports inheritance, allowing classes to inherit attributes and behaviors from parent classes. Polymorphism enables objects of different classes to be treated interchangeably based on shared interfaces or inheritance.
# 5. Code Reusability and Modularity: OOP facilitates code reusability through inheritance and class hierarchies. It promotes modularity by dividing code into classes, making it easier to manage and maintain.
# 6. Emphasis on Relationships: OOP focuses on modeling relationships and interactions between objects, capturing complex systems more naturally.

# Overall, OOP provides a more structured and modular approach to programming, promoting code organization, reusability, and maintainability. It allows for modeling real-world scenarios more effectively by encapsulating data and behavior into objects. Procedural code, on the other hand, is more focused on sequential execution of functions and manipulation of data, without the same level of abstraction and encapsulation provided by OOP.

# help(ClassName) --> entire blueprint of class

# In Python, both class attributes and instance attributes are used to store data associated with a class. However, they have distinct characteristics and purposes. Let's explore the differences between class attributes and instance attributes in Python:

# 1. Class Attribute:
#    - Definition: Class attributes are defined directly within the class and are shared among all instances (objects) of the class. They are defined outside of any methods or constructors.
#    - Access: Class attributes can be accessed using the class name or any instance of the class. When accessed through an instance, the attribute value is inherited from the class.
#    - Modification: Class attributes can be modified by directly reassigning their value using the class name. The modification will be reflected across all instances and any subsequent instances.
#    - Purpose: Class attributes are typically used to store data that is common to all instances of the class. They represent characteristics or properties shared by all objects created from the class.

# Example:

class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

circle1 = Circle(5)
circle2 = Circle(3)

print(circle1.pi)  # Output: 3.14
print(circle2.pi)  # Output: 3.14

Circle.pi = 3.14159  # Modifying the class attribute

print(circle1.pi)  # Output: 3.14159
print(circle2.pi)  # Output: 3.14159

# 2. Instance Attribute:
#    - Definition: Instance attributes are specific to each instance (object) of a class. They are defined inside the methods or constructor of a class using the `self` keyword.
#    - Access: Instance attributes are accessed through the instance (object) of the class to which they belong. Each instance maintains its own copy of instance attributes.
#    - Modification: Instance attributes can be modified by accessing them through the instance and assigning a new value. The modification affects only that particular instance.
#    - Purpose: Instance attributes are used to store data that varies among instances or represents unique characteristics of each object created from the class.

# Example:

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Instance attribute

circle1 = Circle(5)
circle2 = Circle(3)

print(circle1.radius)  # Output: 5
print(circle2.radius)  # Output: 3

circle1.radius = 7  # Modifying the instance attribute for circle1

print(circle1.radius)  # Output: 7
print(circle2.radius)  # Output: 3


# In summary, class attributes are shared among all instances of a class and are defined outside of methods. They are accessed using the class name or any instance and can be modified globally. Instance attributes, on the other hand, are specific to each instance and are defined within methods using the `self` keyword. They are accessed and modified through instances, and each instance maintains its own copy of the attribute.


# __init__ method 

# The `__init__()` method is a special method in Python classes, also known as the constructor. It is automatically called when an object is created from a class. The purpose of the `__init__()` method is to initialize the attributes of an object by accepting arguments and assigning them to the object's instance variables.

# Here are some key points about the `__init__()` method:

# 1. Method Name: The method name must be `__init__` with double underscores on both sides. This is a reserved name in Python for the constructor method.

# 2. Parameters: The `__init__()` method takes at least one parameter, typically named `self`, which refers to the instance being created. It is a reference to the newly created object and allows access to its attributes and methods.

# 3. Initialization: Inside the `__init__()` method, you can define instance attributes by assigning values to `self.attribute_name`. These attributes will be specific to each object created from the class.

# 4. Object Creation: When an object is created from the class, the `__init__()` method is automatically called, and any arguments passed during object creation are passed to the `__init__()` method as well. These arguments can be used to initialize the object's attributes.

# Here's an example that demonstrates the usage of the `__init__()` method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25

print(person2.name)  # Output: Bob
print(person2.age)   # Output: 30

# In the example above, the `Person` class has an `__init__()` method that takes `name` and `age` as parameters. Inside the method, the values passed during object creation (`"Alice"` and `25` for `person1`, `"Bob"` and `30` for `person2`) are assigned to the instance attributes `self.name` and `self.age`, respectively. When the objects are created, the `__init__()` method is automatically called, initializing the objects with the specified attribute values.

# The `__init__()` method allows for convenient and consistent initialization of object attributes. It is commonly used to set up the initial state of an object and prepare it for use throughout its lifetime.


# ---------------------------------------------------



#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2