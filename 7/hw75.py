def outer(a, b):

    def inner():
        nonlocal a, b
        return a + b

    return inner() + 5


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(outer(a, b))