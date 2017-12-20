from classtak import Stack
s = Stack()

def conv_string(num, base):
    
    string_conv = "0123456789ABCDEF"
    while num > 0:
        if num < base:
           s.push(string_conv[num])
        else:
           s.push(string_conv[num% base])
        num = num//base
    res = ""
    while not s.is_empty():
        res = res + str(s.pop())
    return res

print(conv_string(10, 2))
