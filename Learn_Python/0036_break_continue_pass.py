# break, continue and pass

# In Python, break, continue, and pass are control flow statements that can be used to alter the normal execution of a loop or a conditional statement.

# break: The break statement is used to immediately exit a loop. 
# When break is encountered inside a loop, the loop is terminated and control is passed to the next statement following the loop. 

# Here's an example:
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# In this example, the for loop will iterate from 1 to 10. 
# When i becomes 5, the break statement is executed, and the loop is terminated. 
# Therefore, the output will be:

# 1
# 2
# 3
# 4

# continue: The continue statement is used to skip the current iteration of a loop and move on to the next iteration. 
# When continue is encountered inside a loop, the current iteration is skipped and the loop immediately jumps to the next iteration. 

# Here's an example:
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# In this example, the for loop will iterate from 1 to 10. 
# When i is an even number, the continue statement is executed, and the current iteration is skipped. 

# Therefore, the output will be:

# 1
# 3
# 5
# 7
# 9

# pass: The pass statement is a null operation that does nothing. 
# It is used as a placeholder when a statement is required syntactically, but no action is required. 
# For example, if you want to define a function that does nothing, you can use the pass statement as a placeholder:

def my_function():
    pass

# In this example, my_function does nothing. 
# The pass statement is used as a placeholder to indicate that the function does not have any code to execute.
