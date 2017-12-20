def sum_of_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_of_list(num_list[1:])


print(sum_of_list([3,7,2]))
