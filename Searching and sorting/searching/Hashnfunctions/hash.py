def hash(string , tab_siz):
    t_sum = 0
    for pos in range(0, len(string)-1):
        t_sum = t_sum + ord(string[pos])

    return t_sum% tab_siz

print(hash("cat" , 15))


def hash_weg(string , tab):
    t_sum = 0
    for pos in range(0, len(string) - 1):
        t_sum = t_sum + (ord(string[pos])* pos)
    return t_sum% tab

print(hash_weg("cat" , 15))
