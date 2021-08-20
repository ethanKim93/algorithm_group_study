import sys
sys.stdin = open('sample_input.txt')


def push(item):
    stack.append(item)


def pop():
    if stack:
        return stack.pop()


def check(text):
    for i in range(len(text)):
        if text[i] == '(' or text[i] == '{':
            push(text[i])

        elif text[i] == ')':
            if stack and stack[-1] == '(':
                pop()
            else:
                return 0

        elif text[i] == '}':
            if stack and stack[-1] == '{':
                pop()
            else:
                return 0
    if stack:
        return 0
    else:
        return 1


T = int(input())
for test_case in range(1, T+1):
    code = input()
    stack = []
    print('#{} {}'.format(test_case, check(code)))


