# Exception Handling in Python

# Definition:
# Exception handling is used to manage errors that occur during the execution of a program.
# Python uses the try, except, else, and finally blocks to handle exceptions.

# Function to demonstrate exception handling
def divide_numbers(a, b):
    """
    Tries to divide a by b and handles exceptions such as division by zero or invalid types.
    """
    try:
        result = a / b  # Trying to divide the numbers
    except ZeroDivisionError as e:
        print(f"Error: {e}")  # Handle division by zero error
    except TypeError as e:
        # Handle type errors if non-numeric values are passed
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")  # This block runs if no exception occurred
    finally:
        print("Execution complete, whether there was an exception or not.")


# Example: Test the function with different inputs
print("Test 1: Dividing 10 by 2")
divide_numbers(10, 2)  # Expected output: Result: 5.0

print("\nTest 2: Dividing 10 by 0")
divide_numbers(10, 0)  # Expected output: Error: division by zero

print("\nTest 3: Dividing 10 by a string")
# Expected output: Error: unsupported operand type(s) for /: 'int' and 'str'
divide_numbers(10, 'a')


# Example of raising custom exceptions
def check_number(number):
    """
    Checks if the given number is negative or zero, raising exceptions accordingly.
    """
    try:
        if number < 0:
            raise ValueError("Number cannot be negative.")
        elif number == 0:
            raise ZeroDivisionError("Number cannot be zero.")
        else:
            print(f"Number is {number}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example: Checking a number
print("\nTest 4: Checking number -5")
check_number(-5)  # Output: ValueError: Number cannot be negative.

print("\nTest 5: Checking number 0")
check_number(0)   # Output: ZeroDivisionError: Number cannot be zero.

print("\nTest 6: Checking number 10")
check_number(10)  # Output: Number is 10


# Catching all exceptions using a generic 'except' block
try:
    # Code that might raise an exception
    x = 1 / 0
except Exception as e:  # Catch all exceptions
    print(f"An error occurred: {e}")


# Function to demonstrate raising an exception manually
def check_age(age):
    """
    Raises a ValueError if age is less than 18.
    """
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    else:
        print("Age is valid.")


# Example: Checking age of 15
print("\nTest 7: Checking age of 15")
try:
    check_age(15)
except ValueError as e:
    print(f"Error: {e}")

# Explanation of Blocks in Exception Handling:
"""
1. try: 
   - Code that might raise an exception is placed here.
   - If no exception occurs, the code runs normally.

2. except: 
   - Catches specific exceptions. 
   - You can have multiple except blocks to handle different types of errors.

3. else: 
   - Executes if no exception occurs in the try block.
   - Used for code that should run only when no errors are encountered.

4. finally: 
   - Always executes, regardless of whether an exception occurred or not.
   - Used for cleanup actions like closing files, releasing resources, etc.
"""

# Example of catching multiple exceptions


def divide_with_multiple_exceptions(a, b):
    """
    Demonstrates catching multiple types of exceptions.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Please provide numeric values.")
    else:
        print(f"Division successful, result is: {result}")
    finally:
        print("Division attempt finished.")


# Example: Testing the divide_with_multiple_exceptions function
print("\nTest 8: Dividing 10 by 2")
# Expected output: Division successful, result is: 5.0
divide_with_multiple_exceptions(10, 2)

print("\nTest 9: Dividing 10 by 0")
# Expected output: Cannot divide by zero.
divide_with_multiple_exceptions(10, 0)

print("\nTest 10: Dividing 10 by a string")
# Expected output: Please provide numeric values.
divide_with_multiple_exceptions(10, 'a')
