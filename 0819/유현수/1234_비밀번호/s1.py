import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, P = input().split()
    N = int(N)
    stack = []
    for i in range(N):
        if not stack:
            stack.append(P[i])
        else:
            if stack[-1] == P[i]:
                stack.pop()
            else:
                stack.append(P[i])
    print('#{}'.format(tc), end=' ')
    print(''.join(stack))