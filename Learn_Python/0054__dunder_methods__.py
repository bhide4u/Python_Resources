# Dunder methods

# Dunder methods, also known as special methods or magic methods, are predefined methods in Python that start and end with double underscores (i.e., '__'). These methods define specific behaviors for built-in operations and allow you to customize the behavior of objects in various contexts. Dunder methods are invoked implicitly in response to certain operations or can be called explicitly. Here's an explanation of some commonly used dunder methods with examples:

# 1. '__init__(self, ...)': This method is called when an object is instantiated. It initializes the object and sets its initial state. Example:


class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")


# 2. '__str__(self)': This method returns a string representation of the object. It's used when the 'str()' function is called or when an object is printed. Example:


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

person = Person("Alice")
print(person)  # Output: Person: Alice


# 3. '__len__(self)': This method returns the length of the object. It's used when the 'len()' function is called on the object. Example:


class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5


# 4. '__getitem__(self, key)': This method allows the object to be indexed or sliced using square brackets ('[]'). It's used when accessing elements of the object. Example:


class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])  # Output: 3


# 5. '__setitem__(self, key, value)': This method allows the object to be modified through assignment using square brackets ('[]'). It's used when assigning values to elements of the object. Example:


class MyList:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([1, 2, 3, 4, 5])
my_list[2] = 10
print(my_list.items)  # Output: [1, 2, 10, 4, 5]


# These are just a few examples of dunder methods, but there are many more available. Dunder methods allow you to customize the behavior of objects in specific contexts, such as arithmetic operations ('__add__', '__sub__', etc.), comparison operations ('__eq__', '__lt__', etc.), and more. By implementing dunder methods, you can make your objects behave like built-in types and interact with them using familiar syntax and operations.