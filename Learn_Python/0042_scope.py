# Scope

# Scope refers to the visibility and accessibility of variables, objects, and functions within a program. 
# It defines the portion of the code where a particular name or identifier can be referenced.

# In Python, scope rules determine how variables and names are resolved during runtime. 
# The scope rules in Python follow the LEGB rule:

# 1. Local Scope: It refers to the variables defined within the current function. Local variables are only accessible within the function in which they are defined.

# 2. Enclosing (Parent) Local Scope: If a function is defined inside another function, the inner function has access to variables in the outer (enclosing) function's scope.

# 3. Global Scope: It refers to variables defined at the top level of a module or declared as global within a function. Global variables are accessible throughout the module or program.

# 4. Built-in Scope: It refers to the names predefined in the Python built-in module. These names are accessible from any part of the code without the need for explicit import.

# Parameters of a function are considered local to that function. 
# They are defined within the function's local scope and are only accessible within the function.

# The `global` keyword is used to declare a variable in the global scope from within a function. 
# It allows modifying a variable that is defined outside the function, making it accessible and modifiable within the function.

# Dependency injection is a design pattern that allows passing dependencies (objects, functions, or values) into a component or function from the outside. 
# Instead of a component or function creating or managing its dependencies internally, they are provided externally, promoting modularity and flexibility.

# The `nonlocal` keyword is used to access and modify a variable in the enclosing (parent) local scope from within a nested function. 
# It is used when a nested function wants to access or modify a variable that is defined in the outer function's scope.

# Scoping is important in programming for several reasons:

# 1. Avoiding Naming Conflicts: Scoping prevents naming conflicts between variables in different parts of the code, ensuring that each identifier refers to the intended object.

# 2. Encapsulation and Modularity: Scoping allows encapsulation, meaning that variables and functions can be hidden and only accessible within the appropriate scope. This promotes modular code organization and reduces complexity.

# 3. Code Reusability: Scoping allows code to be reused by defining variables and functions in a local or global scope that can be accessed from different parts of the code.

# 4. Variable Lifetime: Scoping defines the lifetime of variables, ensuring that they are created and destroyed within the appropriate scope, freeing up memory resources.

# In summary, scoping defines the visibility and accessibility of variables and names within a program. 
# It enables code organization, modularity, reusability, and prevents naming conflicts. 
# Understanding scoping rules is crucial for writing well-structured and maintainable code.