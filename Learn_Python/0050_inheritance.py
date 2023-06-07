# Inheritance

# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows classes to inherit attributes and methods from other classes. In Python, inheritance is implemented using the syntax 'class ChildClass(ParentClass):'. The child class (also known as derived class or subclass) inherits the properties and behaviors of the parent class (also known as base class or superclass). Here's an explanation of inheritance in Python with examples:

# Example 1: Basic Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Dog barks")

animal = Animal("Generic Animal")
animal.speak()  # Output: Animal speaks

dog = Dog("Buddy", "Labrador")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Labrador
dog.speak()  # Output: Dog barks


# In this example, we have a parent class called 'Animal' with an '__init__' method and a 'speak' method. The child class 'Dog' inherits from the 'Animal' class using the syntax 'class Dog(Animal):'. It has its own '__init__' method and overrides the 'speak' method. We create instances of both classes and observe how the child class inherits the attributes and methods of the parent class. The 'super().__init__(name)' line in the child class calls the parent class's '__init__' method to initialize the 'name' attribute.

# Example 2: Multilevel Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Dog barks")

class GoldenRetriever(Dog):
    def __init__(self, name):
        super().__init__(name, "Golden Retriever")

    def speak(self):
        print("Golden Retriever barks")

animal = Animal("Generic Animal")
animal.speak()  # Output: Animal speaks

dog = Dog("Buddy", "Labrador")
dog.speak()  # Output: Dog barks

golden = GoldenRetriever("Charlie")
print(golden.name)  # Output: Charlie
print(golden.breed)  # Output: Golden Retriever
golden.speak()  # Output: Golden Retriever barks


# In this example, we introduce another level of inheritance. The 'GoldenRetriever' class inherits from the 'Dog' class, which, in turn, inherits from the 'Animal' class. The 'GoldenRetriever' class adds no new attributes but overrides the 'speak' method. When we create an instance of 'GoldenRetriever', it has access to the attributes and methods of both the parent and grandparent classes.

# Inheritance allows for code reuse, promotes modularity, and supports the concept of hierarchical relationships between classes. Child classes can extend the functionality of the parent class by adding new attributes and methods or overriding existing ones. This way, inheritance helps in organizing and structuring code in an efficient and logical manner.