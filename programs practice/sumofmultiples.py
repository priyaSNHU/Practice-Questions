def sum_multiples(n):
    count = 0
    for num in range(0,n):
        if(num % 3 == 0 or num % 5 == 0):
            count +=  num
    return count    
      

print(sum_multiples(1000))
