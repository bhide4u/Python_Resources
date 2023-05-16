# Walrus operator (assignment expressions)

# The walrus operator, also known as assignment expressions, is a feature introduced in Python 3.8. 
# It allows you to assign a value to a variable as part of an expression, rather than as a separate statement. 
# The walrus operator is denoted by `:=`.

# The primary use of the walrus operator is to assign a value to a variable within a conditional statement or a while loop condition. 
# It helps reduce code duplication and improve readability by allowing you to assign a value and use it immediately in the same line.

# Here's an example to illustrate the usage of the walrus operator:

my_list = [1,2,3,4,5,6,7]
# Example 1: Conditional statement
if (n := len(my_list)) > 5:
    print(f"The length of my_list is {n} which is greater than 5.")

# Example 2: While loop condition
while (line := input("Enter a line of text: ")) != "quit":
    print(f"You entered: {line}")

# In Example 1, the walrus operator is used within the conditional statement to assign the length of `my_list` to the variable `n`. 
# The value of `n` is then compared with 5. This avoids the need to compute the length of `my_list` twice.

# In Example 2, the walrus operator is used within the while loop condition to assign the user input to the variable `line`. 
# The input value is checked against the string "quit" to determine whether the loop should continue or exit.

# It's worth noting that the walrus operator has some limitations and considerations:

# - The walrus operator can only be used within an expression, not as a standalone statement.
# - The scope of the assigned variable is limited to the current block or expression where the walrus operator is used.
# - It's important to use the walrus operator judiciously to maintain code readability. Overuse or excessive nesting can lead to code that is harder to understand.

# The walrus operator provides a concise and expressive way to assign values within expressions, reducing the need for separate assignment statements and improving code readability in certain situations.
