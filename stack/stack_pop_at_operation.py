class stack_Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = stack_Node(data)
        temp.next = self.head
        self.head = temp
        current = self.head
        count = 0
        while current:
            count += 1
            if count == 5:
                set_of_stack1 = stack()
                set_of_stack1.push(self, data)
            else:
                current = current.next


set_of_stack = stack()

set_of_stack.push(5)
set_of_stack.push(6)
set_of_stack.push(1)
set_of_stack.push(4)
set_of_stack.push(34)
set_of_stack.push(21)

                
        
