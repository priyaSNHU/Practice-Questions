name = 'priyanka'
name_len = len(name)
name_reverse = ""
for index in range(name_len-1, -1 , -1):
    name_reverse = name_reverse + name[index]
print(name_reverse)
