import sys
sys.stdin = open('input.txt')

def cal(txet):
    stack = []
    for i in text:
        if i.isdigit():
            stack.append(i)
        try:
            if i in callog:
                if i == callog[0]:
                    stack.append((int(stack.pop()) * int(stack.pop())))
                elif i == callog[1]:
                    f = stack.pop()
                    s = stack.pop()
                    stack.append((int(s) - int(f)))
                elif i == callog[2]:
                    stack.append((int(stack.pop()) + int(stack.pop())))
                elif i == callog[3]:
                    f = stack.pop()
                    s = stack.pop()
                    stack.append(int((int(s) / int(f))))
            if i == '.' and len(stack) == 1:
                return int(stack.pop())
            elif i == '.' and len(stack) != 1:
                return 'error'
        except:
            return 'error'

for tc in range(1, int(input())+1):
    text = list(input().split())
    callog = ['*', '-', '+', '/']
    print('#{} {}'.format(tc, cal(text)))