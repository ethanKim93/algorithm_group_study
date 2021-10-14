import sys
from collections import deque
sys.stdin = open("input.txt")

def dfs(start):
    q = deque()
    q.append(start)
    temps[start] = 0
    while q:
        now = q.popleft()
        for i in range(n+1):
            if maps[now][i]:
                if temps[i] > temps[now] + maps[now][i]:
                    temps[i] = temps[now] + maps[now][i]
                    q.append(i)

    return temps[n]

t = int(input())
for tc in range(1, t + 1):
    n, e = map(int,input().split())
    maps = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(e):
        s, g, w = map(int,input().split())
        maps[s][g] = w

    inf = 987654321
    temps = [inf] * (n+1)
    print("#{} {}".format(tc, dfs(0)))

# Pass