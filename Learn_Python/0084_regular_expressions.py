# Regular Expressions

# Regular expressions, often referred to as regex, are powerful tools used for pattern matching and text manipulation in Python and other programming languages. They allow you to search, extract, and manipulate strings based on specific patterns or rules.

# In Python, the 're' module provides functions and methods for working with regular expressions. Here are some commonly used functions and metacharacters in regular expressions:

# 1. 're.search(pattern, string)': Searches for the first occurrence of a pattern in a string.
# 2. 're.match(pattern, string)': Matches the pattern only at the beginning of the string.
# 3. 're.findall(pattern, string)': Returns all non-overlapping occurrences of a pattern in a string as a list.
# 4. 're.split(pattern, string)': Splits the string by the occurrences of the pattern and returns a list.
# 5. 're.sub(pattern, repl, string)': Substitutes occurrences of a pattern in a string with a replacement string.

# Here are some examples to illustrate the usage of regular expressions in Python:


import re

# Example 1: Searching for a pattern
text = "Hello, my name is John Doe. Nice to meet you."
pattern = r"John Doe"
result = re.search(pattern, text)
print(result.group())  # Output: John Doe

# Example 2: Matching at the beginning of a string
text = "Welcome to the Python programming language."
pattern = r"^Welcome"
result = re.match(pattern, text)
print(result.group())  # Output: Welcome

# Example 3: Finding all occurrences of a pattern
text = "The cat and the hat sat on the mat."
pattern = r"at"
result = re.findall(pattern, text)
print(result)  # Output: ['at', 'at', 'at', 'at']

# Example 4: Splitting a string by a pattern
text = "Hello, World! How are you today?"
pattern = r"\W+"  # Matches one or more non-alphanumeric characters
result = re.split(pattern, text)
print(result)  # Output: ['Hello', 'World', 'How', 'are', 'you', 'today']

# Example 5: Substituting occurrences of a pattern
text = "I have 10 apples and 5 oranges."
pattern = r"\d+"  # Matches one or more digits
replacement = "X"
result = re.sub(pattern, replacement, text)
print(result)  # Output: "I have X apples and X oranges."


# In the examples above, we use regular expression patterns such as '"John Doe"', '"^Welcome"', '"at"', '"\W+"', and '"\d+"'. These patterns are defined using special characters and metacharacters that represent specific sets of characters or rules. The 'r' prefix before the pattern strings denotes a raw string literal in Python, which avoids unintended escape character conflicts with regular expression patterns.

# Regular expressions provide a powerful and flexible way to work with text patterns in Python, allowing you to search, match, extract, split, and substitute strings based on specific rules or patterns.


# In regular expressions, patterns are the heart of the matching process. A pattern is a sequence of characters that defines a specific rule or set of rules to match against a given text. It can consist of ordinary characters, metacharacters, and special sequences.

# Let's explore some key components used to build patterns in regular expressions:

# 1. Ordinary Characters: Ordinary characters in a pattern represent themselves and match the same characters in the target text. For example, the pattern '"hello"' will match the exact sequence of characters "hello" in the text.

# 2. Metacharacters: Metacharacters have special meanings in regular expressions. They allow you to define more complex rules and patterns. Here are some commonly used metacharacters:

#    - '.' (dot): Matches any single character except a newline.
#    - '^' (caret): Matches the start of a line.
#    - '$' (dollar): Matches the end of a line.
#    - '*' (asterisk): Matches zero or more occurrences of the preceding character or group.
#    - '+' (plus): Matches one or more occurrences of the preceding character or group.
#    - '?' (question mark): Matches zero or one occurrence of the preceding character or group.
#    - '|' (pipe): Acts as an OR operator, allowing you to specify alternatives.
#    - '[]' (square brackets): Matches any single character within the brackets.
#    - '()' (parentheses): Groups characters or expressions together.

# 3. Special Sequences: Special sequences are predefined patterns that represent common character sets or rules. Here are a few examples:

#    - '\d': Matches any digit (0-9).
#    - '\D': Matches any non-digit character.
#    - '\w': Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore _).
#    - '\W': Matches any non-alphanumeric character.
#    - '\s': Matches any whitespace character (space, tab, newline).
#    - '\S': Matches any non-whitespace character.
#    - '\b': Matches a word boundary.

# Using these components, you can create more complex patterns to match specific text patterns or rules. Here's an example pattern:


import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"The quick (\w+) fox jumps over the (\w+) dog\."

result = re.search(pattern, text)
if result:
    print(result.group(1))  # Output: brown
    print(result.group(2))  # Output: lazy


# In this example, the pattern '"The quick (\w+) fox jumps over the (\w+) dog\."' consists of ordinary characters, metacharacters, and a special sequence. The '(\w+)' represents a group that matches one or more alphanumeric characters, allowing us to extract the words "brown" and "lazy" from the text.

# By combining ordinary characters, metacharacters, and special sequences in various ways, you can create powerful patterns to match and manipulate text based on specific rules or patterns. Regular expressions provide a flexible and expressive language for working with text patterns in Python and other programming languages.

# If you want to spend a few hours learning about RegEx in detail and want to follow a fun interactive tutorial, here is a nice free way to get yourself comfortable with some of the common patterns

# https://regexone.com/
# regex101.com