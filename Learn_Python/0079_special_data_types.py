# Special Data Types

# Three special data types in Python: 'Counter', 'defaultdict', and 'OrderedDict'.

# 1. Counter:
# The 'Counter' class is a specialized data type available in the 'collections' module. It is used for counting hashable objects and storing them as dictionary keys, with the counts stored as dictionary values. Here's an example:


from collections import Counter

numbers = [1, 2, 3, 4, 2, 3, 1, 2, 4, 4, 4]
number_counts = Counter(numbers)
print(number_counts)

# Output:

Counter({4: 5, 2: 3, 1: 2, 3: 2})

# In this example, the 'Counter' object 'number_counts' stores the count of each number in the 'numbers' list. It shows that the number '4' appears 5 times, '2' appears 3 times, '1' appears 2 times, and '3' appears 2 times.

# The 'Counter' class provides various useful methods, such as 'most_common()' to retrieve the most common elements, and arithmetic operations like addition, subtraction, intersection, and union of counters.

# 2. defaultdict:
# The 'defaultdict' class is another data type available in the 'collections' module. It is a subclass of the built-in 'dict' class and provides a default value for missing keys. Here's an example:


from collections import defaultdict

student_grades = defaultdict(int)
student_grades['Alice'] = 95
student_grades['Bob'] = 80
print(student_grades['Alice'])  # Output: 95
print(student_grades['Charlie'])  # Output: 0 (default value)


# In this example, the 'defaultdict' object 'student_grades' is initialized with the default value of 'int', which is '0'. When accessing a key that doesn't exist, like ''Charlie'', it returns the default value rather than raising a 'KeyError'.

# The 'defaultdict' class accepts a callable as an argument, which is used to provide the default value for missing keys. Common callable types include 'int', 'list', 'set', and 'lambda' functions.

# 3. OrderedDict:
# The 'OrderedDict' class is a dictionary subclass available in the 'collections' module. It maintains the order of dictionary elements based on the order of insertion. Here's an example:


from collections import OrderedDict

fruits = OrderedDict()
fruits['apple'] = 5
fruits['banana'] = 2
fruits['orange'] = 8
print(fruits)

# Output:

OrderedDict([('apple', 5), ('banana', 2), ('orange', 8)])

# In this example, the 'OrderedDict' 'fruits' preserves the order in which the fruits were added to the dictionary. When printing the 'OrderedDict', the elements are displayed in the order they were inserted.

# 'OrderedDict' is useful in scenarios where the order of insertion is important, such as preserving the order of configuration settings, maintaining a history of operations, or implementing LRU (Least Recently Used) cache.

# These specialized data types provide additional functionality and features beyond the standard dictionary in Python, allowing you to solve specific problems more effectively.

# Dictionaries are now ordered -
# read more at - https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/

# Three commonly used modules in Python: 'datetime', 'time', and 'array', along with examples.

# 1. datetime:
# The 'datetime' module provides classes for working with dates and times in Python. It allows you to perform various operations like creating, manipulating, and formatting dates and times. Here's an example:


from datetime import datetime, timedelta

# Current date and time
current_datetime = datetime.now()
print("Current DateTime:", current_datetime)

# Formatting DateTime
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted DateTime:", formatted_datetime)

# Creating a DateTime object
custom_datetime = datetime(2022, 6, 15, 10, 30, 0)
print("Custom DateTime:", custom_datetime)

# Manipulating DateTime
modified_datetime = custom_datetime + timedelta(days=5, hours=2)
print("Modified DateTime:", modified_datetime)


# In this example, we import the 'datetime' module and use its classes and methods. We obtain the current date and time using 'datetime.now()', format the DateTime object using 'strftime()', create a custom DateTime object using the 'datetime()' constructor, and manipulate the DateTime object using 'timedelta()'.

# 2. time:
# The 'time' module provides various functions for working with time-related operations in Python. It includes functions for measuring time intervals, converting between time formats, and more. Here's an example:


