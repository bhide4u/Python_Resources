# Methods Resolution Order

# Method Resolution Order (MRO) is the order in which Python searches for methods and attributes in a class hierarchy. It determines the order in which methods are resolved and called when they are invoked on an object. Understanding the MRO is important when dealing with inheritance and multiple inheritance scenarios. Here's an explanation of Method Resolution Order with an example:

# Consider the following class hierarchy:


class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):
    pass


# In this example, we have four classes: 'A', 'B', 'C', and 'D'. Class 'D' inherits from classes 'B' and 'C', and both 'B' and 'C' inherit from 'A'. Let's examine the Method Resolution Order for the class 'D' using the 'mro()' method:


print(D.mro())


# The output will be:

'''
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
'''

# The MRO list shows the order in which Python will search for methods and attributes in the class hierarchy when they are invoked on an object of class 'D'. In this case, the MRO for class 'D' is '[D, B, C, A, object]'.

# When a method is called on an instance of 'D', Python will search for the method in the following order:

# 1. First, it looks for the method in the class 'D' itself.
# 2. If the method is not found in 'D', it looks for the method in the next class in the MRO, which is 'B'.
# 3. If the method is not found in 'B', it continues searching in the next class in the MRO, which is 'C'.
# 4. If the method is not found in 'C', it searches in the next class in the MRO, which is 'A'.
# 5. Finally, if the method is not found in 'A', it searches in the last class in the MRO, which is 'object' (the base class for all classes in Python).

# The search stops as soon as the method is found, and the corresponding implementation is executed. This order ensures that the methods are resolved correctly according to the inheritance hierarchy.

# In our example, if we create an instance of 'D' and call the 'method()' on it:


d = D()
d.method()


# The output will be:

'''
Method from B
'''

# Even though both 'B' and 'C' have a method called 'method()', the MRO ensures that the method from 'B' is called first because 'B' appears before 'C' in the MRO list.

# Understanding the Method Resolution Order is crucial when working with complex inheritance hierarchies, as it determines the order in which methods are resolved and executed. By following the MRO, you can ensure that the correct method is called based on the inheritance hierarchy and the order of classes.