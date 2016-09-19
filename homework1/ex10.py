# coding=utf-8
a = int(input("Какой сейчас год:"))

def year_def(x):
    if x % 100 == 0 and x % 400 != 0:
        return "Не високосный"
    elif x % 4 == 0:
        return "Високосный"
    else:
        return "Не високосный"
print(year_def(a))