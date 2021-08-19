import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    text = list(input())
    stack1 = []
    stack2 = []
    for i in range(len(text)):
        if text[i] == '(':
            stack1.append(text[i])
        if text[i] == '{':
            stack2.append(text[i])

        if text[i]==')':
            stack1.pop(-1)
        if text[i]=='}':
            stack2.pop(-1)

    if stack1 or stack2:
        print('#{} {}'.format(tc, 0))
    elif not stack1 and not stack2:
        print('#{} {}'.format(tc, 1))
