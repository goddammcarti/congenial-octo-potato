def Fibonacce(count = 10, lastnum = 0, num = 1):
    print(lastnum, end=", ")
    count -= 1
    if count <= 0:
        return
    Fibonacce(count, num, lastnum + num )

count = int(input("Введите длину последовательности: "))
Fibonacce(count)