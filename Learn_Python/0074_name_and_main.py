# __name__ and __main__

# In Python, '__name__' and '__main__' are special variables that provide information about the execution context of a script. They are commonly used to determine whether a module is being run as the main program or being imported as a module. Here's an explanation of '__name__' and '__main__' with examples:

# '__name__':
# '__name__' is a built-in variable that holds the name of the current module. When a module is imported, '__name__' is set to the module's name. When a module is executed as the main program, '__name__' is set to '"__main__"'. This allows us to differentiate between the main program and imported modules.

# Example:
# Consider a module named "my_module.py" with the following code:


def greet():
    print("Hello, World!")

print("Module name:", __name__)


# When we run this module directly as the main program, the output will be:

Module name: __main__


# However, if we import this module into another Python script, the output will be:

Module name: my_module


# '__main__':
# '__main__' is the name of the scope in which the top-level code executes. It is the name of the script or module that is being run as the main program. When a module is executed as the main program, the code inside the 'if __name__ == "__main__":' block is executed.

# Example:
# Consider a script named "main_script.py" that imports the "my_module" module:


import my_module

print("Executing main_script.py")

my_module.greet()


# The "my_module" module can have a section of code executed only when it's run as the main program by using the 'if __name__ == "__main__":' block:

def greet():
    print("Hello, World!")

print("Module name:", __name__)

if __name__ == "__main__":
    print("Executing as main program")


# When we run "main_script.py", the output will be:

# Module name: my_module
# Executing main_script.py
# Hello, World!


# In this example, the code inside the 'if __name__ == "__main__":' block in "my_module" is executed when it's run as the main program, but not when it's imported as a module. This allows us to have code that runs only when the module is run directly and not when it's imported.

# Using '__name__' and '__main__' is a common practice in Python to separate the code that should run only when the module is run as the main program from the code that should be available for import in other modules. It provides a way to control the behavior of a module based on how it is being executed.