from classtak import Stack

def infix_postfix(exp):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    s = Stack()
    postfix_list = []
    infix_list = exp.split()

    for ch in infix_list:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or ch in "0123456789":
            postfix_list.append(ch)
        elif ch == "(":
            s.push(ch)
        elif ch == ")":
            top_element = s.pop()
            while top_element != "(":
                postfix_list.append(top_element)
                top_element = s.pop()
        else:
            while (not s.is_empty()) and (prec[s.peek()] >= prec[ch]) :
                postfix_list.append(s.pop())
            s.push(ch)
            
    while (not s.is_empty())        :
        postfix_list.append(s.pop())
    return " ".join(postfix_list)


print(infix_postfix("5 * 3 ** (4 - 2)"))
