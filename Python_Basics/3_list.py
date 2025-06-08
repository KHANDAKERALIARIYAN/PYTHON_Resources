# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5)) - previous version of Python

# print fruits
print(fruits)

# Get a value
print(fruits[1])

# Get the last value
print(fruits[-1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Change value
fruits[0] = 'Blueberries'
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)

# clear list
fruits.clear()
print(fruits)

# copy list
fruits_copy = fruits.copy()

print(fruits)