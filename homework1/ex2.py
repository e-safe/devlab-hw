# coding=utf-8
import math
a = float(input("enter a"))
b = float(input("enter b"))
c = float(input("enter c"))
def formula():
    if a >= (b + c):
        return "Так не бывает, ведь сумма двух сторон треугольника всегда больше чем третья"
    elif b >= (a + c):
        return "Так не бывает, ведь сумма двух сторон треугольника всегда больше чем третья"
    elif c >= (a + b):
        return "Так не бывает, ведь сумма двух сторон треугольника всегда больше чем третья"
    else:
        p = (a + b + c) / 2
        pp = float((p * (p - a) * (p - b) * (p - c)))
        v = float(math.sqrt(pp))
        return v
print(formula())
