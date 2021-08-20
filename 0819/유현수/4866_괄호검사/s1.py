import sys
sys.stdin = open('sample_input.txt')


def push(x):
    stack.append(x)


def match(x):               # 닫는 괄호와 스택의 마지막 값 비교
    if len(stack):
        if stack[-1] == x:
            stack.pop()
            return 1
        else:
            return 0
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    code = input()
    stack = []
    for char in code:
        if char == '(':         # 여는 괄호가 나오면 push
            push('(')
        elif char == '{':
            push('{')
        elif char == ')':       # 닫는 괄호가 나오면 match 확인
            flag = match('(')
            if not flag:
                print('#{} 0'.format(tc))
                break
        elif char == '}':
            flag = match('{')
            if not flag:
                print('#{} 0'.format(tc))
                break
    else:
        if stack:
            print('#{} 0'.format(tc))
        else:
            print('#{} 1'.format(tc))