def factorial(number: int) -> int:
    print("For loop")
    result = 1
    for i in range(2, number+1):
        result *= i

    return result


def fact(number: int) -> int:
    print("While...")
    result = 1  # 120
    while number >= 2:
        result *= number
        number -= 1

    return result


n = int(input("Number:"))
print(factorial(n))
print(fact(n))
