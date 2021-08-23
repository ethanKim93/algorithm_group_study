import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    calculate = input()

    stack = []
    result = []
    number = '0123456789'

    # 후위표기로 변환
    for c in calculate:
        if c in number:
            result.append(c)

        else:
            if len(stack) == 0:
                stack.append(c)

            elif len(stack) != 0 and c == '*' and stack[-1] == '+':
                stack.append(c)

            elif len(stack) != 0 and c == '*' and stack[-1] == '*':
                while len(stack) != 0 and stack[-1] != '+':
                    a = stack.pop(-1)
                    result.append(a)
                stack.append(c)

            elif c == '+':
                while len(stack) != 0:
                    a = stack.pop(-1)
                    result.append(a)
                stack.append(c)

    if len(stack) != 0:
        while len(stack) != 0:
            a = stack.pop(-1)
            result.append(a)


    # 후위표기 계산
    for r in result:
        if r in number:
            stack.append(r)

        else:
            a = stack.pop(-1)
            b = stack.pop(-1)
            if r == '+':
                stack.append(int(a) + int(b))
            else:
                stack.append(int(a) * int(b))
    print('#{}'.format(tc), *stack)