import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    line = list(input().split())
    stack = []

    for i in line:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '.':
            if len(stack) == 1:
                print('#{} {}'.format(tc, stack[0]))
                break
            else:
                print('#{} error'.format(tc))
        else:
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
	                stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                else:
                    stack.append(b // a)


