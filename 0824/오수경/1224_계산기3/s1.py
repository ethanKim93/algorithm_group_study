import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    calculate = input()
    stack = []
    result = []
    priority = {'*': 2, '+': 1, '(': 0, ')': 0}

    # 후위표기로 변환
    for c in calculate:
        if c not in priority:
            result.append(int(c))
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    a = stack.pop(-1)
                    result.append(a)
                stack.pop(-1)
            elif len(stack) != 0 and priority[c] > priority[stack[-1]]:
                stack.append(c)
            elif len(stack) != 0 and priority.get(c) <= priority.get(stack[-1]):
                while priority.get(c) <= priority.get(stack[-1]):
                    a = stack.pop(-1)
                    result.append(a)
                stack.append(c)

    # 후위표기 계산
    for r in result:
        if r not in priority:
            stack.append(r)
        else:
            a = stack.pop(-1)
            b = stack.pop(-1)
            if r == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)
    print('#{}'.format(tc), *stack)