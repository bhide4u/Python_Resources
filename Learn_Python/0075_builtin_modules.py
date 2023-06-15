# Builtin Modules

# Python has a rich collection of built-in modules that provide a wide range of functionalities. Here are some of the most important and commonly used built-in modules in Python, along with examples of their usage:

# 1. 'math': Provides mathematical functions and constants.

   import math

   print(math.sqrt(16))      # Square root
   print(math.pi)            # Value of pi
   print(math.sin(math.pi))  # Sine of pi
   

# 2. 'random': Generates random numbers and selections.
   
   import random

   print(random.random())       # Random float between 0 and 1
   print(random.randint(1, 10))  # Random integer between 1 and 10
   print(random.choice(['a', 'b', 'c']))  # Randomly choose an element
   

# 3. 'datetime': Manipulates dates and times.
   
   import datetime

   now = datetime.datetime.now()
   print(now)
   print(now.year, now.month, now.day)  # Access individual components
   

# 4. 'os': Provides functions for interacting with the operating system.
   
   import os

   print(os.getcwd())            # Get current working directory
   print(os.listdir('/path'))    # List files and directories in a path
   os.makedirs('/path/new_dir')  # Create a new directory


# 5. 'sys': Provides system-specific parameters and functions.
   
   import sys

   print(sys.argv)           # Command-line arguments
   print(sys.platform)       # Platform identifier
   sys.exit(0)               # Exit the program
   

# 6. 'json': Encodes and decodes JSON data.
   
   import json

   data = {'name': 'John', 'age': 30}
   json_str = json.dumps(data)  # Convert to JSON string
   decoded_data = json.loads(json_str)  # Convert back to Python object
   

# 7. 're': Performs regular expression operations.
   
   import re

   pattern = r'\b[A-Za-z]+\b'  # Match words
   text = 'Hello, world!'
   matches = re.findall(pattern, text)
   print(matches)
   

# 8. 'csv': Reads and writes CSV files.
   
   import csv

   with open('data.csv', 'r') as file:
       reader = csv.reader(file)
       for row in reader:
           print(row)
   

# These are just a few examples of the many built-in modules available in Python. Depending on your specific needs, you may explore other modules such as 'time', 'collections', 'itertools', 'os.path', 'sysconfig', and many more. The Python standard library offers an extensive range of modules to simplify and enhance your programming tasks.