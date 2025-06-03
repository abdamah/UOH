secret = 7
max_attempts = 3
count = 0

print("Welcome to the Guess the Number game!")

while count < 3:
    print(f"Attempt {count + 1} of {max_attempts}")

    guess = int(input("Guess a number: "))
    count += 1
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        break
else:
    print("Sorry, you've used all your attempts. Better luck next time!")
