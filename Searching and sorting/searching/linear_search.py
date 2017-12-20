def linear_search(a_list, item):
    found = False
    pos = 0
    while pos < len(a_list) and not found:
        if(a_list[pos] == item):
            found = True
        else:
            pos = pos+1
    return found    
            

a_list = [1,45,22,31,13,7,15,8]
print(linear_search(a_list, 8))
print(linear_search(a_list, 89))
