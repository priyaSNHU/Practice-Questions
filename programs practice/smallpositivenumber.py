def pos_num():
    num = 20
    while True:
        num += 20
        if(num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and
           num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and
           num % 19 == 0 and num % 20 == 0 ):
            print (num)
            break


pos_num()
