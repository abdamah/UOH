# ==========================================
# CHAPTER 5: EXCEPTION HANDLING & MODULES
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

'''try:
import mymodule
import math as m
from math import sqrt
import math
x = int(input("Enter a number: "))
print(10 / x)
except:
    print("An error occurred")

'''
# ------------------------------------------
# 1.2 SPECIFIC EXCEPTIONS
# ------------------------------------------

"""
Handling specific errors is better practice.
"""

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

"""
else runs if NO exception occurs
"""

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

"""
finally ALWAYS runs (error or not)
"""

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

"""
raise is used to create your own error
"""

age = int(input("Enter age: "))

if age < 18:
    raise Exception("You must be 18 or older")


# ==========================================
# 2) MODULES
# ==========================================

"""
Definition:
A module is a file containing Python code (functions, variables).

Used to organize code and promote reuse.
"""


# ------------------------------------------
# 2.1 IMPORT MODULE
# ------------------------------------------


print(math.sqrt(16))


# ------------------------------------------
# 2.2 IMPORT SPECIFIC FUNCTION
# ------------------------------------------


print(sqrt(25))


# ------------------------------------------
# 2.3 IMPORT WITH ALIAS
# ------------------------------------------


print(m.pi)


# ------------------------------------------
# 2.4 CREATE YOUR OWN MODULE
# ------------------------------------------

"""
Create file: mymodule.py
"""

# mymodule.py


def greet(name):
    return "Hello " + name


# main file

print(mymodule.greet("Ali"))


# ------------------------------------------
# 2.5 __name__ VARIABLE
# ------------------------------------------

"""
__name__ == "__main__" ensures code runs only
when file is executed directly
"""


def test():
    print("Running test function")


if __name__ == "__main__":
    test()


# ==========================================
# 3) SIMPLE PROJECT: SAFE CALCULATOR
# ==========================================

"""
Project:
Calculator using exception handling
"""

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
# 4) SUMMARY
# ==========================================

"""
Exception Handling:
- try → test code
- except → handle error
- else → runs if no error
- finally → always runs
- raise → custom error

Modules:
- import module
- from module import function
- alias (as)
- custom modules
- __name__ == "__main__"

Project:
✔ Safe Calculator
"""
