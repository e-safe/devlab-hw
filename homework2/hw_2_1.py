f = open('numbers.txt', 'r')
my_list = f.read().splitlines()
my_list_m = set(my_list)
print(len(my_list_m))