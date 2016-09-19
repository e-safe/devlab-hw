#coding: utf8
cc_num = input('Введите номер карты (16 цифр):')
if len(cc_num) == 16:
    def bn(c):
        c = int(c)
        c *= 2
        if c >= 10:
            c -= 9
        return c
    if (bn(cc_num[0]) + int(cc_num[1]) + bn(cc_num[2]) + int(cc_num[3]) + bn(cc_num[4]) + int(cc_num[5]) + bn(cc_num[6]) + int(cc_num[7]) + bn(cc_num[8]) + int(cc_num[9]) + bn(cc_num[10]) + int(cc_num[11]) + bn(cc_num[12]) + int(cc_num[13]) + bn(cc_num[14]) + int(cc_num[15])) % 10 == 0:
        print("True")
    else:
        print("False")
else:
    print("Необходимо указать 16 цифр!!!")