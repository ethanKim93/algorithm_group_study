import sys
sys.stdin = open('input (1).txt')

operator = {'(': 4, ')': 4, '*': 2, '/': 2, '+': 3, '-': 3}

def operation(t1, t, t2):
    t1 = int(t1)
    t2 = int(t2)
    if t == '+':
        return t1 + t2
    elif t == '-':
        return t1 - t2
    elif t == '*':
        return t1 * t2
    elif t == '/':
        return t1 // t2


T = 10
for tc in range(1, T + 1):
    input()
    t_input = list(input())
    stack_operation = []
    stack_result = []

    for t in t_input:

        if '0' <= t <= '9':
            stack_result.append(t)

        elif t == '(' or not len(stack_operation) or stack_operation[-1] == '(':
            stack_operation.append(t)

        elif operator[t] < operator[stack_operation[-1]] and t != ')':
            stack_operation.append(t)
        else:

            while len(stack_operation) and operator[t] >= operator[stack_operation[-1]]:

                if stack_operation[-1] == '(':
                    stack_operation.pop()
                    break

                stack_result.append(stack_operation.pop())

            if t != ')':
                stack_operation.append(t)


    while len(stack_operation):

        temp = stack_operation.pop()
        if temp != '(':
            stack_result.append(temp)

    for t in stack_result:

        if '0' <= t <= '9':
            stack_operation.append(t)
        else:

            t2 = stack_operation.pop()
            t1 = stack_operation.pop()
            stack_operation.append(operation(t1, t, t2))
    else:

        print('#{} {}'.format(tc, stack_operation[0]))