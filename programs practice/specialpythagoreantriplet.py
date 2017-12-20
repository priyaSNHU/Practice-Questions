def triplet():
    sum = 1000
    for a in range(1,1000):
        for b in range(2,1000):
            for c in range(3,1000):
                if( a+b+c ==sum and a*a + b*b == c*c):
                    product = a*b*c
                    break
    return product
                


triplet()
