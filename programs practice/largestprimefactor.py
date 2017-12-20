def large_prime_factor():
    """find the gratest prime factor"""
    dividend = 600851475143
    divisor = 2
    prime_factors = []
    while dividend > 1:
        if(dividend % divisor == 0): # check is the number is divisible by 2
            prime_factors.append(divisor) # if so then add the divisor to the factors tlist
            dividend = dividend/divisor 
            divisor = divisor + 1 # increment the divisor value
        else:
            divisor = divisor + 1
            if(dividend % divisor == 0):
                prime_factors.append(divisor)
                dividend =  dividend / divisor                
    return max(prime_factors)
    

print(large_prime_factor())
