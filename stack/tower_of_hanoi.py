Init_stack = [0,1,2,3]
Buffer_stack = []
Final_stack = []
n = len(Init_stack)
def move_disks(Init_stack, Buffer_stack, Final_stack, n):
    if n == 0:
        return
    elif n == 1:
        Final_stack.append(Init_stack.pop())
    elif n == 2:
        Buffer_stack.append(Init_stack.pop())
        Final_stack.append(Init_stack.pop())
        Final_stack.append(Buffer_stack.pop())
    else:
        move_disks(Init_stack, Final_stack, Buffer_stack, n-1)
        Final_stack.append(Init_stack.pop())
        move_disks(Buffer_stack, Init_stack, Final_stack,n-1)


