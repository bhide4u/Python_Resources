# Modules in python 

# In Python, a module is a file containing Python definitions and statements. It is used to organize and reuse code by grouping related functionalities together. Modules can be imported and used in other Python programs to access the functions, classes, and variables defined within them. Here's an explanation of modules with examples:

# Example 1: Creating a Module
# Let's say we have a file named 'my_module.py' containing the following code:


def greet(name):
    print(f"Hello, {name}!")

def calculate_square(n):
    return n ** 2

pi = 3.14159


# In this example, 'my_module.py' is a module that defines three entities: 'greet()', 'calculate_square()', and 'pi'. These can be functions, classes, variables, or any other Python objects.

# Example 2: Importing a Module
# To use the functionalities defined in a module, we need to import it into our Python program. Here's an example:


import my_module

my_module.greet("Alice")
square = my_module.calculate_square(5)
print(square)
print(my_module.pi)


# In this example, we import the 'my_module' module using the 'import' statement. We can then access the functions 'greet()' and 'calculate_square()', as well as the variable 'pi', using the module name as a prefix.

# Example 3: Importing Specific Entities
# If we only need certain entities from a module, we can import them specifically. Here's an example:


from my_module import greet, calculate_square

greet("Bob")
square = calculate_square(3)
print(square)


# In this example, we import only the 'greet()' and 'calculate_square()' functions from the 'my_module' module. We can directly use these functions without referencing the module name.

# Example 4: Importing with Alias
# We can also import a module or its entities with an alias, allowing us to use a shorter or more convenient name. Here's an example:


import my_module as mm

mm.greet("Charlie")
square = mm.calculate_square(4)
print(square)


# In this example, we import the 'my_module' module with the alias 'mm'. We can then use 'mm' as a shorter name to access the module's functionalities.

# Example 5: Importing All Entities
# It's also possible to import all entities from a module using the '*' wildcard. However, this approach is generally discouraged as it can lead to naming conflicts. Here's an example:


from my_module import *

greet("Dave")
square = calculate_square(2)
print(square)
print(pi)


# In this example, we import all entities from the 'my_module' module using '*'. We can directly use the functions 'greet()' and 'calculate_square()', as well as the variable 'pi', without referencing the module name.

# Modules in Python provide a way to organize and encapsulate code, promoting reusability and modularity. They allow us to separate concerns, import functionality from other files, and build complex programs by combining multiple modules together.