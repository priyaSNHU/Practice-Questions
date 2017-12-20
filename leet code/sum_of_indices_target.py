def two_sum(a_list , target):
    found = False
    for i in range(0, len(a_list)-1):
        for j in range(i+1, len(a_list)):
            t_sum = a_list[i] + a_list[j]
            if(t_sum == target) and not found:
                print(" the indies which mad target are %d %d", i, j)
                found = True

    return found

a_list = [2,7,11,15]

print(two_sum(a_list, 18))
                   
                   
                   
