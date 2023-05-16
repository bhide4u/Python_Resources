# Short Circuiting
# Short-circuiting is a behavior in Python (and other programming languages) where the evaluation of a boolean expression stops as soon as the truth value of the expression is determined. 
# This means that if the first part of a boolean expression is enough to determine the truth value of the whole expression, the rest of the expression is not evaluated.

# Python has two logical operators that implement short-circuiting: AND and OR.

# For the 'and' operator, if the left operand evaluates to False, the entire expression is False, so the right operand is not evaluated. 
# On the other hand, if the left operand evaluates to True, the right operand is evaluated to determine the final truth value of the expression.

# Example:
x = 5
y = 10
if x > 0 and y/x > 2:
	print("y is at least twice x")
else:
	print("y is not at least twice x")

# In this example, the left operand of the and operator is x > 0, which evaluates to True. Therefore, the right operand y/x > 2 is evaluated to determine the final truth value of the expression. If x were negative, the entire expression would be False and the right operand would not be evaluated.

# For the 'or' operator, if the left operand evaluates to True, the entire expression is True, so the right operand is not evaluated. On the other hand, if the left operand evaluates to False, the right operand is evaluated to determine the final truth value of the expression.

# Example:
x = None
y = 10
z = x or y
print(z)

# In this example, the left operand of the or operator is x, which is None. 
# Since 'None' is considered False in a boolean context, the right operand y is evaluated and its value is assigned to z. 
# If x were a non-empty string or any other value that is considered True in a boolean context, the entire expression would be True and the right operand would not be evaluated.


