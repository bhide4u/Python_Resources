# Object Introspection

# Object introspection in Python refers to the ability to examine and analyze objects at runtime to retrieve information about their structure, attributes, methods, and more. It allows you to programmatically inspect objects and obtain information about their properties, which can be helpful for debugging, exploration, and dynamic behavior.

# Here's an example to demonstrate object introspection:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

person = Person("Alice", 25)

# Checking object type
print(type(person))  # Output: <class '__main__.Person'>

# Listing object attributes
print(dir(person))
# Output:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', 'age', 'greet', 'name']

# Accessing object attributes
print(person.name)  # Output: Alice
print(person.age)  # Output: 25

# Checking if an attribute exists
print(hasattr(person, 'name'))  # Output: True
print(hasattr(person, 'height'))  # Output: False

# Getting the value of an attribute dynamically
attribute = getattr(person, 'age')
print(attribute)  # Output: 25

# Checking if an object has a method
print(hasattr(person, 'greet'))  # Output: True
print(callable(getattr(person, 'greet')))  # Output: True

# Invoking a method dynamically
method = getattr(person, 'greet')
method()  # Output: Hello, my name is Alice.


# In this example, we have a 'Person' class with attributes 'name' and 'age', as well as a method 'greet'. Using object introspection techniques, we perform various operations on an instance of the 'Person' class named 'person':

# - 'type(person)' returns the type of the object as '<class '__main__.Person'>'.
# - 'dir(person)' lists all the attributes and methods of the object.
# - 'hasattr(person, 'name')' checks if the object has an attribute named ''name''.
# - 'getattr(person, 'age')' dynamically retrieves the value of the ''age'' attribute.
# - 'hasattr(person, 'greet')' checks if the object has a method named ''greet''.
# - 'getattr(person, 'greet')' retrieves the method object itself.
# - 'method()' calls the 'greet' method on the object.

# Object introspection allows you to explore the structure of objects dynamically, retrieve attribute values, check for the existence of attributes or methods, and even call methods dynamically. It provides powerful capabilities for inspecting and interacting with objects at runtime.