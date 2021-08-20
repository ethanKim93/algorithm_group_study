import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()

    stack = []
    for i in range(len(text)):
        if (stack == []) or (stack[-1] != text[i]):
            stack.append(text[i])
        elif stack and stack[-1] == text[i]:
            stack.pop()
    # print(stack)

    print('#{} {}'.format(tc, len(stack)))