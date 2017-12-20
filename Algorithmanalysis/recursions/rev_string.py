def rev_string(string):
    if len(string) == 1:
        return string[0]
    else:
        return  rev_string(string[1:]) + string[0]

def pal_str(string):
    found = False
    if string == rev_string(string):
        found = True
        return found
    else:
        return found

    
print(rev_string("priyanka"))
print(pal_str("kayak"))
print(pal_str("reviled did i live, saidias ,evil i did deliver"))


