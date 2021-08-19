import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    words = list(input())
    stack = []
    i = 0
    while i < len(words):
        if (not stack) or (words[i] != stack[-1]):
            stack.append(words[i])
        else:
            stack.pop()
        i += 1
    if stack :
        result = len(stack)
    else:
        result = 0

    print('#{} {}'.format(tc, result))

