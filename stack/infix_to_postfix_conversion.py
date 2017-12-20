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
    def peek(self):
        current = self.head
        return current.data

    def size(self):
        if (self.is_empty()):
            return None
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next
        return count
    
    def infix_postfix(self, exp):
        prec = []
        prec["*"] = 3
        prec["/"] = 3
        prec["**"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        s = stack()
        postfix_list = stack()
        infix_list = exp.split()

        for ch in infix_list:
            if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or ch in "0123456789":
                postfix_list.push(ch)
            elif ch == "(":
                s.push(ch)
            elif ch == ")":
                top_element = s.pop()
                while top_element != "(":
                    postfix_list.push(top_element)
                    top_element = s.pop()
            else:
                while (not s.is_empty()) and (prec[s.peek()] >= prec[ch]) :
                    postfix_list.push(s.pop())
                s.push(ch)
            
        while (not s.is_empty())        :
            postfix_list.push(s.pop())
        return " ".join(postfix_list)




s = stack()
exp = "5 * 3 ** (4 - 2)"
s.infix_postfix(exp)
