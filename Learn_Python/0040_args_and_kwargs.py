# args and kwargs
# In Python, `*args` and `**kwargs` are special syntaxes used in function definitions to handle a varying number of arguments.

# `*args` is used to pass a variable number of non-keyword arguments to a function. 
# The `*args` parameter allows you to pass multiple positional arguments, which are then captured as a tuple inside the function. 
# The name `args` is arbitrary and can be replaced with any valid variable name, but the asterisk (`*`) is necessary to indicate that it is a special parameter.

# Here's an example:
def print_arguments(*args):
    for arg in args:
        print(arg)

print_arguments('apple', 'banana', 'cherry')

# In this example, the `print_arguments` function takes any number of positional arguments. 
# The `*args` parameter captures all the passed arguments into a tuple called `args`. 
# Inside the function, we can iterate over `args` and print each argument.

# `**kwargs` is used to pass a variable number of keyword arguments to a function. 
# The `**kwargs` parameter allows you to pass multiple keyword arguments, which are then captured as a dictionary inside the function. 
# Similar to `*args`, the name `kwargs` is arbitrary, but the double asterisks (`**`) are necessary to indicate that it is a special parameter.

# Here's an example:
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='Alice', age=25, city='New York')

# In this example, the `print_info` function takes any number of keyword arguments. 
# The `**kwargs` parameter captures all the passed keyword arguments into a dictionary called `kwargs`. 
# Inside the function, we can iterate over `kwargs` using the `items()` method and print each key-value pair.

# You can use both `*args` and `**kwargs` together in a function definition if you want to accept both positional and keyword arguments.

# Here's an example that combines `*args` and `**kwargs`:
def print_data(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_data('apple', 'banana', name='Alice', age=25)

# In this example, the `print_data` function accepts both positional arguments (`'apple'`, `'banana'`) and keyword arguments (`name='Alice'`, `age=25`). 
# The `*args` parameter captures the positional arguments as a tuple, while the `**kwargs` parameter captures the keyword arguments as a dictionary.

# Using `*args` and `**kwargs` allows you to create more flexible and versatile functions that can handle different argument types and a varying number of arguments.