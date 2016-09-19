# coding=utf-8
a = int(input("Введите первое числовое значение: "))
b = int(input("Введите второе числовое значение: "))
operation = str(input("Введите одну из операций  +, -, /, *, mod, pow, div: "))
# mod — это взятие остатка от деления.
# pow — возведение в степень.
# div — целочисленное деление.
def calculus():
    if operation in ('+', '-', '/', '*', 'mod', 'pow', 'div'):
        if operation == '+':
            return (a + b)
        elif operation == '-':
            return (a - b)
        elif operation == '/':
            return (a / b)
        elif operation == '*':
            return (a * b)
        elif operation == 'mod':
            return (a % b)
        elif operation == 'pow':
            return (a ** b)
        elif operation == 'div':
            return int(a / b)
    else:
        return 'Ты какую операцию ввел, мудак?'
print(calculus())
