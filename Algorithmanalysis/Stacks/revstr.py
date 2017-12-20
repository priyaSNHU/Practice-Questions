from classtak import Stack

def rev(value):
    s = Stack()
    for ch in value:
        s.push(ch)

    revstk = ''
    while not s.is_empty():
        revstk += s.pop()

    if ( value == revstk):
        print('Given string is palidrome')
    else:
        print('Given string is not palindrome')

    return revstk


print(rev('123'))
print(rev('priyanka'))
print(rev('454'))
print(rev('pop'))
