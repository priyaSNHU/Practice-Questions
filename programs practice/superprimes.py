def is_prime(n, prime):
    prime[0] = prime[1] = False
    for i in range(2, n+1):
        prime[i] = True


    for j in range(2, n+1):
        if (j*j <= n and prime[j] == True):
            for i in range(j*2, n+1,j):
                prime[i] = False
                j += 1
def super_prime(n):
    prime = [1 for i in range(n+1)]
    is_prime(n, prime)

    primes = [0 for i in range(2, n+1)]
    j = 0
    for i in range(2,n+1):
        if (prime[i]):
            primes[j] = i
            j += 1

    for k in range(j):
        if (prime[k+1]):
            print(primes[k])


n = 241
print('the super prime numbers are :')
super_prime(n)
