import sys
sys.stdin = open('input.txt')


def check(n):
    global result
    stack = []
    for i in range(N):
        if magnets[i][n]:
            stack.append(magnets[i][n])
    while stack:
        if stack[0] == 2:
            stack.pop(0)
        else:
            break
    while stack:
        if stack[-1] == 1:
            stack.pop(-1)
        else:
            break

    cnt = 0
    while stack:
        temp = stack.pop(0)
        if temp == 2 and not stack:
            cnt += 1
        elif temp == 2 and stack[0] == 1:
            cnt += 1

    result += cnt


for tc in range(1, 11):
    N = int(input())
    magnets = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for j in range(N):
        check(j)

    print('#{} {}'.format(tc, result))
