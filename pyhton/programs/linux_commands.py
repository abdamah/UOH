# Chapter 3

# Simple Project: Linux Command Dictionary

# Step 1: Create a dictionary of 5 Linux commands plus "unknown"
commands = {
    "ls": "List directory contents",
    "cd": "Change directory",
    "pwd": "Print working directory",
    "cp": "Copy files and directories",
    "mv": "Move or rename files and directories",
    "unknown": "Unknown command"  # Special keyword for unknown commands
}

# Step 2: Iteration over the dictionary by reading input from the user
while True:
    # Asking the user to input a Linux command
    command = input(
        "Enter a Linux command (or 'exit' to quit): ").strip().lower()

    # If the user types 'exit', break out of the loop
    if command == 'exit':
        print("Exiting the program.")
        break

    # Step 3: Use the `get()` method, defaulting to "unknown"
    description = commands.get(command, commands["unknown"])
    print(f"{command}: {description}")
