# Dictionaries

# Dictionaries: A dictionary is a collection of key-value pairs. 
# The keys are unique and used to access the corresponding values. 
# Dictionaries are commonly used to store and retrieve data in a structured way.

person = {'name': 'John', 'age': 25, 'gender': 'Male'}

# A dictionary is a collection of key-value pairs, where each key is associated with a value. 
# Dictionaries are an extremely useful data structure for storing and organizing data, particularly when the data can be accessed and updated using keys.

# Here is an example of a dictionary in Python:

my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

# In this example, we have created a dictionary called my_dict that contains three key-value pairs. 
# The keys are 'name', 'age', and 'gender', and the corresponding values are 'John', 30, and 'male'.

# We can access the values in a dictionary using the keys. 
# For example, to access the value associated with the 'name' key in my_dict, we can use the following code:

print(my_dict['name'])

# This will output:	
# John

# We can also add new key-value pairs to a dictionary using the following syntax:
my_dict['email'] = 'john@example.com'

# This will add a new key-value pair to my_dict with the key 'email' and the value 'john@example.com'.

# To update the value associated with a key, we can simply assign a new value to that key:
my_dict['age'] = 31

# This will update the value associated with the 'age' key to 31.
# We can also remove key-value pairs from a dictionary using the del keyword:
del my_dict['gender']

# This will remove the key-value pair with the key 'gender' from my_dict.

# Dictionaries can also be used in more complex ways, such as storing nested data structures or using them to represent real-world objects. 
# Here is an example of a nested dictionary:

my_dict = {
	'person1': {
    	'name': 'John',
    	'age': 30
	},
	'person2': {
    	'name': 'Jane',
    	'age': 25
		}
}

# In this example, we have a dictionary that contains two key-value pairs, each of which is itself a dictionary. 
# This allows us to store multiple pieces of data for each person.

# Overall, dictionaries are a powerful and flexible data structure in Python that can be used in a variety of ways. 
# They are particularly useful for storing and organizing data that can be accessed and updated using keys.

# Properties of dictionary keys - 
# In Python dictionaries, keys have several properties that distinguish them from other data types:

# Unique: Keys in a dictionary must be unique. If you try to assign a value to a key that already exists in the dictionary, the new value will overwrite the existing value.

# Immutable: Dictionary keys must be immutable. This means that they cannot be changed after they are created. Common examples of immutable data types in Python include strings, numbers, and tuples. Mutable data types like lists cannot be used as dictionary keys.

# Hashable: Since dictionaries are implemented using a hash table, keys must be hashable. This means that the hash value of a key must remain constant throughout the lifetime of the dictionary. Immutable data types like strings and numbers are hashable, while mutable data types like lists and dictionaries are not.

# In addition to these properties, it's important to note that dictionary keys are case-sensitive. This means that 'Name' and 'name' would be considered two different keys in a dictionary.

# Here's an example that demonstrates these properties:

# Valid dictionary with string keys
my_dict = {
	'name': 'John',
	'age': 30
}

# Invalid dictionary with mutable keys
invalid_dict = {
	['name']: 'John',
	['age']: 30
}

# Raises TypeError: unhashable type: 'list'

# Invalid dictionary with non-unique keys
invalid_dict = {
	'name': 'John',
	'name': 'Jane'
}

# Second value overwrites first value

# Valid dictionary with integer keys
valid_dict = {
	1: 'John',
	2: 'Jane'
}

# Uncommon way to create dictionary
user = dict(name='John doe')
