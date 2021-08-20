import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    text = list(input())
    stack = []

    for i in range(len(text)):
        if text[i] == '(':
            stack.append(text[i])
        elif text[i] == '{':
            stack.append(text[i])

        elif text[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(text[i])
        elif text[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(text[i])

    if not stack:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
