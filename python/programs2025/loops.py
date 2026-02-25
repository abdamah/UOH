# Chapter 3: # Python Loops and Iteration
# --------------------------
# Loops are used to execute a block of code repeatedly for a specified number of times
# or until a condition is met. Python provides two main types of loops: `for` and `while`.

# Indentation is critical to define the block of code that belongs to the loop.

# Loop Examples
# -------------

# Example 1: `for` loop
# Used to iterate over a sequence (list, tuple, string, etc.)
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")  # Output: Number: 1, Number: 2, ...

# Example 2: `for` loop with `range()`
# The `range()` function generates a sequence of numbers
for i in range(5):  # Iterates from 0 to 4
    print(f"Index: {i}")  # Output: Index: 0, Index: 1, ...

# Example 3: `while` loop
# Repeats as long as a condition is true
count = 0
while count < 5:
    print(f"Count: {count}")  # Output: Count: 0, Count: 1, ...
    count += 1  # Increment the counter

# Example 4: Using `break` in a loop
# Exits the loop prematurely when a condition is met
for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break  # Stops the loop
    print(f"Value: {i}")  # Output: Value: 0, Value: 1, ...

# Example 5: Using `continue` in a loop
# Skips the rest of the loop body for the current iteration
for i in range(5):
    if i == 2:
        print("Skipping 2")
        continue  # Skip the iteration
    print(f"Value: {i}")  # Output: Value: 0, Value: 1, ...

# Example 6: Nested loops
# Loops inside loops are used for multidimensional iterations
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Output:
# i: 0, j: 0
# i: 0, j: 1
# i: 1, j: 0
# ...

# Example 7: `else` clause in loops
# Executes after the loop ends, unless it is terminated by `break`
for i in range(3):
    print(f"Processing {i}")
else:
    print("Loop finished!")  # Output: Loop finished!

# Example 8: Infinite loop (use with caution!)
# A `while` loop that runs indefinitely until a `break` condition is met
# count = 0
# while True:
#     print(f"Infinite count: {count}")
#     count += 1
#     if count == 5:
#         break  # Stops the infinite loop

# Note: Uncomment the above block to test the infinite loop with a `break`.

# Example 9: Looping through a tuple
# Tuples are immutable sequences of elements
colors = ("red", "green", "blue")
for color in colors:
    print(f"Color: {color}")
# Output:
# Color: red
# Color: green
# Color: blue

# Using `enumerate()` to get the index and value
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")
# Output:
# Index: 0, Color: red
# Index: 1, Color: green
# Index: 2, Color: blue

# Example 10: Looping through a dictionary
# Dictionaries store key-value pairs, and you can loop through keys, values, or both
person = {"name": "Abdallah", "age": 23, "city": "Hargeisa"}

# Loop through keys
for key in person:
    print(f"Key: {key}, Value: {person[key]}")
# Output:
# Key: name, Value: Abdallah
# Key: age, Value: 23
# Key: city, Value: Hargeisa

# Loop through keys and values using `items()`
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Abdallah
# age: 23
# city: Hargeisa

# Example 11: Looping through a set
# Sets are unordered collections of unique elements
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(f"Fruit: {fruit}")
# Output:
# Fruit: apple
# Fruit: banana
# Fruit: cherry
# (Order may vary as sets are unordered)
