def minimum():
    num = [100, 0,300,40,10,11,12,35,92,101,103,99]
    for i in range(len(num) - 1):
        for j in range(i+1 , len(num)):
            if( num[i] > num[j]):
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
            
    print(num)
    print(num[0])
    print(num[-1])
    avg = (num[0] + num[-1])/2
    print(avg)
def minimum_num():
    minvalue = 5
    num = [5 , 4, 31, 1, 15, 10]
    for i in num:
        if i < minvalue:
            minvalue = i
    print(minvalue)


minimum()

