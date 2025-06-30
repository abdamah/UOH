from atm_abstract import ATM


class ATMImpl(ATM):
    def __init__(self):
        self.__balance = 0

    def check_balance(self):
        return f'Balance: ${self.__balance}'

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insuffient Fun!")
        self.__balance -= amount
