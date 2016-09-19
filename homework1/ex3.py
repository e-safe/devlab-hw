a = int(input('INT=?'))
def interwall(x):
    if 12 > x > -15:
        return True
    elif 17 > x > 14:
        return True
    elif x > 19:
        return True
    else:
        return False
print(interwall(a))
