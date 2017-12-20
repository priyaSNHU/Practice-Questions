class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return True if self.is_empty() is None else False

    def push(self, data):
        temp = node(data)
        current = self.head
        self.head = temp

    def pop(self):
        
        current = self.head
        self.head = current.next
        temp = current.data
        return temp

    def size(self):
        
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def middle(self):
        
        temp = self.size()
        if temp % 2 != 0:
            self.pop()
        else:
            n = self.size/2
            current = self.head
            while current:
                count += 1
                if count == n:
                    temp = current.data
                    return temp
                else:
                    current = current.next

s = stack()
s.push(4)
s.push(3)
s.push(15)
s.push(7)
s.push(12)
print(s.middle())


        
