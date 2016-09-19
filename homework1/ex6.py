# coding=utf-8
x = input("Введите 6+ значное число:")
def bilet(n):
    if (n[0] + n[1] + n[2]) == (n[-1] + n[-2] + n[-3]):
        return "Счастливый"
    else:
        return "Обычный"
print(bilet(x))

