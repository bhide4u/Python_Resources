# List methods

my_list = [1, 2, 3, 4, "a", "b", "c"]

# append()
my_list.append("d")
print(my_list)

# copy()
# The copy() method of a list creates a shallow copy of the original list.

# The syntax of the copy() method is as follows:
# 	new_list = original_list.copy()

# Here, original_list is the list that you want to copy, and new_list is the new list that will contain a copy of the elements in original_list.

# A shallow copy means that a new list object is created, but the elements of the new list are still references to the same objects as the elements in the original list. 
# If any of the elements in the original list are mutable objects, such as lists or dictionaries, changes made to those objects in the new list will affect the objects in the original list.

# Here is an example that demonstrates the use of the copy() method:
original_list = [1, 2, [3, 4]]
new_list = original_list.copy()

# Modify an element in the new list
new_list[0] = 5

# Modify an element in a nested list
new_list[2][0] = 6

print(original_list) # Output: [1, 2, [6, 4]]
print(new_list) # Output: [5, 2, [6, 4]]

# Another example
new_list = my_list.copy()
print(new_list)

my_list.clear()
print(new_list)

new_list.clear()
print(new_list)

# clear()
my_list.clear()
print(my_list)

# count()
my_list = [1, 2, 3, 4, "a", "b", "c", "b"]
print(my_list.count("b"))

# extend()
my_list = [1, 2, 3, 4]
other_list = ["a", "b", "c", "b"]

my_list.extend(other_list)
print(my_list)

# index()
print(my_list.index("b"))

# insert()
my_list = [1, 2, 3, 4]
my_list.insert(3, "a")
print(my_list)

# pop()
popped_element = my_list.pop()
print(popped_element)

popped_element = my_list.pop(0)
print(my_list)

# remove()
my_list = [1, 2, 3, 4, "a", "b", "c", "b"]
my_list.remove(3)
print(my_list)

# reverse()
my_list = [1, 2, 3, 4, "a", "b", "c", "b"]
my_list.reverse()
print(my_list)

# sort()
my_list = ["a", "z", "b", "c", "Z", "b"]
my_list.sort()
print(my_list)
