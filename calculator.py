def precedence(op):
    if op == '(':
        return 0
    elif op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return -1

def is_right_associative(op):
    return op == '^'

def apply_operator(op, b, a):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b
    elif op == '^':
        return a ** b
    raise Exception("Invalid operator")

def calculate(s):
    operands = []
    operation = []
    a = ""
    unary = True

    for i in range(len(s)):
        if s[i].isdigit():
            a += s[i]
            unary = False
        elif s[i] == ' ':
            continue
        elif s[i] == '(':
            operation.append('(')
            unary = True
        elif s[i] == ')':
            if a:
                operands.append(int(a))
                a = ""
            while operation and operation[-1] != '(':
                temp = operands.pop()
                temp1 = operands.pop()
                op = operation.pop()
                operands.append(apply_operator(op, temp, temp1))
            if operation:
                operation.pop()
            unary = False
        else:
            if a:
                operands.append(int(a))
                a = ""
            if s[i] == '-' and unary:
                operands.append(0)
                operation.append('-')
            else:
                while (operation and operation[-1] != '(' and
                       (precedence(s[i]) < precedence(operation[-1]) or
                        (precedence(s[i]) == precedence(operation[-1]) and not is_right_associative(s[i])))):
                    temp = operands.pop()
                    temp1 = operands.pop()
                    op = operation.pop()
                    operands.append(apply_operator(op, temp, temp1))
                operation.append(s[i])
                unary = True

    if a:
        operands.append(int(a))

    while operation:
        temp = operands.pop()
        temp1 = operands.pop()
        op = operation.pop()
        operands.append(apply_operator(op, temp, temp1))

    return operands[-1] if operands else 0
