# Indentation in Python
# In Python, indentation is used to define the scope of a code block. 
# Unlike many other programming languages that use curly braces or other characters to denote code blocks, Python uses indentation as a way of indicating which lines of code belong to which block.

# For example, consider the following code that uses an if statement:
	
x = 10
if x > 5:
	print("x is greater than 5")

# In this code, the if statement is followed by a colon (:), and the next line is indented to show that it is part of the code block that is executed if the condition is true. 
# If we didn't indent the second line, Python would raise an IndentationError because it wouldn't know which lines are part of the code block and which are not.


# Here's another example that uses a for loop:

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

# In this code, the for loop is followed by a colon (:), and the next line is indented to show that it is part of the code block that is executed for each iteration of the loop. 
# Similarly, the if statement is followed by a colon (:), and the next two lines are indented to show that they are part of the code block that is executed if the condition is true. 
# Again, if we didn't indent the lines correctly, Python would raise an IndentationError.

# Indentation in Python is typically done using four spaces. 
# While it is possible to use tabs or a combination of tabs and spaces, it's generally recommended to use spaces to avoid any issues with different editors interpreting tabs differently.
