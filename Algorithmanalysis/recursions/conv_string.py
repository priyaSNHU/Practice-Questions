def conv_string(num, base):
    string_conv = "0123456789ABCDEF"
    if base <= 0:
        return print('The base number cannot be 0')
    else:
        if num < base:
            return string_conv[num]
        else:
            return conv_string(num//base , base) + string_conv[num% base]
    

print(conv_string(1453,-1))
