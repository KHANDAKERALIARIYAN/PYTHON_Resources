# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def hello():
    print("Hello, World!")
hello()

def greet(name):
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!

def sayHello(name='Sam'):
    print(f'Hello {name}')

sayHello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 3))

def calculate_avg(a,b,c):
    return (a + b + c) / 3

print(calculate_avg(10, 20, 30))  # Output: 20.