class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def push(self, data):
        temp = node(data)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.is_empty():
            return None
        current = self.head
        self.head = current.next
        temp = current.data
        return temp

    def min(self):
        if self.is_empty():
            return None
        current = self.head
        while current:
            temp = current.data
            current = current.next
            if temp < current.data:
                return temp
            else:
                current = current.next


s = stack()
s.push(45)
s.push(32)
s.push(52)
s.push(12)
s.push(2)
print(s.min())
s.pop()
s.pop()
s.pop()
print(s.min())


            
