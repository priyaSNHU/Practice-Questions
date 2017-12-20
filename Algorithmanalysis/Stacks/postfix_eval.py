from classtak import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = do_math(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()
            

def do_math (op, op1, op2 ):
    if op == "*":
        return op1 * op2
    elif op == "+":
        return op1 + op2
    elif op == "/":
        return op1/op2
    else :
        return op1 - op2

print(postfixEval('17 10 + 3 * 9 / == '))
    
