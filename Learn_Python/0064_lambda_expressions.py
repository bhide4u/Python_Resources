# lambda expressions

# In Python, a lambda expression is a way to create anonymous functions, which are functions without a specified name. 
# Lambda expressions are defined using the 'lambda' keyword, followed by a list of arguments, a colon (':'), and an expression. 
# They are commonly used when you need a simple, one-line function without defining a separate named function.

# Here's the syntax of a lambda expression:

# lambda arguments: expression


# Here's an example that demonstrates the usage of lambda expressions:


# Example 1: Lambda expression to double a number

double = lambda x: x * 2

result = double(5)

print(result)


# Output:

10


# In the above example, we define a lambda expression that takes an argument 'x' and returns the value of 'x' multiplied by 2. 
# We assign this lambda expression to the variable 'double'. 
# We can then call the 'double' function with an argument of 5, which results in '10'.

# Lambda expressions can also take multiple arguments. Here's an example that adds two numbers using a lambda expression:


# Example 2: Lambda expression to add two numbers

add = lambda x, y: x + y

result = add(3, 4)

print(result)

# Output:

7


# In this case, the lambda expression takes two arguments 'x' and 'y' and returns their sum.
# We assign this lambda expression to the variable 'add'. 
# Calling the 'add' function with arguments 3 and 4 results in a sum of '7'.

# Lambda expressions are often used in conjunction with other built-in functions like 'map()', 'filter()', and 'reduce()'. 
# Here's an example that uses a lambda expression with 'map()' to square a list of numbers:

# Example 3: Using lambda expression with map()

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x: x**2, numbers)

squared_numbers = list(squared_numbers)

print(squared_numbers)


# Output:

[1, 4, 9, 16, 25]


# In this example, we use a lambda expression to define a function that squares a number ('x**2'). 
# We pass this lambda expression as the first argument to 'map()', which applies the function to each element of the 'numbers' list, resulting in a new list of squared numbers.

# Lambda expressions provide a concise and expressive way to define small, anonymous functions. 
# They are particularly useful in situations where you need a simple function for a short and specific task without the need to define a separate named function. 
# However, for more complex or reusable logic, it's generally recommended to define named functions for better code organization and readability.