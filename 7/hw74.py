def StepTwo(n, power=0):

    if 2 ** power == n:
        return "Yes"
    elif 2 ** power > n:
        return "No"
    power += 1
    return StepTwo(n, power)

num = int(input("Введите число: "))

print(StepTwo(num))