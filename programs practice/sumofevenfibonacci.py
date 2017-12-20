def sum_even_fibonacci():
    count = 0
    num1 = 1
    num2 = 2
    while(num2 < 4000000):
        temp = num1 + num2
        num1 = num2
        num2 = temp
        if (num1 % 2 == 0):
            count = count + num1
    return count

print(sum_even_fibonacci())
    
