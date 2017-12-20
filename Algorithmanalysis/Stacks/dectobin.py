from classtak import Stack

def dec_bin(num):
    s = Stack()
    while num >0:
        reminder = num % 2
        s.push(reminder)
        num = num // 2

    bindec = ""

    while not s.is_empty():
        bindec += str(s.pop())

    return bindec

print(dec_bin(17))
print(dec_bin(45))
print(dec_bin(96))
