import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, words = input().split()

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
    print('#{} {}'.format(tc, ''.join(stack)))