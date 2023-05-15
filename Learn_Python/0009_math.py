# Math
# The Python math library is a built-in module in Python that provides a wide range of mathematical functions

import math
# Most used Math methods - 

# 1. abs(x): Returns the absolute value of a number x.
print("Absolute of number -3.2 is: ", abs(-3.2))

# round(x, n): Rounds a number x to n decimal places. If n is not provided, it rounds to the nearest integer.
print("Round of number 4.5698712 is: ", round(4.5698712 , 2))

# pow(x, y): Raises x to the power of y.
print("Power of 2 raised to 3: ", pow(2, 3))

# sqrt(x): Returns the square root of x.
print("Square root of 64 is: ", math.sqrt(64))

# floor(x): Returns the largest integer less than or equal to x.
print("Floor of 4.8 is: ", math.floor(4.8))

# ceil(x): Returns the smallest integer greater than or equal to x.
print("Ceil of 5.3 is: ", math.ceil(5.3))

# max(x1, x2, ..., xn): Returns the largest value among the given arguments.
print("Max of given numbers is: ", max(1, 5, 13, 24, 76, 2, 4, 6, 98))

# min(x1, x2, ..., xn): Returns the smallest value among the given arguments.
print("Min of given numbers is: ", min(1, 5, 13, 24, 76, 2, 4, 6, 98))

# sum(iterable): Returns the sum of all elements in an iterable (e.g., list, tuple).
print("Sum of given numbers is: ", sum([1, 5, 13, 24, 76, 2, 4, 6, 98]))

# log(x, base): Returns the logarithm of x with the specified base. If base is not provided, it defaults to the natural logarithm (base e).
print("Log of 10 to the base e is: ", round(math.log(10),2))

