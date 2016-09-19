# coding=utf-8
number = int(input("Введите целое положительное число: "))
def FIB(x):
    a = 0
    b = 1
    counter = 2
    if number <= 0:
        return "Необходимо целое положительное число"
    elif number == 1:
        print("Последовательность Фиббоначи:")
        print(a)
    else:
        print("Последовательность Фиббоначи:")
        print(a, b, end=' ')
        while counter < number:
            c = a + b
            print(c, end=' ')
            a = b
            b = c
            counter += 1
FIB(number)
