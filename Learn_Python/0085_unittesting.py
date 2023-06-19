# Unittesting

# In Python, the 'unittest' module provides a framework for writing and running tests. It allows you to create test cases, organize them into test suites, and execute them to verify the correctness of your code. The 'unittest' module follows the principles of unit testing, where individual units of code are tested in isolation.

# Here's an example that demonstrates the usage of 'unittest' in Python:


import unittest

# The class containing the test cases
class MyTestCase(unittest.TestCase):

    # Setup method (optional) - executed before each test case
    def setUp(self):
        # Initialize any necessary resources or variables
        pass

    # Teardown method (optional) - executed after each test case
    def tearDown(self):
        # Clean up any resources or variables
        pass

    # Test case 1
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)  # Assertion to check the result

    # Test case 2
    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)  # Assertion to check the result

# Executing the tests
if __name__ == '__main__':
    unittest.main()


# In this example, we create a test case class 'MyTestCase' that inherits from 'unittest.TestCase'. Inside this class, we define individual test cases as methods, starting with the prefix 'test_'. Each test case method represents a specific unit of code to be tested.

# Within each test case method, we perform the necessary operations and use assertions provided by the 'unittest.TestCase' class to verify the expected behavior of the code under test. In the example, we use the 'assertEqual' assertion to check if the actual result matches the expected result.

# The 'setUp' and 'tearDown' methods, though optional, can be used for any necessary setup and cleanup operations before and after each test case. For example, initializing resources, connecting to a database, or resetting variables.

# Finally, we execute the tests by calling 'unittest.main()' inside an 'if __name__ == '__main__':' block. This allows us to run the tests when the script is executed directly, but not when imported as a module.

# To run the tests, save the script in a file (e.g., 'test_example.py') and execute it from the command line:


python test_example.py


# The 'unittest' module will discover and execute the test cases defined in the file, providing feedback on the success or failure of each test.

# The 'unittest' module offers many more assertion methods, such as 'assertTrue', 'assertFalse', 'assertRaises', and more, which you can use based on your testing needs. It also provides additional features for organizing tests into test suites and handling more complex scenarios.

# Unit testing with 'unittest' allows you to ensure the correctness of your code, detect regressions, and facilitate future code maintenance.


# Examples ----

# Here's an example of creating three functions in 'main.py' and 'main2.py', along with two corresponding test files 'test1.py' and 'test2.py' containing test cases for each function.

'main.py'

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero!")


'main2.py'

def is_even(number):
    return number % 2 == 0

def is_palindrome(word):
    return word == word[::-1]

def greet(name):
    return f"Hello, {name}!"


'test1.py'

import unittest
from main import add_numbers, multiply_numbers

class TestAddition(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-5, 8)
        self.assertEqual(result, 3)

class TestMultiplication(unittest.TestCase):

    def test_multiply_numbers(self):
        result = multiply_numbers(2, 3)
        self.assertEqual(result, 6)

    def test_multiply_numbers_zero(self):
        result = multiply_numbers(5, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()


'test2.py'

import unittest
from main2 import is_even, is_palindrome, greet

class TestEven(unittest.TestCase):

    def test_is_even(self):
        result = is_even(4)
        self.assertTrue(result)

    def test_is_even_negative(self):
        result = is_even(5)
        self.assertFalse(result)

class TestPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        result = is_palindrome("radar")
        self.assertTrue(result)

    def test_is_palindrome_false(self):
        result = is_palindrome("hello")
        self.assertFalse(result)

class TestGreeting(unittest.TestCase):

    def test_greet(self):
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")

    def test_greet_empty(self):
        result = greet("")
        self.assertEqual(result, "Hello, !")

if __name__ == '__main__':
    unittest.main()


# In this example, 'main.py' contains three functions: 'add_numbers', 'multiply_numbers', and 'divide_numbers', while 'main2.py' contains three functions: 'is_even', 'is_palindrome', and 'greet'. The test cases for each function are written in 'test1.py' and 'test2.py' files.

# To run the tests, execute the following commands in the terminal:

python test1.py
python test2.py

# These commands will execute the tests in 'test1.py' and 'test2.py' files respectively, providing feedback on the success or failure of each test case.

# To run all the test files ('test1.py' and 'test2.py') at once, you can organize your folder structure as follows:

'''
project/
├── main.py
├── main2.py
├── tests/
│   ├── test1.py
│   └── test2.py
'''

# In this structure, the 'main.py' and 'main2.py' files are placed in the root folder, while the test files ('test1.py' and 'test2.py') are stored inside a separate folder called 'tests'.

# To run all the test files together, you can use a test runner tool, such as 'pytest', which can discover and execute all the test files in a specified directory.

# Here are the steps to run the tests using 'pytest':

# 1. Install 'pytest' by running the following command in your terminal:
   
   pip install pytest
   

# 2. Ensure that you have the following folder structure:
   
   '''
   project/
   ├── main.py
   ├── main2.py
   └── tests/
       ├── test1.py
       └── test2.py
   '''

# 3. Open the terminal and navigate to the root folder of your project ('project' in this case).

# 4. Run the command 'pytest' followed by the name of the folder containing the test files ('tests'):
   
   pytest tests
   

#    'pytest' will automatically discover all the test files ('test1.py' and 'test2.py') within the 'tests' folder and execute them.

# By following this folder structure and using 'pytest', you can run all the test files in one go and receive consolidated test results. Additionally, 'pytest' offers various advanced features and plugins for testing, making it a popular choice for testing in Python projects.