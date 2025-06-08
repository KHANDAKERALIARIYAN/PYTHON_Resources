# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'ARIYAN'
age = 21

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings 
print(f'Hello, my name is {name} and I am {age}')

# String Methods

fullname=" Khandaker Ali Ariyan "

# Capitalize string
print(fullname.capitalize())

# Make all uppercase
print(fullname.upper())

# Make all lower
print(fullname.lower())

# Swap case
print(fullname.swapcase())

# Get length
print(len(fullname))

# Replace
print(fullname.replace('Ariyan', 'Samir'))

# Count
sub = 'a'
print(fullname.count(sub))

# Starts with
print(fullname.startswith('Khandaker'))

# Ends with
print(fullname.endswith(' '))

# Split into a list
print(fullname.split())

# Find position
print(fullname.find('r'))

# Is all alphanumeric
print(fullname.isalnum())

# Is all alphabetic
print(fullname.isalpha())

# Is all numeric
print(fullname.isnumeric())
