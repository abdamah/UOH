# Chapter 3
# Simple App: Track Unique Visitors

# Step 1: Initialize an empty set to store usernames
visitors = set()

# Step 2: Create a loop to interact with the user
while True:
    print("\nMenu:")
    print("1. Add a visitor")
    print("2. View all unique visitors")
    print("3. Exit")

    # Step 3: Take user input for menu choice
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == "1":
        # Add a visitor
        username = input("Enter the visitor's username: ").strip()
        if username:
            visitors.add(username)  # Add the username to the set
            print(f"Visitor '{username}' added.")
        else:
            print("Invalid username. Please try again.")
    elif choice == "2":
        # View all unique visitors
        print("Unique Visitors:")
        if visitors:
            for index, visitor in enumerate(visitors):
                print(f"{index + 1}:{visitor}")
            count += 1
        else:
            print("No visitors yet.")
    elif choice == "3":
        # Exit the app
        print("Exiting the app. Goodbye!")
        break
    else:
        # Invalid input
        print("Invalid choice. Please select 1, 2, or 3.")
