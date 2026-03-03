# ==========================================
# CHAPTER 3: CONDITIONAL AND LOOPING STATEMENTS
# ==========================================


# ==========================================
# 1) CONDITIONAL STATEMENTS
# ==========================================

"""
Definition:
Conditional statements are used to make decisions in a program.
They execute certain blocks of code based on conditions.
"""

# ------------------------------------------
# 1.1 IF Statement
# ------------------------------------------

"""
Definition:
The if statement executes a block of code 
only if the condition is True.
"""

age = 18

if age >= 18:
    print("You are eligible to vote.")


# ------------------------------------------
# 1.2 IF-ELSE Statement
# ------------------------------------------

"""
Definition:
if-else executes one block if condition is True,
otherwise it executes another block.
"""

number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ------------------------------------------
# 1.3 IF-ELIF-ELSE Statement
# ------------------------------------------

"""
Definition:
Used when there are multiple conditions.
Python checks conditions from top to bottom.
"""

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ------------------------------------------
# 1.4 Nested IF
# ------------------------------------------

"""
Definition:
An if statement inside another if statement.
"""

num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")


# ==========================================
# 2) LOOPING STATEMENTS
# ==========================================

"""
Definition:
Loops are used to execute a block of code repeatedly.
"""

# ------------------------------------------
# 2.1 FOR Loop
# ------------------------------------------

"""
Definition:
Used to iterate over a sequence 
(list, tuple, string, range, etc.)
"""

# Example 1: Using range()
for i in range(5):
    print("Value:", i)

# Example 2: Loop through string
for letter in "Python":
    print(letter)


# ------------------------------------------
# 2.2 WHILE Loop
# ------------------------------------------

"""
Definition:
Executes a block of code as long as the condition is True.
"""

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# ------------------------------------------
# 2.3 BREAK Statement
# ------------------------------------------

"""
Definition:
Break is used to exit the loop immediately.
"""

for i in range(10):
    if i == 5:
        break
    print(i)


# ------------------------------------------
# 2.4 CONTINUE Statement
# ------------------------------------------

"""
Definition:
Continue skips the current iteration 
and moves to the next iteration.
"""

for i in range(5):
    if i == 2:
        continue
    print(i)


# ------------------------------------------
# 2.5 PASS Statement
# ------------------------------------------

"""
Definition:
Pass is a null statement.
It does nothing and is used as a placeholder.
"""

for i in range(3):
    pass


# ==========================================
# 3) SUMMARY
# ==========================================

"""
Conditional Statements:
- if
- if-else
- if-elif-else
- nested if

Looping Statements:
- for loop
- while loop
- break
- continue
- pass

Conditionals are used for decision-making.
Loops are used for repetition.
"""


# ==========================================================
# 0) READING INPUT FROM USER
# ==========================================================


# Example:
name = input("Enter your name: ")
print("Hello", name)

# Example with type casting:
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)


# ==========================================================
# SIMPLE PROJECT 1: STUDENT GRADE SYSTEM
# ==========================================================

"""
Project:
Take student marks as input and print grade.
"""

marks = int(input("Enter student marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# ==========================================================
# SIMPLE PROJECT 2: FIZZBUZZ (1 TO 100)
# ==========================================================

"""
Project:
Print numbers from 1 to 100
If divisible by 3 → Fizz
If divisible by 5 → Buzz
If divisible by both → FizzBuzz
"""

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ==========================================================
# SIMPLE PROJECT 3: GUESS THE SECRET NUMBER GAME
# ==========================================================

"""
Project:
User must guess the secret number.
Loop continues until correct guess.
"""

secret_number = 7
guess = 0

while guess != secret_number:

    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("Congratulations! You guessed it right!")
    else:
        print("Wrong guess. Try again!")


# ==========================================================
# 4) LOOP CONTROL STATEMENTS
# ==========================================================

"""
break    → stops the loop completely
continue → skips current iteration
pass     → does nothing (placeholder)
"""

# break example
for i in range(10):
    if i == 5:
        break
    print(i)

# continue example
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass example
for i in range(3):
    pass


# ==========================================================
# SUMMARY
# ==========================================================

"""
1) input() is used to read data from user.
2) if-elif-else is used for decision-making.
3) for loop is used for iteration.
4) while loop runs until condition becomes False.
5) break, continue, pass control loop behavior.

Projects Included:
✔ Student Grade System
✔ FizzBuzz (1–100)
✔ Guess the Secret Number Game
"""
