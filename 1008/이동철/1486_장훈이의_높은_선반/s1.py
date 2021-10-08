import sys
sys.stdin = open('input.txt', 'r')


def max_percent(idx, total):
    global result

    if total <= result:
        return

    if idx == N and total > result:
        result = total
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            max_percent(idx + 1, total * arr[i][idx] * 0.01)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 0

    max_percent(0, 1)

    print('#{} {:6f}'.format(tc, result * 100))
