import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    postfix = list(input().split())

    operand = []

    for n in postfix:
        if n.isdecimal():
            operand.append(int(n))
        else:
            if n == '+':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    continue
                num2 = operand.pop()
                operand.append(num2 + num1)
            elif n == '*':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    continue
                num2 = operand.pop()
                operand.append(num2 * num1)
            elif n == '-':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    continue
                num2 = operand.pop()
                operand.append(num2 - num1)
            elif n == '/':
                num1 = operand.pop()
                if not operand:
                    operand.clear()
                    continue
                num2 = operand.pop()
                operand.append(num2 // num1)
            elif n == '.':
                if not operand:
                    operand.clear()

                result = ''.join(map(str, operand))
                if operand:
                    print('#{} {}'.format(tc, result))
                elif not operand:
                    print('#{} error'.format(tc))
            else:
                    print('#{} error'.format(tc))

