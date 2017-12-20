from classdeque import Deque

def check_palindrome(a_string):
    intial_deque = Deque()

    for ch in a_string:
        intial_deque.add_rear(ch)

    pal = True

    while intial_deque.size() > 1 and pal:
        first = intial_deque.remove_front()
        last = intial_deque.remove_rear()
        if (first != last):
            pal = False
    return pal


print(check_palindrome('madam'))
print(check_palindrome('nfcehrgfusyd13'))
