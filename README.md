# README

## Commenting

Commenting in code can be done in two ways:

1. Single Line Commenting:
   Use `#` to add comments on a single line. For example:
   ```
   # This is a single line comment
   ```

2. Multi-line Commenting:
   Use triple quotes (`'''` or `"""`) to add comments spanning multiple lines. For example:
   ```
   '''
   This is a
   multi-line comment
   '''
   ```

## Variables

Variables are containers used to store data in programming. Here are some rules for variable declaration:

1. Descriptive names, easy to read: Choose meaningful names that describe the purpose of the variable.
2. Avoid reserved keywords as variable names: Do not use keywords reserved by the programming language as variable names.
3. Use lowercase letters and separate words with underscores (snake_case): Follow a consistent naming convention for variables.
4. Declare variables close to where they are used: Declare variables in the smallest scope possible.
5. Define constants in all capital letters: Use uppercase letters with underscores for constant variables.
6. Don't reuse variables in the same block of code: Avoid using the same variable name for different purposes within the same block of code.
7. Avoid using global variables unless absolutely necessary: Use local variables whenever possible to limit the scope and potential conflicts.
8. Use variable type annotations: Specify the variable type using annotations. For example:
   ```python
   num_students: int = 20
   ```

## Special Variables / Magic Variables

In Python, there are special variables with specific uses:

1. `_` (underscore): Used as a placeholder for variables that are not used in the code.
2. `__` (double underscore):
   - Used for name mangling in Python classes. Name mangling makes a variable or method private to a class.
   - `__init__`: Double underscore on both sides. It is used for special methods or attributes in Python classes.

## Variable Assignments

Variable assignments can be done in different ways:

1. Multiple values to multiple variables:
   ```python
   a, b, c = 1, 2, 3
   ```

2. One value to multiple variables:
   ```python
   a = b = c = "apple"
   ```

3. Unpacking a collection:
   ```python
   a, b, c = [1, 2, 3]
   ```

## Variable Scoping

Variables have different scopes that determine where they can be accessed:

1. Global:
   - Defined outside of any function or class definition.
   - Can be accessed from anywhere in your code.
   - Modifying a global variable from within a function requires using the `global` keyword (not recommended).

2. Local:
   - Defined within a function or class definition.
   - Can only be accessed from within that function or class.

## Data Type vs Data Structure

Data Type:
- A data type is a classification of data that determines the type of operations that can be performed on it.
- Examples of data types include integers, floats, strings, and booleans.
- Each data type has its own set of operations that can be performed on it.

Data Structures:
- Data structures are ways of organizing and storing data in a computer so that it can be accessed and used efficiently.
- Built-in data structures in Python include lists, tuples, dictionaries, and sets.
- Each data structure has its own set of methods and operations that can be performed on it.
- For example, lists have methods like `append()`, and dictionaries have methods like `keys()`.

## Data Types in Python

1. Numeric Types:
   - `int`, `float`, `complex`

2. Text Type:
   - `str`

3. Sequence Types:
   - `list`, `tuple`, `range`

4. Mapping Type:
   - `dict`

5. Set Types:
   - `set`, `frozenset`

6. Boolean Type:
   - `bool`

7. Binary Types:
   - `bytes`, `bytearray`, `memoryview`

8. None Type:
   - `None`

## Specialized Data Types in Python

1. Lists:
   - A collection of items that can be of any data type.
   - Ordered and mutable.
   - Created using square brackets `[]`, with commas `,` used to separate values.
   - List indexing starts from 0.
   - List slicing: `List[start:end:step]`
   - Matrix: Multi-dimensional lists. Individual elements accessed using two indices, e.g., `matrix[1][2]`.
   - List methods: `append`, `copy` (shallow copying), `clear`, `count`, `extend`, `index`, `insert`, `pop`, `remove`, `reverse`, `sort`.
   - List unpacking: `a, b, *c = [1, 2, 3, 4, 5]`. Can be used for swapping variables: `a, b = b, a`.

