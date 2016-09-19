lst = input('x:')
def modify_list(x):
    digits = []
    for symbol in lst:
        if '1234567890'.find(symbol) != -1:
            digits.append(int(symbol))
    a = []
    for i in digits:
        if i % 2 == 0:
            a.append(int(i))
    return a
print(modify_list(lst))
