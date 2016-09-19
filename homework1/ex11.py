a = int(input("a = "))


list = range(1, a + 1)
n = 1
if a <= 0:
    print("Impossible")
else:
    while n <= len(list):
        for i in range(len(list) - n):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        print(n * "*")
        n += 1
