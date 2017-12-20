def hanoi(n , source , dest , temp):
    if n == 1:
        print (" Move disk from ", source , " to " , dest)
    else:
        hanoi(n-1 , source , temp, dest )
        hanoi(1, source, dest, temp)
        hanoi(n-1, temp, dest, source)


hanoi(6,"A", "B", "C")
