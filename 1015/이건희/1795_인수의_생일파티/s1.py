import sys
from collections import deque
sys.stdin = open("input.txt")

def go(start):
    q = deque()
    go_temps = [inf] * (n + 1)
    q.append(start)
    go_temps[start] = 0
    while q:
        now = q.popleft()
        for i in range(1, n + 1):
            if maps2[now][i]:
                if go_temps[i] > go_temps[now] + maps2[now][i]:
                    go_temps[i] = go_temps[now] + maps2[now][i]
                    q.append(i)
    return go_temps

def come(start):
    q = deque()
    come_temps = [inf] * (n + 1)
    q.append(start)
    come_temps[start] = 0
    while q:
        now = q.popleft()
        for y in range(1, n + 1):
            if maps[now][y]:
                if come_temps[y] > come_temps[now] + maps[now][y]:
                    come_temps[y] = come_temps[now] + maps[now][y]
                    q.append(y)
    return come_temps


t = int(input())
for tc in range(1, t + 1):
    n, m, x = map(int, input().split())
    maps = [[0] * (n + 1) for _ in range(n + 1)]
    maps2 = [[0] * (n + 1) for _ in range(n + 1)]
    inf = 999999
    for _ in range(m):
        s, g, w = map(int, input().split())
        maps[s][g] = w
        maps2[g][s] = w

    mx = 0
    go_dist, come_dist = go(x), come(x)
    for i in range(1, n + 1):
        if i != x:
            res = go_dist[i] + come_dist[i]
            mx = max(mx, res)

    print("#{} {}".format(tc, mx))

# Pass
