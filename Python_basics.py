# Print a string 
print("Hello, World!")
name = "Alice"        # String
age = 25              # Integer
height = 5.6          # Float
is_student = True     # Boolean
print(f"Hello {name}")

'''
Multi line 
comment
'''
x = int("5")      # Converts string to int
y = float("3.14") # Converts string to float
z = str(10)       # Converts int to string
# use type to print type of variable
print(type(x)) # class int
print(type(y)) # class float
print(type(z)) # class str

print(str.upper("adsgf"))
print(name.upper())

# conditional statememts
# age = 10; 
if age > 18:
    print("Adult")
elif age == 18:
    print("Just 18")
else:
    print("Minor")

print("For loop")
# for loop
for i in range(5):
    print(i)

print("while loop")
# while loop
i = 0
while i < 5:
    print(i)
    i += 1

def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

# List
fruits = ["apple", "banana", "mango"]
print(fruits[0])
fruits.append("orange")
print(fruits)

# tupple
point = (10, 20)
print(point)

# Dictionary (Key-Value)
person = {"name": "Alice", "age": 25}
print(person["name"])

# set
nums = {1, 2, 3, 1}
print(nums)  # {1, 2, 3}

# exception handling in python
try:
    x = int("abc")
except ValueError:
    print("Invalid input!")
finally:
    print("This always runs.")

# Writing to a file
with open("test.txt", "w") as f:
    f.write("Hello File!")

# Reading from a file
with open("test.txt", "r") as f:
    print(f.read())

import math
print(math.sqrt(16))

# best practise for the try catch anc caught all exception
try:
    print(greet("roach"))
except Exception as e:
    print(f"Something went wrong: {e}")


# | Feature    | List      | Tuple     | Set       |
# | ---------- | --------- | --------- | --------- |
# | Ordered    | ✅         | ✅        | ❌        |
# | Mutable    | ✅         | ❌        | ✅        |
# | Duplicates | ✅         | ✅        | ❌        |
# | Indexing   | ✅         | ✅        | ❌        |
# | Syntax     | [1,2,3]    | (1,2,3)  |  {1,2,3}  |





