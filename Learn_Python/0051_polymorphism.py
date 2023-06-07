# Polymorphism

# Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables different classes to have a common interface, while each class can provide its own implementation. In Python, polymorphism is achieved through method overriding and duck typing. Here's an explanation of polymorphism in Python with examples:

# Example 1: Method Overriding

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal):
    animal.speak()

animal = Animal()
dog = Dog()
cat = Cat()

make_animal_speak(animal)  # Output: Animal speaks
make_animal_speak(dog)  # Output: Dog barks
make_animal_speak(cat)  # Output: Cat meows


# In this example, we have a parent class 'Animal' with a 'speak' method. The child classes 'Dog' and 'Cat' inherit from the 'Animal' class and override the 'speak' method with their own implementations. The 'make_animal_speak' function takes an 'animal' parameter of type 'Animal' and calls the 'speak' method on it. When we pass instances of 'Animal', 'Dog', and 'Cat' classes to 'make_animal_speak', the appropriate 'speak' method based on the actual object's type is executed.

# Example 2: Duck Typing

class Car:
    def drive(self):
        print("Car drives on roads")

class Boat:
    def drive(self):
        print("Boat sails on water")

class Plane:
    def fly(self):
        print("Plane flies in the sky")

def make_vehicle_drive(vehicle):
    vehicle.drive()

car = Car()
boat = Boat()
plane = Plane()

make_vehicle_drive(car)  # Output: Car drives on roads
make_vehicle_drive(boat)  # Output: Boat sails on water


# In this example, we have different classes 'Car', 'Boat', and 'Plane', each with their own 'drive' or 'fly' method. The 'make_vehicle_drive' function takes a 'vehicle' parameter, which can be any object that has a 'drive' method. The function doesn't rely on the specific type of the object but rather on the presence of the required method. This is known as duck typing, where the object's suitability is determined by the presence of the required methods rather than its actual class or inheritance hierarchy.

# Polymorphism allows for code flexibility and extensibility. By treating objects of different classes as instances of a common superclass or by relying on the presence of specific methods, we can write more generic and reusable code. This flexibility becomes especially useful when dealing with collections of objects or when designing frameworks and APIs that can accommodate various implementations.