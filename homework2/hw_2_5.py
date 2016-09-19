with open('my_text.txt') as my_text:
    a = my_text.read().split()
    c = set(a)
    for i in c:
        b = a.count(i)
        print(i, b)
