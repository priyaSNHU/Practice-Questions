def selection(a_list):
    for i in range(len(a_list)-1,0,-1):
        pos_max = 0
        for j in range(1, i+1 ):
            if (a_list [j] > a_list[pos_max]):
                pos_max = j

        a_list[i], a_list[pos_max] = a_list[pos_max], a_list[i]

    


a_list = [ 54,26,93,17,77, 31, 44, 55, 20]
selection(a_list)
print(a_list)
