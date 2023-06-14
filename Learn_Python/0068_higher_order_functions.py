# Higher Order Functions

# In Python, higher-order functions are functions that can accept other functions as arguments or return functions as results. This concept is based on the idea of treating functions as first-class objects, allowing them to be manipulated and passed around like any other data type.

# Here are a few examples that demonstrate the usage of higher-order functions in Python:

# 1. map(): The 'map()' function applies a given function to each item of an iterable and returns an iterator of the results.


def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

print(list(squared_numbers))


# Output:

[1, 4, 9, 16, 25]

# In this example, the 'map()' function takes the 'square()' function as the first argument and the 'numbers' list as the second argument. It applies the 'square()' function to each element of the 'numbers' list, resulting in a new iterator that yields the squared numbers.

# 2. filter(): The 'filter()' function creates an iterator from elements of an iterable for which a given function returns 'True'.

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]

even_numbers = filter(is_even, numbers)

print(list(even_numbers))

# Output:

[2, 4]

# In this example, the 'filter()' function takes the 'is_even()' function as the first argument and the 'numbers' list as the second argument. It filters out the elements of the 'numbers' list for which the 'is_even()' function returns 'True', resulting in a new iterator that yields the even numbers.

# 3. reduce(): The 'reduce()' function, which was part of the 'functools' module in Python 3, applies a given function to the elements of an iterable in a cumulative way, reducing them to a single value.

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

product = reduce(multiply, numbers)

print(product)

# Output:
    
120

# In this example, the 'reduce()' function takes the 'multiply()' function as the first argument and the 'numbers' list as the second argument. 
# It applies the 'multiply()' function to the first two elements of the 'numbers' list, then applies it again to the result and the next element, and so on until a single value is obtained, which is the product of all the numbers.

# Higher-order functions allow for modular and reusable code. 
# They provide a way to separate the logic or behavior of a program into smaller, self-contained functions. 
# By accepting or returning functions, higher-order functions enable greater flexibility and abstraction in programming.