number = int(input('Enter your number: '))

if number > 1:
    for i in range(2, number):
        if (number % i is 0):
            print('The given number is not prime number')
            break
    else:
        print('the given number is prime number')

else:
    print('the given number is not prime')
