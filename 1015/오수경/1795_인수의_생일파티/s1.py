# 역시 DFS는 시간초과...

import sys
sys.stdin = open('input.txt')
from collections import deque


def round_trip(node, end, cnt, start, lst):
    way = deque()
    way.append(node)

    if node == end:
        if lst[start] > cnt:
            lst[start] = cnt
        return cnt

    elif cnt > lst[start]:
        return

    else:
        now = way.popleft()
        visited[now] = 1
        for i in range(1, N+1):
            if D[now][i] != 0 and visited[i] == 0:
                way.append(i)

    while way:
        next = way.popleft()
        round_trip(next, end, cnt+D[node][next], start, lst)
        visited[next] = 0


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    D = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())     # x->y : 비용 c
        D[x][y] = c

    go = [9999999]*(N+1)
    back = [9999999]*(N+1)
    for i in range(1, N+1):
        if i != X:
            visited = [0] * (N + 1)
            round_trip(i, X, 0, i, go)

            visited = [0] * (N + 1)
            round_trip(X, i, 0, i, back)

    time = 0
    for i in range(1, N+1):
        if i != X and go[i] + back[i] > time:
            time = go[i] + back[i]

    print('#{} {}'.format(tc, time))

