# Chapter 3
# Note: Mixing tabs and spaces in the same block will raise an IndentationError.

# Conditional Statements Examples
# -------------------------------

# Example 1: Simple `if` statement
# Checks a condition and executes the code block if true
age = 18
if age >= 18:
    print("You are eligible to vote.")  # Output: You are eligible to vote.

# Example 2: `if-else` statement
# Provides an alternate code block to execute when the condition is false
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    # Output: You are not eligible to vote.
    print("You are not eligible to vote.")

# Example 3: `if-elif-else` statement
# Checks multiple conditions in sequence and executes the first matching block
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")  # Output: Grade: B
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Example 4: Nested `if` statement
# An `if` statement inside another `if` to check multiple levels of conditions
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("You are eligible to vote.")  # Output: You are eligible to vote.
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not old enough to vote.")

# Example 5: Conditional expression (Ternary Operator)
# A compact way to write an `if-else` statement
age = 17
message = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(message)  # Output: Not eligible to vote
