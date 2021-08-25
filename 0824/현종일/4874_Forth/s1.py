import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    oper = input().split()
    stack = []
    opers = ['+', '-', '*', '/']
    flag = False
    for i in oper:
        if i.isdecimal():
            stack.append(i)
        elif i in opers:
            if len(stack) > 1:
                b = int(stack.pop())
                a = int(stack.pop())
                temp = 0
                if i == '+':
                    temp = a + b
                elif i == '*':
                    temp = a * b
                elif i == '-':
                    temp = a - b
                else:
                    temp = a / b
                stack.append(temp)
            else:
                flag = True
                break

    print('#{}'.format(tc), end=' ')
    if flag or len(stack) > 1:
        print('error')
    else:
        print(int(*stack))
