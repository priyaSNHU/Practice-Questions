def lin_search(a_list,item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if (a_list[pos] == item):
            found = True
        else:
            if(a_list[pos] > item):
                stop = True
                print ("the item is greater then the element present at postion: ", pos)
            else:
                pos = pos+1
    return found

a_list = [1,5,10,15,18,21,34,48,59]

print(lin_search(a_list, 11))
print(lin_search(a_list, 1))
print(lin_search(a_list, 20))
