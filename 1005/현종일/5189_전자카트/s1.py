import sys
sys.stdin = open("sample_input.txt")

def route(now,total,cnt):
    global result

    if total >= result:
        return

    if cnt >= N-1:
        total += field[now][1]
        if total < result:
            result = total
        return

    for i in range(2, N+1):
        if not visited[i]:
            visited[i] = 1
            route(i, total + field[now][i], cnt+1)
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    field = [[0] * N] + [[0] + list(map(int, input().split())) for _ in range(N)]
    result = N * 100
    visited = [0] * (N + 1)
    route(1, 0, 0)
    print('#{} {}'.format(tc, result))


