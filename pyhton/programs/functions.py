# Chapter 4

# Functions in Python

# 1. What is a Function?
# A function is a reusable block of code designed to perform a specific task.

# 2. Defining a Function
def greet():
    """This is a simple function to print a greeting message."""
    print("Hello, welcome to Python!")


# 3. Calling a Function
greet()  # Output: Hello, welcome to Python!

# 4. Function with Parameters


def greet_person(name):
    """Greets a person by their name."""
    print(f"Hello, {name}! Welcome to Python.")


greet_person("Abdallah")  # Output: Hello, Abdallah! Welcome to Python.

# 5. Function with a Return Value


def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


result = add_numbers(5, 7)
print(result)  # Output: 12

# 6. Default Parameters


def greet_person(name="Guest"):
    """Greets a person. Defaults to 'Guest'."""
    print(f"Hello, {name}! Welcome.")


greet_person()  # Output: Hello, Guest! Welcome.
greet_person("Abdallah")  # Output: Hello, Abdallah! Welcome.

# 7. Keyword Arguments


def describe_person(name, age):
    """Describes a person."""
    print(f"{name} is {age} years old.")


describe_person(age=23, name="Abdallah")
# Output: Abdallah is 23 years old.

# 8. Variable-Length Arguments

# Using *args for Variable-Length Positional Arguments


def sum_numbers(*args):
    """Calculates the sum of all positional arguments."""
    print(f"Arguments received: {args}")
    return sum(args)


print(sum_numbers(10, 20, 30))  # Output: 60
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# Using **kwargs for Variable-Length Keyword Arguments


def describe_person(**kwargs):
    """Prints details about a person provided as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


describe_person(name="Abdallah", age=23, city="Hargeisa")
# Output:
# name: Abdallah
# age: 23
# city: Hargeisa

# 9. Positional-Only Arguments


def greet_person(first_name, /):
    """Greets a person using their first name."""
    print(f"Hello, {first_name}!")


greet_person("Abdallah")  # Output: Hello, Abdallah!

# 10. Keyword-Only Arguments


def greet_full_name(*, first_name, last_name):
    """Greets a person using their full name."""
    print(f"Hello, {first_name} {last_name}!")


# Output: Hello, Abdallah Mahmoud!
greet_full_name(first_name="Abdallah", last_name="Mahmoud")

# 11. Anonymous Functions (Lambda)


def add(x, y): return x + y


print(add(3, 5))  # Output: 8

# 12. Scopes: Global and Local
x = 10  # Global variable


def display_number():
    x = 5  # Local variable
    print("Inside function:", x)


display_number()  # Output: Inside function: 5
print("Outside function:", x)  # Output: Outside function: 10

# 13. Global Variable Examples
counter = 0


def increment_counter():
    """Increments the global counter by 1."""
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")


print(f"Counter before function call: {counter}")  # Output: 0
increment_counter()  # Output: Counter inside function: 1
print(f"Counter after function call: {counter}")  # Output: 1

# Example without global keyword


def increment_counter_without_global():
    try:
        counter += 1
        print(f"Counter inside function: {counter}")
    except UnboundLocalError as e:
        print(f"Error: {e}")


increment_counter_without_global()
# Output:
# Error: local variable 'counter' referenced before assignment

# 14. Docstrings


def square(num):
    """Returns the square of a number."""
    return num * num


help(square)

# 15. Example Program: Menu with Functions


def menu():
    """Displays a menu."""
    print("1. Add Numbers")
    print("2. Multiply Numbers")
    print("3. Exit")


def add_numbers(a, b):
    """Adds two numbers."""
    return a + b


def multiply_numbers(a, b):
    """Multiplies two numbers."""
    return a * b


while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", add_numbers(x, y))
    elif choice == 2:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", multiply_numbers(x, y))
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again!")
