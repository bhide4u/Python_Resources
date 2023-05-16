# Ternary operator - (also called as ternary expressions)

# In Python, the ternary operator is a shorthand way of writing a simple conditional expression. 
# It allows you to write an expression in a more concise way, by combining the if and else clauses into a single line. 

# The syntax of the ternary operator in Python is:

# value_if_true if condition else value_if_false

# Here, condition is the expression that is evaluated to a Boolean value, and value_if_true and value_if_false are the values that are returned if the condition is True or False, respectively.

# Here is an example of how to use the ternary operator in Python:

x = 5
y = 10
max_value = x if x > y else y
print(max_value)

# In this example, we have two variables x and y with values of 5 and 10, respectively. We want to find the maximum value between these two variables. The ternary operator is used to check if x is greater than y. If the condition is true, x is assigned to max_value, otherwise y is assigned to max_value.

# When we run this code, the output will be:
# 10

# Since y is greater than x, the value of y is assigned to max_value.