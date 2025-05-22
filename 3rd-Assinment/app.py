
# Lesson 05: Control Flow & Loops

# IF-ELSE Example
age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ELIF Example
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
else:
    print("Grade: B")

# FOR LOOP Example
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# WHILE LOOP Example
print("Countdown from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1
 
 
# Lesson 06: Lists, Tuples & Dictionary

# LIST Example
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print("Fruits List:", fruits)

# Accessing elements
print("First fruit:", fruits[0])

# TUPLE Example
colors = ("red", "green", "blue")
print("Tuple of Colors:", colors)
print("Second color:", colors[1])

# DICTIONARY Example
student = {
    "name": "Ali",
    "age": 21,
    "course": "Python"
}
print("Student Info:", student)
print("Student Name:", student["name"])

# Adding a new key
student["grade"] = "A"
print("Updated Info:", student)
 
# Lesson 07: Set & Frozenset

# SET Example
numbers = {1, 2, 3, 4}
numbers.add(5)
numbers.add(3)  # No duplicates
print("Set:", numbers)

# Removing element
numbers.discard(2)
print("After Discard:", numbers)

# FROZENSET Example
frozen = frozenset(["apple", "banana", "cherry"])
print("Frozenset:", frozen)
 
 

