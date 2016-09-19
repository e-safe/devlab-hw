# coding=utf-8
word = str(input("Введите что нибудь:"))
result = ''
glasn = 'ауеыоэяию'
for i in word:
    if i not in glasn:
        result += i
print(result)