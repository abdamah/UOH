balance = 0.0
while True:
    print("Welcome to the ATM")
    print("1. Check Balance\n2. Deposit\n3. Withdraw \n4. Exit")
    choice = int(input("Choice:"))

    if choice == 1:
        print(f"Your balance is: {balance}")
    elif choice == 2:
        deposit = float(input("Enter amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f"Your new balance is: {balance}")
        else:
            print("Invalid deposit amount.")
    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: "))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print(f"Your new balance is: {balance}")
        else:
            print("Invalid withdrawal amount.")
    elif choice == 4:
        print("Exiting ATM. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
