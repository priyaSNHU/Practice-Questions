temp = 0
temp2 = 0
for i in range (1,101,1):
    mul = i * i
    temp = temp + mul

print('the sum of squares of first 100 natural numbers: ',temp)

for i in range(1,101,1):
    temp2 = temp2 + i
    mul2  =  temp2 * temp2
print('The square of the sum of first 100 natural numbers: ', mul2)

diff = mul2 - temp
print('the sidderence between sum of square and square of sum: ', diff)
