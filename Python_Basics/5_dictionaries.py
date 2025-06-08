# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# get(): Safely get a value
print("Name:", my_dict.get("name"))  # Output: Alice
print("Country (with default):", my_dict.get("country", "USA"))  # Output: USA

# keys(): Get all keys
print("Keys:", list(my_dict.keys()))

# values(): Get all values
print("Values:", list(my_dict.values()))

# items(): Get all key-value pairs
print("Items:", list(my_dict.items()))

# update(): Add or update multiple key-value pairs
my_dict.update({"age": 26, "country": "USA"})
print("After update:", my_dict)

# pop(): Remove key and return value
age = my_dict.pop("age")
print("Popped 'age':", age)
print("After pop:", my_dict)

# popitem(): Remove and return the last inserted key-value pair
last_item = my_dict.popitem()
print("Last item popped:", last_item)
print("After popitem:", my_dict)

# setdefault(): Get value if key exists, else insert with default
language = my_dict.setdefault("language", "English")
print("Set default language:", language)
print("After setdefault:", my_dict)

# copy(): Make a shallow copy
copy_dict = my_dict.copy()
print("Copied dict:", copy_dict)

# clear(): Remove all items
temp = copy_dict.copy()
temp.clear()
print("After clear:", temp)

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
print("Dictionary comprehension:", squared)

# Membership test
print("Is 'name' a key?", 'name' in my_dict)
print("Is 'Alice' a value?", 'Alice' in my_dict.values())

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])