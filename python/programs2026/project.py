# ==========================================================
# ATM PROJECT - ALL VERSIONS
# ==========================================================


# ==========================================================
# VERSION 1: NORMAL (BASIC)
# ==========================================================

def atm_basic():
    balance = 1000

    while True:
        print("\n===== ATM V1 MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = int(input("Enter amount: "))
            balance += amount
            print("Deposited:", amount)

        elif choice == "2":
            amount = int(input("Enter amount: "))
            if amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print("Withdrawn:", amount)

        elif choice == "3":
            print("Balance:", balance)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


# ==========================================================
# VERSION 2: FUNCTIONS
# ==========================================================

def deposit(balance, amount):
    if amount <= 0:
        print("Amount must be positive")
        return balance
    balance += amount
    print("Deposited:", amount)
    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("Amount must be positive")
        return balance
    if amount > balance:
        print("Insufficient balance")
        return balance
    balance -= amount
    print("Withdrawn:", amount)
    return balance


def check_balance(balance):
    print("Balance:", balance)


def atm_functions():
    balance = 1000

    while True:
        print("\n===== ATM V2 MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            balance = deposit(balance, amount)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            balance = withdraw(balance, amount)

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


# ==========================================================
# VERSION 3: OOP
# ==========================================================

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Balance:", self.balance)


def atm_oop():
    atm = ATM(1000)

    while True:
        print("\n===== ATM V3 MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            atm.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            atm.withdraw(amount)

        elif choice == "3":
            atm.check_balance()

        elif choice == "4":
            break

        else:
            print("Invalid choice")


# ==========================================================
# VERSION 4-A: FUNCTIONS + EXCEPTION HANDLING
# ==========================================================

def deposit_safe(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    balance += amount
    print("Deposited:", amount)
    return balance


def withdraw_safe(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise Exception("Insufficient balance")
    balance -= amount
    print("Withdrawn:", amount)
    return balance


def atm_safe_functions():
    balance = 1000

    while True:
        print("\n===== ATM V4-A MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        try:
            choice = input("Enter choice: ")

            if choice == "1":
                amount = float(input("Enter amount: "))
                balance = deposit_safe(balance, amount)

            elif choice == "2":
                amount = float(input("Enter amount: "))
                balance = withdraw_safe(balance, amount)

            elif choice == "3":
                print("Balance:", balance)

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except ValueError as ve:
            print("Error:", ve)

        except Exception as e:
            print("Error:", e)

        finally:
            print("Transaction complete\n")


# ==========================================================
# VERSION 4-B: OOP + EXCEPTION HANDLING
# ==========================================================

class SafeATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise Exception("Insufficient balance")
        self.balance -= amount
        print("Withdrawn:", amount)

    def check_balance(self):
        print("Balance:", self.balance)


def atm_safe_oop():
    atm = SafeATM(1000)

    while True:
        print("\n===== ATM V4-B MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        try:
            choice = input("Enter choice: ")

            if choice == "1":
                amount = float(input("Enter amount: "))
                atm.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter amount: "))
                atm.withdraw(amount)

            elif choice == "3":
                atm.check_balance()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except ValueError as ve:
            print("Error:", ve)

        except Exception as e:
            print("Error:", e)

        finally:
            print("Transaction complete\n")


# ==========================================================
# MAIN MENU (SELECT VERSION)
# ==========================================================

def main():
    while True:
        print("\n========= SELECT ATM VERSION =========")
        print("1. Basic")
        print("2. Functions")
        print("3. OOP")
        print("4. Functions + Exception")
        print("5. OOP + Exception")
        print("6. Exit")

        choice = input("Choose version: ")

        if choice == "1":
            atm_basic()
        elif choice == "2":
            atm_functions()
        elif choice == "3":
            atm_oop()
        elif choice == "4":
            atm_safe_functions()
        elif choice == "5":
            atm_safe_oop()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    main()
