# super()

# In Python, 'super()' is a built-in function that allows you to call a method from the parent class. It provides a convenient way to invoke methods of the superclass, enabling you to reuse and extend functionality from the parent class. Here's an in-depth explanation of 'super()' with examples:

# Example 1: Basic Usage

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"I'm {self.age} years old.")

child = Child("Alice", 10)
child.greet()

# In this example, we have a parent class called 'Parent' with an '__init__' method and a 'greet' method. The child class 'Child' inherits from the 'Parent' class using 'class Child(Parent):'. The child class overrides the '__init__' and 'greet' methods, but it still wants to call the parent class's '__init__' method to initialize the 'name' attribute. By using 'super().__init__(name)', the child class invokes the '__init__' method of the parent class and passes the 'name' argument to it.

# Example 2: Multiple Inheritance

class A:
    def __init__(self):
        print("Initializing A")

    def method(self):
        print("Method from A")

class B(A):
    def __init__(self):
        print("Initializing B")
        super().__init__()

    def method(self):
        print("Method from B")
        super().method()

class C(A):
    def __init__(self):
        print("Initializing C")
        super().__init__()

    def method(self):
        print("Method from C")
        super().method()

class D(B, C):
    def __init__(self):
        print("Initializing D")
        super().__init__()

    def method(self):
        print("Method from D")
        super().method()

d = D()
d.method()


# In this example, we have a complex inheritance hierarchy. Class 'A' is the parent class for classes 'B' and 'C', which are then inherited by class 'D'. Each class has its own '__init__' and 'method' methods. By using 'super()', we can ensure that the methods are called in the correct order based on the Method Resolution Order (MRO) of the classes. In this case, the MRO for class 'D' is 'D -> B -> C -> A', so when 'd.method()' is called, it follows the MRO and executes the methods accordingly.

# 'super()' is particularly useful when dealing with multiple inheritance scenarios, allowing you to traverse the inheritance hierarchy and call methods from the parent classes in a consistent and predictable manner.

# It's important to note that 'super()' is not limited to just '__init__' and can be used with any method of the parent class. By using 'super()', you ensure that the method calls are dynamically resolved based on the class hierarchy and can accommodate changes in the inheritance structure without requiring explicit references to the parent class names.