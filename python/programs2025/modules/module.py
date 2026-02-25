# Modules in Python
# A module in Python is a file containing Python definitions and statements.
# Modules allow you to organize code by grouping related functionality together,
# making it easier to maintain, reuse, and understand.

# Benefits of Using Modules:
# - Code Reusability: Write a function or class once and reuse it across multiple programs.
# - Code Organization: Group related functionalities together for better readability.
# - Namespace Management: Avoid conflicts between identifiers by encapsulating them within modules.

# Example: Basic Module (calculation.py)
# Create a file named calculation.py that contains basic functions for addition, subtraction, multiplication, and division.

# Calculation functions

from calculation import *
import calculation as calc
from calculation import multiply, divide
import calculation  # Assuming these functions are in a separate file named `calculation.py`


def add(a, b):
    """Adds two numbers."""
    return a + b


def subtract(a, b):
    """Subtracts the second number from the first."""
    return a - b


def multiply(a, b):
    """Multiplies two numbers."""
    return a * b


def divide(a, b):
    """Divides the first number by the second. Raises an error for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Main Program: Demonstrating different ways to use the calculation functions


# 1. Import the entire module
# Recommended: Keeps namespace explicit, avoids conflicts.

print("1. Import the entire module:")
print("Addition:", calculation.add(5, 3))
print("Subtraction:", calculation.subtract(5, 3))

# 2. Import specific functions
# Recommended: Import only needed functions to improve clarity.

print("\n2. Import specific functions:")
print("Multiplication:", multiply(5, 3))
print("Division:", divide(5, 3))

# 3. Import with an alias
# Recommended: Simplifies long module names and improves readability.

print("\n3. Import with an alias:")
print("Addition using alias:", calc.add(10, 4))
print("Subtraction using alias:", calc.subtract(10, 4))

# 4. Import all functions
# Not Recommended: Can cause namespace pollution and conflicts.

print("\n4. Import all functions:")
print("Multiplication using wildcard import:", multiply(6, 2))
print("Division using wildcard import:", divide(6, 2))
