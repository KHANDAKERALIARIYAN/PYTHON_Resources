# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Creating a sample tuple
my_tuple = (10, 20, 30, 40, 20, 10)

# count(): returns number of occurrences of a value
print("Count of 20:", my_tuple.count(20))  # Output: 2

# index(): returns first index of a value
print("Index of 30:", my_tuple.index(30))  # Output: 2

# Slicing: extract part of the tuple
print("Sliced tuple [1:4]:", my_tuple[1:4])  # Output: (20, 30, 40)

# Length of tuple
print("Length:", len(my_tuple))  # Output: 6

# Membership test
print("Is 40 in tuple?", 40 in my_tuple)  # Output: True

# Iterating through tuple
print("Tuple elements:")
for item in my_tuple:
    print(item)

# Unpacking tuple
a, b, c = (1, 2, 3)
print("Unpacked values:", a, b, c)

# Concatenation of tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("Concatenated tuple:", t3)  # Output: (1, 2, 3, 4)

# Tuple repetition
t4 = ("A",) * 3
print("Repeated tuple:", t4)  # Output: ('A', 'A', 'A')

# Nested tuples
nested = (1, (2, 3), 4)
print("Access nested tuple:", nested[1][0])  # Output: 2

# Tuple with different data types
mixed = (1, "Hello", 3.14, True)
print("Mixed data types:", mixed)

# Using tuple() to convert list to tuple
my_list = [100, 200, 300]
converted_tuple = tuple(my_list)
print("Converted from list:", converted_tuple)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

# print(fruits_set)

# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# add(): Add a single element
set1.add(10)
print("After add(10):", set1)

# update(): Add multiple elements
set1.update([11, 12])
print("After update([11, 12]):", set1)

# remove(): Remove specific element (raises error if not found)
set1.remove(2)
print("After remove(2):", set1)

# discard(): Remove element (no error if not found)
set1.discard(100)  # No error
print("After discard(100):", set1)

# pop(): Remove and return an arbitrary element
popped = set1.pop()
print("Popped element:", popped)
print("After pop():", set1)

# clear(): Remove all elements
temp_set = set1.copy()
temp_set.clear()
print("After clear():", temp_set)

# copy(): Create a shallow copy
copy_set = set1.copy()
print("Copy of set1:", copy_set)

# union(): Elements from both sets
print("Union:", set1.union(set2))  # or set1 | set2

# intersection(): Common elements
print("Intersection:", set1.intersection(set2))  # or set1 & set2

# difference(): Elements in set1 but not in set2
print("Difference:", set1.difference(set2))  # or set1 - set2

# symmetric_difference(): Elements in either set but not both
print("Symmetric Difference:", set1.symmetric_difference(set2))  # or set1 ^ set2

# isdisjoint(): True if sets have no elements in common
print("Is Disjoint?", set1.isdisjoint({100, 200}))  # True

# issubset(): True if set1 is subset of set2
print("Is Subset?", {1, 2}.issubset(set1))

# issuperset(): True if set1 is superset of set2
print("Is Superset?", set1.issuperset({1, 3}))

# Membership Test
print("Is 3 in set1?", 3 in set1)

# Creating a set from a list
list_data = [1, 2, 2, 3]
unique_set = set(list_data)
print("Unique elements from list:", unique_set)

# Set comprehension
squares = {x * x for x in range(5)}
print("Set comprehension:", squares)
