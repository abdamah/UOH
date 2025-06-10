def add(*args, a=3):
    s = 0
    for i in args:
        s += i

    s += a

    return s


print(add())
print(add(1, 2, 4, a=3))
