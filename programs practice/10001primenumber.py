num = int(input("Enter the range of primenumbers you want to find: "))
prime_list = []

for x in range(2, num+1):
    isprime = True
    for y in range(2, int(x**0.5) +1):
        if x%y == 0:
            isprime = False
            break

    if isprime:
        prime_list.append(x)

print(prime_list)





