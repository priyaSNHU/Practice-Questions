from classqueue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, item):
        self.q1.enqueue(item)
    def pop(self):
        for x in range(-1,0,1): 
            self.q2.enqueue(self.q1.dequeue)
            self.q1.enqueue(self.q2.dequeue)
        return self.q1.dequeue() 
    def size(self):
        return self.q1.size() + self.q2.size()
    def is_empty(self):
        if self.size != []:
            return True
        else:
            return False




s = Stack()
print(s.push('7'))
print(s.push(9))
print(s.push(5))
print(s.push(0))
print(s.push('priya'))
print(s.pop())
print(s.is_empty())
