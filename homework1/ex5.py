a = int(input("a = ?"))
b = int(input("b = ?"))
c = int(input("c = ?"))


list = [a, b, c]

n = 1
while n < len(list):
    for i in range(len(list) - n):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
    n += 1

print('Max:', list[2])
print('Min:', list[0])
print('Mid:', list[1])