# Set Methods

my_set = {1,2,3,4,5}

# add()
my_set.add(6)
print(my_set)

# clear()
my_set.clear()
print(my_set)

my_set = {1,2,3,4,5}
# copy()
new_set = my_set.copy()
print(new_set)

new_set.clear()
print(new_set)
print(my_set)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# difference()
difference = set1.difference(set2)
print(difference)

# difference_update()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.difference_update(set2)
print(set1)

# discard()
my_set = {1, 2, 3, 4, 5}

my_set.discard(3)
print(my_set)

# intersection()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection_set = set1.intersection(set2)
print(intersection_set)

# intersection_update()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.intersection_update(set2)
print(set1)

# isdisjoint()
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set3 = {4, 5, 11, 12, 13}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))


# issubset()
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5}

print(set1.issubset(set2))
print(set1.issubset(set3))

# issuperset()
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
set3 = {4, 5}

print(set1.issuperset(set2))
print(set1.issuperset(set3))


# pop()
my_set = {1, 2, 3, 4, 5}

removed_element = my_set.pop()
print(removed_element)
print(my_set)

# remove()
my_set = {1, 2, 3, 4, 5}

my_set.remove(3)
print(my_set)

# symmetric_difference()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)


# symmetric_difference_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.symmetric_difference_update(set2)
print(set1)

# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

union_set = set1.union(set2, set3)
print(union_set)

# update()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

set1.update(set2, set3)
print(set1)

