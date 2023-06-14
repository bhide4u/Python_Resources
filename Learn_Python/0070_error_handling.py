# Error handling

# Error handling in Python involves handling and managing exceptions that may occur during the execution of a program. Exceptions are raised when errors or exceptional conditions occur, such as division by zero, file not found, or invalid input. Proper error handling allows you to gracefully handle these exceptions and prevent your program from crashing.

# Here's an example that demonstrates error handling in Python:


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", str(e))


# In this example, we use a 'try-except' block to handle potential exceptions. The code within the 'try' block is the normal execution flow. If an exception occurs within the 'try' block, the corresponding 'except' block is executed.

# - The 'ValueError' exception is raised if the user enters an invalid input, such as a non-integer value. The 'except ValueError' block handles this exception and displays an error message.
# - The 'ZeroDivisionError' exception is raised if the user enters '0' as the second number, resulting in division by zero. The 'except ZeroDivisionError' block handles this exception and displays an error message.
# - The 'except Exception as e' block is a catch-all block that handles any other exceptions that may occur. It prints a generic error message along with the specific exception details obtained from the 'Exception' object.

# By properly handling exceptions, you can gracefully handle errors and guide the program's execution flow even in the presence of unexpected events.

# Additionally, you can use the 'else' and 'finally' clauses with the 'try-except' block:

# - The 'else' block is executed if no exceptions occur within the 'try' block. It is useful for executing code that should run only when the 'try' block succeeds without exceptions.
# - The 'finally' block is always executed, regardless of whether an exception occurred or not. It is useful for performing cleanup operations or releasing resources, such as closing files or database connections.

# Here's an example that demonstrates the usage of 'else' and 'finally' clauses:


try:
    file = open("data.txt", "r")
    data = file.read()
    print("File contents:", data)
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File reading successful.")
finally:
    if file:
        file.close()
        print("File closed.")


# In this example, the 'try' block attempts to open and read a file. If the file is found and read successfully, the 'else' block is executed, indicating that the file reading was successful. The 'finally' block is always executed, ensuring that the file is closed, even if an exception occurred or not.

# Proper error handling in Python helps make your code more robust and user-friendly by gracefully handling unexpected situations. It allows you to handle specific exceptions, provide meaningful error messages, and perform necessary cleanup tasks.


# Exception handling in Python involves managing and handling exceptional situations or errors that may occur during the execution of a program. Python provides a mechanism to catch and handle exceptions using the 'try-except' block. 

# Here's an example that demonstrates exception handling in Python:


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", str(e))


# In this example, we use a 'try-except' block to handle potential exceptions. The code within the 'try' block is the normal execution flow. If an exception occurs within the 'try' block, the corresponding 'except' block is executed.

# - The 'ValueError' exception is raised if the user enters an invalid input, such as a non-integer value. The 'except ValueError' block handles this exception and displays an error message.
# - The 'ZeroDivisionError' exception is raised if the user enters '0' as the second number, resulting in division by zero. The 'except ZeroDivisionError' block handles this exception and displays an error message.
# - The 'except Exception as e' block is a catch-all block that handles any other exceptions that may occur. It prints a generic error message along with the specific exception details obtained from the 'Exception' object.

# By using exception handling, you can anticipate and handle specific types of exceptions, allowing your program to gracefully handle errors and prevent it from crashing.

# You can also include an 'else' clause to the 'try-except' block:


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("The square of the number is:", num ** 2)


# In this example, if the user enters a valid number, the 'else' block is executed, and the square of the number is printed. If an invalid input is provided, the 'except ValueError' block handles the exception and displays an error message.

# Exception handling allows you to deal with exceptional situations and gracefully recover from errors. It helps in maintaining program flow, providing appropriate error messages, and handling different types of exceptions selectively. Exception handling is an essential aspect of writing robust and reliable code in Python.


# In Python, you can create a custom exception handling class by subclassing the built-in 'Exception' class or any of its subclasses. This allows you to define your own exception hierarchy and handle specific types of exceptions in a customized way. 

 
# Here's an example of creating a custom exception class and demonstrating its usage:

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomException: {self.message}"

# Usage of the custom exception class
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise CustomException("Number must be positive.")
except CustomException as ce:
    print(ce)


# In this example, we define a custom exception class called 'CustomException' by subclassing the built-in 'Exception' class. The 'CustomException' class overrides the '__init__()' method to accept a custom error message, and the '__str__()' method to specify the string representation of the exception.

# Inside the 'try' block, we take input from the user and check if the number is less than zero. If it is, we raise an instance of 'CustomException' with a specific error message. The 'except CustomException as ce' block catches the raised exception and prints the custom error message using the '__str__()' method of the 'CustomException' class.

# You can define additional methods and properties in your custom exception class based on your specific needs. By creating custom exception classes, you can provide more specific and meaningful error messages, handle different types of exceptions separately, and organize your code in a more structured manner.

# Note: It is generally recommended to follow the naming convention of suffixing custom exception class names with "Error" to make them easily recognizable as exceptions. For example, 'CustomException' could be renamed to 'CustomError'.