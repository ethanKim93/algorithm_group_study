T = int(input())

for tc in range(1, T+1):
    post = input().split()
    stack = []
    for i in post:
        if i.isdigit():
            stack.append(int(i))
        elif len(stack) > 1:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == '/':
                stack.append(a/b)
            else:
                print('#{} error'.format(tc))
                break
        elif len(stack) == 1 and i == '.':
            print('#{} {}'.format(tc, int(stack[0])))
        else:
            print('#{} error'.format(tc))
            break


