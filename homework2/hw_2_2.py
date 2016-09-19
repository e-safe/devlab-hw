f = open('numbers.txt', 'r')
my_list = f.read().splitlines()
with open('numbers-new.txt', 'w') as f:
    for i in my_list:
        a = my_list.count(i)
        if a > 1:
            f.write(i + '\n')
        else:
            pass