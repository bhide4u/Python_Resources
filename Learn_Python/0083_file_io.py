# File I/O

# File I/O (Input/Output) in Python refers to the process of reading from and writing to files. It allows you to work with external files, such as text files, CSV files, binary files, and more. In Python, file I/O is handled through built-in functions and methods provided by the 'open()' function and the file object. Let's explore file I/O in Python in-depth with examples.

# **Opening a File:**
# To open a file, you need to use the 'open()' function. The general syntax for opening a file is as follows:


file_object = open(file_path, mode)


# - 'file_path': The path to the file you want to open. It can be a relative or absolute path.
# - 'mode': The mode in which the file should be opened. It can be "r" for reading, "w" for writing, "a" for appending, or "x" for creating a new file. Additional modes include "t" for text mode (default) and "b" for binary mode.

# **Example:**
# Let's say we have a file called "example.txt" located in the current working directory. We want to open it in read mode.


file_path = "example.txt"
file_object = open(file_path, "r")


# **Reading from a File:**
# Once a file is open in read mode, you can read its contents using various methods.

# - 'read(size)': Reads and returns a specified number of characters from the file. If no size is given, it reads the entire file.


# Reading the entire file
content = file_object.read()
print(content)

# Reading the first 10 characters
content = file_object.read(10)
print(content)


# - 'readline()': Reads and returns a single line from the file.


# Reading the first line
line = file_object.readline()
print(line)


# - 'readlines()': Reads and returns all the lines of the file as a list.


# Reading all lines
lines = file_object.readlines()
print(lines)


# **Closing a File:**
# After you have finished working with a file, it is essential to close it using the 'close()' method. This releases the system resources associated with the file.


file_object.close()


# It's considered good practice to close a file when you're done working with it.

# **Writing to a File:**
# To write data to a file, you need to open it in write mode ("w") or append mode ("a").

# - 'write(data)': Writes the specified data to the file.


file_path = "example.txt"
file_object = open(file_path, "w")

file_object.write("Hello, World!")
file_object.close()


# This code snippet will open the file in write mode and write the text "Hello, World!" to it. If the file already exists, its previous contents will be overwritten.

# **Appending to a File:**
# If you want to add content to an existing file without overwriting its contents, you can open the file in append mode ("a").


file_path = "example.txt"
file_object = open(file_path, "a")

file_object.write("\nThis is a new line.")
file_object.close()


# Here, we are opening the file in append mode and adding a new line to it.

# **Working with Files Using 'with' Statement:**
# Python provides a convenient way to work with files using the 'with' statement. It automatically takes care of opening and closing the file for you.


file_path = "example.txt"

# Reading from a file using 'with'

# statement
with open(file_path, "r") as file_object:
    content = file_object.read()
    print(content)

# Writing to a file using 'with' statement
with open(file_path, "w") as file_object:
    file_object.write("New content")


# When the code execution leaves the 'with' block, the file is automatically closed, ensuring that resources are properly released.

# Remember to handle exceptions and errors that may occur while working with files, using try-except blocks or the 'finally' statement, to ensure proper cleanup and error handling.

# These are the basic concepts of file I/O in Python. With these techniques, you can read from and write to files, allowing you to process and manipulate external data in your Python programs.


# In Python, the 'open()' function allows you to specify different modes for file I/O operations. Modes determine how the file will be opened and what operations can be performed on it. Here are the commonly used modes in Python file I/O:

# 1. **Read Mode ('r'):** This is the default mode. It opens the file for reading. If the file does not exist, it raises a 'FileNotFoundError'. You can perform read operations on the file using methods like 'read()', 'readline()', or 'readlines()'.

# Example:

file_object = open("example.txt", "r")


# 2. **Write Mode ('w'):** It opens the file for writing. If the file exists, it truncates its contents, i.e., it removes all existing data. If the file does not exist, it creates a new file. You can write data to the file using the 'write()' method.

# Example:

file_object = open("example.txt", "w")


# 3. **Append Mode ('a'):** It opens the file for appending. If the file exists, it moves the file pointer to the end of the file, allowing you to add new data without overwriting the existing contents. If the file does not exist, it creates a new file. You can append data to the file using the 'write()' method.

# Example:

file_object = open("example.txt", "a")


# 4. **Binary Mode ('b'):** This mode is used for handling binary files, such as images, audio files, or any non-text files. It is often used in combination with other modes. For example, "rb" is used to open a file in binary read mode.

# Example:

file_object = open("image.jpg", "rb")


# 5. **Text Mode ('t'):** This mode is used to handle text files. It is the default mode and can be omitted when opening a file for text operations. For example, "rt" is the same as using "r" alone.

# Example:

file_object = open("example.txt", "rt")


# 6. **Create Mode ('x'):** It opens the file for exclusive creation. If the file already exists, it raises a 'FileExistsError'. This mode is useful when you want to create a new file and ensure it does not already exist.

# Example:

file_object = open("new_file.txt", "x")


# It's important to note that if you do not explicitly specify the mode, it defaults to text mode ("rt"). Also, after performing file operations, it is good practice to close the file using the 'close()' method or by using the 'with' statement, which automatically takes care of closing the file.

# Here's an example that demonstrates multiple modes:

with open("example.txt", "r") as file_object:
    content = file_object.read()
    print(content)

with open("new_file.txt", "w") as file_object:
    file_object.write("This is a new file.")

with open("data.bin", "ab") as file_object:
    file_object.write(b"\x00\x01\x02\x03")


