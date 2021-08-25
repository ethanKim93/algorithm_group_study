import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    L = int(input())
    f = input()
    prior = {'(':0, '+':1, '*':2}
    stack = []
    answer = []
    for i in f:
        if i.isdecimal():
            answer.append(int(i))
        else:
            if stack:
                if i =='(':
                    stack.append(i)
                elif i ==')':
                    while stack:
                        answer.append(stack.pop())
                        if stack[-1] == '(':
                            stack.pop()
                            break
                else:
                    if stack and prior[i] > prior[stack[-1]]:
                        stack.append(i)
                    else:
                        answer.append(stack.pop())
                        if stack and prior[stack[-1]] >= prior[i]:
                            answer.append(stack.pop())
                        stack.append(i)
            else:
                stack.append(i)
    while stack:
        answer.append(stack.pop())

    stack = []
    for i in answer:
        if type(i)==int:
            stack.append(i)
        else:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                c = int(a) + int(b)
                stack.append(c)
            else:
                a = stack.pop()
                b = stack.pop()
                c = int(a) * int(b)
                stack.append(c)
    print('#{}'.format(tc), end=' ')
    print(*stack)