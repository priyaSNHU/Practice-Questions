def fac_num(num):
    if num <= 1:
        return num
    else:
        return num * fac_num(num-1)


print(fac_num(5))