2. Strings:
   - Enclosed in single quotes `''` or double quotes `""`.
   - Displayed using `print()`.
   - Multiline Strings: Enclosed in triple quotes `'''` or `"""`.
   - Strings are arrays and can be accessed using square brackets `[]` (index starts from 0).
   - String concatenation using `+`.
   - Formatted strings: `f"{expression}"`, `{pi:.2f}`, `"{}".format()`, with format specification like `"{:.2f}"`.
   - String indexing and slicing: `string[start:end:step]`.
   - String methods: `capitalize`, `count`, `endswith`, `find`, `index`, `join`, `lower`, `lstrip`, `replace`, `rstrip`, `split`, `startswith`, `strip`, `title`, `upper`.
   - Strings are immutable.

3. Booleans:
   - `True`, `False`.
   - Used in conditional statements to represent logical values.

4. None:
   - Represents the absence of a value.
   - Used to indicate that a variable or function argument does not have a meaningful value.
   - Functions without an explicit return value default to `None`.

5. Dictionaries:
   - A collection of key-value pairs.
   - Each key is associated with a value.
   - Accessing values: `my_dict['name']`.
   - Adding new key-value pair: `my_dict['email'] = 'john@example.com'`.
   - Deleting key-value pair: `del my_dict['gender']`.
   - Nested dictionaries.
   - Properties of dictionary keys: Unique, Immutable, Hashable, Case-sensitive.
   - Dictionary methods: `clear`, `copy`, `fromkeys`, `get`, `items`, `keys`, `pop`, `popitem`, `update`, `values`.

6. Tuples:
   - An ordered and immutable collection of elements.
   - Enclosed in parentheses `()`.
   - Single-element tuples require a trailing comma.
   - Indexing and slicing.
   - Tuple concatenation with `+`.
   - Tuple unpacking for returning multiple values from a function or creating a collection of unmodifiable elements.
   - Tuple methods: `count`, `

index`.

7. Sets:
   - An unordered collection of unique elements.
   - Useful for performing operations like intersection, union, and difference.
   - Membership test using the `in` operator.
   - Set methods: `add`, `clear`, `copy`, `difference`, `difference_update`, `discard`, `intersection`, `intersection_update`, `isdisjoint`, `issubset`, `issuperset`, `pop`, `remove`, `symmetric_difference`, `symmetric_difference_update`, `union`, `update`.
   - Difference between `discard()` and `remove()` methods: `remove()` raises a `KeyError` if the element to remove is not found.

## Python Keywords

The following are Python keywords:

- `and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `None`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `while`, `with`, `yield`

## Escape Sequences

The following are escape sequences in Python:

- `\n` - newline
- `\t` - tab
- `\'` - single quote
- `\"` - double quote
- `\\` - backslash

## Operators

