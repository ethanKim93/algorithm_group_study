import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    words = list(input())

    stack = []
    top = ''
    for word in words:
        if word != top:
            stack.append(word)
        else:
            stack.pop()
        if not stack:
            top = ''
        else:
            top = stack[-1]
    print('#{} {}'.format(tc, len(stack)))