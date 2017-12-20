list = [1,3,5,8,10,13,18,36,78,]

n = len(list)
print(n)

a = []

for i in range(2,n,2):
    if list[i] % 2 == 0:
        a.append(list[i])
print(a)
