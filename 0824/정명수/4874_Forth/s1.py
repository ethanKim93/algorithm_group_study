import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    s = list(map(str,input().split()))
    s = s[:-1]
    stack = []
    try:
        for i in s:
            if i.isdecimal():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(b//a)
                elif i == '-':
                    stack.append(b-a)
        if len(stack)>=2:
            print('#{} '.format(tc), end='')
            print('error')
        else:
            print('#{} '.format(tc), end='')
            print(*stack)
    except:
        print('#{} '.format(tc), end='')
        print('error')
