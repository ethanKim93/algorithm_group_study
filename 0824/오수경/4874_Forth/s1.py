import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    result = list(input().split())
    stack = []
    number = 0


    for e in result:
        if e.isdecimal():
            number += 1

    if len(result) - number != number:
        print('#{} error'.format(tc))

    else:
        for r in result:
            if r.isdecimal():
                stack.append(r)

            else:
                if r == '.':
                    print('#{}'.format(tc), *stack)
                else:
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    if r == '+':
                        stack.append(int(a) + int(b))
                    elif r == '*':
                        stack.append(int(a) * int(b))
                    elif r == '-':
                        stack.append(int(b) - int(a))
                    elif r == '/':
                        stack.append(int(b) // int(a))

