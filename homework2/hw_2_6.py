with open('exam_results.csv') as f:
    my_list = f.read().splitlines()
    with open('new.txt', 'w') as new:
        for i in my_list:
            a = i.split(',')
            if int(a[1]) > 60 and int(a[2]) > 60 and int(a[3]) > 60:
                b = str(a[0])
                new.write(b + '\n')
            else:
                pass