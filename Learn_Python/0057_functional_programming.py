# Functional Programming

# Functional programming is a programming paradigm that emphasizes writing programs using pure functions and avoiding mutable state and side effects. 
# It treats computation as the evaluation of mathematical functions and encourages immutability and declarative programming.

# A pure function is a function that, given the same input, will always produce the same output and has no side effects on the program state. 
# It doesn't modify any external state or rely on mutable data. 
# Pure functions are deterministic and have referential transparency, meaning you can replace a function call with its result without affecting the behavior of the program.

# Here's an example of a pure function in Python:

def square(x):
    return x * x


# The 'square' function takes an input 'x' and returns the square of 'x'. 
# It doesn't modify any external state and always produces the same result for the same input.

# On the other hand, a impure function may have side effects or rely on mutable data. Here's an example:


total = 0

def add_to_total(x):
    global total
    total += x
    return total


# The 'add_to_total' function modifies the external variable 'total' each time it is called. 
# It has a side effect by changing the state outside the function.

# In functional programming, you strive to use pure functions as much as possible because they have several benefits:

# 1. Predictability: Pure functions are predictable and easier to reason about since they only depend on their inputs and produce a reliable output.
# 2. Testability: Pure functions are easy to test because they don't rely on external state or have side effects.
# 3. Reusability: Pure functions can be reused in different parts of the codebase without worrying about unexpected interactions with other parts of the program.
# 4. Parallelism: Since pure functions don't rely on mutable state, they can be executed in parallel without causing conflicts or race conditions.

# Functional programming in Python is not as strict as in languages like Haskell or Lisp, but you can still adopt functional programming principles to write more maintainable and modular code.