# ==========================================
# Chapter 2: PYTHON BASIC NOTES
# ==========================================

# ==========================================
# 1) FIRST PROGRAM
# ==========================================

"""
Definition:
The first Python program usually uses print() 
to display a message on the screen.
"""

# Example:
print("Hello, World!")


# ==========================================
# 2) PYTHON EXECUTION PROCESS
# ==========================================

"""
Definition:
Python is an interpreted language.

Execution Steps:
1. Write source code (.py file)
2. Python Interpreter reads the code
3. Converts the code into Bytecode (.pyc)
4. Python Virtual Machine (PVM) executes the bytecode
5. Output is displayed
"""

# Example:
print("Python execution example")


# ==========================================
# 3) COMMENTS
# ==========================================

"""
Definition:
A comment is a piece of text in the code that is ignored by the Python interpreter.
Comments are used to explain code, improve readability, and provide documentation.
"""

# Single-line Comment
# This is a single-line comment
print("Single-line comment example")

# Multi-line Comment using #
# This is line 1 of multi-line comment
# This is line 2
# This is line 3
print("Multi-line comment using #")

# Docstring (official documentation)
"""
This is a docstring.
It can span multiple lines.
Used for documentation of modules, classes, or functions.
"""


def greet():
    """This function prints a greeting message"""
    print("Hello from function!")


greet()


# ==========================================
# 4) DATA TYPES
# ==========================================

"""
Definition:
A data type defines the type of value a variable can store.
Python automatically detects the data type.
"""

# Examples of basic data types
name = "Abdallah"       # string data type (text)
age = 25                # integer data type (whole number)
fee = 25.99             # float data type (decimal number)
is_admin = True         # boolean data type (True or False)
complex_number = 3 + 4j  # complex data type (real + imaginary)

# Print values
print("Name:", name)
print("Age:", age)
print("Fee:", fee)
print("Is Admin:", is_admin)
print("Complex Number:", complex_number)

# Print data types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of fee:", type(fee))
print("Type of is_admin:", type(is_admin))
print("Type of complex_number:", type(complex_number))


# ==========================================
# 5) VARIABLES
# ==========================================

"""
Definition:
A variable is a container used to store data.
The value of a variable can change during program execution.
"""

# Examples
x = 10
y = 5
print("x:", x)
print("y:", y)

# Variable reassignment
x = 20
print("New x:", x)

# Rules:
# - Must start with letter or underscore
# - No spaces allowed
# - Case-sensitive (Name != name)
_name = "Ali"  # valid
# 1name = "Ali" # invalid


# ==========================================
# 6) OPERATORS
# ==========================================

"""
Definition:
Operators are symbols used to perform operations on variables and values.
"""

a = 10
b = 3

# Arithmetic Operators
print("Addition (+):", a + b)         # adds two numbers
print("Subtraction (-):", a - b)      # subtracts one number from another
print("Multiplication (*):", a * b)   # multiplies two numbers
print("Division (/):", a / b)         # normal division (float)
print("Floor Division (//):", a // b)  # integer division (removes decimal)
print("Modulus (%):", a % b)          # remainder of division
print("Power (**):", a ** b)          # a to the power b

# Comparison Operators
print("Equal (==):", a == b)          # checks equality
print("Greater than (>):", a > b)     # checks if left is greater
print("Less than (<):", a < b)        # checks if left is smaller


# ==========================================
# 7) IMPORTANT NOTES
# ==========================================

"""
- Everything in Python is an object.
- type() shows the type of object:
    <class 'str'>, <class 'int'>, <class 'float'>, <class 'bool'>, <class 'complex'>, <class 'NoneType'>
- Comments help explain code and improve readability.
- Variables store values that can change.
- Operators perform operations on values.
"""