# This code snippet reads from a file in read mode, writes to a new file in write mode, and appends binary data to a file in append mode.

# These are the common modes used in Python file I/O. You can combine different modes to suit your requirements and perform various operations on files.

# **File Cursor and .seek() method:**
# In Python, when you open a file, there is an internal cursor or pointer that keeps track of the current position in the file. This cursor indicates where the next read or write operation will occur. The 'seek()' method is used to move the file cursor to a specific position within the file.

# The general syntax of the 'seek()' method is:

file_object.seek(offset, whence)

# - 'offset': It specifies the number of bytes to move the cursor. A positive value moves the cursor forward, while a negative value moves it backward.
# - 'whence': It indicates the reference position from where the offset is calculated. Possible values are:
#   - '0' (default): The offset is calculated from the beginning of the file.
#   - '1': The offset is calculated from the current cursor position.
#   - '2': The offset is calculated from the end of the file.

# Example:

with open("example.txt", "r") as file_object:
    # Move the cursor to the 10th byte from the beginning of the file
    file_object.seek(10)
    data = file_object.read()
    print(data)

# In this example, the 'seek(10)' method moves the cursor to the 10th byte from the beginning of the file, and then the 'read()' method reads the data from that position.

# **File Paths:**
# File paths are used to specify the location of a file within a file system. There are several types of file paths in Python:

# 1. **Relative Path:** A relative path specifies the location of a file relative to the current working directory. It does not start with the root directory ('/' in Unix-based systems) or drive letter (e.g., 'C:\' in Windows). Relative paths can use special symbols like '.' (current directory) and '..' (parent directory).

#    Examples:
#    - 'file.txt': Refers to a file in the current working directory.
#    - './data/file.txt': Refers to a file in the 'data' subdirectory of the current working directory.
#    - '../file.txt': Refers to a file in the parent directory of the current working directory.

# 2. **Absolute Path:** An absolute path specifies the complete path from the root directory to the file. It starts with the root directory ('/' in Unix-based systems) or drive letter (e.g., 'C:\' in Windows).

#    Examples:
#    - '/home/user/file.txt': Refers to a file located at '/home/user' in Unix-based systems.
#    - 'C:\Documents\file.txt': Refers to a file located at 'C:\Documents' in Windows.

# 3. **File Path Manipulation:**
#    Python provides the 'os.path' module to manipulate file paths. It offers functions like 'join()', 'dirname()', 'basename()', and more, which are useful for working with file paths across different platforms.

#    Example:
   
   import os

   path = os.path.join("dir", "subdir", "file.txt")
   print(path)  # Outputs: dir/subdir/file.txt

   directory = os.path.dirname(path)
   print(directory)  # Outputs: dir/subdir

   filename = os.path.basename(path)
   print(filename)  # Outputs: file.txt
   

# Understanding file paths and how to manipulate them is crucial for working with files in different directories and across platforms. It helps in locating and accessing files correctly within the file system.

# Pathlib

# 'pathlib' is a module introduced in Python 3 that provides an object-oriented approach for working with file paths. It offers a more convenient and intuitive way to manipulate file paths compared to traditional string-based path handling. The 'pathlib' module includes the 'Path' class, which represents file and directory paths as objects.

# Here's an overview of some common operations with 'pathlib':

# **Importing the 'pathlib' module:**
# To use the 'pathlib' module, you need to import it:


from pathlib import Path


# **Creating a 'Path' object:**
# To work with a file or directory path, you can create a 'Path' object by instantiating the 'Path' class with the desired path:


file_path = Path("path/to/file.txt")
directory_path = Path("path/to/directory")


# **Accessing different components of a path:**
# 'Path' objects provide attributes and methods to access various components of a path:

# - 'name': Returns the name of the file or directory in the path.
# - 'parent': Returns the parent directory of the path.
# - 'suffix': Returns the file extension (including the dot) of the path.
# - 'stem': Returns the file name without the extension.


path = Path("path/to/file.txt")

print(path.name)  # Outputs: file.txt
print(path.parent)  # Outputs: path/to
print(path.suffix)  # Outputs: .txt
print(path.stem)  # Outputs: file


# **Joining paths:**
# You can join paths together using the '/' operator or the 'joinpath()' method:


directory = Path("path/to")
file = Path("file.txt")

path = directory / file
# Equivalent to: path = directory.joinpath(file)


# **Checking if a path exists:**
# The 'Path' class provides the 'exists()' method to check if a file or directory exists:


path = Path("path/to/file.txt")

if path.exists():
    print("Path exists")
else:
    print("Path does not exist")


# **Iterating over directory contents:**
# You can iterate over the contents of a directory using the 'iterdir()' method:


directory = Path("path/to/directory")

for item in directory.iterdir():
    print(item)


# **Creating a directory:**
# To create a directory, you can use the 'mkdir()' method:


directory = Path("path/to/new_directory")
directory.mkdir()


# **Reading the contents of a file:**
# To read the contents of a file, you can use the 'read_text()' method, which returns the contents as a string:


file = Path("path/to/file.txt")
content = file.read_text()

print(content)


# **Writing to a file:**
# To write data to a file, you can use the 'write_text()' method, which writes the specified data to the file:


file = Path("path/to/file.txt")
file.write_text("Hello, World!")


# These are just a few examples of the operations you can perform using the 'pathlib' module. It provides a rich set of methods and attributes for working with file paths, making file I/O operations more readable and convenient.