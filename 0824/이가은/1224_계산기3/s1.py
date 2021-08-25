import sys
sys.stdin = open('input.txt')

def postfix(oper_str):
    N = input
    eq = input()
    stack, post = [], []
    for i in eq:
        if i.isdecimal():
            post.append(int(i))
        else:
            if i == '+':
                while stack:
                    post.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
    while stack:
        post.append(stack.pop())

for tc in range(10):
    N = int(input())
    operation = input()

    while ')' not in operation:
        for i in range(len(operation)):
            if operation[i] == ')':
                for j in range(i,-1,-1):
                    if operation[j] == '(':
                        a = j
                        break
                break
        new = postfix(operation[i-a+1:a-1])
        operation = ''.join((operation[:i-a],new,operation[a:]))
    print(operation)

