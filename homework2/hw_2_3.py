# coding=utf-8
c = int(input('c:'))
g=''
for i in range(0,10):
    a = str(i)
    b = a*i
    g+=b
g = g[0:c]
print(g)
