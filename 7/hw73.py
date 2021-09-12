import random

def multList(list2mult, i = 0):
    if(i == len(list2mult)):
        return 1
    i += 1
    return list2mult[i - 1] * multList(list2mult, i)

l = list()

for _ in range(5):
    l.append(random.randint(1, 20))

print(l)
print(multList(l))