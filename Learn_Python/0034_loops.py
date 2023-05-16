# Loops
# In Python, a for loop is used to iterate over a sequence of elements, such as a list, tuple, or string. 

# for loop -
# The basic syntax of a for loop is as follows:

# for variable in sequence:
    # statements to be executed for each element

# In this syntax, variable is a new variable that takes on the value of each element in the sequence on each iteration of the loop. 
# The statements to be executed for each element are indented underneath the for loop header.

# Here's an example that shows how to use a for loop to iterate over a list of numbers:
numbers = [1, 2, 3, 4, 5]

for num in numbers:
	print(num)

# In this example, we have a list of numbers. 
# The for loop iterates over each element in the list and assigns it to the variable num. 
# The print statement inside the loop prints out each number on a new line.

# The output of this code will be:

# 1
# 2
# 3
# 4
# 5

# We can also use the built-in range() function to generate a sequence of numbers and iterate over them using a for loop. 
# Here's an example:

for i in range(1, 6):
    print(i)

# In this example, the range() function generates a sequence of numbers from 1 to 5 (inclusive). 
# The for loop iterates over each number in the sequence and prints it out.

# The output of this code will be:

# 1
# 2
# 3
# 4
# 5

# In addition to iterating over sequences of elements, for loops can also be used to iterate over the keys or values in a dictionary using the items() method. 
# Here's an example:

person = {"name": "Alice", "age": 25, "city": "New York"}

for key, value in person.items():
	print(key, ":", value)

# In this example, we have a dictionary 'person' that contains information about a person. 
# The for loop iterates over the items() in the dictionary, which returns a sequence of key-value pairs. 
# On each iteration of the loop, the key variable takes on the key of the current item, and the value variable takes on the value of the current item. 
# The print statement inside the loop prints out the key and value of each item.

# The output of this code will be:

# name : Alice
# age : 25
# city : New York

# Overall, for loops are a powerful tool for iterating over sequences of elements, and they are a fundamental construct in Python programming.


# While Loops - 

# A while loop in Python is a control flow statement that allows you to execute a block of code repeatedly as long as a specified condition is true. 
# The basic syntax of a while loop in Python is as follows:

# while condition:
    # Code to execute while the condition is true

# The condition is an expression that is evaluated before each iteration of the loop. If the condition is true, the code inside the loop is executed. This process is repeated until the condition becomes false.

# Here's an example that uses a while loop to print the numbers from 1 to 5:
i = 1
while i <= 5:
	print(i)
	i += 1
else:
	print('Done with all the work')

# In this example, the loop starts with i equal to 1. 
# The condition i <= 5 is true, so the code inside the loop is executed. 
# The print(i) statement outputs the value of i, which is 1. 
# The statement i += 1 increments the value of i by 1, so i is now equal to 2.

# The loop then repeats, and the condition is checked again. 
# Since i is still less than or equal to 5, the loop continues to execute. 
# This process is repeated until i becomes 6, at which point the condition i <= 5 is false, and the loop stops executing.

# Here's another example that uses a while loop to prompt the user for input until they enter a valid integer:

while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
    		print("Invalid input! Please enter an integer.")

# In this example, the while loop continues to execute until the break statement is encountered. 
# The loop prompts the user for input using the input() function and attempts to convert the input to an integer using the int() function. 
# If the input is not a valid integer, a ValueError exception is raised, and the except block is executed. The except block outputs an error message and then continues the loop, prompting the user for input again. 
# If the input is valid, the break statement is executed, and the loop stops executing.

# while loops are useful when you want to execute a block of code repeatedly while a certain condition is true. 
# However, it's important to be careful when using while loops, as an infinite loop can occur if the condition never becomes false.

# While - else - 
# In Python, the else statement in a while loop is an optional clause that can be used to execute a block of code after the loop finishes executing normally. 
# This means that if the loop condition becomes false and the loop terminates, the code inside the else block will be executed. 
# However, if the loop is exited prematurely, such as with a break statement, the else block will not be executed.

# Here is an example of how the else statement can be used in a while loop:
	
count = 0
while count < 5:
	print(count)
	count += 1
else:
	print("Loop completed")

# In this example, the while loop will iterate five times, printing the value of count each time. 
# After the loop finishes normally, the message "Loop completed" will be printed.

# Another example of using else with a while loop is to check whether a condition has been met within the loop. 
# For example, the following code uses a while loop to search for the first occurrence of the letter "e" in a string, and prints a message if the letter is found:

word = "Python"
index = 0
while index < len(word):
    if word[index] == "e":
        print("Found 'e' at index", index)
        break
    index += 1
else:
	print("Letter 'e' not found")

# In this example, the while loop will iterate through each character in the string word, checking if the current character is equal to the letter "e". 
# If the letter is found, a message is printed and the loop is exited with a break statement. 
# If the loop finishes normally without finding the letter, the message "Letter 'e' not found" is printed.