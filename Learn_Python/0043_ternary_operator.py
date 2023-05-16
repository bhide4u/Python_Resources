# Ternary Operator

# The ternary operator is a shorthand way of writing an `if` statement in Python. 
# It allows you to write a concise one-liner code that evaluates an expression and returns one of two values based on whether the expression is true or false.

# The syntax of the ternary operator in Python is:

# `value_if_true if condition else value_if_false`

# Here, `condition` is the expression that is evaluated and if it is `True`, then the `value_if_true` is returned, otherwise, `value_if_false` is returned.

# For example, consider the following code that checks if a number is even or odd and prints a message accordingly:

num = 5
if num % 2 == 0:
    message = "even"
else:
    message = "odd"

print("The number is", message)

# The same code can be written using a ternary operator as follows:


num = 5
message = "even" if num % 2 == 0 else "odd"
print("The number is", message)

# Here, the ternary operator evaluates the expression `num % 2 == 0` and returns `"even"` if it is true, and `"odd"` if it is false.

# The ternary operator is particularly useful in situations where you need to make a quick decision based on a condition, without having to write a lengthy `if-else` statement. 
# However, it is important to use the ternary operator judiciously, as using it too frequently can make the code harder to read and maintain.