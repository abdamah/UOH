from atm_impl import ATMImpl


def main():
    atm = ATMImpl()
    atm.deposit(100)
    print(atm.check_balance())
    try:
        atm.withdraw(200)
    except ValueError as e:
        print(e)
    print(atm.check_balance())


if __name__ == '__main__':
    main()
