def pascal(n):
    l = [[1]]
    for i in range(n-1):
        l.append([1,1])
        for j in range(len(l[-2])-1):
            l[-1].insert(-1,l[-2][j]+l[-2][j+1])
    return l

print(pascal(6))
