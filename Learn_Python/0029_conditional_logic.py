# Conditional Logic
# Conditional logic in Python allows you to make decisions based on conditions. 
# In Python, the if statement is used for conditional logic. 

# Here's an example:
x = 10
if x > 5:
    print("x is greater than 5")

# In this example, we first define a variable x with a value of 10. 
# We then use the if statement to test whether x is greater than 5. 
# Since x is indeed greater than 5, the code inside the if block will be executed, and the output will be:
# x is greater than 5

# Here are some other examples of conditional logic in Python:

# If-else statement:
x = 10
if x > 5:
	print("x is greater than 5")
else:
	print("x is less than or equal to 5")

# In this example, we use the if-else statement to print a different message depending on the value of x.

# Elif statement:
x = 10
if x > 10:
	print("x is greater than 10")
elif x == 10:
	print("x is equal to 10")
else:
	print("x is less than 10")


# Nested if statement:
x = 10
y = 5
if x > 5:
    if y > 3:
        print("Both x and y are greater than their respective values")
    else:
    	print("x is greater than 5, but y is not greater than 3")
else:
	print("x is not greater than 5")

# In this example, we use nested if statements to test two conditions. 
# The first if statement checks whether x is greater than 5. 
# If it is, we then check whether y is greater than 3.

# Conditional logic is an important aspect of programming, as it allows you to write code that can make decisions based on different conditions.
