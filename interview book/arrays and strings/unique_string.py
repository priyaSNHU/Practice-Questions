def unique(string):
    uni_char = []
    for i in string:
        if i in uni_char:
            return False
        uni_char.append(i)
    return True

def is_unique(string):
    if unique(string):
        print('The given string has all unique characters')
    else:
        print('The given string doesnot have unique characters')

is_unique('priyanka')
is_unique('PriyankA')
is_unique('mat')
