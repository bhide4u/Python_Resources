# Dictionary methods

my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

# clear()
my_dict.clear()
print(my_dict)

my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

# copy()
new_dict = my_dict.copy()
print(new_dict)

new_dict['name'] = "Mary"
print(my_dict)
print(new_dict)

# fromkeys()
keys = ['name', 'age', 'city']
value = 'Unknown'

my_dict = dict.fromkeys(keys, value)
print(my_dict)

# get()
my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

print(my_dict.get('name'))

#  items()
a,b,c = my_dict.items()
print(a)
print(b)
print(c)

# keys()
my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

a,b,c = my_dict.keys()
print(a)
print(b)
print(c)

# pop()
my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

my_dict.pop('age')
print(my_dict)

# popitem()
my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

my_dict.popitem()
print(my_dict)

# update()
original_dict = {'name': 'John', 'age': 30}
new_dict = {'city': 'New York', 'occupation': 'Engineer'}

original_dict.update(new_dict)
print(original_dict)

# values()
my_dict = {
	'name': 'John',
	'age': 30,
	'gender': 'male'
}

print(my_dict.values())