1. Arithmetic Operators:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Modulo (%)
   - Floor Division (//)
   - Exponentiation (**)

   Operator Precedence determines the order in which operations are evaluated in an expression.

2. Assignment Operators:
   - Addition and Assignment (+=)
   - Subtraction and Assignment (-=)
   - Multiplication and Assignment (*=)
   - Division and Assignment (/=)
   - Modulo and Assignment (%=)

3. Comparison Operators:
   - Equal to (==)
   - Not equal to (!=)
   - Greater than (>)
   - Less than (<)
   - Greater than or equal to (>=)
   - Less than or equal to (<=)

4. Logical Operators:
   - AND (and)
   - OR (or)
   - NOT (not)

## Walrus Operator (Assignment Expressions)

The walrus operator (`:=`) allows assignment within expressions. It has the following considerations:

- The walrus operator can only be used within an expression, not as a standalone statement.
- The scope of the assigned variable is limited to the current block or expression where the walrus operator is used.
- It's important to use the walrus operator judiciously to maintain code readability. Overuse or excessive nesting can lead to code that is harder to understand.

The walrus operator provides a concise and expressive way to assign values within expressions, reducing the need for separate assignment statements and improving code readability in certain situations.

## `in` Keyword (Membership Operator)

The `in` keyword is a membership operator used to test if a value is present in a sequence (such as a string, list, or tuple). It returns `True` if the value is found and `False` otherwise. For example:

```python
my_list = [1, 2, 3]
print(2 in my_list)  # Output: True
print(4 in my_list)  # Output: False
```

The `in` keyword is useful for checking membership and performing conditional operations based on the presence or absence of a value in a sequence.

## Expression vs Statement

In Python, there is a distinction between expressions and statements:

- Expression: A piece of code that produces a value when executed. It can be as simple as a single variable or involve more complex calculations. Expressions can be part of a larger statement or stand alone.
- Statement: A complete unit of execution that performs an action. It can include expressions, but it cannot be part of an expression itself.

## Type Conversion

Python provides built-in functions for type conversion:

- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a floating-point number.
- `str()`: Converts a value to a string.
- `list()`: Converts a value to a list.
- `tuple()`: Converts a value to a tuple.
- `set()`: Converts a value to a set.
- `bool()`: Converts a value to a Boolean.

These functions allow you to convert values from one type to another as needed in your code.

## Must-Know Functions

Here are some essential functions in Python:

1. `print()`: Prints output to the console.
2. `type(variable)`: Returns the type of the given variable.
3. `len()`: Returns the length of a sequence or collection. Note that `len()` is used to find the length of sequences, while `.count()` is used to count occurrences within a sequence.
4. `sorted()`: Returns a sorted version of a sequence or collection. Note that `sorted()` creates a new sorted list, while the `.sort()` method sorts the list in place.
5. `range()`: Generates a sequence of numbers within a specified range. The `range()` function can take parameters for start, stop, and step.
6. `help()`: Displays documentation and information about Python objects, modules, and functions.

## Built-in Modules

Python provides several built-in modules that offer additional functionality. Here are a couple of examples:

1. `random`: A module for generating random numbers. It includes methods like `randint()` and `randrange()`.
2. `math`: A module for mathematical operations. It includes functions like `abs()`, `round()`, `pow()`, `sqrt()`, `floor()`, `ceil()`, `min()`, `max()`, `sum()`, and `log()`.

You can import these modules and use their functions in your Python programs to perform specific tasks.

## Conditional Logic

Conditional logic allows you to execute different blocks of code based on specific conditions. In Python, you can use the following constructs:

- `if` statement: Executes a block of code if a condition is true.
- `elif` statement: Provides additional conditions to check if the preceding `if` or `elif` conditions are false.
- `else` statement: Executes a block of code if none of the preceding conditions are true.

You can also have nested `if` statements, where one `if` statement is placed inside another.

## Ternary Operator

The ternary operator is a shorthand way of writing an `if` statement in Python. It allows you to write a concise one-liner code that evaluates an expression and returns one of two values based on whether the expression is true or false. The syntax of the ternary operator is as follows:

```
value_if_true if condition else value_if_false
```

Using the ternary operator can make your code more compact and readable when you have simple conditional expressions.

## Loops

Loops are used to iterate over a sequence of elements in Python. There are two main types of loops:

- `for` loop: Used for iterating over sequences such as lists, tuples, and strings. It can also iterate over the keys or values in a dictionary using the `items()` method.
- `while` loop: Executes a block of code repeatedly as long as a specified condition is true. It can be controlled using the `while` statement, and it also supports an `else` block.

Within loops, you can use the following statements:

- `break`: Terminates the loop and exits its current iteration.
- `continue`: Skips the rest of the current iteration and moves to the next iteration.
- `pass`: Acts as a placeholder, allowing you to have an empty block of code.

## Iterables

An iterable is any object that can be looped over using a `for` loop. In Python, an iterable is an object that has the following characteristics:

- It has an `__iter__()` method that returns an iterator object.
- It has a `__next__()` method that returns the next item in the sequence and raises a `StopIteration` exception when there are no more items to return.

Python provides several built-in iterables, including lists, tuples, dictionaries, sets, and strings. These objects can be directly used in `for` loops.

Additionally, Python provides some built-in functions for iteration:

- `range()`: Generates a sequence of numbers within a specified range. It can take parameters for start, stop, and step.
- `enumerate()`: Returns an iterator that contains pairs of the form `(index, value)` for each item in the iterable. It is useful when you want to keep track of the index of each item in an iterable object. The `enumerate()` function can save you from writing a separate counter variable and incrementing it manually. It accepts an iterable and an optional `start` parameter.

You can also create your own iterable objects by defining a class with an `__iter__()` method that returns an iterator object. This allows you to customize the iteration behavior of your objects.

By understanding loops and iterables, you can efficiently process and manipulate data in Python.

## Functions

Functions in Python are blocks of reusable code that perform specific tasks. They allow you to break your program down into smaller, more manageable pieces, making your code easier to read, write, and maintain. Here are some key points about functions:

- Functions can have optional and required arguments. Optional arguments have default values, while required arguments must be provided when calling the function.
- Functions can return multiple values using tuples or other data structures.
- It is recommended that functions follow certain conventions:
  - Each function should do one thing really well, focusing on a specific task.
  - Functions should return a value, even if it is `None`.
  
When working with functions, it's important to understand the distinction between arguments and parameters:

- Parameters are the values that a function expects to receive when it is defined. They are defined in the function signature and act as placeholders for the values to be passed.
  - Default parameters can be set, which provide default values if no arguments are provided.
- Arguments are the actual values passed to a function when it is called. They correspond to the parameters defined in the function declaration.
  - Arguments can be passed as keyword arguments or positional arguments.

The `return` keyword is used to specify the value that a function should return. It allows functions to provide output or results to the caller.

Functions can also be nested, meaning one function can be defined inside another. Nested functions have access to variables defined in their containing function and can be useful for organizing code and reducing redundancy.

Methods are functions that are associated with objects. They are defined within classes and operate on the attributes and data of the objects they are called on. Methods are accessed using the dot notation and can access and manipulate the object's data.

Docstrings (Documentation Strings) are string literals used to provide documentation and descriptions for modules, classes, functions, and methods. They serve as a way to document the purpose, behavior, parameters, and return values of a piece of code. Docstrings are placed immediately after the definition of a module, class, function, or method using triple quotes (''' or """). Docstrings can be accessed using the `help()` function or by accessing the `__doc__` attribute of an object. They can also be automatically extracted to generate documentation in various formats using tools like Sphinx.

By understanding functions and their related concepts, you can write modular, reusable, and well-documented code in Python.
## Magic Methods or Dunder Methods

In Python, magic methods, also known as dunder methods (short for double underscore methods), are special methods with double underscore (`__`) names. These methods provide functionality to classes that allows them to emulate built-in behavior or operations. Some commonly used magic methods include `__init__`, `__str__`, `__len__`, `__add__`, and many more. By implementing magic methods, you can customize the behavior of your classes to work with Python's built-in functions and operators.

## *args and **kwargs

`*args` and `**kwargs` are special syntaxes used in function definitions to handle a varying number of arguments:

- `*args` is used to pass a variable number of non-keyword arguments to a function. It allows you to pass multiple positional arguments, which are then captured as a tuple inside the function.
- `**kwargs` is used to pass a variable number of keyword arguments to a function. It allows you to pass multiple keyword arguments, which are then captured as a dictionary inside the function.

You can use both `*args` and `**kwargs` together in a function definition if you want to accept both positional and keyword arguments. When using arguments in a function call, the order is as follows: actual parameters, `*args`, default parameters, `**kwargs`.

Inside the function, you can iterate over `args` (or any other variable name used in place of `args`) and access each argument. Similarly, you can iterate over `kwargs` to access each key-value pair using the `items()` method.

## Python Indentation

In Python, indentation plays a crucial role in defining the structure and scope of the code. Instead of using braces or keywords, Python uses indentation to indicate blocks of code. The standard convention is to use four spaces for each level of indentation. Proper indentation is important for maintaining the readability and integrity of the code. It is recommended to consistently use indentation throughout your Python codebase.

## Truthy vs Falsey

In Python, truthy and falsey values are used to evaluate conditions in control flow statements such as `if` statements and `while` loops. A value is considered truthy if it evaluates to `True` in a Boolean context, and falsey if it evaluates to `False`. Truthy values include non-zero numbers, non-empty containers (such as lists, tuples, dictionaries, and sets), and non-empty strings. Falsey values include `None`, `False`, `0`, empty containers, and empty strings.

Understanding truthy and falsey values helps you write more expressive and concise code when dealing with conditions and control flow in Python.
## Miscellaneous

### Why `print('a' > 'A')` evaluates to `True`?

The expression `print('a' > 'A')` evaluates to `True` because the comparison is performed based on the lexicographic order of the characters. In the ASCII table, 'a' has a greater value than 'A'. Therefore, when comparing these two characters, 'a' is considered greater than 'A', resulting in the expression evaluating to `True`.

### What will be the output of `print(1 < 2 > 3 < 4 < 5)` in Python and why?

The output of `print(1 < 2 > 3 < 4 < 5)` will be `False`. Comparison operators in Python, such as `<` and `>`, have left-to-right associativity. This means the expression is evaluated from left to right, and the comparison operations are evaluated in pairs. In this case, the expression is evaluated as `(1 < 2) and (2 > 3) and (3 < 4) and (4 < 5)`, and since the second comparison `2 > 3` is `False`, the overall result is `False`.

### `is` vs `==`

The `==` operator is used to compare the values of two objects. It checks whether the two objects have the same value or not. On the other hand, the `is` operator is used to compare the identity of two objects. It checks whether the two objects refer to the same memory location or not. In other words, `==` compares the contents, while `is` compares the references of the objects.

## Clean Coding

Clean coding refers to writing code that is easy to read, understand, and maintain. It involves following established conventions and best practices to ensure code quality. Some principles of clean coding include:

### DRY Principle

DRY stands for "Don't Repeat Yourself." The DRY principle encourages code reuse and reducing duplication. It suggests that code should have a single, authoritative representation to avoid redundancy. By eliminating duplicated code, you improve maintainability, reduce the chances of introducing bugs, and make your code more concise.

## Scope

Scope in Python refers to the visibility and accessibility of variables and names within a program. The scope rules in Python follow the LEGB rule, which stands for Local, Enclosing, Global, and Built-in.

Scoping is important because it provides the following benefits:

- Avoiding Naming Conflicts: Scoping helps prevent naming conflicts by limiting the visibility of variables to specific scopes.
- Encapsulation and Modularity: Scoping allows you to encapsulate variables and functions within their respective scopes, promoting modularity and reducing code dependencies.
- Code Reusability: Scoping enables code reusability by controlling the visibility and accessibility of variables.
- Variable Lifetime: Scoping determines the lifetime of variables, ensuring they are available only when needed.

The `nonlocal` keyword allows you to modify variables in an outer (enclosing) scope from within an inner scope, such as a nested function.

## Dependency Injection

Dependency injection is a software design pattern that promotes loose coupling and modular development. It involves providing the dependencies of a component from the outside, rather than having the component create or manage its dependencies.

By using dependency injection, you can decouple the components, improve testability, and make your code more flexible and maintainable. Instead of hardcoding dependencies within a component, they are passed as arguments or provided through a container, allowing for easy substitution or modification of dependencies.

Dependency injection helps to achieve the following:

- Separation of Concerns: Dependencies are managed separately from the component, ensuring better separation of concerns and modular design.
- Testability: Dependencies can be easily mocked or replaced during testing, enabling unit testing and reducing coupling.
- Flexibility: Components can be easily reconfigured or extended by modifying the injected dependencies, promoting flexibility and adaptability.

Overall, dependency injection promotes decoupling and improves the overall quality and maintainability of the codebase.