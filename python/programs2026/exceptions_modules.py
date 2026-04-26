# ==========================================
# CHAPTER 5: EXCEPTION HANDLING , MODULES & FILE HANDLING
# ==========================================


# ==========================================
# 1) EXCEPTION HANDLING
# ==========================================

"""
Definition:
Exceptions are runtime errors that occur during program execution.

Exception handling allows us to handle errors gracefully
without crashing the program.
"""


# ------------------------------------------
# 1.1 BASIC TRY-EXCEPT
# ------------------------------------------

try:
import mymodule
import math as m
from math import sqrt
import math
x = int(input("Enter a number: "))
print(10 / x)
except:
    print("An error occurred")


# ------------------------------------------
# 1.2 SPECIFIC EXCEPTIONS
# ------------------------------------------

try:
    num = int(input("Enter number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input (not a number)")


# ------------------------------------------
# 1.3 ELSE BLOCK
# ------------------------------------------

try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error")
else:
    print("Result:", result)


# ------------------------------------------
# 1.4 FINALLY BLOCK
# ------------------------------------------

try:
    file = open("test.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")


# ------------------------------------------
# 1.5 MULTIPLE EXCEPT IN ONE LINE
# ------------------------------------------

try:
    x = int(input("Enter number: "))
    print(10 / x)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")


# ------------------------------------------
# 1.6 CUSTOM EXCEPTION (raise)
# ------------------------------------------

age = int(input("Enter age: "))

if age < 18:
    raise Exception("You must be 18 or older")


# ==========================================
# 2) MODULES
# ==========================================

"""
Definition:
A module is a file containing Python code (functions, variables).
Used for code reuse and organization.
"""


print(math.sqrt(16))
print(sqrt(25))
print(m.pi)


# ------------------------------------------
# 2.4 CREATE YOUR OWN MODULE
# ------------------------------------------

"""
File: mymodule.py
"""


def greet(name):
    return "Hello " + name


print(mymodule.greet("Ali"))


# ------------------------------------------
# 2.5 __name__ VARIABLE
# ------------------------------------------

def test():
    print("Running test function")


if __name__ == "__main__":
    test()


# ==========================================
# 3) FILE HANDLING
# ==========================================

"""
Definition:
File handling is used to store and read data from files.
Modes:
- r → read
- w → write (overwrite)
- a → append
- x → create new file
"""


# ------------------------------------------
# 3.1 WRITE TO FILE
# ------------------------------------------

file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("File Handling Example")
file.close()


# ------------------------------------------
# 3.2 READ FILE
# ------------------------------------------

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


# ------------------------------------------
# 3.3 APPEND TO FILE
# ------------------------------------------

file = open("data.txt", "a")
file.write("\nNew line added")
file.close()


# ------------------------------------------
# 3.4 WITH STATEMENT (BEST PRACTICE)
# ------------------------------------------

"""
Automatically closes file after use
"""

with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# ------------------------------------------
# 3.5 READ LINE BY LINE
# ------------------------------------------

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


# ------------------------------------------
# 3.6 FILE HANDLING + EXCEPTION
# ------------------------------------------

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")


# ==========================================
# 4) SIMPLE PROJECT: SAFE CALCULATOR
# ==========================================

while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            print("Result:", num1 / num2)
        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid number input")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    finally:
        print("Operation completed\n")

    cont = input("Continue? (y/n): ")
    if cont.lower() != "y":
        break


# ==========================================
# 5) SUMMARY
# ==========================================

"""
Exception Handling:
- try, except, else, finally, raise

Modules:
- import module
- from module import function
- alias (as)
- custom modules
- __name__ == "__main__"

File Handling:
- r → read
- w → write
- a → append
- x → create
- with open() → best practice

Project:
✔ Safe Calculator
"""
