# Decorators

# In Python, decorators are a way to modify or enhance the functionality of functions or classes without directly modifying their source code. Decorators provide a clean and convenient syntax to wrap or modify the behavior of functions or classes dynamically.

# A decorator is implemented as a callable object that takes a function or class as an argument and returns a modified version of that function or class. The modified version typically adds extra functionality or modifies the behavior of the original function or class.

# Here's an example that demonstrates the usage of decorators:


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code to execute before the original function
        print("Before the function is called")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Code to execute after the original function
        print("After the function is called")

        # Return the result of the original function
        return result

    # Return the wrapper function
    return wrapper_function


@decorator_function
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# Output:

# Before the function is called
# Hello, Alice!
# After the function is called


# In this example, we define a decorator function called 'decorator_function', which takes the original function ('greet') as an argument. Inside the decorator function, we define a wrapper function ('wrapper_function'), which wraps the original function.

# The wrapper function is responsible for executing any code before and after the original function is called. In this case, it prints a message before and after calling the original function. It also calls the original function ('original_function(*args, **kwargs)') and returns its result.

# The '@decorator_function' syntax is used to apply the decorator to the 'greet' function. It is equivalent to 'greet = decorator_function(greet)'. This syntax makes it more readable and intuitive to apply decorators to functions.

# Decorators can also accept arguments. 

# Here's an example of a decorator that takes an argument:

def repeat(n):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            for _ in range(n):
                result = original_function(*args, **kwargs)
            return result

        return wrapper_function

    return decorator_function


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Bob")


# Output:

# Hello, Bob!
# Hello, Bob!
# Hello, Bob!


# In this example, we define a decorator function called 'repeat', which takes an argument 'n'. 
# Inside the decorator function, we define the wrapper function ('wrapper_function'), which calls the original function 'n' times.
function
# The '@repeat(3)' syntax is used to apply the 'repeat' decorator with an argument of '3' to the 'greet' function.

# Decorators are powerful tools in Python that allow you to modify the behavior of functions or classes transparently. They can be used for various purposes, such as logging, timing, input validation, authorization, and more. Decorators help keep the code modular, reusable, and easier to maintain.


# In Python, decorators utilize the concept of higher-order functions to modify or enhance the behavior of functions or classes. Decorators are implemented as higher-order functions that take a function or class as an argument and return a modified version of that function or class.

# Here's an example that demonstrates how higher-order functions are used in decorators:


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Code to execute before the original function
        print("Before the function is called")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Code to execute after the original function
        print("After the function is called")

        # Return the result of the original function
        return result

    # Return the wrapper function
    return wrapper_function


@decorator_function
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# Output:

# Before the function is called
# Hello, Alice!
# After the function is called


# In this example, the 'decorator_function' is a higher-order function that takes the original function ('greet') as an argument. Inside the 'decorator_function', a wrapper function ('wrapper_function') is defined.

# The 'wrapper_function' is a closure that wraps the original function. It adds extra functionality by executing code before and after calling the original function. In this case, it prints messages before and after calling the original function. It also calls the original function ('original_function(*args, **kwargs)') and returns its result.

# The decorator is applied to the 'greet' function using the '@decorator_function' syntax, which is equivalent to 'greet = decorator_function(greet)'. This syntax passes the 'greet' function as an argument to the 'decorator_function' and assigns the returned wrapper function as the new implementation of 'greet'.

# By using higher-order functions, decorators provide a convenient and expressive way to modify the behavior of functions without directly modifying their source code. This promotes code reusability and separation of concerns. Decorators can be easily applied to multiple functions, and their functionality can be reused across different parts of the codebase.




# Decorators in Python are useful for a variety of reasons. They allow for code reuse, separation of concerns, and provide a clean and expressive way to add functionality to functions or classes without modifying their original implementation. Let's consider a real-world use case scenario to illustrate the need for decorators.

# Example: Logging Decorator

# Suppose you have multiple functions in your codebase, and you want to add logging functionality to each function to track when they are called and with what arguments. Instead of adding logging code to each function individually, you can use a decorator to achieve this in a more modular and reusable way.

# Here's an example implementation of a logging decorator:


def log_function_call(original_function):
    def wrapper_function(*args, **kwargs):
        # Log function call
        print(f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Log function completion
        print(f"{original_function.__name__} completed")

        # Return the result of the original function
        return result

    return wrapper_function


# In the above code, 'log_function_call' is the decorator function. It takes the original function as an argument and returns a wrapper function. The wrapper function logs the function call, executes the original function, logs the function completion, and returns the result.

# To apply the decorator to a function, you can use the '@' syntax. 

# Here's an example of applying the 'log_function_call' decorator to two functions:


@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b


# Now, when you call the 'add' or 'multiply' functions, the logging functionality will be automatically applied:


add(3, 4)
multiply(2, 5)


# Output:

# Calling add with args: (3, 4), kwargs: {}
# add completed
# Calling multiply with args: (2, 5), kwargs: {}
# multiply completed

# In this example, the logging decorator eliminates the need to add logging code directly into each function. 
# It provides a reusable and centralized way to add the logging functionality to any function you decorate with '@log_function_call'. 
# This promotes code modularity and allows you to easily enable or disable logging for specific functions or groups of functions.

# This demonstrates the need for decorators in Python. 
# They enable you to enhance the behavior of functions or classes in a modular and reusable manner, promoting code organization, readability, and maintainability. 
# Decorators are powerful tools that help separate concerns and allow for the addition of cross-cutting functionality to functions or classes without modifying their core implementation.