import time

# Current time in seconds since the epoch
current_time = time.time()
print("Current Time:", current_time)

# Sleep for 2 seconds
time.sleep(2)
print("Slept for 2 seconds")

# Formatting time
formatted_time = time.strftime("%H:%M:%S", time.localtime())
print("Formatted Time:", formatted_time)


# In this example, we import the 'time' module and utilize its functions. We retrieve the current time in seconds since the epoch using 'time.time()', pause the program execution for 2 seconds using 'time.sleep()', and format the time using 'time.strftime()'.

# 3. array:
# The 'array' module provides an array data structure that is more efficient than traditional lists when working with large sequences of homogeneous data. It offers functionality for creating, manipulating, and accessing array elements. Here's an example:


from array import array

# Creating an array of integers
integer_array = array('i', [1, 2, 3, 4, 5])
print("Integer Array:", integer_array)

# Accessing array elements
print("Element at index 2:", integer_array[2])

# Appending elements to the array
integer_array.append(6)
print("Updated Integer Array:", integer_array)

# Converting array to a list
array_list = list(integer_array)
print("Array converted to list:", array_list)


# In this example, we import the 'array' module and use it to create an array of integers using the 'array()' function. We access individual elements using index notation, append elements using the 'append()' method, and convert the array to a list using the 'list()' function.

# The 'array' module supports different data types, such as integers (''i''), floats (''f''), and characters (''c''), allowing you to work with different types of arrays efficiently.

# These modules ('datetime', 'time', and 'array') provide valuable functionality for working with dates, times, and efficient array data structures in Python, respectively.

# In Python, lists and arrays are both used to store collections of items, but they have some differences in terms of functionality and underlying implementation. Let's discuss the differences between lists and arrays with an example:

# 1. Mutability:
#    - Lists: Lists are mutable, meaning you can modify, add, or remove elements after the list is created. You can change the size of a list dynamically.
#    - Arrays: Arrays are also mutable, allowing you to modify elements. However, the size of an array is fixed when it is created, and you cannot change it dynamically. You would need to create a new array if you want to change the size.

# Example:

# Lists are mutable
my_list = [1, 2, 3]
my_list[0] = 4
print(my_list)  # Output: [4, 2, 3]

# Arrays are also mutable
from array import array
my_array = array('i', [1, 2, 3])
my_array[0] = 4
print(my_array)  # Output: array('i', [4, 2, 3])


# 2. Data Type:
#    - Lists: Lists in Python can contain elements of different data types. You can have a mix of integers, floats, strings, or even other lists within a single list.
#    - Arrays: Arrays in Python are designed to store elements of the same data type. When creating an array, you need to specify the data type of its elements. This leads to more efficient memory storage and faster access.

# Example:

# Lists can contain elements of different data types
mixed_list = [1, 2.5, "hello"]
print(mixed_list)  # Output: [1, 2.5, 'hello']

# Arrays store elements of the same data type
from array import array
float_array = array('f', [1.0, 2.5, 3.7])
print(float_array)  # Output: array('f', [1.0, 2.5, 3.7])


# 3. Functionality:
#    - Lists: Lists have built-in methods like `append()`, `pop()`, `extend()`, and `sort()` that provide flexibility and convenience for manipulating and operating on list elements.
#    - Arrays: Arrays have a more limited set of operations compared to lists. They provide basic functionality such as indexing, appending, and removing elements. However, they lack some of the advanced methods available for lists.

# Example:

# Lists have built-in methods for manipulation
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Arrays have limited operations
from array import array
my_array = array('i', [1, 2, 3])
my_array.append(4)  # No append() method for arrays
print(my_array)  # Output: array('i', [1, 2, 3, 4])


# In general, lists are more flexible and versatile due to their mutability and ability to store elements of different data types. Arrays, on the other hand, are more efficient in terms of memory usage and offer faster access to elements when they contain homogeneous data. Thus, the choice between lists and arrays depends on the specific requirements of your program.