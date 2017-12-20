class stack_node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def push(self, data):
        temp = stack_node(data)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if (self.is_empty()):
            return None
        current = self.head
        self.head = current.next
        pop_node = current.data
        return pop_node

    def size(self):
        if (self.is_empty()):
            return None
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next
        return count

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
                temp = current.data
            


s = stack()
s.is_empty()
s.push(5)
s.push(4)
s.push(8)
s.push(2)
s.push(0)
s.push(21)

print(s.pop())
print(s.size())
print(s.min())
            
            
            
        
