def two_sum(a_list , target):
    found = False
    num1 = []
    for i in range(0, len(a_list)-1):
        t_sum = a_list[i] + a_list[i+1]
        if(t_sum == target) and not found:
            num1 = [i, i+1]
    return num1




a_list = [3,2,3]
print(two_sum(a_list, 6))
