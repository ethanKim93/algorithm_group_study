import  sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []

    for i in text:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)

    result = 0 if stack else 1
    print('#{} {}'.format(tc, result))