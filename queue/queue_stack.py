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

    def size(self):
        if self.is_empty():
            return 0
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next
        return count
class queue:
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        return self.stack2.push(self.stack1.pop())
    
    
    def size(self):
        return self.stack1.size()


q = queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(7)
print(q.dequeue())
print(q.size())
        
