import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    forth = input().split()
    stack = []
    for f in forth:
        try:
            if f.isdecimal():
                stack.append(int(f))
            else:
                if f == '+':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b+a)
                elif f == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b-a)
                elif f == '*':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b*a)
                elif f == '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b//a)
                elif f == '.':
                    if len(stack) == 1:
                        print('#{} {}'.format(tc, stack.pop()))
                    else:
                        print('#{} error'.format(tc))
        except:
            print('#{} error'.format(tc))
            break