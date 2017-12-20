def ispalindrome(number):
    return int(str(number)[::-1]) == number

pal_num = 0
for num1 in range(999,100,-1):
    for num2 in range(999,100,-1):
        temp = num2 * num1
        if ispalindrome(temp) and temp > pal_num:
            pal_num = temp
print(pal_num)
            
