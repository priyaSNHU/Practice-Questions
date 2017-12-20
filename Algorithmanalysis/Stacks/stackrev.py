from classtak import Stack

def stack_rev(input_stack):
    temp_stack = Stack()
    while not input_stack.is_empty():
        temp = input_stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            input_stack.push(temp_stack.pop())
        temp_stack.push(temp)

    return temp_stack
   
    
    
s = Stack()
s.push(31)
s.push(3)
s.push(15)
s.push(98)
s.push(92)
s.push(23)

print(stack_rev(s))
    
