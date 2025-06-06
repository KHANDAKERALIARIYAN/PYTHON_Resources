# Comments

# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# Variables

a = 5 # integer
b = 3.14 # float
c = "Hello, World!" # string
d = True # boolean
e = None # NoneType (no value)

print(a , type(a))
print(b , type(b))
print(c , type(c))
print(d , type(d))
print(e , type(e))

# Basic math - operator 

# Arithmatic operators
print("Arithmatic Operators : ")
a1=10
a2=2
print(" a1 + a2 = ",a1+a2)
print(" a1 - a2 = ",a1-a2)
print(" a1 * a2 = ",a1*a2)
print(" a1 / a2 = ",a1/a2)
print(" a1 % a2 = ",a1%a2)
print(" a1 ** a2 = ",a1**a2)
print(" a1 // a2 = ",a1//a2)

# Assignment operators
print("Assignment Operators : ")
a = 10
print("a =", a) # Assigns 10 to a
a += 5 # Adds 5 to a
print("a after += 5:", a) # Now a is 15
a -= 3 # Subtracts 3 from a
print("a after -= 3:", a) # Now a is 12
a *= 2 # Multiplies a by 2
print("a after *= 2:", a) # Now a is 24
a /= 4 # Divides a by 4
print("a after /= 4:", a) # Now a is 6.0
a %= 2 # Modulus of a by 2
print("a after %= 2:", a) # Now a is 0.0
a **= 3 # Raises a to the power of 3
print("a after **= 3:", a) # Now a is 0.0
a //= 1 # Floor division of a by 1
print("a after //= 1:", a) # Now a is 0.0

# Comparison operators
print("Comparison Operators : ")
a1=10
a2=20
print(" a1 == a2 = ",a1==a2)
print(" a1 != a2 = ",a1!=a2)
print(" a1 > a2 = ",a1>a2)
print(" a1 < a2 = ",a1<a2)
print(" a1 >= a2 = ",a1>= a2)
print(" a1 <= a2 = ",a1<= a2) 

# Logical operators
print("Logical Operators : ")

print("\n OR Gate Truth Table : ")
print("False OR False = ", False or False)
print("False OR True = ", False or True)
print("True OR False = ", True or False)
print("True OR True = ", True or True)

print("\n AND Gate Truth Table : ")
print("False AND False = ", False and False)
print("False AND True = ", False and True)
print("True AND False = ", True and False)
print("True AND True = ", True and True)

print("\n NOT Gate Truth Table : ")
print("NOT False = ", not False)
print("NOT True = ", not True)

# casting
x1=10
x2=10.89
x1=float(x1)
print(x1)
x2=int(x2)
print(x2)