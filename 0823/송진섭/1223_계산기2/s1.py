import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    expression = input()
    operation_dict = {'a': 0, '+': 1, '*': 2}
    stack = ['a']
    result = []
    number_stack = []

    for i in expression:
        if i not in operation_dict.keys():
            result.append(i)
        else:
            if operation_dict.get(stack[-1]) < operation_dict.get(i):
                stack.append(i)
            else:
                while operation_dict.get(stack[-1]) >= operation_dict.get(i):
                    result.append(stack.pop())
                stack.append(i)
    for i in range(len(stack)-1):
        result.append(stack.pop())

    for i in result:
        if i not in operation_dict.keys():
            number_stack.append(i)
        elif i == '+':
            b = number_stack.pop()
            a = number_stack.pop()
            c = int(a) + int(b)
            number_stack.append(c)
        else:
            b = number_stack.pop()
            a = number_stack.pop()
            c = int(a) * int(b)
            number_stack.append(c)
        if len(number_stack) == 1:
            answer = number_stack[0]

    print('#{} {}'.format(tc, answer))













