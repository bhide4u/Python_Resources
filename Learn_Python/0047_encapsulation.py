# Encapsulation

# Encapsulation is a fundamental concept in object-oriented programming (OOP) that allows you to bundle data and the methods that operate on that data into a single unit called a class. It provides a way to control access to the data and protects it from being modified or accessed directly from outside the class. In Python, encapsulation is achieved using access modifiers and property decorators. Here's an example to illustrate encapsulation step by step:

class Car:
    def __init__(self, make, model, year):
        self._make = make  # Using a single underscore to indicate a protected attribute
        self._model = model
        self._year = year
        self._odometer = 0

    def drive(self, distance):
        self._odometer += distance

    def get_odometer(self):
        return self._odometer

    def set_make(self, make):
        self._make = make

    def get_make(self):
        return self._make

# 1. In the code above, we define a 'Car' class with private attributes: '_make', '_model', '_year', and a protected attribute: '_odometer'. By convention, a single underscore prefix indicates that an attribute is intended to be protected, although it can still be accessed from outside the class.

# 2. The constructor method '__init__()' initializes the car's make, model, year, and sets the odometer to zero.

# 3. The 'drive()' method takes a distance parameter and increments the odometer by that distance.

# 4. The 'get_odometer()' method allows external code to retrieve the value of the odometer attribute.

# 5. The 'set_make()' and 'get_make()' methods provide controlled access to the make attribute. They allow setting a new make and retrieving the current make value, respectively.

# By using encapsulation, we hide the implementation details of the 'Car' class and expose only the necessary methods and attributes. Now, let's see how we can use the 'Car' class:


my_car = Car("Toyota", "Corolla", 2022)
my_car.drive(100)
print(my_car.get_odometer())  # Output: 100

my_car.set_make("Honda")
print(my_car.get_make())  # Output: Honda


# 1. We create an instance of the 'Car' class called 'my_car', passing in the make ("Toyota"), model ("Corolla"), and year (2022) as arguments to the constructor.

# 2. We call the 'drive()' method on 'my_car' and pass 100 as the distance. This increments the odometer attribute by 100.

# 3. We use the 'get_odometer()' method to retrieve the current value of the odometer and print it, which outputs 100.

# 4. We set the make of the car to "Honda" using the 'set_make()' method.

# 5. Finally, we call the 'get_make()' method to retrieve the updated make value and print it, which outputs "Honda".

# By encapsulating the data and providing controlled access through methods, we ensure that the internal state of the 'Car' class is protected and can be modified or accessed only through the defined methods.